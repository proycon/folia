#!/usr/bin/env python
#-*- coding:utf-8 -*-

#---------------------------------------------------------------
# ReStructuredText to FoLiA Converter
#   by Maarten van Gompel
#   Centre for Language Studies
#   Radboud University Nijmegen
#   proycon AT anaproy DOT nl
#
#   Licensed under GPLv3
#
# This script converts RST to FoLiA format.
#
#----------------------------------------------------------------

from __future__ import print_function, unicode_literals, division, absolute_import

import sys
import glob
import gzip
import os

from collections import defaultdict
from copy import copy

from docutils import writers, nodes
from docutils.core import publish_cmdline, default_description

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

LIBVERSION = "0.1"

class Writer(writers.Writer):

    DEFAULTID = "untitled"
    TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="folia2html.xsl"?>
<FoLiA xmlns="http://ilk.uvt.nl/folia" xmlns:xlink="http://www.w3.org/1999/xlink" xml:id="%(docid)s" version="0.11" generator="docutils-rst2folia-%(libversion)s">
<metadata type="native">
 <annotations>
%(declarations)s
 </annotations>
%(metadata)s
</metadata>
%(content)s
</FoLiA>
"""

    DEFAULTSETS = {
        'div': 'https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/divisions.foliaset.xml',
        'style': 'https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/styles.foliaset.xml',
        'note': 'https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/notes.foliaset.xml',
    }

    #Formats this writer supports
    supported = ('folia',)

    settings_spec = (
        'FoLiA-Specific Options',
        None,
        (
            ('Document ID.  Default is "%s".' % DEFAULTID, ['--docid'], {'default': DEFAULTID, 'metavar': '<string>'}),
        )
    )

    visitor_attributes = ('declarations','metadata','content')

    def translate(self):
        sets = copy(self.DEFAULTSETS)
        self.visitor =  FoLiATranslator(self.document, sets)
        self.document.walkabout(self.visitor)
        for attr in self.visitor_attributes:
            setattr(self, attr, getattr(self.visitor, attr))
        self.output = self.apply_template()

    def apply_template(self):
        subs = self.interpolation_dict()
        return self.TEMPLATE % subs

    def interpolation_dict(self):
        subs = {}
        for attr in self.visitor_attributes:
            subs[attr] = ''.join(getattr(self, attr)).rstrip('\n')
        subs['encoding'] = self.document.settings.output_encoding
        subs['libversion'] = LIBVERSION
        subs['docid'] = self.document.settings.docid
        return subs

    def assemble_parts(self):
        writers.Writer.assemble_parts(self)
        for part in self.visitor_attributes:
            self.parts[part] = ''.join(getattr(self, part))



class FoLiATranslator(nodes.NodeVisitor):


    def __init__(self, document, sets={}):
        self.textbuffer = []
        self.path = [] #(tag, id) tuples of the current FoLiA path
        self.content = [] #will contain all XML content as strings
        self.metadata = []
        self.declarations = []
        self.id_store = defaultdict( lambda: defaultdict(int) )
        self.docid = document.settings.docid
        self.list_enumerated = [] #contains a 2-list of boolean, int pairs, indicating whether the list is enumerated or not, and the number of items in it thus-far (used for labels), support nesting.
        self.rootdiv = False #create a root div element?
        self.sets = sets
        self.declared = {}
        self.inmarkup = False
        nodes.NodeVisitor.__init__(self, document)

    ############# HELPERS ###############

    def astext(self):
        return ''.join(self.head + self.content)

    def encode(self, text):
        """Encode special characters in `text` & return."""
        if sys.version < '3' and not isinstance(text, unicode):
            text = unicode(text, 'utf-8')
        elif sys.version >= '3' and not isinstance(text, str):
            text = str(text, 'utf-8')
        return text.translate({
            ord('&'): u'&amp;',
            ord('<'): u'&lt;',
            ord('"'): u'&quot;',
            ord('>'): u'&gt;',
        })

    def initstructure(self, tag, **attribs):
        """Generic visit function for structure elements"""
        #Generate an ID
        if not self.path:
            assert tag == "text"
            id = self.docid + ".text"
        else:
            parenttag, parentid = self.path[-1]
            id = self.generate_id(parentid, tag)
        self.declare(tag)
        self.path.append( (tag, id ) )
        indentation = (len(self.path)-1) * " "
        o = indentation + "<" + tag + " xml:id=\"" + id + "\""
        if attribs:
            for key, value in attribs.items():
                if key == "cls": key = "class"
                if sys.version < '3':
                    o += " " + key + "=\"" + unicode(value) + "\""
                elif sys.version >= '3':
                    o += " " + key + "=\"" + str(value) + "\""
        o += ">\n"
        self.content.append(o)

    def closestructure(self, tag):
        """Generic depart function for structure elements"""
        tag, id = self.path.pop()
        indentation = len(self.path) * " "
        o = ""
        if self.textbuffer:
            o += indentation + " <t>"  + "".join(self.textbuffer) + "</t>\n"
        o += indentation + "</" + tag + ">\n"
        self.textbuffer.clear()
        self.content.append(o)

    def generate_id(self, parentid, tag ):
        self.id_store[parentid][tag] += 1
        return parentid + "." + tag + "." + str(self.id_store[parentid][tag])


    def rightsibling(self, node):
        fetch = False
        for sibling in node.traverse(None,1,0,1,0):
            if sibling is node:
                fetch = True
            elif fetch:
                return sibling
        return None


    def ignore_depart(self, node):
        try:
            if node.ignore_depart:
                return True
        except AttributeError:
            return False

    ############# TRANSLATION HOOKS (MAIN STRUCTURE) ################


    def visit_document(self, node):
        self.initstructure('text')

    def depart_document(self, node):
        if self.rootdiv:
            self.closestructure('div')
        self.closestructure('text')

    def visit_paragraph(self, node):
        if node.parent.__class__.__name__ == 'list_item':
            #this paragraph is in an item, we don't want paragraphs in items unless there actually are multiple elements in the item
            sibling = self.rightsibling(node)
            if sibling:
                self.initstructure('p')
            else:
                node.ignore_depart = True
        else:
            self.initstructure('p')

    def depart_paragraph(self, node):
        if not self.ignore_depart(node):
            self.closestructure('p')

    def visit_section(self, node):
        self.initstructure('div',cls="section")

    def depart_section(self, node):
        self.closestructure('div')

    def visit_title(self, node):
        if node.parent.__class__.__name__ == 'document':
            self.rootdiv = True
            self.initstructure('div',cls="document")
        self.initstructure('head')

    def depart_title(self, node):
        self.closestructure('head')

    def visit_bullet_list(self,node):
        self.list_enumerated.append([False,0])
        self.initstructure('list')

    def depart_bullet_list(self,node):
        self.list_enumerated.pop()
        self.closestructure('list')

    def visit_enumerated_list(self,node):
        self.list_enumerated.append([True,0])
        self.initstructure('list')

    def depart_enumerated_list(self,node):
        self.list_enumerated.pop()
        self.closestructure('list')

    def visit_list_item(self,node):
        if self.list_enumerated[-1][0]:
            self.list_enumerated[-1][1] += 1
            self.initstructure('item',n=self.list_enumerated[-1][1])
        else:
            self.initstructure('item')

    def depart_list_item(self,node):
        self.closestructure('item')


    def addstyle(self,node,style):
        self.inmarkup = True
        self.declare('style')
        self.textbuffer.append(  '<t-style class="' + style + '">' + self.encode(node.astext()) + '</t-style>' )

    def addmetadata(self, key, node):
        self.metadata.append(  " <meta id=\"" + key + "\">" + self.encode(node.astext()) + "</meta>\n" )


    def declare(self, annotationtype):
        if not annotationtype in self.declared:
            if annotationtype in self.sets and self.sets[annotationtype]:
                self.declarations.append("   <" + annotationtype + "-annotation set=\"" + self.sets[annotationtype] + "\" />\n")
                self.declared[annotationtype] = True

    ############# TRANSLATION HOOKS (TEXT & MARKUP) ################

    def visit_Text(self, node):
        if not self.inmarkup:
            self.textbuffer.append(  self.encode(node.astext()) )

    def depart_Text(self, node):
        pass

    def visit_strong(self, node):
        self.addstyle(node,"strong")

    def depart_strong(self, node):
        self.inmarkup = False

    def visit_emphasis(self, node):
        self.addstyle(node,"emphasis")

    def depart_emphasis(self, node):
        self.inmarkup = False

    def visit_literal(self, node):
        self.addstyle(node,"literal")

    def depart_literal(self, node):
        self.inmarkup = False
    ############# TRANSLATION HOOKS (OTHER STRUCTURE) ################

    def visit_attention(self,node):
        self.initstructure('div',cls='attention')
    def depart_attention(self,node):
        pass

    def visit_hint(self,node):
        self.initstructure('div',cls='hint')
    def depart_hint(self,node):
        pass
    def visit_footnote(self,node):
        #TODO: handle footnote numbering:  http://code.nabla.net/doc/docutils/api/docutils/transforms/references/docutils.transforms.references.Footnotes.html
        self.initstructure('note',cls='footnote')
    def depart_footnote(self,node):
        pass
    def visit_note(self,node):
        self.initstructure('note',cls='note')
    def depart_note(self,node):
        pass

    def visit_caution(self,node):
        self.initstructure('note',cls='caution')
    def depart_caution(self,node):
        pass
    def visit_warning(self,node):
        self.initstructure('note',cls='warning')
    def depart_warning(self,node):
        pass
    def visit_danger(self,node):
        self.initstructure('note',cls='danger')
    def depart_danger(self,node):
        pass
    def visit_admonition(self,node):
        self.initstructure('note',cls='admonition')
    def depart_admonition(self,node):
        pass
    def visit_tip(self,node):
        self.initstructure('note',cls='tip')
    def depart_tip(self,node):
        pass
    def visit_error(self,node):
        self.initstructure('note',cls='error')
    def depart_error(self,node):
        pass
    def visit_important(self,node):
        self.initstructure('note',cls='important')
    def depart_important(self,node):
        pass
    ############# TRANSLATION HOOKS (METADATA, rst-specific fields) ################

    def visit_docinfo(self, node):
        pass
    def depart_docinfo(self, node):
        pass
    def visit_authors(self, node):
        pass
    def depart_authors(self, node):
        pass

    def visit_author(self, node):
        self.addmetadata('author', node)

    def depart_author(self, node):
        pass

    def visit_date(self, node):
        self.addmetadata('date', node)

    def depart_date(self, node):
        pass

    def visit_contact(self, node):
        self.addmetadata('contact', node)

    def depart_contact(self, node):
        pass

    def visit_status(self, node):
        self.addmetadata('status', node)

    def depart_status(self, node):
        pass


    def visit_version(self, node):
        self.addmetadata('version', node)

    def depart_version(self, node):
        pass

    def visit_copyright(self, node):
        self.addmetadata('copyright', node)

    def depart_copyright(self, node):
        pass

    def visit_organization(self, node):
        self.addmetadata('organization', node)

    def depart_organization(self, node):
        pass


    def visit_address(self, node):
        self.addmetadata('address', node)

    def depart_address(self, node):
        pass

    def visit_contact(self, node):
        self.addmetadata('contact', node)

    def depart_contact(self, node):
        pass

def main():
    description = 'Generates FoLiA documents from reStructuredText. ' + default_description
    publish_cmdline(writer=Writer(), writer_name='folia', description=description)

if __name__ == '__main__':
    main()
