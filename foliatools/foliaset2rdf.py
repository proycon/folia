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
import argparse

from pynlpl.formats import folia, foliaset
from pynlpl.common import u, isstring


def main():
    parser = argparse.ArgumentParser(description="Convert legacy FoLiA Set Definitions to RDF (Turtle). Outputs to stdout.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--basenamespace', type=str,help="Base RDF namespace to use", action='store',default="",required=False)
    parser.add_argument('filename', nargs='?', help='Path to a legacy FoLiA Set Definition file (XML)')

    args = parser.parse_args()
    if args.filename[0] not in ('.','/'):
        args.filename = './' + args.filename
    setdefinition = foliaset.SetDefinition(args.filename, basens=args.basenamespace)
    print(str(setdefinition.graph.serialize(None, 'turtle',base=setdefinition.basens),'utf-8') )


if __name__ == "__main__":
    main()
