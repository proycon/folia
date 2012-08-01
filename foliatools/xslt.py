# -*- coding: utf8 -*-

import lxml.etree
import sys
import glob
import getopt
import os.path

def transform(xsltfilename, sourcefilename, targetfilename = None, encoding = 'utf-8'):    
    xsldir = os.path.dirname(__file__)
    if xsltfilename[0] != '/': xsltfilename = xsldir + '/' + xsltfilename
    if not os.path.exists(xsltfilename):
        raise Exception("XSL Stylesheet not found: " + xsltfilename)
    elif not os.path.exists(sourcefilename):
        raise Exception("File not found: " + sourcefilename)        
    xslt = lxml.etree.parse(xsltfilename)
    transformer = lxml.etree.XSLT(xslt)
    parsedsource = lxml.etree.parse(sourcefilename)
    transformed = transformer(parsedsource)
    if targetfilename:
        f = open(targetfilename, 'w')
        f.write( lxml.etree.tostring(transformed, pretty_print=True, encoding=encoding) )
        f.close()
    else:
        print lxml.etree.tostring(transformed, pretty_print=True, encoding=encoding)
        
        
def usage():        
    print >>sys.stderr, settings.usage
    print >>sys.stderr, ""
    print >>sys.stderr, "Parameters for output:"        
    print >>sys.stderr, "  -o [filename]                Output to file (instead of default stdout)"    
    print >>sys.stderr, "  -e [encoding]                Output encoding (default: utf-8)" 
    print >>sys.stderr, "Parameters for processing directories:"
    print >>sys.stderr, "  -r                           Process recursively"
    print >>sys.stderr, "  -E [extension]               Set extension (default: xml)"
    print >>sys.stderr, "  -q                           Ignore errors"
    
    

class settings:
    autooutput = False
    extension = 'xml'
    recurse = False
    ignoreerrors = False
    encoding = 'utf-8'
    xsltfilename = "undefined.xsl"
    outputextension = 'UNDEFINED'
    usage = "UNDEFINED"

def processdir(d, outputfilename = None):
    print >>sys.stderr, "Searching in  " + d
    for f in glob.glob(d + '/*'):        
        if f[-len(settings.extension) - 1:] == '.' + settings.extension and f[-len(settings.outputextension) - 1:] != '.' + settings.outputextension: 
            outputfilename =  f[:-len(settings.extension) - 1] + '.' + settings.outputextension
            process(f, outputfilename)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, outputfilename)
    
def process(inputfilename, outputfilename=None):    
    try:
        transform(settings.xsltfilename, inputfilename, outputfilename, settings.encoding)
    except Exception as e:
        if settings.ignoreerrors:
            print >>sys.stderr, "ERROR: An exception was raised whilst processing " + inputfilename + ":", e            
        else:
            raise        
    

def main(xsltfilename, outputextension, usagetext):   
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:E:hrq", ["help"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    settings.xsltfilename = xsltfilename
    settings.outputextension = outputextension
    settings.usage = usagetext
    
    outputfilename = ""
    

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-t':
            settings.retaintokenisation = True
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-o':
            outputfilename = a
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            settings.ignoreerrors = True
        else:            
            raise Exception("No such option: " + o)
                
    if args:              
        for x in args:
            if os.path.isdir(x):
                processdir(x)
            elif os.path.isfile(x):
                if len(sys.argv) > 2: outputfilename = outputfilename =  x[:-len(settings.extension) - 1] + '.' + settings.outputextension
                process(x, outputfilename)    
            else:
                print >>sys.stderr, "ERROR: File or directory not found: " + x
                sys.exit(3)
    else:
        print >>sys.stderr,"ERROR: Nothing to do, specify one or more files or directories"
