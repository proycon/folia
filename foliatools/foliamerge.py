#!/usr/bin/env python
# -*- coding: utf8 -*-

import getopt
import sys
try:
    from pynlpl.formats import folia
except:
    print >>sys.stderr,"ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git"
    sys.exit(2)
    
def usage():
    print >>sys.stderr, "foliamerge"
    print >>sys.stderr, "  by Maarten van Gompel (proycon)"
    print >>sys.stderr, "  Radboud University Nijmegen"
    print >>sys.stderr, "  2012 - Licensed under GPLv3"
    print >>sys.stderr, ""
    print >>sys.stderr, "Merges annotations from two or more FoLiA documents. Structural elements are never added. Annotations can only be merged if their parent elements have IDs."
    print >>sys.stderr, ""
    print >>sys.stderr, "Usage: foliamerge [options] file1 file2 file3 ... "
    print >>sys.stderr, ""
    print >>sys.stderr, "Options:"
    print >>sys.stderr, "  -o [file]                    Output file"
    print >>sys.stderr, "  -s                           Substitute: use first input file as output as well"



def foliamerge(outputfile, *files):
        outputdoc = None
        
        for i, filename in enumerate(files):
            inputdoc = folia.Document(file=filename)
            if i == 0:
                 outputdoc = inputdoc
            else:
                for annotationtype,set in inputdoc.annotations:
                    if not outputdoc.declared(annotationtype,set):
                        outputdoc.declare( annotationtype, set)

                
                for e in inputdoc.items():
                    if isinstance(e, folia.AbstractAnnotation) or isinstance(e, folia.AbstractAnnotationLayer):                         
                        try:
                            e.ANNOTATIONTYPE
                        except:
                            continue                       
                        if (e.ANNOTATIONTYPE, e.set) in outputdoc.annotations:
                            parent = e.parent
                            if parent.id in outputdoc:
                                newparent = outputdoc[parent.id]
                                #check if the annotation already exists
                                if isinstance(e, folia.AbstractTokenAnnotation) and newparent.hasannotation(e.ANNOTATIONTYPE, e.set):
                                    pass
                                elif isinstance(e, folia.AbstractAnnotationLayer) and newparent.hasannotationlayer(e.ANNOTATIONTYPE, e.set):    
                                    pass
                                else:
                                    c = e.copy(outputdoc) #make a copy, linked to outputdoc
                                    newparent.append(c) #append to outputdoc
                                    
        if outputfile:
            outputdoc.save(outputfile)

        return outputdoc    

def main():   
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:sh", ["help"])
    except getopt.GetoptError, err:
        print str(err)
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
        print >>sys.stderr, "ERROR: At least two files need to be specified"
        sys.exit(2)
        
    if substitute:
        outputfile = args[0]
    
    outputdoc = foliamerge(outputfile, *args)
    if not outputfile:
        print outputdoc.xmlstring()
        

if __name__ == "__main__":
    main()    
    
    
        
