#!/usr/bin/env python
# -*- coding: utf8 -*-


from __future__ import print_function, unicode_literals, division, absolute_import

import getopt
import sys
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git",file=sys.stderr)
    sys.exit(2)

def usage():
    print("foliacat",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Radboud University Nijmegen",file=sys.stderr)
    print("  2014 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("Concatenates multiple FoLiA documents into one; provided that all IDs are unique.",file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: foliacat [options] file1 file2 file3 ... ",file=sys.stderr)
    print("",file=sys.stderr)
    print("Options:",file=sys.stderr)
    print("  -o [file]                    Output file",file=sys.stderr)
    print("  -i [id]                      ID for output file (mandatory)",file=sys.stderr)


def concat(target, source):
    merges = 0
    for e in source:
        c = e.copy(target.doc)
        target.append(c)
        merges += 1
    return merges



def foliacat(id, outputfile, *files):
    totalmerges = 0
    outputdoc = folia.Document(id=id)
    text = outputdoc.append(folia.Text(outputdoc,id=id + ".text"))
    for i, filename in enumerate(files):
        merges = 0
        print("Processing " + filename, file=sys.stderr)
        inputdoc = folia.Document(file=filename)
        print("(merging document)",file=sys.stderr)

        for annotationtype,set in inputdoc.annotations:
            if not outputdoc.declared(annotationtype,set):
                outputdoc.declare( annotationtype, set)

        for d in inputdoc.data:
            merges += concat(text, d)

        print("(merged " + str(merges) + " elements, with all elements contained therein)",file=sys.stderr)
        totalmerges += merges

    print("(TOTAL: merged " + str(totalmerges) + " elements, with all elements contained therein)",file=sys.stderr)
    if outputfile and merges > 0:
        outputdoc.save(outputfile)

    return outputdoc

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:i:h", ["help"])
    except getopt.GetoptError as err:
        print(str(err),file=sys.stderr)
        usage()
        sys.exit(2)

    outputfile = None
    substitute = False

    id = None
    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-o':
            outputfile = a
        elif o == '-i':
            id = a
        else:
            raise Exception("No such option: " + o)

    if len(args) < 2:
        print("WARNING: only one file specified", file=sys.stderr)
    if not id:
        print("ERROR: Please specify an ID for the result document with the -i option",file=sys.stderr)
        sys.exit(2)


    if substitute:
        outputfile = args[0]

    outputdoc = foliacat(id, outputfile, *args)
    if not outputfile:
        xml = outputdoc.xmlstring()
        if sys.version < '3':
            if isinstance(xml,unicode):
                print(xml.encode('utf-8'))
            else:
                print(xml)
        else:
            print(xml)


if __name__ == "__main__":
    main()



