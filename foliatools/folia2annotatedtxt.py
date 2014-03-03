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
    print >>sys.stderr, "folia2annotatedtxt"
    print >>sys.stderr, "  by Maarten van Gompel (proycon)"
    print >>sys.stderr, "  Tilburg University / Radboud University Nijmegen"
    print >>sys.stderr, "  2012 - Licensed under GPLv3"
    print >>sys.stderr, ""
    print >>sys.stderr, "This conversion script reads a FoLiA XML document and produces a"
    print >>sys.stderr, "simple inline output format in which tokens are space-separated and annotations are separated by a pipe symbol (|)"
    print >>sys.stderr, "Note that only simple token annotations are supported and a lot"
    print >>sys.stderr, "of FoLiA data can not be intuitively expressed in a simple columned format!"
    print >>sys.stderr, ""
    print >>sys.stderr, "Usage: folia2inline [options] -C [columns] file-or-dir1 file-or-dir2 ..etc.."

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
    print >>sys.stderr, "  -o [filename]                Output to a single output file instead of stdout"
    print >>sys.stderr, "  -O                           Output each file to similarly named file (.columns or .csv)"
    print >>sys.stderr, "  -e [encoding]                Output encoding (default: utf-8)"
    print >>sys.stderr, "  -S                           Output one sentence per line"
    print >>sys.stderr, "Parameters for processing directories:"
    print >>sys.stderr, "  -r                           Process recursively"
    print >>sys.stderr, "  -E [extension]               Set extension (default: xml)"
    print >>sys.stderr, "  -O                           Output each file to similarly named .txt file"
    print >>sys.stderr, "  -P                           Like -O, but outputs to current working directory"
    print >>sys.stderr, "  -q                           Ignore errors"

class settings:
    output_header = True
    outputfile = None
    ignoreerrors = False
    autooutput = False
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'
    sentenceperline = False
    columnconf = []

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:OPhHSc:x:E:rq", ["help", "csv"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    outputfile = None

    for o, a in opts:
        if o == '-c':
            for a in a.split(','):
                settings.columnconf.append(a)
        elif o == '-h':
            usage()
            sys.exit(0)
        elif o == '-H':
            settings.output_header = False
        elif o == '-e':
            settings.encoding = a
        elif o == '-o':
            outputfile = a
        elif o == '-O':
            settings.autooutput = True
        elif o == '-P':
            settings.autooutput = True
            settings.autooutput_cwd = True
        elif o == '-E':
            settings.extension = a
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            settings.ignoreerrors = True
        elif o == '-S':
            settings.sentenceperline = True
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
        prevpar = None

        if settings.autooutput:
            ext = '.txt'
            if filename[-len(settings.extension) - 1:].lower() == '.' +settings.extension:
                outfilename = filename[:-len(settings.extension) - 1] + ext
            else:
                outfilename += ext
            if settings.autooutput_cwd:
                outfilename = os.path.basename(outfilename)

            print >>sys.stderr, " Saving as " + outfilename
            outputfile = codecs.open(outfilename,'w',settings.encoding)


        wordnum = 0


        for i, w in enumerate(doc.words()):
            if settings.sentenceperline:
                if w.sentence() != prevsen and i > 0:
                    if outputfile:
                        outputfile.write("\n")
                    else:
                        print
                wordnum = 0
            if w.paragraph() != prevpar and i > 0:
                if outputfile:
                    outputfile.write("\n")
                else:
                    print
                wordnum = 0
            prevpar = w.paragraph()
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


            word = "|".join(columns).strip()
            if outputfile:
                if wordnum > 1: outputfile.write(" ")
                outputfile.write(word)
            else:
                #if wordnum > 1: print " ",
                print word.encode(settings.encoding),

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
