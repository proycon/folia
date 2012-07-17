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
    print >>sys.stderr, "  -p                           Add text content on paragraph level"    
    print >>sys.stderr, "  -d                           Add text content on division level"
    print >>sys.stderr, "  -t                           Add text content on global text level"    
    print >>sys.stderr, "  -X                           Do NOT add offset information"    
    print >>sys.stderr, "  -e [encoding]                Output encoding (default: utf-8)"
    print >>sys.stderr, "  -w                           Edit file(s) (overwrites input files)" 
    print >>sys.stderr, "Parameters for processing directories:"
    print >>sys.stderr, "  -r                           Process recursively"
    print >>sys.stderr, "  -E [extension]               Set extension (default: xml)"



def propagatetext(element, Classes, setoffset=True,  cls='current', previousdelimiter=""):
       
    if not element.PRINTABLE: #only printable elements can hold text
        raise folia.NoSuchText
   
    #print >>sys.stderr, repr(element), element.id
    
    if element.hastext(cls):            
        s = element.textcontent(cls).value
        #print >>stderr, "text content: " + s            
    else:                 
        addtext = False
        for c in Classes:
            if isinstance(element,c):
                addtext = True
                break
        
        #Not found, descend into children
        delimiter = ""
        s = ""            
        for e in element:            
            if e.PRINTABLE and not isinstance(e, folia.TextContent):
                try:
                    t = propagatetext(e,  Classes, setoffset,cls, delimiter)
                    if addtext and setoffset and e.hastext(cls):
                        extraoffset = len(t) - len(e.textcontent(cls).value)
                        e.textcontent(cls).offset = len(s) + extraoffset
                    s += t
                    delimiter = e.gettextdelimiter(False)
                    #delimiter will be buffered and only printed upon next iteration, this prevent the delimiter being output at the end of a sequence
                    #print >>stderr, "Delimiter for " + repr(e) + ": " + repr(delimiter)
                except folia.NoSuchText:
                    continue           
                
    
        s = s.strip(' \r\n\t')
        if s and addtext:
            element.append(folia.TextContent, cls=cls, value=s)

    s = s.strip(' \r\n\t')
    if s and previousdelimiter:
        #print >>stderr, "Outputting previous delimiter: " + repr(previousdelimiter)
        return previousdelimiter + s
    elif s:
        return s
    else:
        print >>sys.stderr, "No text for: " + repr(element)
        #No text found at all :`(
        raise folia.NoSuchText
        
def process(filename, outputfile = None):
    print >>sys.stderr, "Converting " + filename
    doc = folia.Document(file=filename)
    
    propagatetext(doc.data[0], settings.Classes, settings.offsets)

                    
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
    Classes = []
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
        elif o == '-d':
            settings.Classes.append(folia.Division)            
        elif o == '-t':
            settings.Classes.append(folia.Text)            
        elif o == '-s':
            settings.Classes.append(folia.Sentence)            
        elif o == '-p':
            settings.Classes.append(folia.Paragraph)                        
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
