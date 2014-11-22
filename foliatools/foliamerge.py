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
    print("foliamerge",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Radboud University Nijmegen",file=sys.stderr)
    print("  2012 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("Merges annotations from two or more FoLiA documents. Structural elements are never added. Annotations can only be merged if their parent elements have IDs.",file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: foliamerge [options] file1 file2 file3 ... ",file=sys.stderr)
    print("",file=sys.stderr)
    print("Options:",file=sys.stderr)
    print("  -o [file]                    Output file",file=sys.stderr)
    print("  -s                           Substitute: use first input file as output as well",file=sys.stderr)


def mergechildren(parent, outputdoc):
    merges = 0
    for e in parent:
        if (isinstance(e, folia.AbstractAnnotation) or isinstance(e, folia.AbstractAnnotationLayer)) and parent.id:
            try:
                e.ANNOTATIONTYPE
            except:
                continue

            if (e.ANNOTATIONTYPE, e.set) in outputdoc.annotations:
                assert e.parent == parent
                try:
                    newparent = outputdoc[parent.id]
                except:
                    pass
                #check if the annotation already exists
                if isinstance(e, folia.AbstractTokenAnnotation) and newparent.hasannotation(e.__class__, e.set):
                    print("Annotation type " + e.__class__.__name__ + ", set " + e.set + ", under " + newparent.id + " , already exists... skipping", file=sys.stderr)
                    pass
                elif isinstance(e, folia.AbstractAnnotationLayer) and newparent.hasannotationlayer(e.__class__, e.set):
                    print("Annotation type " + e.__class__.__name__ + ", set " + e.set + ", under " + newparent.id + " , already exists... skipping", file=sys.stderr)
                    pass
                else:
                    print("Adding Annotation type " + e.__class__.__name__ + ", set " + str(e.set) + " to " + newparent.id, file=sys.stderr)
                    c = e.copy(outputdoc) #make a copy, linked to outputdoc
                    newparent.append(c) #append to outputdoc
                    merges += 1
        elif isinstance(e, folia.AbstractElement):
            merges += mergechildren(e, outputdoc)
    return merges



def foliamerge(outputfile, *files):
        outputdoc = None
        merges = 0

        for i, filename in enumerate(files):
            print("Processing " + filename, file=sys.stderr)
            inputdoc = folia.Document(file=filename)
            if i == 0:
                 print("(pivot document)",file=sys.stderr)
                 outputdoc = inputdoc
            else:
                print("(merging document)",file=sys.stderr)

                for annotationtype,set in inputdoc.annotations:
                    if not outputdoc.declared(annotationtype,set):
                        outputdoc.declare( annotationtype, set)

                for e in inputdoc:
                    merges += mergechildren(e, outputdoc)

        if outputfile and merges > 0:
            outputdoc.save(outputfile)

        return outputdoc

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:sh", ["help"])
    except getopt.GetoptError as err:
        print(str(err),file=sys.stderr)
        usage()
        sys.exit(2)

    outputfile = None
    substitute = False

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-o':
            outputfile = a
        elif o == '-s':
            substitute = True
        else:
            raise Exception("No such option: " + o)

    if len(args) < 2:
        print("ERROR: At least two files need to be specified",file=sys.stderr)
        sys.exit(2)

    if substitute:
        outputfile = args[0]

    outputdoc = foliamerge(outputfile, *args)
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



