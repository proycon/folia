#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import getopt
import io
import sys
import os
import glob
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo pip install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git", file=sys.stderr)
    sys.exit(2)

def usage():
    print("folia2columns", file=sys.stderr)
    print("  by Maarten van Gompel (proycon)", file=sys.stderr)
    print("  Tilburg University / Radboud University Nijmegen", file=sys.stderr)
    print("  2012 - Licensed under GPLv3", file=sys.stderr)
    print("", file=sys.stderr)
    print("This conversion script reads a FoLiA XML document and produces a", file=sys.stderr)
    print("simple columned output format in which each token appears on one", file=sys.stderr)
    print("line. Note that only simple token annotations are supported and a lot", file=sys.stderr)
    print("of FoLiA data can not be intuitively expressed in a simple columned format!", file=sys.stderr)
    print("", file=sys.stderr)
    print("Usage: folia2columns [options] -C [columns] file-or-dir1 file-or-dir2 ..etc..", file=sys.stderr)

    print("Parameters:", file=sys.stderr)
    print("  -c [columns]                 Comma separated list of desired column layout (mandatory), choose from:", file=sys.stderr)
    print("                               id      - output word ID", file=sys.stderr)
    print("                               text    - output the text of the word (the word itself)", file=sys.stderr)
    print("                               pos     - output PoS annotation class", file=sys.stderr)
    print("                               poshead - output PoS annotation head feature", file=sys.stderr)
    print("                               lemma   - output lemma annotation class", file=sys.stderr)
    print("                               sense   - output sense annotation class", file=sys.stderr)
    print("                               phon    - output phonetic annotation class", file=sys.stderr)
    print("                               senid   - output sentence ID", file=sys.stderr)
    print("                               parid   - output paragraph ID", file=sys.stderr)
    print("                               N     - word/token number (absolute)", file=sys.stderr)
    print("                               n     - word/token number (relative to sentence)", file=sys.stderr)
    print("Options:", file=sys.stderr)
    print("  --csv                        Output in CSV format", file=sys.stderr)
    print("  -o [filename]                Output to a single output file instead of stdout", file=sys.stderr)
    print("  -O                           Output each file to similarly named file (.columns or .csv)", file=sys.stderr)
    print("  -e [encoding]                Output encoding (default: utf-8)", file=sys.stderr)
    print("  -H                           Suppress header output", file=sys.stderr)
    print("  -S                           Suppress sentence spacing  (no whitespace between sentences)", file=sys.stderr)
    print("  -x [sizeinchars]             Space columns for human readability (instead of plain tab-separated columns)", file=sys.stderr)
    print("Parameters for processing directories:", file=sys.stderr)
    print("  -r                           Process recursively", file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)", file=sys.stderr)
    print("  -O                           Output each file to similarly named .txt file", file=sys.stderr)
    print("  -P                           Like -O, but outputs to current working directory", file=sys.stderr)
    print("  -q                           Ignore errors", file=sys.stderr)

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
        opts, args = getopt.getopt(sys.argv[1:], "o:OPhHSc:x:E:rq", ["help", "csv"])
    except getopt.GetoptError as err:
        print(str(err), file=sys.stderr)
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
        elif o == '-S':
            settings.sentencespacing = False
        elif o == '-e':
            settings.encoding = a
        elif o == '-o':
            outputfile = a
        elif o == '-O':
            settings.autooutput = True
        elif o == '-P':
            settings.autooutput = True
            settings.autooutput_cwd = True
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
        print("ERROR: No column configuration specified (use -c)", file=sys.stderr)
        usage()
        sys.exit(2)


    if args:
        if outputfile: outputfile = io.open(outputfile,'w',encoding=settings.encoding)
        for x in args:
            if os.path.isdir(x):
                processdir(x,outputfile)
            elif os.path.isfile(x):
                process(x, outputfile)
            else:
                print("ERROR: File or directory not found: " + x, file=sys.stderr)
                sys.exit(3)
        if outputfile: outputfile.close()
    else:
        print ("ERROR: Nothing to do, specify one or more files or directories", file=sys.stderr)



def resize(s, i, spacing):
    if len(s) >= spacing[i]:
        s = s[0:spacing[i] - 1] + ' '
    elif len(s) < spacing[i]:
        s = s + (' ' * (spacing[i] - len(s)))
    #print '[' + s + ']', len(s), spacing[i]
    return s

def processdir(d, outputfile = None):
    print("Searching in  " + d, file=sys.stderr)
    for f in glob.glob(os.path.join(d, '*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            process(f, outputfile)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, outputfile)

def process(filename, outputfile=None):
    try:
        print("Processing " + filename, file=sys.stderr)
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
            if settings.autooutput_cwd:
                outfilename = os.path.basename(outfilename)

            print(" Saving as " + outfilename, file=sys.stderr)
            outputfile = io.open(outfilename,'w',encoding=settings.encoding)


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
                outputfile.write(line)
                outputfile.write('\n')
            else:
                if sys.version < '3':
                    print(line.encode(settings.encoding))
                else:
                    print(line)

        wordnum = 0



        for i, w in enumerate(doc.words()):
            if w.sentence() != prevsen and i > 0:
                if settings.sentencespacing:
                    if outputfile:
                        outputfile.write('\n')
                    else:
                        print()
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
                    print("ERROR: Unsupported configuration: " + c, file=sys.stderr)
                    sys.exit(1)

            if settings.nicespacing and not settings.csv:
                columns = [ resize(x,j, spacing) for j,x  in enumerate(columns) ]

            if settings.csv:
                line = ",".join([ '"' + x  + '"' for x in columns ])
            else:
                line = "\t".join(columns)

            if outputfile:
                outputfile.write(line)
                outputfile.write('\n')
            else:
                if sys.version < '3':
                    print(line.encode(settings.encoding))
                else:
                    print(line)

        if settings.autooutput:
            outputfile.close()
        elif outputfile:
            outputfile.flush()
    except Exception as e:
        if settings.ignoreerrors:
            print("ERROR: An exception was raised whilst processing " + filename, e, file=sys.stderr)
        else:
            raise

if __name__ == "__main__":
    main()
