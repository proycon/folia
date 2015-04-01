#! /usr/bin/env python
# -*- coding: utf8 -*-


from __future__ import print_function, unicode_literals, division, absolute_import

import getopt
import io
import sys
import os
import glob
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git",file=sys.stderr)
    sys.exit(2)

def usage():
    print("foliatextcontent",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Radboud University Nijmegen",file=sys.stderr)
    print("  2015 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("This tool operates on some of the redundancy regarding text context inherent in FoLiA documents. It adds text content elements,  on the higher (untokenised) levels, adding offset information and mark-up element if present. Secondly, the tool may als adds text-markup elements for substrings (str element) (provided there is no overlap).",file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: foliatextcontent [options] file-or-dir1 file-or-dir2 ..etc..",file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for output:"        ,file=sys.stderr)
    print("  -s                           Add text content on sentence level",file=sys.stderr)
    print("  -p                           Add text content on paragraph level"    ,file=sys.stderr)
    print("  -d                           Add text content on division level",file=sys.stderr)
    print("  -t                           Add text content on global text level"    ,file=sys.stderr)
    print("  -T                           Add text content for the specified elements (comma separated list of folia xml tags)"    ,file=sys.stderr)
    print("  -X                           Do NOT add offset information"    ,file=sys.stderr)
    print("  -F                           Force offsets to refer to the specified structure only (only works if you specified a single element type for -T!!!)"    ,file=sys.stderr)
    print("  -M                           Add substring markup linking to string elements (if any, and when there is no overlap)"    ,file=sys.stderr)
    print("  -e [encoding]                Output encoding (default: utf-8)",file=sys.stderr)
    print("  -w                           Edit file(s) (overwrites input files), will output to stdout otherwise" ,file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)


def linkstrings(element, cls='current'):
    if element.hastext(cls,strict=True):
        text = element.textcontent(cls)
        for string in element.select(folia.String, None, False):
            if string.hastext(cls):
                stringtext = string.textcontent(cls)
                if stringtext.offset is not None:
                    #find the right insertion point
                    offset = stringtext.offset
                    length = len(stringtext.text())

                    cursor = 0
                    fits = False
                    replaceindex = 0
                    replace = []
                    for i, subtext in enumerate(text):
                        if isinstance(subtext, str):
                            subtextlength = len(subtext.text())
                            if offset >= cursor and offset+length <= cursor+subtextlength:
                                #string fits here
                                fits = True
                                replaceindex = i
                                kwargs = {}
                                if string.id:
                                    kwargs['idref'] = string.id
                                if string.set:
                                    kwargs['set'] = string.set
                                if string.cls:
                                    kwargs['cls'] = string.cls
                                replace = [subtextlength[:cursor], folia.TextMarkupString(element.doc, **kwargs), subtextlength[cursor+length:]]
                                break

                            cursor += subtextlength
                        elif isinstance(subtext, folia.AbstractTextMarkup):
                            raise NotImplementedError

                if fits:
                    text.data[replaceindex] = replace

def gettextsequence(element, cls):
    assert element.PRINTABLE
    if element.TEXTCONTAINER:
        if isinstance(element.TextContent) and element.cls != cls:
            raise StopIteration

        for e in element:
            if isinstance(e, str):
                yield element
            else: #markup (don't recurse)
                yield subelement
                yield subelement.gettextdelimiter()
    else:
        for e in element:
            if e.PRINTABLE and not isinstance(e, folia.String):
                for subelement in gettextsequence(e):
                    yield subelement
                    yield subelement.gettextdelimiter()


def settext(element, cls='current', offsets=True, forceoffsetref=False):
    assert element.PRINTABLE
    #get the raw text sequence
    try:
        textsequence = list(gettextsequence(element,cls))
    except folia.NoSuchText:
        return None

    if textsequence:
        newtextsequence = []
        offset = 0
        for e in textsequence:
            if e: #filter out empty strings
                if isinstance(e,str):
                    length = len(e)
                else:
                    e = e.copy()
                    length = len(e.text())
                    if offsets:
                        if e.offset is None:
                            if e.ancestor(folia.AbstractStructureElement) is element:
                                e.offset = offset
                            elif forceoffsetref:
                                e.offset = offset
                                e.ref = element
                newtextsequence.append(e)
                offset += length

        return element.replace(folia.TextContent, *newtextsequence, cls=cls) #appends if new


def processelement(element, settings):
    for e in elements:
        processelement(e,settings)
    if element.PRINTABLE:
        if any( isinstance(element,C) for C in settings.Classes):
            for cls in element.doc.textclasses:
                settext(element, cls, settings.offsets, settings.forceoffsetref)


def process(filename, outputfile = None):
    print("Converting " + filename,file=sys.stderr)
    doc = folia.Document(file=filename)

    if settings.linkstrings:
        for element in folia.select(AbstractStructureElement):
            if settings.linkstrings:
                linkstrings(element, cls)

    if settings.Classes:
        for e in doc.data:
            processelement(e, settings.Classes)


    if settings.inplaceedit:
        doc.save()
    else:
        print(doc.xmlstring())

def processdir(d, outputfile = None):
    print("Searching in  " + d, file=sys.stderr)
    for f in glob.glob(os.path.join(d ,'*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            process(f, outputfile)
        elif settings.recurse and os.path.isdir(f):
            processdir(f)



class settings:
    Classes = []
    inplaceedit = False
    offsets = True
    forceoffsetref = False
    linkstrings = False

    extension = 'xml'
    recurse = False
    encoding = 'utf-8'

    textclasses =[]


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "E:hsSpPdDtTXMe:wT:Fc:", ["help"])
    except getopt.GetoptError as err:
        print(str(err),file=sys.stderr)
        usage()
        sys.exit(2)


    outputfile = None


    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-d':
            settings.Classes.append(folia.Division)
        elif o == '-t':
            settings.Classes.append(folia.Text)
        elif o == '-s':
            settings.Classes.append(folia.Sentence)
        elif o == '-p':
            settings.Classes.append(folia.Paragraph)
        elif o == '-T':
            settings.Classes += [ folia.XML2CLASS[tag] for tag in a.split(',') ]
        elif o == '-X':
            settings.offsets = False
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-F':
            settings.forceoffsetref = True
        elif o == '-M':
            settings.linkstrings = True
        elif o == '-w':
            settings.inplaceedit = True
        elif o == '-r':
            settings.recurse = True
        else:
            raise Exception("No such option: " + o)


    if outputfile: outputfile = io.open(outputfile,'w',encoding=settings.encoding)

    if len(settings.Classes) > 1:
        settings.forceoffsetref = False

    if args:
        for x in args:
            if os.path.isdir(x):
                processdir(x,outputfile)
            elif os.path.isfile(x):
                process(x, outputfile)
            else:
                print("ERROR: File or directory not found: " + x,file=sys.stderr)
                sys.exit(3)
    else:
        print("ERROR: Nothing to do, specify one or more files or directories",file=sys.stderr)

if __name__ == "__main__":
    main()
