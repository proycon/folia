#! /usr/bin/env python
# -*- coding: utf8 -*-

import xslt    
    
def main():
    usage = """folia2dcoi
  by Maarten van Gompel (proycon)
  Tilburg University / Radboud University Nijmegen
  2012 - Licensed under GPLv3

This conversion script converts one or more FoLiA documents to D-Coi XML format, omitting
any annotations that can not be represented in the D-Coi format.

Usage: folia2dcoi [options] file-or-dir1 file-or-dir2 ..etc.."""

    xslt.main('folia2dcoi.xsl','dcoi.xml', usage)

if __name__ == "__main__":
    main()
