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
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo pip install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git",file=sys.stderr)
    sys.exit(2)

def usage():
    print("folia2txt",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Tilburg University / Radboud University Nijmegen",file=sys.stderr)
    print("  2012-2016 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("This conversion script reads a FoLiA XML document and outputs the",file=sys.stderr)
    print("document's text as plain text, *without* any annotations.",file=sys.stderr)
    print("Use folia2annotatedtxt if you want limited support for inline annotations.",file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: folia2txt [options] file-or-dir1 file-or-dir2 ..etc..",file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for output:",file=sys.stderr)
    print("  -t                           Retain tokenisation, do not detokenise",file=sys.stderr)
    print("                               (By default output will be detokenised if",file=sys.stderr)
    print("                               such information is explicitly available in the",file=sys.stderr)
    print("                               FoLiA document)",file=sys.stderr)
    print("  -c                           Text class to output (defaults to: current)",file=sys.stderr)
    print("  -w                           One word per line",file=sys.stderr)
    print("  -s                           One sentence per line",file=sys.stderr)
    print("  -p                           One paragraph per line",file=sys.stderr)
    print("  -o [filename]                Output to a single file (instead of default stdout)",file=sys.stderr)
    print("  -e [encoding]                Output encoding (default: utf-8)",file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)
    print("  -O                           Output each file to similarly named .txt file",file=sys.stderr)
    print("  -P                           Like -O, but outputs to current working directory",file=sys.stderr)
    print("  -q                           Ignore errors",file=sys.stderr)

def out(s, outputfile):
    if sys.version < '3':
        if outputfile:
            outputfile.write(s + "\n")
        else:
            print(s.encode(settings.encoding))
    else:
        if outputfile:
            print(s,file=outputfile)
        else:
            print(s)


def process(filename, outputfile = None):
    print("Converting " + filename,file=sys.stderr)
    try:
        doc = folia.Document(file=filename)

        if settings.autooutput:
            if filename[-len(settings.extension) - 1:].lower() == '.' +settings.extension:
                outfilename = filename[:-len(settings.extension) - 1] + '.txt'
            else:
                outfilename += '.txt'
            if settings.autooutput_cwd:
                outfilename = os.path.basename(outfilename)

            print(" Saving as " + outfilename,file=sys.stderr)
            outputfile = io.open(outfilename,'w',encoding=settings.encoding)

        if settings.wordperline:
            for word in doc.words():
                out(word.text(settings.textclass, settings.retaintokenisation), outputfile)
        elif settings.sentenceperline:
            for sentence in doc.sentences():
                out(sentence.text(settings.textclass, settings.retaintokenisation) , outputfile)
        elif settings.paragraphperline:
            for paragraph in doc.paragraphs():
                out(paragraph.text(settings.textclass, settings.retaintokenisation) , outputfile)
        else:
            out(doc.text(settings.textclass, settings.retaintokenisation) , outputfile)

        if settings.autooutput:
            outputfile.close()
        elif outputfile:
            outputfile.flush()
    except Exception as e:
        if settings.ignoreerrors:
            print("ERROR: An exception was raised whilst processing " + filename + ":", e, file=sys.stderr)
        else:
            raise




def processdir(d, outputfile = None):
    print("Searching in  " + d, file=sys.stderr)
    for f in glob.glob(os.path.join(d, '*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            process(f, outputfile)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, outputfile)


class settings:
    wordperline = False
    sentenceperline = False
    paragraphperline = False
    retaintokenisation = False
    autooutput = False
    autooutput_cwd = False
    extension = 'xml'
    recurse = False
    ignoreerrors = False
    encoding = 'utf-8'
    textclass = "current"


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:OPE:htspwrqc:", ["help"])
    except getopt.GetoptError as err:
        print(str(err), file=sys.stderr)
        usage()
        sys.exit(2)


    outputfile = None


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
            outputfile = a
        elif o == '-O':
            settings.autooutput = True
        elif o == '-P':
            settings.autooutput = True
            settings.autooutput_cwd = True
        elif o == '-c':
            settings.textclass = a
        elif o == '-s':
            settings.sentenceperline = True
        elif o == '-p':
            settings.paragraphperline = True
        elif o == '-w':
            settings.wordperline = True
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            settings.ignoreerrors = True
        else:
            raise Exception("No such option: " + o)


    if outputfile: outputfile = io.open(outputfile,'w',encoding=settings.encoding)

    if args:
        for x in args:
            if os.path.isdir(x):
                processdir(x,outputfile)
            elif os.path.isfile(x):
                process(x, outputfile)
            else:
                print("ERROR: File or directory not found: " + x, file=sys.stderr)
                sys.exit(3)
    else:
        print("ERROR: Nothing to do, specify one or more files or directories", file=sys.stderr)

    if outputfile: outputfile.close()

if __name__ == "__main__":
    main()
