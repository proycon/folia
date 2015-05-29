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
    print("foliacount",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Tilburg University / Radboud University Nijmegen",file=sys.stderr)
    print("  2015 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("This conversion script reads a FoLiA XML document and counts certain structure elements.", file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: foliacount [options] file-or-dir1 file-or-dir2 ..etc..",file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)
    print("  -C [type>count,type<count]   Count only documents that match the constraints", file=sys.stderr)
    print("  -t [types]                   Output only these elements (comma separated list)", file=sys.stderr)
    print("  -P                           Like -O, but outputs to current working directory",file=sys.stderr)
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


def process(filename, outputfile = None):
    print("Processing " + filename,file=sys.stderr)
    count = Counter()
    try:
        doc = folia.Document(file=filename)
        count['documents'] += 1

        for e in doc.select(folia.AbstractElement):
            if e.XMLTAG and (not settings.types or e.XMLTAG in settings.types):
                count[e.XMLTAG] += 1

        for constraintag, constrainf in settings.constraints:
            if not constrainf(count[constraintag]): 
                print("Skipping due to unmet constraints (" + constraintag+"): " + filename,file=sys.stderr)
                return Counter({'skipped_documents':1})

        print("Counted " + filename,file=sys.stderr)

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


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:OPE:ht:spwrqC:", ["help"])
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
        elif o == '-C':
            for rawconstraint in a.split(','):
                if '>' in rawconstraint:
                    tag, value = rawconstraint.split('>')
                    value = int(value)
                    settings.constraints.append( (tag, lambda x: x > value) )
                elif '<' in rawconstraint:
                    tag, value = rawconstraint.split('<')
                    value = int(value)
                    settings.constraints.append( (tag, lambda x: x < value) )
                elif rawconstraint.find('>=') != -1:
                    tag, value = rawconstraint.split('>=')
                    value = int(value)
                    settings.constraints.append( (tag, lambda x: x >= value) )
                elif rawconstraint.find('<=') != -1:
                    tag, value = rawconstraint.split('<=')
                    value = int(value)
                    settings.constraints.append( (tag, lambda x: x <= value) )
                elif rawconstraint.find('==') != -1:
                    tag, value = rawconstraint.split('==')
                    value = int(value)
                    settings.constraints.append( (tag, lambda x: x == value) )
                elif rawconstraint.find('!=') != -1:
                    tag, value = rawconstraint.split('!=')
                    value = int(value)
                    settings.constraints.append( (tag, lambda x: x != value) )
                else:
                    tag = a
                    settings.constraints.append( (tag, lambda x: x > 0) )
        elif o == '-q':
            settings.ignoreerrors = True
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
