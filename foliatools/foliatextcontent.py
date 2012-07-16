#! /usr/bin/env python
# -*- coding: utf8 -*-


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
    print >>sys.stderr, "foliatextcontent"
    print >>sys.stderr, "  by Maarten van Gompel (proycon)"
    print >>sys.stderr, "  Radboud University Nijmegen"
    print >>sys.stderr, "  2012 - Licensed under GPLv3"
    print >>sys.stderr, ""
    print >>sys.stderr, "This conversion takes a FoLiA XML document and adds text content element on higher levels, adding offset information."    
    print >>sys.stderr, ""
    print >>sys.stderr, "Usage: folia2txt [options] file-or-dir1 file-or-dir2 ..etc.."
    print >>sys.stderr, ""
    print >>sys.stderr, "Parameters for output:"        
    print >>sys.stderr, "  -s                           Add text content on sentence level"
    print >>sys.stderr, "  -S                           Remove text content on sentence level"
    print >>sys.stderr, "  -p                           Add text content on paragraph level"
    print >>sys.stderr, "  -P                           Remove content on paragraph level"
    print >>sys.stderr, "  -t                           Add text content on global text level"
    print >>sys.stderr, "  -T                           Remove text content on global text level"
    print >>sys.stderr, "  -X                           Do not add offset information"    
    print >>sys.stderr, "  -e [encoding]                Output encoding (default: utf-8)"
    print >>sys.stderr, "  -w                           Edit file(s) (overwrites input files)" 
    print >>sys.stderr, "Parameters for processing directories:"
    print >>sys.stderr, "  -r                           Process recursively"
    print >>sys.stderr, "  -E [extension]               Set extension (default: xml)"



def addtext(element, subelementclass):
    if element.hastext():
        return False
    
    text = ""
    offset = 0
    for e in element.items():    
        if isinstance(e, subelementclass) and e.hastext():            
            textcontent = e.textcontent()       
            
            if textcontent.offset is None and settings.offsets:
                textcontent.offset = offset
                if not (e.parent is element):                    
                    textcontent.ref = element
                    
            offset += len(textcontent.value)        
            delimiter = e.overridetextdelimiter()  
            if delimiter: offset += len(delimiter)
            text += textcontent.value + delimiter       
        
        elif isinstance(e, folia.AbstractStructureElement) and e.TEXTDELIMITER:  
            if text:
                text += e.TEXTDELIMITER
                offset += len(e.TEXTDELIMITER) 

    text = text.strip()            
    element.append(folia.TextContent, cls='current', value=text)    
    return text
        
    

def process(filename, outputfile = None):
    print >>sys.stderr, "Converting " + filename
    doc = folia.Document(file=filename)
    
    
    if settings.sentencelevel == 1:
        for e in doc.sentences():
            addtext(e, folia.Word)
        
    if settings.paragraphlevel == 1:
        if settings.sentencelevel == 1:
            subelementclass = folia.Sentence
        else:
            subelementclass = folia.Word
        for e in doc.paragraphs():
            addtext(e, subelementclass)        
        
    if settings.globallevel == 1:
        if settings.paragraphlevel == 1:
            subelementclass = folia.Paragraph        
        if settings.sentencelevel == 1:
            subelementclass = folia.Sentence
        else:
            subelementclass = folia.Word
        for e in doc:
            addtext(e, subelementclass) 
                    
    if settings.inplaceedit:
        doc.save()
    else:
        print doc.xmlstring()

def processdir(d, outputfile = None):
    print >>sys.stderr, "Searching in  " + d
    for f in glob.glob(d + '/*'):        
        if f[-len(settings.extension) - 1:] == '.' + settings.extension: 
            process(f, outputfile)
        elif settings.recurse and os.path.isdir(f):
            processdir(f)
            
            

class settings:
    globallevel = 0
    sentencelevel = 0
    paragraphlevel = 0
    divlevel = 0
    inplaceedit = False
    offsets = True
    
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'


def main():   
    try:
        opts, args = getopt.getopt(sys.argv[1:], "E:hsSpPdDtTXe:w", ["help"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)


    outputfile = None
    

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-t':
            settings.globallevel = 1          
        elif o == '-s':
            settings.sentencelevel = 1            
        elif o == '-p':
            settings.paragraphlevel = 1            
        elif o == '-T':
            settings.globallevel = -1           
        elif o == '-S':
            settings.sentencelevel = -1            
        elif o == '-P':
            settings.paragraphlevel = -1            
        elif o == '-X':
            settings.offsets = False
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-w':
            settings.inplaceedit = True     
        elif o == '-r':
            settings.recurse = True
        else:            
            raise Exception("No such option: " + o)
                
    
    if outputfile: outputfile = codecs.open(outputfile,'w',settings.encoding)
        
    if args:
        for x in args:
            if os.path.isdir(x):
                processdir(x,outputfile)
            elif os.path.isfile(x):
                process(x, outputfile)    
            else:
                print >>sys.stderr, "ERROR: File or directory not found: " + x
                sys.exit(3)
    else:
        print >>sys.stderr,"ERROR: Nothing to do, specify one or more files or directories"
    
if __name__ == "__main__":
    main()
