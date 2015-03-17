# -*- coding: utf8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import lxml.etree
import sys
import glob
import getopt
import os.path
import io

def transform(xsltfilename, sourcefilename, targetfilename = None, encoding = 'utf-8'):
    xsldir = os.path.dirname(__file__)
    if xsltfilename[0] != '/': xsltfilename = os.path.join(xsldir, xsltfilename)
    if not os.path.exists(xsltfilename):
        raise Exception("XSL Stylesheet not found: " + xsltfilename)
    elif not os.path.exists(sourcefilename):
        raise Exception("File not found: " + sourcefilename)
    xslt = lxml.etree.parse(xsltfilename)
    transformer = lxml.etree.XSLT(xslt)
    parsedsource = lxml.etree.parse(sourcefilename)
    transformed = transformer(parsedsource)
    if targetfilename:
        f = io.open(targetfilename, 'w',encoding='utf-8')
        if sys.version < '3':
            f.write( lxml.etree.tostring(transformed, pretty_print=True, encoding=encoding) )
        else:
            f.write(str(lxml.etree.tostring(transformed, pretty_print=True, encoding=encoding),encoding))
        f.close()
    else:
        if sys.version < '3':
            print(lxml.etree.tostring(transformed, pretty_print=True, encoding=encoding))
        else:
            print(str(lxml.etree.tostring(transformed, pretty_print=True, encoding=encoding),encoding))


def usage():
    print(settings.usage,file=sys.stderr)
    print("",file=sys.stderr)
    print("Parameters for output:"        ,file=sys.stderr)
    print("  -o [filename]                Output to file (instead of default stdout)"    ,file=sys.stderr)
    print("  -e [encoding]                Output encoding (default: utf-8)" ,file=sys.stderr)
    print("Parameters for processing directories:",file=sys.stderr)
    print("  -r                           Process recursively",file=sys.stderr)
    print("  -E [extension]               Set extension (default: xml)",file=sys.stderr)
    print("  -q                           Ignore errors",file=sys.stderr)



class settings:
    autooutput = False
    extension = 'xml'
    recurse = False
    ignoreerrors = False
    encoding = 'utf-8'
    xsltfilename = "undefined.xsl"
    outputextension = 'UNDEFINED'
    usage = "UNDEFINED"

def processdir(d, outputfilename = None):
    print("Searching in  " + d, file=sys.stderr)
    for f in glob.glob(os.path.join(d,'*')):
        if f[-len(settings.extension) - 1:] == '.' + settings.extension and f[-len(settings.outputextension) - 1:] != '.' + settings.outputextension:
            outputfilename =  f[:-len(settings.extension) - 1] + '.' + settings.outputextension
            process(f, outputfilename)
        elif settings.recurse and os.path.isdir(f):
            processdir(f, outputfilename)

def process(inputfilename, outputfilename=None):
    try:
        transform(settings.xsltfilename, inputfilename, outputfilename, settings.encoding)
    except Exception as e:
        if settings.ignoreerrors:
            print("ERROR: An exception was raised whilst processing " + inputfilename + ":", e, file=sys.stderr)
        else:
            raise


def main(xsltfilename, outputextension, usagetext):
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:E:hrq", ["help"])
    except getopt.GetoptError as err:
        print(str(err), file=sys.stderr)
        usage()
        sys.exit(2)

    settings.xsltfilename = xsltfilename
    settings.outputextension = outputextension
    settings.usage = usagetext

    outputfilename = ""


    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        elif o == '-t':
            settings.retaintokenisation = True
        elif o == '-e':
            settings.encoding = a
        elif o == '-E':
            settings.extension = a
        elif o == '-o':
            outputfilename = a
        elif o == '-r':
            settings.recurse = True
        elif o == '-q':
            settings.ignoreerrors = True
        else:
            raise Exception("No such option: " + o)

    if args:
        for x in args:
            if os.path.isdir(x):
                processdir(x)
            elif os.path.isfile(x):
                if len(sys.argv) > 2: outputfilename = outputfilename =  x[:-len(settings.extension) - 1] + '.' + settings.outputextension
                process(x, outputfilename)
            else:
                print("ERROR: File or directory not found: " + x, file=sys.stderr)
                sys.exit(3)
    else:
        print("ERROR: Nothing to do, specify one or more files or directories",file=sys.stderr)
