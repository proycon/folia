#! /usr/bin/env python
# -*- coding: utf8 -*-


from __future__ import print_function, unicode_literals, division, absolute_import

import getopt
import io
import sys
import os
import glob
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git",file=sys.stderr)
    sys.exit(2)

def usage():
    print("foliatextcontent",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Radboud University Nijmegen",file=sys.stderr)
    print("  2015 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("This tool operates on some of the redundancy regarding text context inherent in FoLiA documents. It adds text content elements,  on the higher (untokenised) levels, adding offset information and mark-up element if present. Secondly, the tool may als adds text-markup elements for substrings (str element) (provided there is no overlap).",file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: foliatextcontent [options] file-or-dir1 file-or-dir2 ..etc..",file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for output:"        ,file=sys.stderr)
    print("  -s                           Add text content on sentence level",file=sys.stderr)
    print("  -p                           Add text content on paragraph level"    ,file=sys.stderr)
    print("  -d                           Add text content on division level",file=sys.stderr)
    print("  -t                           Add text content on global text level"    ,file=sys.stderr)
    print("  -T                           Add text content for the specified elements (comma separated list of folia xml tags)"    ,file=sys.stderr)
    print("  -X                           Do NOT add offset information"    ,file=sys.stderr)
    print("  -F                           Force offsets to refer to the specified structure only (only works if you specified a single element type for -T!!!)"    ,file=sys.stderr)
    print("  -M                           Add substring markup linking to string elements (if any, and when there is no overlap)"    ,file=sys.stderr)
    print("  -e [encoding]                Output encoding (default: utf-8)",file=sys.stderr)
    print("  -w                           Edit file(s) (overwrites input files), will output to stdout otherwise" ,file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)


def linkstrings(element, cls='current',debug=False):
    if element.hastext(cls,strict=True) and element.hasannotation(folia.String):
        text = element.textcontent(cls, correctionhandling=folia.CorrectionHandling.EITHER)

        for string in element.select(folia.String, None, False):
            try:
                stringtextcontent = string.textcontent(cls, correctionhandling=folia.CorrectionHandling.EITHER)
                stringtext = stringtextcontent.text()
                stringoffset = stringtextcontent.offset
            except folia.NoSuchText:
                continue

            if not stringtext:
                continue

            if debug: print("Finding string '" + stringtext + "' in text: ", text.text(), file=sys.stderr)

            offset = 0 #current offset cursor
            length = len(stringtext)
            replaceindex = 0
            replace = []
            for i, subtext in enumerate(text):
                if isinstance(subtext, str):
                    subtextlength = len(subtext)
                    if stringoffset >= offset and stringoffset+length <= offset+subtextlength:
                        reloffset = stringoffset-offset

                        if subtext[reloffset:reloffset+length] != stringtext:
                            print(" String refers to offset " + str(stringoffset) + ", but is not found there ! Found '" + subtext[reloffset:reloffset+length] + "' instead.",file=sys.stderr)
                        else:
                            #match!
                            kwargs = {}
                            replaceindex = i
                            if string.id:
                                kwargs['idref'] = string.id
                            replace = [subtext[:reloffset], folia.TextMarkupString(element.doc, *stringtext, **kwargs), subtext[reloffset+length:]]
                            break

                elif isinstance(subtext, folia.AbstractTextMarkup):
                    subtextlength = len(subtext.text())
                    if stringoffset >= offset and stringoffset+length <= offset+subtextlength:
                        raise NotImplementedError("String fits within other markup element (possibly another string), not implemented yet")

                offset += subtextlength

            if replace:
                if debug: print("Replacing item " + str(replaceindex) + " with: ", replace,file=sys.stderr)
                del text.data[replaceindex]
                for x in reversed(replace):
                    if x:
                        text.data.insert(replaceindex,x)
            else:
                if string.id:
                    print("Could not find string " + string.id + " !!!",file=sys.stderr)

def gettextsequence(element, cls, debug=False):
    assert element.PRINTABLE
    if debug: print(" Getting text for ", repr(element),file=sys.stderr)
    if element.TEXTCONTAINER:
        if debug: print("  Found textcontainer ", repr(element), "in", repr(element.ancestor(folia.AbstractStructureElement)),file=sys.stderr)

        if isinstance(element,folia.TextContent) and element.cls != cls:
            if debug: print("  Class mismatch", element.cls,"vs",cls,file=sys.stderr)
            raise StopIteration

        for e in element:
            if isinstance(e, str):
                if debug: print("  Found: ", e,file=sys.stderr)
                yield e, element
            else: #markup (don't recurse)
                if debug: print("  Found markup: ", repr(e),file=sys.stderr)
                yield e, element
                yield e.gettextdelimiter(), None

        yield None,None #Signals a break after this, if we have text content we needn't delve deeper
    else:
        #Do we have a text content?
        foundtext = False
        if debug: print(" Looking for text in ", repr(element),file=sys.stderr)
        for e in element:
            if isinstance(e, folia.TextContent) and e.cls == cls:
                foundtext = True
                for x in gettextsequence(e, cls, debug):
                    yield x
            elif isinstance(e, folia.Correction):
                foundtextincorrection =False
                try:
                    if e.hasnew() and e.new().textcontent(cls):
                        foundtextincorrection = True
                        for x in gettextsequence(e.new().textcontent(cls), cls, debug):
                            yield x
                except folia.NoSuchText:
                    pass
                except folia.NoSuchAnnotation:
                    pass
                if not foundtextincorrection:
                    try:
                        if e.hascurrent() and e.current().textcontent(cls):
                            foundtextincorrection = True
                            for x in gettextsequence(e.current().textcontent(cls), cls, debug):
                                yield x
                    except folia.NoSuchText:
                        pass
                    except folia.NoSuchAnnotation:
                        pass
                if not foundtextincorrection:
                    try:
                        if e.hasoriginal() and e.original().textcontent(cls):
                            foundtextincorrection = True
                            for x in gettextsequence(e.current().textcontent(cls), cls, debug):
                                yield x
                    except folia.NoSuchText:
                        pass
                    except folia.NoSuchAnnotation:
                        pass
                foundtext = foundtextincorrection

        if not foundtext:
            if debug: print(" Looking for text in children of ", repr(element),file=sys.stderr)
            for e in element:
                if e.PRINTABLE and not isinstance(e, folia.String):
                    #abort = False
                    for x in gettextsequence(e, cls, debug):
                        foundtext = True
                        if x[0] is None:
                            abort = True
                            break
                        yield x
                    #if abort:
                    #    print(" Abort signal received, not processing further elements in ", repr(element),file=sys.stderr)
                    #    break
                if foundtext:
                    delimiter = e.gettextdelimiter()
                    if debug: print(" Got delimiter " + repr(delimiter) + " from " + repr(element), file=sys.stderr)
                    yield e.gettextdelimiter(), None
                elif isinstance(e, folia.AbstractStructureElement) and not isinstance(e, folia.Linebreak) and not isinstance(e, folia.Whitespace):
                    raise folia.NoSuchText("No text was found in the scope of the structure element")


def settext(element, cls='current', offsets=True, forceoffsetref=False, debug=False):
    assert element.PRINTABLE

    if debug: print("In settext for  ", repr(element),file=sys.stderr)

    #get the raw text sequence
    try:
        textsequence = list(gettextsequence(element,cls,debug))
    except folia.NoSuchText:
        return None

    if debug: print("Raw text:  ", textsequence,file=sys.stderr)

    if textsequence:
        newtextsequence = []
        offset = 0
        prevsrc = None
        for i, (e, src) in enumerate(textsequence):
            if e: #filter out empty strings
                if isinstance(e,str):
                    length = len(e)

                    #only whitespace from here on?
                    if not e.strip():
                        onlywhitespace = True
                        for x,y in textsequence[i+1:]:
                            if y is not None:
                                onlywhitespace = False
                        if onlywhitespace:
                            break
                elif isinstance(e, folia.AbstractTextMarkup):
                    e = e.copy()
                    length = len(e.text())

                if src and offsets and src is not prevsrc:
                    ancestors = list(src.ancestors(folia.AbstractStructureElement))
                    if len(ancestors) >= 2 and ancestors[1] is element:
                        if debug: print("Setting offset for text in  " + repr(ancestors[0]) + " to " + str(offset) + ", reference " + repr(element) ,file=sys.stderr)
                        src.offset = offset
                    elif forceoffsetref:
                        src.offset = offset
                        src.ref = element
                    prevsrc = src

                newtextsequence.append(e)
                offset += length

        if newtextsequence:
            if debug: print("Setting text for " + repr(element) + ":" , newtextsequence, file=sys.stderr)
            return element.replace(folia.TextContent, *newtextsequence, cls=cls) #appends if new



def processelement(element, settings):
    if not isinstance(element, folia.AbstractSpanAnnotation): #prevent infinite recursion
        for e in element:
            if isinstance(e, folia.AbstractElement):
                if settings.debug: print("Processing ", repr(e),file=sys.stderr)
                processelement(e,settings)
        if element.PRINTABLE:
            if any( isinstance(element,C) for C in settings.Classes):
                for cls in element.doc.textclasses:
                    settext(element, cls, settings.offsets, settings.forceoffsetref, settings.debug)


def process(filename, outputfile = None):
    print("Converting " + filename,file=sys.stderr)
    doc = folia.Document(file=filename)

    if settings.linkstrings:
        for element in doc.select(folia.AbstractStructureElement):
            if settings.linkstrings:
                for cls in element.doc.textclasses:
                    linkstrings(element, cls, settings.debug)

    if settings.Classes:
        for e in doc.data:
            processelement(e, settings)


    if settings.inplaceedit:
        doc.save()
    else:
        print(doc.xmlstring())

def processdir(d, outputfile = None):
    print("Searching in  " + d, file=sys.stderr)
    for f in glob.glob(os.path.join(d ,'*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension:
            process(f, outputfile)
        elif settings.recurse and os.path.isdir(f):
            processdir(f)



class settings:
    Classes = []
    inplaceedit = False
    offsets = True
    forceoffsetref = False
    linkstrings = False

    extension = 'xml'
    recurse = False
    encoding = 'utf-8'

    debug = False

    textclasses =[]


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "E:hsSpPdDtTXMe:wT:Fc:", ["help"])
    except getopt.GetoptError as err:
        print(str(err),file=sys.stderr)
        usage()
        sys.exit(2)


    outputfile = None


    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-d':
            settings.Classes.append(folia.Division)
        elif o == '-t':
            settings.Classes.append(folia.Text)
        elif o == '-s':
            settings.Classes.append(folia.Sentence)
        elif o == '-p':
            settings.Classes.append(folia.Paragraph)
        elif o == '-T':
            settings.Classes += [ folia.XML2CLASS[tag] for tag in a.split(',') ]
        elif o == '-X':
            settings.offsets = False
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-F':
            settings.forceoffsetref = True
        elif o == '-M':
            settings.linkstrings = True
        elif o == '-w':
            settings.inplaceedit = True
        elif o == '-r':
            settings.recurse = True
        elif o == '-D':
            settings.debug = True
        else:
            raise Exception("No such option: " + o)


    if outputfile: outputfile = io.open(outputfile,'w',encoding=settings.encoding)

    if len(settings.Classes) > 1:
        settings.forceoffsetref = False

    if args:
        for x in args:
            if os.path.isdir(x):
                processdir(x,outputfile)
            elif os.path.isfile(x):
                process(x, outputfile)
            else:
                print("ERROR: File or directory not found: " + x,file=sys.stderr)
                sys.exit(3)
    else:
        print("ERROR: Nothing to do, specify one or more files or directories",file=sys.stderr)

if __name__ == "__main__":
    main()
