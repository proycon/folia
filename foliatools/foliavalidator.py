#!/usr/bin/env python
# -*- coding: utf8 -*-

import getopt
import sys
import os
import glob
import lxml.etree
try:
    from pynlpl.formats import folia
except:
    print >>sys.stderr,"ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git"
    sys.exit(2)

def usage():
    print >>sys.stderr, "foliavalidator"
    print >>sys.stderr, "  by Maarten van Gompel (proycon)"
    print >>sys.stderr, "  Radboud University Nijmegen"
    print >>sys.stderr, "  2013 - Licensed under GPLv3"
    print >>sys.stderr, ""
    print >>sys.stderr, "FoLiA " + folia.FOLIAVERSION + ", library version " + folia.LIBVERSION
    print >>sys.stderr, ""
    print >>sys.stderr, "Validates FoLiA documents."
    print >>sys.stderr, ""
    print >>sys.stderr, "Usage: foliavalidator [options] file-or-dir1 file-or-dir2 ..etc.."
    print >>sys.stderr, ""
    print >>sys.stderr, "Parameters for processing directories:"
    print >>sys.stderr, "  -r                           Process recursively"
    print >>sys.stderr, "  -q                           Quick (more shallow) validation, only validate against RelaxNG schema - do not load document in FoLiA library"
    print >>sys.stderr, "  -E [extension]               Set extension (default: xml)"
    print >>sys.stderr, "  -V                           Show version info"






def validate(filename, schema = None, quick=False):
    try:
        folia.validate(filename, schema)
    except Exception as e:
        print >>sys.stderr, "VALIDATION ERROR against RelaxNG schema (stage 1/2), in " + filename
        print >>sys.stderr, str(e)
        return False
    try:
        d = folia.Document(file=filename)
    except Exception as e:
        print >>sys.stderr, "VALIDATION ERROR on full parse by library (stage 2/2), in " + filename
        print >>sys.stderr, str(e)
        return False

    print >>sys.stderr, "Validated successfully: " +  filename
    return True




def processdir(d, schema = None,quick=False):
    print >>sys.stderr, "Searching in  " + d
    for f in glob.glob(d + '/*'):
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
    except getopt.GetoptError, err:
        print str(err)
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
            print >>sys.stderr, "FoLiA " + folia.FOLIAVERSION + ", library version " + folia.LIBVERSION
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
                    print >>sys.stderr, "ERROR: File or directory not found: " + x
                    sys.exit(3)
    else:
        print >>sys.stderr,"ERROR: No files specified"
        sys.exit(2)

if __name__ == "__main__":
    main()
