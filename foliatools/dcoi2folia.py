#! /usr/bin/env python
# -*- coding: utf8 -*-

import xslt
    
def main():
    usage = """dcoi2folia
  by Maarten van Gompel (proycon)
  Tilburg University / Radboud University Nijmegen
  2012 - Licensed under GPLv3

This conversion script converts one or more D-Coi XML documents to FoLiA.

Usage: dcoi2folia [options] file-or-dir1 file-or-dir2 ..etc.."""
    
    xslt.main('dcoi2folia.xsl','folia.xml', usage)
    
if __name__ == "__main__":
    main()
    
