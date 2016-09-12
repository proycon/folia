#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import getopt
import io
import sys
import os
import glob
from collections import Counter
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo pip install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git",file=sys.stderr)
    sys.exit(2)

def usage():
    print("foliatree",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Centre for Language and Speech Technology, Radboud University Nijmegen",file=sys.stderr)
    print("  2016 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("This conversion script reads a FoLiA XML document and outputs a tree of its structure", file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: foliatree [options] file-or-dir1 file-or-dir2 ..etc..",file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)
    print("  -t [types]                   Output only these elements (comma separated list)", file=sys.stderr)
    print("  -P                           Like -O, but outputs to current working directory",file=sys.stderr)
    print("  -i                           Print IDs",file=sys.stderr)
    print("  -c                           Print classes",file=sys.stderr)
    print("  -a                           Print annotator",file=sys.stderr)
    print("  -x                           Print text content",file=sys.stderr)
    print("  -s                           Print structural elements only",file=sys.stderr)
    print("  -q                           Ignore errors",file=sys.stderr)

def out(s, outputfile):
    if sys.version < '3':
        if outputfile:
            outputfile.write(s + "\n")
        else:
            print(s.encode(settings.encoding))
    else:
        if outputfile:
            print(s,file=outputfile)
        else:
            print(s)


def processelement(element, depth=0, inspan=False):
    if not isinstance(element, folia.AbstractElement): return False
    if settings.structureonly and not isinstance(element, folia.AbstractStructureElement): return False
    isspan = isinstance(element, folia.AbstractSpanAnnotation)
    try:
        if (not settings.types or element.XMLTAG in settings.types) and element.XMLTAG:
            out = "    " * depth
            out += element.XMLTAG
            if settings.ids and element.id:
                out += "; id=" + element.id
            if settings.classes and element.cls:
                out += "; class=" + element.cls
            if settings.annotators and element.annotator:
                out += "; annotator=" + element.annotator
            if settings.text and isinstance(element, (folia.TextContent, folia.PhonContent)):
                out += "; text=\"" + str(element) + "\""
            print(out)
            if not inspan:
                for e in element.data:
                    processelement(e,depth+1, isspan and isinstance(e, folia.AbstractStructureElement) )
    except AttributeError:
        pass
    return True

def process(filename, outputfile = None):
    print("Processing " + filename,file=sys.stderr)
    count = Counter()
    try:
        doc = folia.Document(file=filename)

        for e in doc.data:
            processelement(e)

    except Exception as e:
        if settings.ignoreerrors:
            print("ERROR: An exception was raised whilst processing " + filename + ":", e, file=sys.stderr)
        else:
            raise

    return count




def processdir(d, outputfile = None):
    print("Searching in  " + d, file=sys.stderr)
    count = Counter()
    for f in glob.glob(os.path.join(d, '*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            count.update(process(f, outputfile))
        elif settings.recurse and os.path.isdir(f):
            count.update(processdir(f, outputfile))
    return count


class settings:
    extension = 'xml'
    recurse = False
    ignoreerrors = False
    types = None
    constraints = []
    ids = False
    classes = False
    annotators = False
    text = False
    structureonly = False


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "E:ht:swrqicaxs", ["help"])
    except getopt.GetoptError as err:
        print(str(err), file=sys.stderr)
        usage()
        sys.exit(2)


    outputfile = None


    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-E':
            settings.extension = a
        elif o == '-r':
            settings.recurse = True
        elif o == '-t':
            settings.types = a.split(',')
        elif o == '-q':
            settings.ignoreerrors = True
        elif o == '-i':
            settings.ids = True
        elif o == '-c':
            settings.classes = True
        elif o == '-a':
            settings.annotators = True
        elif o == '-s':
            settings.structureonly = True
        elif o == '-x':
            settings.text = True
        else:
            raise Exception("No such option: " + o)


    if outputfile: outputfile = io.open(outputfile,'w',encoding=settings.encoding)

    if args:
        for x in args:
            if os.path.isdir(x):
                count = processdir(x,outputfile)
            elif os.path.isfile(x):
                count = process(x, outputfile)
            else:
                print("ERROR: File or directory not found: " + x, file=sys.stderr)
                sys.exit(3)

        for xmltag, freq in sorted(count.items(), key=lambda x: x[1]*-1):
            print(xmltag+"\t" + str(freq))
    else:
        print("ERROR: Nothing to do, specify one or more files or directories", file=sys.stderr)



if __name__ == "__main__":
    main()
