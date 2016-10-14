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
    assert isinstance(classinfo, dict)
    print(indent + " -> CLASS " + classinfo['id'] + printuri + ": " + classinfo['label'])
    if 'subclasses' in classinfo:
        for subclassinfo in classinfo['subclasses'].values():
            printclass(subclassinfo, args, indent + "  ")


def main():
    parser = argparse.ArgumentParser(description="A tool to read FoLiA Set Definitions and perform some operations on them. By default it will print all sets and classes. This tool can also convert from legacy XML to RDF.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--basenamespace', type=str,help="Base RDF namespace to use when converting from legacy XML to RDF", action='store',default="",required=False)
    parser.add_argument('--rdfttl', help="Output RDF in Turtle", action='store_true',required=False)
    parser.add_argument('--rdfxml',help="Output RDF in XML", action='store_true',required=False)
    parser.add_argument('--json', help="Output set definition in JSON", action='store_true',required=False)
    parser.add_argument('--outputuri',help="Output full RDF URIs in text output", action='store_true',required=False)
    parser.add_argument('--class', type=str,help="Test for the specified class, by ID", action='store',required=False)
    parser.add_argument('--subset', type=str,help="Test for the specified subset (--class will be interpreted relative to subset then)", action='store',required=False)
    parser.add_argument('--shell', help="Start an interactive Python shell for debugging (with PDB)", action='store_true',required=False)
    parser.add_argument('url', nargs=1, help='URL or filename to a FoLiA Set Definition')

    args = parser.parse_args()
    url = args.url[0]
    if url[0] not in ('.','/') and not url.startswith('http'):
        url = './' + url
    setdefinition = foliaset.SetDefinition(url, basens=args.basenamespace)
    if args.rdfttl:
        print(str(setdefinition.graph.serialize(None, 'turtle',base=setdefinition.basens),'utf-8') )
    elif args.rdfxml:
        print(str(setdefinition.graph.serialize(None, 'xml',base=setdefinition.basens),'utf-8') )
    elif args.json:
        print(json.dumps(setdefinition.json()))
    elif args.shell:
        print("Set Definition is loaded in variable: setdefinition; RDF graph in setdefinition.graph",file=sys.stderr)
        import pdb; pdb.set_trace()
    else:
        #default visualization
        setinfo = setdefinition.mainset()
        if args.outputuri:
            printuri = " <" + setinfo['uri'] + ">"
        else:
            printuri = ""
        print("SET " + setinfo['id'] + printuri + ": " + setinfo['label'])
        for classinfo in setdefinition.orderedclasses(setinfo['uri'], nestedhierarchy=True):
            printclass(classinfo, args, "  ")
        print()

        for subsetinfo in sorted(setdefinition.subsets(), key=lambda subsetinfo: subsetinfo['label'] if 'label' in subsetinfo else subsetinfo['id']):
            if args.outputuri:
                printuri = " <" + subsetinfo['uri'] + ">"
            else:
                printuri = ""
            print("SUBSET " + subsetinfo['id'] + printuri + ": " + subsetinfo['label'])
            for classinfo in setdefinition.orderedclasses(subsetinfo['uri'], nestedhierarchy=True):
                printclass(classinfo, args, "  ")
            print()



if __name__ == "__main__":
    main()
