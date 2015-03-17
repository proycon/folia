#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import getopt
import sys
import os
import glob
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git",file=sys.stderr)
    sys.exit(2)

def usage():
    print("foliaquery",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Tilburg University / Radboud University Nijmegen",file=sys.stderr)
    print("  2012 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("Query one or more FoLiA documents for certain patterns.",file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: foliaquery [options] file-or-dir1 file-or-dir2 ..etc..",file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for output:"        ,file=sys.stderr)
    print("  --text \"[words]\"           Text pattern (Case sensitive)",file=sys.stderr)
    print("  --pos \"[postags]\"          Pos pattern",file=sys.stderr)
    print("  --lemma \"[lemmas]\"         Lemma pattern",file=sys.stderr)
    print("  --sense \"[sense]\"          Sense pattern",file=sys.stderr)
    print("  --phon \"[phon]\"            Phonetic pattern",file=sys.stderr)
    print("  -i                           Patterns are case-insensitive",file=sys.stderr)
    print("  -L [length]                  Left-context size words/tokens (default: 0)",file=sys.stderr)
    print("  -R [length]                  Right-context size in words/tokens (default: 0)"    ,file=sys.stderr)
    print("  -e [encoding]                Output encoding (default: utf-8)"     ,file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)
    print("  -q                           Ignore errors",file=sys.stderr)
    print("",file=sys.stderr)
    print("Pattern syntax:",file=sys.stderr)
    print("    Fixed-width wildcard: ^ ",file=sys.stderr)
    print("    Variable-width wildcard: * ",file=sys.stderr)
    print("    Disjunction: | ",file=sys.stderr)
    print("    Regular Expression: {REGEXP}",file=sys.stderr)

    print(""    ,file=sys.stderr)
    print("Examples:",file=sys.stderr)
    print("   1) foliaquery --text=\"to be * to be\"",file=sys.stderr)
    print("       Matches any gap of any size (up to the maximum)"    ,file=sys.stderr)
    print("   2) foliaquery --text=\"to be ^ ^ to be\""   ,file=sys.stderr)
    print("       Matches any gap of exactly two tokens",file=sys.stderr)
    print("   3) foliaquery --pos=\"ADJ NOUN\"",file=sys.stderr)
    print("       Searching by annotation"    ,file=sys.stderr)
    print("   4) foliaquery --text=\"rent\" --pos=\"NOUN\"",file=sys.stderr)
    print("       Patterns may be combined, matches have to satisfy all patterns",file=sys.stderr)
    print("   5) foliaquery --text=\"he leaves|departs today|tomorrow\" --pos=\"PRON VERB ^\"",file=sys.stderr)
    print("       The pipe character allows for disjunctions in single tokens",file=sys.stderr)
    print("   6a) foliaquery --text=\"we {w[io]n}\" --pos=\"PRON VERB\"",file=sys.stderr)
    print("   6b) foliaquery --text=\"{.*able}\" --pos=\"ADJ\"",file=sys.stderr)
    print("       Curly braces specify a regular expression for a single token"    ,file=sys.stderr)




def parsepattern(rawpattern, annotationtype): #, annotationset=None):
    components = []
    for tokenpattern in rawpattern.strip().split(' '):
        if tokenpattern == '*':
            components.append('*')
        elif tokenpattern == '^':
            components.append(True)
        elif tokenpattern[0] == '{' and tokenpattern[-1] == '}':
            components.append( folia.RegExp(tokenpattern[1:-1]) )
        elif '|' in tokenpattern:
            components.append( tuple(tokenpattern.split('|')) )
        else:
            components.append(tokenpattern)
    d = {'casesensitive':settings.casesensitive}
    if annotationtype:
        d['matchannotation'] = annotationtype
    return folia.Pattern(*components,**d) #, matchannotationset=annotationset)



def process(filename, patterns):
    try:
        print("Processing " + filename, file=sys.stderr)
        doc = folia.Document(file=filename)
        for match in doc.findwords(*patterns ):
            s = ""
            for token in match:
                s += "\t" + token.text()
            s = filename + "\t" + match[0].id + s
            if sys.version < '3':
                print(s.encode(settings.encoding))
            else:
                print(s)
    except Exception as e:
        if settings.ignoreerrors:
            print("ERROR: An exception was raised whilst processing " + filename + ":", e            ,file=sys.stderr)
        else:
            raise


def processdir(d, patterns):
    print("Searching in  " + d,file=sys.stderr)
    for f in glob.glob(os.path.join(d,'*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            process(f, patterns)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, patterns)


class settings:
    leftcontext = 0
    rightcontext = 0

    extension = 'xml'
    recurse = False
    encoding = 'utf-8'

    ignoreerrors = False
    casesensitive = True


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:OE:hqr", ["help","text=","pos=","lemma=","sense=","phon="])
    except getopt.GetoptError as err:
        print(str(err), file=sys.stderr)
        usage()
        sys.exit(2)



    patterns = []

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '--text':
            patterns.append( parsepattern(a, None) )
        elif o == '--pos':
            patterns.append( parsepattern(a, folia.PosAnnotation) )
        elif o == '--lemma':
            patterns.append( parsepattern(a, folia.LemmaAnnotation) )
        elif o == '--sense':
            patterns.append( parsepattern(a, folia.SenseAnnotation) )
        elif o == '--phon':
            patterns.append( parsepattern(a, folia.PhonAnnotation) )


        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            settings.ignoreerrors = True
        else:
            raise Exception("No such option: " + o)


    if args:
        for x in args:
            if os.path.isdir(x):
                processdir(x, patterns)
            elif os.path.isfile(x):
                process(x, patterns)
            elif x[0:2] != '--':
                print("ERROR: File or directory not found: " + x,file=sys.stderr)
                sys.exit(3)
    else:
        print("ERROR: Nothing to do, specify one or more files or directories",file=sys.stderr)

if __name__ == "__main__":
    main()
