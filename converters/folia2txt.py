#!/usr/bin/env python
#-*- coding:utf-8 -*-

import getopt
import codecs
import sys
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
    print >>sys.stderr, "Parameters:"
    print >>sys.stderr, "  -f [FoLiA XML file]          Specify a FoLiA document to process (mandatory)"    
    print >>sys.stderr, "  -t                           Retain tokenisation, do not detokenise"
    print >>sys.stderr, "  -w                           One word per line"
    print >>sys.stderr, "  -s                           One sentence per line"
    print >>sys.stderr, "  -p                           One paragraph per line" 
    print >>sys.stderr, "  -o [filename]                Output to file instead of stdout"
    print >>sys.stderr, "  -O                           Output to similarly named .txt file"
    print >>sys.stderr, "  -e [encoding]                Output encoding (default: utf-8)"

   
try:
    opts, args = getopt.getopt(sys.argv[1:], "f:o:Ohtspw", ["help"])
except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(2)

filename = None

outputfile = None

allowemptylines = True
sentenceperline = False
paragraphperline = False
detokenise = False
retaintokenisation = False
autooutput = False

encoding = 'utf-8'

for o, a in opts:
    if o == '-f':
        filename = a
    elif o == '-h':
        usage()
        sys.exit(0)
    elif o == '-t':
        retaintokenisation = True
    elif o == '-e':
        encoding = a
    elif o == '-o':
        outputfile = a
    elif o == '-O':
        autooutput = True
    elif o == '-s':
        sentenceperline = True
    elif o == '-p':
        paragraphperline = True
    elif o == '-w':
        wordperline = True     
    else:
        
        raise Exception("No such option: " + o)

if not filename:
    print >>sys.stderr,"ERROR: No FoLiA document specified (use -f)"
    usage()
    sys.exit(2)    
    

if '*' in filename or '?' in filename:
    filenames = glob.glob(filename)
else:
    filenames = [filename]

if outputfile: outputfile = codecs.open(outputfile,'w',encoding)

for filename in filenames:
    doc = folia.Document(file=filename)

    if autooutput:    
        if filename[-4:].lower() == '.xml':
            outfilename = filename[-4:] + '.txt'
        else:
            outfilename += '.txt'
        
        outputfile = codecs.open(outfilename,'w',encoding)

    if wordperline:
        for word in doc.words():        
            if outputfile:
                outputfile.write(word.text('current', retaintokenisation) + "\n")
            else:
                print word.encode(encoding)
    elif sentenceperline:    
        for sentence in doc.sentences():        
            if outputfile:
                outputfile.write(sentence.text('current', retaintokenisation) + "\n")
            else:
                print word.encode(encoding)    
    elif paragraphperline:    
        for paragraph in doc.paragraphs():        
            if outputfile:
                outputfile.write(paragraph.text('current', retaintokenisation) + "\n")
            else:
                print word.encode(encoding)     
    else:
        if outputfile:
            outputfile.write( doc.text('current', retaintokenisation) )
        else:
            print doc.text('current', retaintokenisation).encode(encoding)

    if autooutput:
        outputfile.close()
