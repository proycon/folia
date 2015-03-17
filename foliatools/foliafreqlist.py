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
    from pynlpl.statistics import FrequencyList
    from pynlpl.textprocessors import Windower
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git",file=sys.stderr)
    sys.exit(2)

def usage():
    print("foliafreqlist",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Radboud University Nijmegen",file=sys.stderr)
    print("  2012 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("Compute a frequency list on one or more *tokenised* FoLiA documents.",file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: foliafreqlist [options] file-or-dir1 file-or-dir2 ..etc..",file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for output:",file=sys.stderr)
    print("  -i                           Case insensitive",file=sys.stderr)
    print("  -n [n]                       Count n-grams rather than unigrams",file=sys.stderr)
    print("  -s                           Add begin/end of sentence markers (with -n > 1)",file=sys.stderr)
    print("  -o [filename]                Output to a single file (instead of default stdout)",file=sys.stderr)
    print("  -e [encoding]                Output encoding (default: utf-8)",file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)
    print("  -O                           Output each file to similarly named .freqlist file",file=sys.stderr)
    print("  -q                           Ignore errors",file=sys.stderr)





def process(filename):
    try:
        print("Processing " + filename,file=sys.stderr)
        doc = folia.Document(file=filename)

        freqlist = FrequencyList()

        if settings.n == 1:
            for word in doc.words():
                text = word.toktext()
                if settings.casesensitive: text = text.lower()
                freqlist.count(text)
        elif settings.sentencemarkers:
            for sentence in doc.sentences():
                for ngram in Windower(sentence.words(), settings.n):
                    text = ' '.join([x for x in ngram.toktext() ])
                    if settings.casesensitive: text = text.lower()
                    freqlist.count(text)
        else:
            for word in Windower(sentence.words(), settings.n, None, None):
                text = ' '.join([x for x in ngram.toktext() ])
                if settings.casesensitive: text = text.lower()
                freqlist.count(text)

        if settings.autooutput:
            if filename[-len(settings.extension) - 1:].lower() == '.' +settings.extension:
                outfilename = filename[:-len(settings.extension) - 1] + '.freqlist'
            else:
                outfilename += '.freqlist'
            freqlist.save(outfilename,True)
    except Exception as e:
        if settings.ignoreerrors:
            print("ERROR: An exception was raised whilst processing " + filename, e,file=sys.stderr)
        else:
            raise

    return freqlist



def processdir(d, freqlist = None):
    if not freqlist: freqlist = FrequencyList()
    print("Searching in  " + d,file=sys.stderr)
    for f in glob.glob(os.path.join(d ,'*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            freqlist += process(f)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, freqlist)
    return freqlist


class settings:
    casesensitive = True
    autooutput = False
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'
    sentencemarkers = False
    ignoreerrors = False
    n = 1


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:OE:htspwrq", ["help"])
    except getopt.GetoptError as err:
        print(str(err),file=sys.stderr)
        usage()
        sys.exit(2)

    outputfile = None


    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-o':
            outputfile = a
        elif o == '-O':
            settings.autooutput = True
        elif o == '-s':
            settings.sentencemarkers = True
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            settings.ignoreerrors = True
        else:
            raise Exception("No such option: " + o)


    if outputfile: outputfile = io.open(outputfile,'w',encoding=settings.encoding)

    if len(sys.argv) >= 2:
        freqlist = FrequencyList()
        for x in sys.argv[1:]:
            if os.path.isdir(x):
                processdir(x,freqlist)
            elif os.path.isfile(x):
                freqlist += process(x)
            else:
                print("ERROR: File or directory not found: " + x,file=sys.stderr)
                sys.exit(3)
        if outputfile:
            freqlist.save(outputfile, True)
        else:
            for line in freqlist.output("\t", True):
                print(line)
    else:
        print("ERROR: No files specified",file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
