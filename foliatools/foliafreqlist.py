#!/usr/bin/env python
#-*- coding:utf-8 -*-

import getopt
import codecs
import sys
import os
import glob
try:
    from pynlpl.formats import folia
    from pynlpl.statistics import FrequencyList
    from pynlpl.textprocessors import Windower
except:
    print >>sys.stderr,"ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git"
    sys.exit(2)
    
def usage():
    print >>sys.stderr, "foliafreqlist"
    print >>sys.stderr, "  by Maarten van Gompel (proycon)"
    print >>sys.stderr, "  Radboud University Nijmegen"
    print >>sys.stderr, "  2012 - Licensed under GPLv3"
    print >>sys.stderr, ""
    print >>sys.stderr, "Compute a frequency list on one or more *tokenised* FoLiA documents."
    print >>sys.stderr, ""
    print >>sys.stderr, "Usage: foliafreqlist [options] file-or-dir1 file-or-dir2 ..etc.."
    print >>sys.stderr, ""
    print >>sys.stderr, "Parameters for output:"
    print >>sys.stderr, "  -i                           Case insensitive"
    print >>sys.stderr, "  -n [n]                       Count n-grams rather than unigrams"
    print >>sys.stderr, "  -s                           Add begin/end of sentence markers (with -n > 1)"
    print >>sys.stderr, "  -o [filename]                Output to a single file (instead of default stdout)"    
    print >>sys.stderr, "  -e [encoding]                Output encoding (default: utf-8)"
    print >>sys.stderr, "Parameters for processing directories:"
    print >>sys.stderr, "  -r                           Process recursively"
    print >>sys.stderr, "  -E [extension]               Set extension (default: xml)"
    print >>sys.stderr, "  -O                           Output each file to similarly named .freqlist file"
    print >>sys.stderr, "  -q                           Ignore errors"
    


    

def process(filename):
    try:
        print >>sys.stderr, "Processing " + filename
        doc = folia.Document(file=filename)

        freqlist = FrequencyList()
        
        if settings.n == 1:
            for word in doc.words():
                text = word.toktext()
                if settings.casesensitive: text = text.lower()
                freqlist.count(text)
        elif settings.sentencemarkers:
            for sentence in doc.sentences():
                for ngram in Windower(sentence.words(), settings.n):
                    text = ' '.join([x for x in ngram.toktext() ])
                    if settings.casesensitive: text = text.lower()
                    freqlist.count(text)                
        else:
            for word in Windower(sentence.words(), settings.n, None, None):
                text = ' '.join([x for x in ngram.toktext() ])
                if settings.casesensitive: text = text.lower()
                freqlist.count(text)                        
                    
        if settings.autooutput:                
            if filename[-len(settings.extension) - 1:].lower() == '.' +settings.extension:
                outfilename = filename[:-len(settings.extension) - 1] + '.freqlist'
            else:
                outfilename += '.freqlist'
            freqlist.save(outfilename,True)    
    except Exception as e:
        if settings.ignoreerrors:
            print >>sys.stderr, "ERROR: An exception was raised whilst processing " + filename, e            
        else:
            raise        
                                       
    return freqlist
        
                    

def processdir(d, freqlist = None):
    if not freqlist: freqlist = FrequencyList()
    print >>sys.stderr, "Searching in  " + d
    for f in glob.glob(d + '/*'):        
        if f[-len(settings.extension) - 1:] == '.' + settings.extension: 
            freqlist += process(f)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, freqlist)
    return freqlist
            

class settings:
    casesensitive = True
    autooutput = False
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'
    sentencemarkers = False
    ignoreerrors = False
    n = 1


def main():   
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:OE:htspwrq", ["help"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    outputfile = None
    

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-o':
            outputfile = a
        elif o == '-O':
            settings.autooutput = True
        elif o == '-s':
            settings.sentencemarkers = True
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            settings.ignoreerrors = True            
        else:            
            raise Exception("No such option: " + o)
                
    
    if outputfile: outputfile = codecs.open(outputfile,'w',settings.encoding)
        
    if len(sys.argv) >= 2:    
        freqlist = FrequencyList()
        for x in sys.argv[1:]:
            if os.path.isdir(x):
                processdir(x,freqlist)
            elif os.path.isfile(x):
                freqlist += process(x)
            else:
                print >>sys.stderr, "ERROR: File or directory not found: " + x
                sys.exit(3)    
        if outputfile:
            freqlist.save(outputfile, True)
        else:
            for line in freqlist.output("\t", True):
                print line
    else:
        print >>sys.stderr,"ERROR: No files specified"
        sys.exit(2)
            
if __name__ == "__main__":
    main()    
