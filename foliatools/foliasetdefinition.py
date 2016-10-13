#!/usr/bin/env python
#-*- coding:utf-8 -*-

#---------------------------------------------------------------
# FoLiA to ReStructuredText Converter
#   by Maarten van Gompel
#   Centre for Language Studies
#   Radboud University Nijmegen
#   proycon AT anaproy DOT nl
#
#   Licensed under GPLv3
#
# This script converts RST to FoLiA format.
#
#----------------------------------------------------------------

from __future__ import print_function, unicode_literals, division, absolute_import

import sys
import glob
import gzip
import os
import io
import json
import argparse

from pynlpl.formats import folia, foliaset
from pynlpl.common import u, isstring

def printclass(classinfo, args, indent):
    if args.outputuri:
        printuri = " <" + classinfo['uri'] + ">"
    else:
        printuri = ""
    print(indent + " -> CLASS " + classinfo['id'] + printuri + ": " + classinfo['label'])
    if 'subclasses' in classinfo:
        for subclassinfo in classinfo['subclasses'].values():
            printclass(subclassinfo, args, indent + "  ")


def main():
    parser = argparse.ArgumentParser(description="A tool to read FoLiA Set Definitions and perform some operations on them. By default it will print all sets and classes. This tool can also convert from legacy XML to RDF.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--basenamespace', type=str,help="Base RDF namespace to use when converting from legacy XML to RDF", action='store',default="",required=False)
    parser.add_argument('--rdfttl', type=str,help="Output RDF in Turtle", action='store_bool',required=False)
    parser.add_argument('--rdfxml', type=str,help="Output RDF in XML", action='store_bool',required=False)
    parser.add_argument('--json', type=str,help="Output set definition in JSON", action='store_bool',required=False)
    parser.add_argument('--outputuri', type=str,help="Output full URIs in text output", action='store_bool',required=False)
    parser.add_argument('url', nargs='?', help='URL or filename to a FoLiA Set Definition')

    args = parser.parse_args()
    if args.filename[0] not in ('.','/'):
        args.filename = './' + args.filename
    setdefinition = foliaset.SetDefinition(args.filename, basens=args.basenamespace)
    if args.rdfttl:
        print(str(setdefinition.graph.serialize(None, 'turtle',base=setdefinition.basens),'utf-8') )
    elif args.rdfxml:
        print(str(setdefinition.graph.serialize(None, 'turtle',base=setdefinition.basens),'utf-8') )
    elif args.json:
        json.dumps(setdefinition.json())
    else:
        #default visualization
        seturi, setid, setlabel = setdefinition.mainset()
        if args.outputuri:
            printuri = " <" + seturi + ">"
        else:
            printuri = ""
        print("SET " + setid + printuri + ": " + setlabel)
        for classinfo in setdefinition.classes(seturi, nestedhierarchy=True):
            printclass(classinfo, args, "  ")
        print()

        for subseturi, subsetid, subsetlabel in setdefinition.subsets():
            if args.outputuri:
                printuri = " <" + subseturi + ">"
            else:
                printuri = ""
            print("SUBSET " + subsetid + printuri + ": " + subsetlabel)
            for classinfo in setdefinition.classes(subseturi, nestedhierarchy=True):
                printclass(classinfo, args, "  ")
            print()



if __name__ == "__main__":
    main()
