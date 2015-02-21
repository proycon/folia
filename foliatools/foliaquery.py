#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import getopt
import sys
import os
import glob
try:
    from pynlpl.formats import folia, fql
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git",file=sys.stderr)
    sys.exit(2)

def usage():
    print("foliaquery",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Radboud University Nijmegen",file=sys.stderr)
    print("  2015 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("Query one or more FoLiA documents for certain patterns.",file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: foliaquery [options] -q <FQL query> file-or-dir1 file-or-dir2 ..etc..",file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for output:"        ,file=sys.stderr)
    print("  -q 'fql query'               Query (May be specified multiple times)",file=sys.stderr)
    print("  -e [encoding]                Output encoding (default: utf-8)"     ,file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)
    print("  -i                           Ignore errors",file=sys.stderr)
    print("",file=sys.stderr)



def process(filename, queries):
    try:
        print("Processing " + filename, file=sys.stderr)
        doc = folia.Document(file=filename)
        for query in queries:
            query(doc)
        #TODO: save document if changes are made
    except Exception as e:
        if settings.ignoreerrors:
            print("ERROR: An exception was raised whilst processing " + filename + ":", e            ,file=sys.stderr)
        else:
            raise


def processdir(d, patterns):
    print("Searching in  " + d,file=sys.stderr)
    for f in glob.glob(d + '/*'):
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
        opts, args = getopt.getopt(sys.argv[1:], "o:OE:hqnr", ["help","text=","pos=","lemma=","sense=","phon="])
    except getopt.GetoptError as err:
        print(str(err), file=sys.stderr)
        usage()
        sys.exit(2)

    queries = []

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-r':
            settings.recurse = True
        elif o == '-n':
            settings.ignoreerrors = True
        elif o == '-q':
            try:
                queries.append(fql.Query(a))
            except:
                print("FQL SYNTAX ERROR: " + str(e), file=sys.stderr)
        else:
            raise Exception("No such option: " + o)


    if queries and args:
        for x in args:
            if os.path.isdir(x):
                processdir(x, queries)
            elif os.path.isfile(x):
                process(x, queries)
            elif x[0:2] != '--':
                print("ERROR: File or directory not found: " + x,file=sys.stderr)
                sys.exit(3)
    elif not queries:
        docs = []
        if len(args) > 50:
            print("ERROR: Too many files specified for interactive mode, specify a query on the command line instead",file=sys.stderr)
        for x in args:
            if os.path.isdir(x):
                print("ERROR: Directories are not allowed in interactive mode, specify a query on the command line",file=sys.stderr)
        for x in args:
            print("Loading " + x + "...",file=sys.stderr)
            docs.append( folia.Document(file=x) )

        import readline
        print("Starting interactive mode, enter your FQL queries, QUIT to end.",file=sys.stderr)
        while True:
            query = input("FQL> ")
            if query == "QUIT":
                break
            if query.startswith == "LOAD ":
                print("Loading " + x + "...",file=sys.stderr)
                docs.append( folia.Document(file=query[5:]))
                continue

            try:
                query = fql.Query(query)
            except fql.SyntaxError as e:
                print("FQL SYNTAX ERROR: " + str(e), file=sys.stderr)
                continue

            if query.format == "python":
                query.format = "xml"

            for doc in docs:
                output = query(doc)
                print(output)

        #TODO: save documents if changes are made
    else:
        print("ERROR: Nothing to do, specify one or more files or directories",file=sys.stderr)

if __name__ == "__main__":
    main()
