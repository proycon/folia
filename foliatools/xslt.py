#! /usr/bin/env python
# -*- coding: utf8 -*-

import lxml.etree
import os.path

def transform(xsltfilename, sourcefilename, targetfilename = None, encoding = 'utf-8'):    
    xsldir = os.path.dirname(__file__)
    if xsltfilename[0] != '/': xsltfilename = xsldir + '/' + xsltfilename
    if not os.path.exists(xsltfilename):
        raise Exception("XSL Stylesheet not found: " + xsltfilename)
    elif not os.path.exists(sourcefilename):
        raise Exception("File not found: " + sourcefilename)        
    xslt = lxml.etree.parse(xsltfilename)
    transformer = lxml.etree.XSLT(xslt)
    parsedsource = lxml.etree.parse(sourcefilename)
    transformed = transformer(parsedsource)
    if targetfilename:
        f = open(targetfilename, 'w')
        f.write( lxml.etree.tostring(transformed, pretty_print=True, encoding=encoding) )
        f.close()
    else:
        print lxml.etree.tostring(transformed, pretty_print=True, encoding=encoding)
