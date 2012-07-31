#!/usr/bin/env python
#-*- coding:utf-8 -*-

import getopt
import sys
import os
import glob
try:
    from pynlpl.formats import folia
except:
    print >>sys.stderr,"ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git"
    sys.exit(2)
    
def usage():
    print >>sys.stderr, "foliaquery"
    print >>sys.stderr, "  by Maarten van Gompel (proycon)"
    print >>sys.stderr, "  Tilburg University / Radboud University Nijmegen"
    print >>sys.stderr, "  2012 - Licensed under GPLv3"
    print >>sys.stderr, ""
    print >>sys.stderr, "Query one or more FoLiA documents for certain patterns."
    print >>sys.stderr, ""
    print >>sys.stderr, "Usage: foliaquery [options] file-or-dir1 file-or-dir2 ..etc.."
    print >>sys.stderr, ""
    print >>sys.stderr, "Parameters for output:"        
    print >>sys.stderr, "  --text \"[words]\"           Text pattern (Case sensitive)"
    print >>sys.stderr, "  --pos \"[postags]\"          Pos pattern"
    print >>sys.stderr, "  --lemma \"[lemmas]\"         Lemma pattern"
    print >>sys.stderr, "  --sense \"[sense]\"          Sense pattern"
    print >>sys.stderr, "  --phon \"[phon]\"            Phonetic pattern"
    print >>sys.stderr, "  -i                           Patterns are case-insensitive"
    print >>sys.stderr, "  -L [length]                  Left-context size words/tokens (default: 0)"
    print >>sys.stderr, "  -R [length]                  Right-context size in words/tokens (default: 0)"    
    print >>sys.stderr, "  -e [encoding]                Output encoding (default: utf-8)"     
    print >>sys.stderr, "Parameters for processing directories:"
    print >>sys.stderr, "  -r                           Process recursively"
    print >>sys.stderr, "  -E [extension]               Set extension (default: xml)"
    print >>sys.stderr, "  -q                           Ignore errors"
    print >>sys.stderr, ""
    print >>sys.stderr, "Pattern syntax:"
    print >>sys.stderr, "    Fixed-width wildcard: ^ "
    print >>sys.stderr, "    Variable-width wildcard: * "
    print >>sys.stderr, "    Disjunction: | "
    print >>sys.stderr, "    Regular Expression: {REGEXP}"
    
    print >>sys.stderr, ""    
    print >>sys.stderr, "Examples:"
    print >>sys.stderr, "   1) foliaquery --text=\"to be * to be\""
    print >>sys.stderr, "       Matches any gap of any size (up to the maximum)"    
    print >>sys.stderr, "   2) foliaquery --text=\"to be ^ ^ to be\""   
    print >>sys.stderr, "       Matches any gap of exactly two tokens"
    print >>sys.stderr, "   3) foliaquery --pos=\"ADJ NOUN\""
    print >>sys.stderr, "       Searching by annotation"    
    print >>sys.stderr, "   4) foliaquery --text=\"rent\" --pos=\"NOUN\""
    print >>sys.stderr, "       Patterns may be combined, matches have to satisfy all patterns"
    print >>sys.stderr, "   5) foliaquery --text=\"he leaves|departs today|tomorrow\" --pos=\"PRON VERB ^\""
    print >>sys.stderr, "       The pipe character allows for disjunctions in single tokens"
    print >>sys.stderr, "   6a) foliaquery --text=\"we {w[io]n}\" --pos=\"PRON VERB\""
    print >>sys.stderr, "   6b) foliaquery --text=\"{.*able}\" --pos=\"ADJ\""
    print >>sys.stderr, "       Curly braces specify a regular expression for a single token"    
        
    

    
def parsepattern(rawpattern, annotationtype): #, annotationset=None):    
    components = []
    for tokenpattern in rawpattern.strip().split(' '):
        if tokenpattern == '*':
            components.append('*')
        elif tokenpattern == '^':            
            components.append(True)
        elif tokenpattern[0] == '{' and tokenpattern[-1] == '}':
            components.append( folia.RegExp(tokenpattern[1:-1]) )
        elif '|' in tokenpattern:
            components.append( tuple(tokenpattern.split('|')) )
        else:
            components.append(tokenpattern)
    d = {'casesensitive':settings.casesensitive}
    if annotationtype:
        d['matchannotation'] = annotationtype            
    return folia.Pattern(*components,**d) #, matchannotationset=annotationset)    


    
def process(filename, patterns):
    try:
        print >>sys.stderr, "Processing " + filename
        doc = folia.Document(file=filename)
        for match in doc.findwords(*patterns ):
            s = u""
            for token in match:
                s += u"\t" + token.text()
            s = filename + "\t" + match[0].id + s
            print s.encode(settings.encoding)
    except Exception as e:
        if settings.ignoreerrors:
            print >>sys.stderr, "ERROR: An exception was raised whilst processing " + filename + ":", e            
        else:
            raise        
        

def processdir(d, patterns):
    print >>sys.stderr, "Searching in  " + d
    for f in glob.glob(d + '/*'):        
        if f[-len(settings.extension) - 1:] == '.' + settings.extension: 
            process(f, patterns)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, patterns)
            

class settings:
    leftcontext = 0
    rightcontext = 0
    
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'
    
    ignoreerrors = False
    casesensitive = True


def main():   
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:OE:hqr", ["help","text="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)


    
    patterns = []

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '--text':
            patterns.append( parsepattern(a, None) )
        elif o == '--pos':
            patterns.append( parsepattern(a, folia.PosAnnotation) )
        elif o == '--lemma':
            patterns.append( parsepattern(a, folia.LemmaAnnotation) )            
        elif o == '--sense':
            patterns.append( parsepattern(a, folia.SenseAnnotation) )
        elif o == '--phon':
            patterns.append( parsepattern(a, folia.PhonAnnotation) )
                                      
                                      
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            settings.ignoreerrors = True        
        else:            
            raise Exception("No such option: " + o)
            
        
    if args:
        for x in args:
            if os.path.isdir(x):
                processdir(x, patterns)
            elif os.path.isfile(x):
                process(x, patterns)
            elif x[0:2] != '--':
                print >>sys.stderr, "ERROR: File or directory not found: " + x
                sys.exit(3)
    else:
        print >>sys.stderr,"ERROR: Nothing to do, specify one or more files or directories"
    
if __name__ == "__main__":
    main()
