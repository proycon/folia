#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import getopt
import sys
import os
import glob
import traceback
import lxml.etree
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git", file=sys.stderr)
    sys.exit(2)

def usage():
    print("foliavalidator", file=sys.stderr)
    print("  by Maarten van Gompel (proycon)", file=sys.stderr)
    print("  Radboud University Nijmegen", file=sys.stderr)
    print("  2014 - Licensed under GPLv3", file=sys.stderr)
    print("", file=sys.stderr)
    print("FoLiA " + folia.FOLIAVERSION + ", library version " + folia.LIBVERSION, file=sys.stderr)
    print("", file=sys.stderr)
    print("Validates FoLiA documents.", file=sys.stderr)
    print("", file=sys.stderr)
    print("Usage: foliavalidator [options] file-or-dir1 file-or-dir2 ..etc..", file=sys.stderr)
    print("", file=sys.stderr)
    print("Parameters for processing directories:", file=sys.stderr)
    print("  -r                           Process recursively", file=sys.stderr)
    print("  -q                           Quick (more shallow) validation, only validate against RelaxNG schema - do not load document in FoLiA library", file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)", file=sys.stderr)
    print("  -V                           Show version info", file=sys.stderr)







def validate(filename, schema = None, quick=False):
    try:
        folia.validate(filename, schema)
    except Exception as e:
        print("VALIDATION ERROR against RelaxNG schema (stage 1/2), in " + filename,file=sys.stderr)
        print(str(e), file=sys.stderr)
        return False
    try:
        folia.Document(file=filename)
    except Exception as e:
        print("VALIDATION ERROR on full parse by library (stage 2/2), in " + filename,file=sys.stderr)
        print(e.__class__.__name__ + ": " + str(e),file=sys.stderr)
        print("Full traceback follows:",file=sys.stderr)
        ex_type, ex, tb = sys.exc_info()
        traceback.print_tb(tb)
        return False

    print("Validated successfully: " +  filename,file=sys.stderr)
    return True




def processdir(d, schema = None,quick=False):
    print("Searching in  " + d,file=sys.stderr)
    for f in glob.glob(os.path.join(d ,'*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            validate(f, schema,quick)
        elif settings.recurse and os.path.isdir(f):
            processdir(f,schema,quick)


class settings:
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'

def main():
    quick = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "E:srhqV", ["help"])
    except getopt.GetoptError as err:
        print(str(err), file=sys.stderr)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-E':
            settings.extension = a
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            quick = True
        elif o == '-V':
            print("FoLiA " + folia.FOLIAVERSION + ", library version " + folia.LIBVERSION,file=sys.stderr)
            sys.exit(0)
        else:
            raise Exception("No such option: " + o)

    schema  = lxml.etree.RelaxNG(folia.relaxng())

    if len(args) >= 1:
        for x in sys.argv[1:]:
            if x[0] != '-':
                if os.path.isdir(x):
                    processdir(x,schema,quick)
                elif os.path.isfile(x):
                    validate(x, schema,quick)
                else:
                    print("ERROR: File or directory not found: " + x,file=sys.stderr)
                    sys.exit(3)
    else:
        print("ERROR: No files specified",file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
