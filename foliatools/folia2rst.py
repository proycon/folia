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

from pynlpl.formats import folia
from pynlpl.common import u, isstring


ADORNMENT = ['=','-','+','~','`',"'",'#']



def element2rst(element, retaintokenisation=False, _previousdelimiter=""):
    """Get the text associated with this element (of the specified class), will always be a unicode instance.
    If no text is directly associated with the element, it will be obtained from the children. If that doesn't result
    in any text either, a NoSuchText exception will be raised.

    If retaintokenisation is True, the space attribute on words will be ignored, otherwise it will be adhered to and text will be detokenised as much as possible.
    """


    prefix = suffix = ""
    indent = ""


    if element.TEXTCONTAINER:
        if isinstance(element, folia.TextMarkupStyle):
            #we guess how possible class names may be mapped to RST directly, set-agnostic
            if element.href:
                prefix = "`"
                suffix = " <" + element.href + ">`_"
            elif element.cls and (element.cls == 'strong' or element.cls[:4] == 'bold' or element.cls == 'b'):
                prefix = suffix ="**"
            elif element.cls and (element.cls[:2] == 'em' or element.cls[:6] == 'italic' or element.cls == 'i' or element.cls[:5] == 'slant'):
                prefix = suffix ="*"
            elif element.cls and (element.cls[:3] == 'lit' or element.cls[:4] == 'verb' or element.cls[:4] == 'code'):
                prefix = suffix ="``"
        s = prefix
        for e in element:
            if isstring(e):
                s += e
            else:
                if s: s += e.TEXTDELIMITER #for AbstractMarkup, will usually be ""
                s += element2rst(e)
        return s + suffix
    if not element.PRINTABLE: #only printable elements can hold text
        raise folia.NoSuchText


    if isinstance(element, folia.ListItem):
        if element.n:
            prefix = element.n + ") "
        else:
            prefix = "- "
    elif isinstance(element, folia.Head):
        level = 0
        for div in element.ancestors(folia.Division):
            if div.count(folia.Head,None,[folia.Division]):
                level += 1
        suffix = "\n" + ADORNMENT[level-1] * (len(element.text()) + 10) + "\n\n"
    elif isinstance(element, folia.Figure) and element.src:
        prefix = ".. figure::" + element.src + "\n\n"
    elif isinstance(element, folia.Note):
        #TODO
        pass
    elif isinstance(element, folia.Caption):
        indent =  "    "
    elif isinstance(element, folia.Quote) and not isinstance(element.parent, folia.Sentence) and not isinstance(element.parent, folia.Paragraph):
        indent = "    " #block quote
    elif isinstance(element, folia.Gap) and not isinstance(element.parent, folia.Sentence) and not isinstance(element.parent, folia.Paragraph):
        prefix = "\n\n::\n\n" + element.content() + "\n\n" #literal block
    elif isinstance(element, folia.List):
        suffix = "\n\n"



    if element.hastext():
        if indent:
            for i, ss in enumerate(element2rst(element.textcontent()).split("\n")):
                if i == 0:
                    s = indent + prefix + ss + "\n"
                else:
                    s = indent + ss + "\n"
        else:
            s = prefix + element2rst(element.textcontent())
    else:
        #Not found, descend into children
        delimiter = ""
        s = ""
        for e in element:
            if e.PRINTABLE and not isinstance(e, folia.TextContent):
                try:
                    if indent:
                        for ss in element2rst(e,retaintokenisation, delimiter).split("\n"):
                            if not s:
                                s += indent + prefix + ss + "\n"
                            else:
                                s += indent + ss + "\n"
                    else:
                        if not s: s += prefix
                        s += element2rst(e,retaintokenisation, delimiter)
                    delimiter = e.gettextdelimiter(retaintokenisation)
                    #delimiter will be buffered and only printed upon next iteration, this prevents the delimiter being output at the end of a sequence
                except folia.NoSuchText:
                    continue


    if s and _previousdelimiter:
        return _previousdelimiter + s + suffix
    elif s:
        return s + suffix
    else:
        #No text found at all :`(
        raise folia.NoSuchText


def main():
    inputfile = None
    outputfile = None
    if len(sys.argv) == 2:
        inputfile = sys.argv[1]
    if len(sys.argv) == 3:
        outputfile = sys.argv[2]

    if inputfile:
        doc = folia.Document(file=inputfile)
    else:
        #stdin
        data = sys.stdin.read()
        doc = folia.Document(string=data)

    if outputfile:
        f = io.open(outputfile,'w',encoding='utf-8')
    else:
        f = sys.stdout
    for data in doc:
        print(element2rst(data), file=f)


if __name__ == "__main__":
    main()
