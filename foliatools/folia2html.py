#! /usr/bin/env python
# -*- coding: utf8 -*-

import xslt
    
def main():    
    usage = """folia2html
  by Maarten van Gompel (proycon)
  Tilburg University / Radboud University Nijmegen
  2012 - Licensed under GPLv3


This conversion script converts one or more FoLiA documents to a semi-interactive HTML document for
viewing in a web-browser.

Usage: folia2html [options] file-or-dir1 file-or-dir2 ..etc.."""

    xslt.main('folia2html.xsl','html',usage)
    
if __name__ == "__main__":
    main()
