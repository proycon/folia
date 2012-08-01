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
    print >>sys.stderr, "folia2columns"
    print >>sys.stderr, "  by Maarten van Gompel (proycon)"
    print >>sys.stderr, "  Tilburg University / Radboud University Nijmegen"
    print >>sys.stderr, "  2012 - Licensed under GPLv3"
    print >>sys.stderr, ""
    print >>sys.stderr, "This conversion script reads a FoLiA XML document and produces a"
    print >>sys.stderr, "simple columned output format in which each token appears on one"
    print >>sys.stderr, "line. Note that only simple token annotations are supported and a lot"
    print >>sys.stderr, "of FoLiA data can not be intuitively expressed in a simple columned format!"
    print >>sys.stderr, ""
    print >>sys.stderr, "Usage: folia2columns [options] -C [columns] file-or-dir1 file-or-dir2 ..etc.."
    
    print >>sys.stderr, "Parameters:"    
    print >>sys.stderr, "  -c [columns]                 Comma separated list of desired column layout (mandatory), choose from:"
    print >>sys.stderr, "                               id      - output word ID"
    print >>sys.stderr, "                               text    - output the text of the word (the word itself)"    
    print >>sys.stderr, "                               pos     - output PoS annotation class"
    print >>sys.stderr, "                               poshead - output PoS annotation head feature"
    print >>sys.stderr, "                               lemma   - output lemma annotation class"
    print >>sys.stderr, "                               sense   - output sense annotation class"
    print >>sys.stderr, "                               phon    - output phonetic annotation class"
    print >>sys.stderr, "                               senid   - output sentence ID"
    print >>sys.stderr, "                               parid   - output paragraph ID"
    print >>sys.stderr, "                               N     - word/token number (absolute)"
    print >>sys.stderr, "                               n     - word/token number (relative to sentence)"
    print >>sys.stderr, "Options:"
    print >>sys.stderr, "  --csv                        Output in CSV format"            
    print >>sys.stderr, "  -o [filename]                Output to a single output file instead of stdout"
    print >>sys.stderr, "  -O                           Output each file to similarly named file (.columns or .csv)"
    print >>sys.stderr, "  -e [encoding]                Output encoding (default: utf-8)"
    print >>sys.stderr, "  -H                           Suppress header output"    
    print >>sys.stderr, "  -S                           Suppress sentence spacing  (no whitespace between sentences)"            
    print >>sys.stderr, "  -x [sizeinchars]             Space columns for human readability (instead of plain tab-separated columns)"    
    print >>sys.stderr, "Parameters for processing directories:"
    print >>sys.stderr, "  -r                           Process recursively"
    print >>sys.stderr, "  -E [extension]               Set extension (default: xml)"
    print >>sys.stderr, "  -O                           Output each file to similarly named .txt file"
    print >>sys.stderr, "  -q                           Ignore errors"    

class settings:
    output_header = True
    csv = False
    outputfile = None
    sentencespacing = True
    ignoreerrors = False
    nicespacing = 0
    autooutput = False
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'
    columnconf = []
    
def main():    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:OhHSc:x:E:rq", ["help", "csv"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)


    for o, a in opts:
        if o == '-c':
            for a in a.split(','):
                settings.columnconf.append(a)
        elif o == '-h':
            usage()
            sys.exit(0)
        elif o == '-H':
            settings.output_header = False        
        elif o == '-S':
            settings.sentencespacing = False
        elif o == '-e':
            settings.encoding = a
        elif o == '-o':
            outputfile = a
        elif o == '-O':
            settings.autooutput = True
        elif o == '-x':        
            settings.nicespacing = int(a)
        elif o == '-E':
            settings.extension = a
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            settings.ignoreerrors = True            
        elif o == '--csv':
            settings.csv = True
        else:
            raise Exception("No such option: " + o)

    if not settings.columnconf:
        print >>sys.stderr,"ERROR: No column configuration specified (use -c)"
        usage()
        sys.exit(2)
        
    
    if args:
        if outputfile: outputfile = codecs.open(outputfile,'w',settings.encoding)
        for x in args:
            if os.path.isdir(x):
                processdir(x,outputfile)
            elif os.path.isfile(x):
                process(x, outputfile)    
            else:
                print >>sys.stderr, "ERROR: File or directory not found: " + x
                sys.exit(3)
        if outputfile: outputfile.close()                
    else:
        print >>sys.stderr,"ERROR: Nothing to do, specify one or more files or directories"
    
    
    
def resize(s, i, spacing):
    if len(s) >= spacing[i]:
        s = s[0:spacing[i] - 1] + ' '
    elif len(s) < spacing[i]:
        s = s + (' ' * (spacing[i] - len(s)))
    #print '[' + s + ']', len(s), spacing[i]
    return s

def processdir(d, outputfile = None):
    print >>sys.stderr, "Searching in  " + d
    for f in glob.glob(d + '/*'):        
        if f[-len(settings.extension) - 1:] == '.' + settings.extension: 
            process(f, outputfile)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, outputfile)

def process(filename, outputfile=None):
    try:
        print >>sys.stderr, "Processing " + filename
        doc = folia.Document(file=filename)
        prevsen = None

        if settings.autooutput:    
            if settings.csv:
                ext = '.csv'
            else: 
                ext = '.columns'
            if filename[-len(settings.extension) - 1:].lower() == '.' +settings.extension:
                outfilename = filename[:-len(settings.extension) - 1] + ext
            else:
                outfilename += ext
            
            print >>sys.stderr, " Saving as " + outfilename
            outputfile = codecs.open(outfilename,'w',settings.encoding)
                    
            
        if settings.nicespacing:
            spacing = []
            for c in settings.columnconf:
                if c == 'n':
                    spacing.append(3)
                elif c == 'N':
                    spacing.append(7)
                elif c == 'poshead':
                    spacing.append(5)
                else:
                    spacing.append(settings.nicespacing)
            
        if settings.output_header:        
            
            if settings.csv:
                columns = [ '"' + x.upper()  + '"' for x in settings.columnconf ]
            else:
                columns = [ x.upper()  for x in settings.columnconf ]

            if settings.nicespacing and not settings.csv:
                columns = [ resize(x, i, spacing) for i, x in enumerate(settings.columnconf) ]
            
            if settings.csv:
                line = ','.join(columns)
            else:
                line = '\t'.join(columns)

            if outputfile:
                outputfile.write(line + '\n')
            else:    
                print line.encode(settings.encoding)    

        wordnum = 0



        for i, w in enumerate(doc.words()):
            if w.sentence() != prevsen and i > 0:
                if settings.sentencespacing:
                    if outputfile:
                        outputfile.write('\n')
                    else:
                        print         
                wordnum = 0
            prevsen = w.sentence()
            wordnum += 1
            columns = []
            for c in settings.columnconf:
                if c == 'id':
                    columns.append(w.id)
                elif c == 'text':
                    columns.append(w.text())
                elif c == 'n':
                    columns.append(str(wordnum))
                elif c == 'N':
                    columns.append(str(i+1))
                elif c == 'pos':
                    try:
                        columns.append(w.annotation(folia.PosAnnotation).cls)    
                    except:
                        columns.append('-')
                elif c == 'poshead':
                    try:
                        columns.append(w.annotation(folia.PosAnnotation).feat('head'))    
                    except:
                        columns.append('-')     
                elif c == 'lemma':
                    try:
                        columns.append(w.annotation(folia.LemmaAnnotation).cls)    
                    except:
                        columns.append('-')
                elif c == 'sense':
                    try:
                        columns.append(w.annotation(folia.SenseAnnotation).cls)    
                    except:
                        columns.append('-')
                elif c == 'phon':
                    try:
                        columns.append(w.annotation(folia.PhonAnnotation).cls)    
                    except:
                        columns.append('-')                
                elif c == 'senid':
                    columns.append(w.sentence().id)
                elif c == 'parid':            
                    try:
                        columns.append(w.paragraph().id)
                    except:
                        columns.append('-')
                elif c:
                    print >>sys.stderr,"ERROR: Unsupported configuration: " + c
                    sys.exit(1)
                
            if settings.nicespacing and not settings.csv:
                columns = [ resize(x,j, spacing) for j,x  in enumerate(columns) ]
                
            if settings.csv:
                line = ",".join([ '"' + x  + '"' for x in columns ]) 
            else:
                line = "\t".join(columns)
                
            if outputfile:
                outputfile.write(line+'\n')
            else:    
                print line.encode(settings.encoding)

        if settings.autooutput:
            outputfile.close()
        elif outputfile:
            outputfile.flush()
    except Exception as e:
        if settings.ignoreerrors:
            print >>sys.stderr, "ERROR: An exception was raised whilst processing " + filename, e            
        else:
            raise        
        
if __name__ == "__main__":
    main()
