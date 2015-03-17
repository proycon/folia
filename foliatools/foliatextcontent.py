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
    print("  2012 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("This conversion takes a FoLiA XML document and adds text content element on higher levels, adding offset information."    ,file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: folia2txt [options] file-or-dir1 file-or-dir2 ..etc..",file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for output:"        ,file=sys.stderr)
    print("  -s                           Add text content on sentence level",file=sys.stderr)
    print("  -p                           Add text content on paragraph level"    ,file=sys.stderr)
    print("  -d                           Add text content on division level",file=sys.stderr)
    print("  -t                           Add text content on global text level"    ,file=sys.stderr)
    print("  -X                           Do NOT add offset information"    ,file=sys.stderr)
    print("  -e [encoding]                Output encoding (default: utf-8)",file=sys.stderr)
    print("  -w                           Edit file(s) (overwrites input files)" ,file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)



def propagatetext(element, Classes, setoffset=True,  cls='current', previousdelimiter=""):

    if not element.PRINTABLE: #only printable elements can hold text
        raise folia.NoSuchText


    if element.hastext(cls):
        s = element.textcontent(cls).value
        #print >>stderr, "text content: " + s
    else:
        addtext = False
        for c in Classes:
            if isinstance(element,c):
                addtext = True
                break

        #Not found, descend into children
        delimiter = ""
        s = ""
        for e in element:
            if e.PRINTABLE and not isinstance(e, folia.TextContent):
                try:
                    t = propagatetext(e,  Classes, setoffset,cls, delimiter)
                    if addtext and setoffset and e.hastext(cls):
                        extraoffset = len(t) - len(e.textcontent(cls).value)
                        e.textcontent(cls).offset = len(s) + extraoffset
                    s += t
                    delimiter = e.gettextdelimiter(False)
                    #delimiter will be buffered and only printed upon next iteration, this prevent the delimiter being output at the end of a sequence
                    #print >>stderr, "Delimiter for " + repr(e) + ": " + repr(delimiter)
                except folia.NoSuchText:
                    continue


        s = s.strip(' \r\n\t')
        if s and addtext:
            element.append(folia.TextContent, cls=cls, value=s)

    s = s.strip(' \r\n\t')
    if s and previousdelimiter:
        #print >>stderr, "Outputting previous delimiter: " + repr(previousdelimiter)
        return previousdelimiter + s
    elif s:
        return s
    else:
        print >>sys.stderr, "No text for: " + repr(element)
        #No text found at all :`(
        raise folia.NoSuchText

def process(filename, outputfile = None):
    print("Converting " + filename,file=sys.stderr)
    doc = folia.Document(file=filename)

    propagatetext(doc.data[0], settings.Classes, settings.offsets)


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

    extension = 'xml'
    recurse = False
    encoding = 'utf-8'


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "E:hsSpPdDtTXe:w", ["help"])
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
        elif o == '-X':
            settings.offsets = False
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-w':
            settings.inplaceedit = True
        elif o == '-r':
            settings.recurse = True
        else:
            raise Exception("No such option: " + o)


    if outputfile: outputfile = io.open(outputfile,'w',encoding=settings.encoding)

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
