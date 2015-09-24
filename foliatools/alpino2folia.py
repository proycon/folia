#! /usr/bin/env python3
# -*- coding: utf8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import lxml
import getopt
import sys
import os
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git", file=sys.stderr)
    sys.exit(2)

def usage():
    print("alpino2folia",file=sys.stderr)
    print("  by Maarten van Gompel (proycon)",file=sys.stderr)
    print("  Radboud University Nijmegen",file=sys.stderr)
    print("  2012-2015 - Licensed under GPLv3",file=sys.stderr)
    print("",file=sys.stderr)
    print("This conversion script reads an Alpino XML document and converts",file=sys.stderr)
    print("it to FoLiA. If multiple input files are specified, and/or the output FoLiA document already exists, then the",file=sys.stderr)
    print("converter will append it.",file=sys.stderr)
    print("",file=sys.stderr)
    print("Usage: alpino2folia [options] alpino-input [alpino-input 2..] folia-output"   ,file=sys.stderr)

def extract_syntax(alpinonode, folianode, foliasentence, alpinoroot):
    for node in alpinonode:
        if 'word' in node.attrib:
            folianode.append(folia.SyntacticUnit, foliasentence[int(node.attrib['begin'])], cls=node.attrib['pos'],id=foliasentence.id+'.alpinonode.'+node.attrib['id'] )
        elif 'cat' in node.attrib:
            su = folianode.append(folia.SyntacticUnit, cls=node.attrib['cat'],id=foliasentence.id+'.alpinonode.'+node.attrib['id'] )
            extract_syntax(node, su, foliasentence,alpinoroot)
        else:
            print("SYNTAX: Don't know what to do with node...", repr(node.attrib) ,file=sys.stderr)

def extract_dependencies(alpinonode, deplayer, foliasentence):
    deps = []
    head = None
    for node in alpinonode:
        #print("DEP:", node,file=sys.stderr)
        if not 'word' in node.attrib:
            extract_dependencies(node, deplayer, foliasentence )
        if 'rel' in node.attrib:
            if node.attrib['rel'] == 'hd':
                head = folia.DependencyHead(deplayer.doc, foliasentence[int(node.attrib['begin'])])
            else:
                deps.append( (node.attrib['rel'], folia.DependencyDependent(deplayer.doc, foliasentence[int(node.attrib['begin'])]) )  )

    if head:
        for cls, dep in deps:
            deplayer.append( folia.Dependency, head, dep, cls=cls)


def makefoliadoc(outputfile):
    baseid = os.path.basename(outputfile).replace('.folia.xml','').replace('.xml','')
    foliadoc = folia.Document(id=baseid)
    foliadoc.append(folia.Text(foliadoc, id=baseid+'.text'))

    if not foliadoc.declared(folia.AnnotationType.TOKEN, 'alpino-tokens'):
        foliadoc.declare(folia.AnnotationType.TOKEN, 'alpino-tokens')
    if not foliadoc.declared(folia.LemmaAnnotation, 'alpino-lemmas'):
        foliadoc.declare(folia.LemmaAnnotation, 'alpino-lemmas')
    if not foliadoc.declared(folia.SenseAnnotation, 'alpino-sense'):
        foliadoc.declare(folia.SenseAnnotation, 'alpino-sense')
    if not foliadoc.declared(folia.PosAnnotation, 'alpino-pos'):
        foliadoc.declare(folia.PosAnnotation, 'alpino-pos')
    if not foliadoc.declared(folia.AnnotationType.DEPENDENCY, 'alpino-dependency'):
        foliadoc.declare(folia.AnnotationType.DEPENDENCY, 'alpino-dependency')
    if not foliadoc.declared(folia.AnnotationType.SYNTAX, 'alpino-syntax'):
        foliadoc.declare(folia.AnnotationType.SYNTAX, 'alpino-syntax')
    if not foliadoc.declared(folia.AnnotationType.MORPHOLOGICAL, 'alpino-morphology'):
        foliadoc.declare(folia.AnnotationType.MORPHOLOGICAL, 'alpino-morphology')

    return foliadoc


def alpino2folia(alpinofile, foliadoc):
    tree = lxml.etree.parse(alpinofile)
    alpinoroot = tree.getroot()
    if alpinoroot.tag != 'alpino_ds':
        raise Exception("source file is not an alpino file")
    sentencenode = alpinoroot.xpath('//sentence')[0]


    foliatextbody = foliadoc[-1]
    foliasentence = foliatextbody.append(folia.Sentence)


    #first pass, extract words
    alpinowords = sentencenode.text.split(' ')
    for alpinoword in alpinowords:
        foliasentence.append(folia.Word,alpinoword.strip())


    #loop over lexical nodes
    for node in alpinoroot.xpath('//node'):
        if 'word' in node.attrib and 'pos' in node.attrib:
            index = int(node.attrib['begin'])
            if alpinowords[index].strip() != node.attrib['word'].strip():
                raise Exception("Inconsistency in Alpino XML! Node@begin refers to word index " + str(index) + ", which has value \"" + alpinowords[index] + "\" and does not correspond with node@word \"" + node.attrib['word'] +  "\"")
            foliaword = foliasentence[index]

            if 'lemma' in node.attrib:
                foliaword.append(folia.LemmaAnnotation, cls=node.attrib['lemma'])
            if 'sense' in node.attrib:
                foliaword.append(folia.SenseAnnotation, cls=node.attrib['sense'])
            if 'root' in node.attrib:
                layer = foliaword.append(folia.MorphologyLayer)
                layer.append(folia.Morpheme, folia.TextContent(foliadoc, node.attrib['root']), cls='root')

            if 'postag' in node.attrib and 'pt' in node.attrib:
                foliapos = foliaword.append(folia.PosAnnotation, cls=node.attrib['postag'], head=node.attrib['pt'])
            elif 'frame' in node.attrib:
                foliaword.append(folia.PosAnnotation, cls=node.attrib['frame'], head=node.attrib['pos'])
            else:
                foliaword.append(folia.PosAnnotation, cls=node.attrib['pos'])

            #gather pos features
            for key, value in node.attrib.items():
                if key in ('wh','per','num','gen','case','def','infl','sc','buiging','refl','tense','comparative','positie','pvagr','pvtijd','graad','pdtype','wvorm','ntype','vwtype','getal','status','naamval','persoon','genus'):
                    foliapos.append(folia.Feature, subset=key, cls=value)
                elif not key in ('sense','pos','rel','postag','pt','frame','root','lemma','id','begin','end','word','index'):
                    print("WARNING: Ignored attribute " + key + "=\"" + value + "\" on node ",file=sys.stderr)

    foliasyntaxlayer = foliasentence.append(folia.SyntaxLayer)
    foliasyntaxtop = foliasyntaxlayer.append(folia.SyntacticUnit, cls='top')

    #extract syntax
    extract_syntax(alpinoroot[0], foliasyntaxtop, foliasentence, alpinoroot)

    foliadeplayer = foliasentence.append(folia.DependenciesLayer)

    #extract dependencies:
    extract_dependencies(alpinoroot[0], foliadeplayer, foliasentence)

    return foliadoc


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "-h", ["help"])
    except getopt.GetoptError as err:
        print(str(err),file=sys.stderr)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        else:
            raise Exception("No such option: " + o)

    if len(args) < 2:
        usage()
        sys.exit(2)
    else:
        alpinofiles = []
        for i, arg in enumerate(args):
            if i < len(args) - 1:
                alpinofiles.append(arg)
        foliafile = args[-1]

    if os.path.exists(foliafile):
        doc = folia.Document(file=foliafile)
    else:
        doc = makefoliadoc(foliafile)
    for alpinofile in alpinofiles:
        doc = alpino2folia(alpinofile, doc)
    doc.save(foliafile)

if __name__ == "__main__":
    main()
