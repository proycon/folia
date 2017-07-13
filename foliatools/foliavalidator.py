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
    print("  2016 - Licensed under GPLv3", file=sys.stderr)
    print("", file=sys.stderr)
    print("FoLiA " + folia.FOLIAVERSION + ", library version " + folia.LIBVERSION, file=sys.stderr)
    print("", file=sys.stderr)
    print("Validates FoLiA documents.", file=sys.stderr)
    print("", file=sys.stderr)
    print("Usage: foliavalidator [options] file-or-dir1 file-or-dir2 ..etc..", file=sys.stderr)
    print("", file=sys.stderr)
    print("Parameters for processing directories:", file=sys.stderr)
    print("  -d                           Deep validation", file=sys.stderr)
    print("  -r                           Process recursively", file=sys.stderr)
    print("  -q                           Quick (more shallow) validation, only validate against RelaxNG schema - do not load document in FoLiA library", file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)", file=sys.stderr)
    print("  -V                           Show version info", file=sys.stderr)
    print("  -t                           Treat text validation errors strictly (recommended)", file=sys.stderr)
    print("  -i                           Ignore validation failures, always report a successful exit code", file=sys.stderr)







def validate(filename, schema = None, quick=False, deep=False, stricttextvalidation=False):
    try:
        folia.validate(filename, schema)
    except Exception as e:
        print("VALIDATION ERROR against RelaxNG schema (stage 1/2), in " + filename,file=sys.stderr)
        print(str(e), file=sys.stderr)
        return False
    try:
        document = folia.Document(file=filename, deepvalidation=deep,textvalidation=True,verbose=True)
    except folia.DeepValidationError as e:
        print("DEEP VALIDATION ERROR on full parse by library (stage 2/2), in " + filename,file=sys.stderr)
        print(e.__class__.__name__ + ": " + str(e),file=sys.stderr)
        return False
    except Exception as e:
        print("VALIDATION ERROR on full parse by library (stage 2/2), in " + filename,file=sys.stderr)
        print(e.__class__.__name__ + ": " + str(e),file=sys.stderr)
        print("-- Full traceback follows -->",file=sys.stderr)
        ex_type, ex, tb = sys.exc_info()
        traceback.print_exception(ex_type, ex, tb)
        return False
    if document.textvalidationerrors:
        if stricttextvalidation:
            print("VALIDATION ERROR because of text validation errors, in " + filename,file=sys.stderr)
            return False
        else:
            print("WARNING: there were " + str(document.textvalidationerrors) + " text validation errors but these are currently not counted toward the full validation result (use -t for strict text validation, experimental at this stage)", file=sys.stderr)

    print("Validated successfully: " +  filename,file=sys.stderr)
    return True




def processdir(d, schema = None,quick=False,deep=False,stricttextvalidation=False):
    success = False
    print("Searching in  " + d,file=sys.stderr)
    for f in glob.glob(os.path.join(d ,'*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            r = validate(f, schema,quick,deep,stricttextvalidation)
        elif settings.recurse and os.path.isdir(f):
            r = processdir(f,schema,quick,deep,stricttextvalidation)
        if not r: success = False
    return success


class settings:
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'
    deep = False
    stricttextvalidation = False

def main():
    quick = False
    nofail = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "E:srhdqVi", ["help"])
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
        elif o == '-t':
            settings.stricttextvalidation = True
        elif o == '-d':
            settings.deep = True
        elif o == '-q':
            quick = True
        elif o == '-i':
            nofail = True
        elif o == '-V':
            print("FoLiA " + folia.FOLIAVERSION + ", library version " + folia.LIBVERSION,file=sys.stderr)
            sys.exit(0)
        else:
            raise Exception("No such option: " + o)

    schema  = lxml.etree.RelaxNG(folia.relaxng())

    if len(args) >= 1:
        success = True
        for x in sys.argv[1:]:
            if x[0] != '-':
                if os.path.isdir(x):
                    r = processdir(x,schema,quick,settings.deep, settings.stricttextvalidation)
                elif os.path.isfile(x):
                    r = validate(x, schema,quick,settings.deep, settings.stricttextvalidation)
                else:
                    print("ERROR: File or directory not found: " + x,file=sys.stderr)
                    sys.exit(3)
                if not r: success= False
            if not success and not nofail:
                sys.exit(1)
    else:
        print("ERROR: No files specified",file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
