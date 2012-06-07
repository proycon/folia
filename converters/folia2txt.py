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


   
try:
    opts, args = getopt.getopt(sys.argv[1:], "f:d:o:OE:htspwr", ["help"])
except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(2)

filename = None
dirname = None

outputfile = None

allowemptylines = True
wordperline = False
sentenceperline = False
paragraphperline = False
detokenise = False
retaintokenisation = False
autooutput = False
extension = 'xml'
recurse = False

encoding = 'utf-8'

for o, a in opts:
    if o == '-f':
        filename = a
    elif o == '-d':
        dirname = a
    elif o == '-h':
        usage()
        sys.exit(0)
    elif o == '-t':
        retaintokenisation = True
    elif o == '-e':
        encoding = a
    elif o == '-E':
        extension = a
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
    elif o == '-r':
        recurse = True
    else:
        
        raise Exception("No such option: " + o)

if not filename and not dirname:
    print >>sys.stderr,"ERROR: No FoLiA document specified (use -f or -d)"
    usage()
    sys.exit(2)    
    

def process(filename):
    global autooutput, outputfile
    print >>sys.stderr, "Converting " + filename
    doc = folia.Document(file=filename)

    if autooutput:    
        if filename[-len(extension) - 1:].lower() == '.' + extension:
            outfilename = filename[:-len(extension) - 1] + '.txt'
        else:
            outfilename += '.txt'
        
        print >>sys.stderr, " Saving as " + outfilename
        outputfile = codecs.open(outfilename,'w',encoding)

    if wordperline:
        for word in doc.words():        
            if outputfile:
                outputfile.write(word.text('current', retaintokenisation) + "\n")
            else:
                print word.text('current', retaintokenisation).encode(encoding)
    elif sentenceperline:    
        for sentence in doc.sentences():        
            if outputfile:
                outputfile.write(sentence.text('current', retaintokenisation) + "\n")
            else:
                print sentence.text('current', retaintokenisation).encode(encoding)    
    elif paragraphperline:    
        for paragraph in doc.paragraphs():        
            if outputfile:
                outputfile.write(paragraph.text('current', retaintokenisation) + "\n")
            else:
                print paragraph.text('current', retaintokenisation).encode(encoding)     
    else:
        if outputfile:
            outputfile.write( doc.text(retaintokenisation) )
        else:
            print doc.text( retaintokenisation).encode(encoding)

    if autooutput:
        outputfile.close()
    


def processdir(d, extension, recurse):
    print >>sys.stderr, "Searching in  " + d
    for f in glob.glob(d + '/*'):        
        if f[-len(extension) - 1:] == '.' + extension: 
            process(f)
        elif recurse and os.path.isdir(f):
            processdir(f, extension, recurse)
            

if outputfile: outputfile = codecs.open(outputfile,'w',encoding)
    
if filename:
    process(filename)
elif dirname:
    processdir(dirname, extension, recurse)
else:
    print >>sys.stderr,"Error: Nothing to do, specify -f or -d"
    
