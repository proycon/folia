#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import getopt
import sys
import os
import glob
import traceback
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git", file=sys.stderr)
    sys.exit(2)

def usage():
    print("foliacorrect", file=sys.stderr)
    print("  by Maarten van Gompel (proycon)", file=sys.stderr)
    print("  Radboud University Nijmegen", file=sys.stderr)
    print("  2015 - Licensed under GPLv3", file=sys.stderr)
    print("", file=sys.stderr)
    print("FoLiA " + folia.FOLIAVERSION + ", library version " + folia.LIBVERSION, file=sys.stderr)
    print("", file=sys.stderr)
    print("Corrections are one of the most complex forms of annotation in FoLiA. It may occur that you want to strip explicit corrections from a document, and leave only either the corrected or original version. The document can then be parsed by simpler parsers that can not handle explicit corrections. Alternatively, you may want to accept the best suggestion for correction (with or without stripping the correction element). This tool provides the means to do all that.", file=sys.stderr)
    print("", file=sys.stderr)
    print("Usage: foliacorrect [options] file-or-dir1 file-or-dir2 ..etc..", file=sys.stderr)
    print("", file=sys.stderr)
    print("Parameters for processing directories:", file=sys.stderr)
    print("  -r                           Process recursively", file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)", file=sys.stderr)
    print("  -V                           Show version info", file=sys.stderr)
    print("  -q                           Ignore errors",file=sys.stderr)
    print("  --corrected                  Keep the corrected versions, removing all explicit corrections", file=sys.stderr)
    print("  --original                   Keep the original versions,  removing all explicit corrections", file=sys.stderr)
    print("  --acceptsuggestion           Automatically accept the suggestion with the hightest confidence (can not be used with --original, can be used with --corrected)", file=sys.stderr)
    print("  --set                        Correction set to filter on", file=sys.stderr)
    print("  --class                      Correction class to filter on", file=sys.stderr)
    print("  --print                      Print all corrections, do not change the document", file=sys.stderr)



def replace(correction, correctionchild):
    parent = correction.parent
    index = parent.getindex(correction)
    elements = correctionchild.copychildren(correction.doc)
    parent.remove(correction)
    for i, e in enumerate(elements):
        if isinstance(e, folia.TextContent) and e.cls == 'original':
            e.cls = 'current'
        parent.insert(index+i, e)



def correct(filename,corrected, original, acceptsuggestion, setfilter,classfilter, output):
    changed = False
    try:
        doc = folia.Document(file=filename)
        for text in doc:
            for correction in list(text.select(folia.Correction, setfilter)):
                if not classfilter or correction.cls == classfilter:
                    if original:
                        if correction.hasoriginal():
                            #restore original
                            print("Restoring original version for " + str(correction.id),file=sys.stderr)
                            replace(correction, correction.original())
                            changed = True
                        elif correction.hasoriginal(True): #check for empty original
                            #insertion, remove it
                            correction.parent.remove(correction)
                    elif corrected:
                        if correction.hasnew():
                            print("Keeping corrected version for " + str(correction.id),file=sys.stderr)
                            replace(correction, correction.new())
                            changed = True
                    elif correction.hassuggestions() and acceptsuggestion:
                        bestsuggestion = None
                        changed = True
                        for suggestion in correction.hassuggestions():
                            if not bestsuggestion or (suggestion.confidence and not bestsuggestion.confidence) or (suggestion.confidence and bestsuggestion.confidence and suggestion.confidence > bestsuggestion.confidence):
                                bestsuggestion = suggestion
                        if bestsuggestion:
                            if corrected:
                                replace(correction, bestsuggestion)
                            else:
                                raise NotImplementedError #TODO
                    if output:
                        print(correction.xmlstring())
        if changed:
            if settings.stdout:
                print(doc.xmlstring())
            else:
                doc.save()
    except Exception as e:
        if settings.ignoreerrors:
            print("ERROR: An exception was raised whilst processing " + filename + ":", e, file=sys.stderr)
        else:
            raise




def processdir(d,corrected, original, acceptsuggestion, setfilter,classfilter,output):
    print("Searching in  " + d,file=sys.stderr)
    for f in glob.glob(os.path.join(d ,'*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            correct(f,corrected,original,  acceptsuggestion, setfilter,classfilter,output)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, corrected,original, acceptsuggestion, setfilter,classfilter,output)


class settings:
    extension = 'xml'
    recurse = False
    encoding = 'utf-8'
    ignoreerrors = False
    stdout = False

def main():
    original = acceptsuggestion = output = corrected = False
    setfilter = classfilter = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "E:srhqVO", ["help","original","corrected","acceptsuggestion","set=","class=","print"])
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
            settings.ignoreerrors = True
        elif o == '-O':
            settings.stdout = True
        elif o == '-V':
            print("FoLiA " + folia.FOLIAVERSION + ", library version " + folia.LIBVERSION,file=sys.stderr)
            sys.exit(0)
        elif o == '--original':
            original = True
        elif o == '--corrected':
            corrected = True
        elif o == '--acceptsuggestion':
            acceptsuggestion = True
        elif o == '--set' or o == '--set=':
            setfilter = a
        elif o == '--class' or o == '--class=':
            classfilter = a
        elif o == '--print':
            output = True
        else:
            raise Exception("No such option: " + o)


    if len(args) >= 1:
        for x in sys.argv[1:]:
            if x[0] != '-':
                if os.path.isdir(x):
                    processdir(x,corrected,original, acceptsuggestion, setfilter,classfilter,output)
                elif os.path.isfile(x):
                    correct(x,corrected, original, acceptsuggestion, setfilter,classfilter,output)
                else:
                    print("ERROR: File or directory not found: " + x,file=sys.stderr)
                    sys.exit(3)
    else:
        print("ERROR: No files specified",file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
