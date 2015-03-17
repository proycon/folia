#!/usr/bin/env python
#-*- coding:utf-8 -*-

#---------------------------------------------------------------
# CGN to FoLiA Converter
#   by Maarten van Gompel
#   Centre for Language Studies
#   Radboud University Nijmegen
#   proycon AT anaproy DOT nl
#
#   Licensed under GPLv3
#
# This script converts CGN to FoLiA format. (Note that paragraph information
# is not available in CGN and therefore not stored in FoLiA format either.)
#
#----------------------------------------------------------------

from __future__ import print_function, unicode_literals, division, absolute_import

import sys
import glob
import gzip
import os
from pynlpl.formats import folia

CGN_ENCODING = 'iso-8859-15' #not yet used!

if len(sys.argv) != 3:
    print("SYNTAX: ./cgn2folia.py cgnrootdir outputdir", file=sys.stderr)
    sys.exit(1)

cgndir = sys.argv[1]
outdir = sys.argv[2]


plkdir = os.path.join(cgndir,"data","annot","text","plk")
for compdir in glob.glob(os.path.join(plkdir, "comp-*")):
    collection_id = "CGN-" + os.path.basename(compdir)
    print(collection_id)
    try:
        os.mkdir(os.path.join(outdir, collection_id))
    except:
        pass
    files = list(glob.glob(os.path.join(compdir,"nl","*.gz"))) + list(glob.glob(os.path.join(compdir, "vl","*.gz")))
    for path in files:
        text_id = os.path.basename(path).split(".")[0]
        print("\t" + text_id)
        full_id = collection_id + "_" + text_id
        au_id = None
        sentence = None

        doc = folia.Document(id=full_id)
        doc.metadatatype = folia.MetaDataType.IMDI
        doc.metadatafile = text_id + ".imdi"
        textbody = doc.append(folia.Text(doc, id=full_id+"."+text_id))
        doc.declare(folia.PosAnnotation, set="hdl:1839/00-SCHM-0000-0000-000B-9")
        doc.declare(folia.LemmaAnnotation, set="hdl:1839/00-SCHM-0000-0000-000E-3")

        fin = gzip.open(path,'r')
        for line in fin:
            line = unicode(line,CGN_ENCODING)
            if line:
                if line[0:3] == '<au':
                    end = line[8:].find('"')
                    if end != -1:
                        end += 8
                        au_id = line[8:end]
                        sentence = textbody.append(folia.Sentence, id=full_id + ".s." + au_id)
                elif line[0:3] == '<mu':
                    au_id = None
                    pass #ignore
                elif au_id:
                    try:
                        wordtext,pos,lemma, extra = line.split("\t",3)
                    except ValueError:
                        print("\tWARNING: Line malformed: ", line, file=sys.stderr)
                        continue
                    word = sentence.append(folia.Word, wordtext)
                    word.append(folia.PosAnnotation, cls=pos)
                    word.append(folia.LemmaAnnotation, cls=lemma)
        fin.close()
        doc.save(os.path.join(outdir ,collection_id, full_id , '.folia.xml'))



