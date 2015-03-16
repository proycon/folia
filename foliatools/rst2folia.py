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
<FoLiA xmlns="http://ilk.uvt.nl/folia" xmlns:xlink="http://www.w3.org/1999/xlink" xml:id="%(docid)s" version="0.9" generator="docutils-rst2folia-%(libversion)s">
<metadata type="native">
 <annotations>
%(declarations)s
 </annotations>
%(metadata)s
</metadata>
%(content)s
</FoLiA>
"""

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
        self.visitor =  FoLiATranslator(self.document)
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


    def __init__(self, document):
        self.textbuffer = []
        self.path = [] #(tag, id) tuples of the current FoLiA path
        self.content = [] #will contain all XML content as strings
        self.metadata = []
        self.declarations = []
        self.id_store = defaultdict( lambda: defaultdict(int) )
        self.docid = document.settings.docid
        self.list_enumerated = [] #contains a 2-list of boolean, int pairs, indicating whether the list is enumerated or not, and the number of items in it thus-far (used for labels), support nesting.
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
        self.path.append( (tag, id ) )
        indentation = (len(self.path)-1) * " "
        o = indentation + "<" + tag + " xml:id=\"" + id
        if attribs:
            for key, value in attribs.items():
                if sys.version < '3' and not isinstance(key, unicode):
                    o += " " + key + "=\"" + unicode(value) + "\""
                elif sys.version >= '3' and not isinstance(key, str):
                    o += " " + key + "=\"" + str(value) + "\""
        o += "\">\n"
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



    ############# TRANSLATION HOOKS (STRUCTURE) ################


    def visit_document(self, node):
        self.initstructure('text')

    def depart_document(self, node):
        self.closestructure('text')

    def visit_paragraph(self, node):
        self.initstructure('p')

    def depart_paragraph(self, node):
        self.closestructure('p')

    def visit_section(self, node):
        self.initstructure('div')

    def depart_section(self, node):
        self.closestructure('div')

    def visit_title(self, node):
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

    ############# TRANSLATION HOOKS (TEXT & MARKUP) ################

    def visit_Text(self, node):
        self.textbuffer.append(  self.encode(node.astext()) )

    def depart_Text(self, node):
        pass

def main():
    description = 'Generates FoLiA documents from reStructuredText. ' + default_description
    publish_cmdline(writer=Writer(), writer_name='folia', description=description)

if __name__ == '__main__':
    main()
