#!/usr/bin/env python
#-*- coding:utf-8 -*-

import getopt
import codecs
import sys
import os
import glob
try:
    from pynlpl.formats import folia
except:
    print >>sys.stderr,"ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git"
    sys.exit(2)
    
def usage():
    print >>sys.stderr, "folia2txt.py"
    print >>sys.stderr, "  by Maarten van Gompel (proycon)"
    print >>sys.stderr, "  Tilburg University / Radboud University Nijmegen"
    print >>sys.stderr, "  2012 - Licensed under GPLv3"
    print >>sys.stderr, ""
    print >>sys.stderr, "This conversion script reads a FoLiA XML document and outputs the"
    print >>sys.stderr, "document's text as plain text, *without* any annotations."
    print >>sys.stderr, ""
    print >>sys.stderr, "Parameters for single files:"
    print >>sys.stderr, "  -f [FoLiA XML file]          Specify a FoLiA document to process"        
    print >>sys.stderr, "  -o [filename]                Output to file instead of stdout"    
    print >>sys.stderr, "  -e [encoding]                Output encoding (default: utf-8)"
    print >>sys.stderr, "Parameters for processing multiple files:"
    print >>sys.stderr, "  -d [directory]               Specify a directory to process (instead of -f)"
    print >>sys.stderr, "  -r                           Process recursively"
    print >>sys.stderr, "  -E [extension]               Set extention (default: xml)"
    print >>sys.stderr, "  -O                           Output each file to similarly named .txt file"
    print >>sys.stderr, "Parameters for output format:"
    print >>sys.stderr, "  -t                           Retain tokenisation, do not detokenise"
    print >>sys.stderr, "  -w                           One word per line"
    print >>sys.stderr, "  -s                           One sentence per line"
    print >>sys.stderr, "  -p                           One paragraph per line" 





    

def process(filename, outputfile = None):
    print >>sys.stderr, "Converting " + filename
    doc = folia.Document(file=filename)

    if settings.autooutput:    
        if filename[-len(settings.extension) - 1:].lower() == '.' +settings.extension:
            outfilename = filename[:-len(settings.extension) - 1] + '.txt'
        else:
            outfilename += '.txt'
        
        print >>sys.stderr, " Saving as " + outfilename
        outputfile = codecs.open(outfilename,'w',settings.encoding)

    if settings.wordperline:
        for word in doc.words():        
            if outputfile:
                outputfile.write(word.text('current', settings.retaintokenisation) + "\n")
            else:
                print word.text('current', settings.retaintokenisation).encode(settings.encoding)
    elif settings.sentenceperline:    
        for sentence in doc.sentences():        
            if outputfile:
                outputfile.write(sentence.text('current', settings.retaintokenisation) + "\n")
            else:
                print sentence.text('current', settings.retaintokenisation).encode(settings.encoding)    
    elif settings.paragraphperline:    
        for paragraph in doc.paragraphs():        
            if outputfile:
                outputfile.write(paragraph.text('current', settings.retaintokenisation) + "\n")
            else:
                print paragraph.text('current', settings.retaintokenisation).encode(settings.encoding)     
    else:
        if outputfile:
            outputfile.write( doc.text(settings.retaintokenisation) )
        else:
            print doc.text( settings.retaintokenisation).encode(settings.encoding)

    if settings.autooutput:
        outputfile.close()
    


def processdir(d, outputfile = None):
    print >>sys.stderr, "Searching in  " + d
    for f in glob.glob(d + '/*'):        
        if f[-len(settings.extension) - 1:] == '.' + settings.extension: 
            process(f, outputfile)
        elif settings.recurse and os.path.isdir(f):
            processdir(f)
            

class settings:
    wordperline = False
    sentenceperline = False
    paragraphperline = False
    detokenise = False
    retaintokenisation = False
    autooutput = False
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'


def main():   
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:d:o:OE:htspwr", ["help"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    filename = None
    dirname = None
    outputfile = None
    

    for o, a in opts:
        if o == '-f':
            filename = a
        elif o == '-d':
            dirname = a
        elif o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-t':
            settings.retaintokenisation = True
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-o':
            outputfile = a
        elif o == '-O':
            settings.autooutput = True
        elif o == '-s':
            settings.sentenceperline = True
        elif o == '-p':
            settings.paragraphperline = True
        elif o == '-w':
            settings.wordperline = True     
        elif o == '-r':
            settings.recurse = True
        else:            
            raise Exception("No such option: " + o)
                
    
    if outputfile: outputfile = codecs.open(outputfile,'w',settings.encoding)
        
    if filename:
        process(filename, outputfile)
    elif dirname:
        processdir(dirname, outputfile)
    elif len(sys.argv) >= 2:
        for x in sys.argv[1:]:
            if os.path.isdir(x):
                processdir(x,outputfile)
            elif os.path.isfile(x):
                process(x, outputfile)    
    else:
        print >>sys.stderr,"ERROR: Nothing to do, specify -f or -d"
    
if __name__ == "__main__":
    main()
