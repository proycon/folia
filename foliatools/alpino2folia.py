#! /usr/bin/env python
# -*- coding: utf8 -*-

import lxml
import getopt
import sys
import os
try:
    from pynlpl.formats import folia
except:
    print >>sys.stderr,"ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo easy_install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git"
    sys.exit(2)
    
def usage():
    print >>sys.stderr, "alpino2folia"
    print >>sys.stderr, "  by Maarten van Gompel (proycon)"
    print >>sys.stderr, "  Radboud University Nijmegen"
    print >>sys.stderr, "  2012 - Licensed under GPLv3"
    print >>sys.stderr, ""
    print >>sys.stderr, "This conversion script reads an Alpino XML document and converts"
    print >>sys.stderr, "it to FoLiA. If the output FoLiA document already exists, then the"
    print >>sys.stderr, "converter will append it."
    print >>sys.stderr, ""
    print >>sys.stderr, "Usage: alpino2folia [options] alpino-input folia-output"   
    
def extract_syntax(alpinonode, folianode, foliasentence, alpinoroot):    
    for node in alpinonode:
        print >>sys.stderr,"SYNTAX:", node
        if 'word' in node.attrib:
            folianode.append(folia.SyntacticUnit, foliasentence[int(node.attrib['begin'])], cls=node.attrib['pos'])
        elif 'cat' in node.attrib:
            su = folianode.append(folia.SyntacticUnit, cls=node.attrib['cat'])
            extract_syntax(node, su, foliasentence,alpinoroot)
        elif 'index' in node.attrib:
                pos = foliasentence[int(node.attrib['index'])-1].annotation(folia.PosAnnotation)
                
                if pos.feat('head'):
                    pos = pos.feat('head')
                else:                                    
                    pos = pos.cls
                folianode.append(folia.SyntacticUnit, foliasentence[int(node.attrib['index'])-1], cls=pos )
        else:            
            print >>sys.stderr,"SYNTAX: Don't know what to do with node...", repr(node.attrib) 
            
def extract_dependencies(alpinonode, deplayer, foliasentence):
    deps = []
    head = None
    for node in alpinonode:
        print >>sys.stderr,"DEP:", node
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
                

def alpino2folia(alpinofile, foliadoc=None):
    tree = lxml.etree.parse(alpinofile)
    alpinoroot = tree.getroot()
    if alpinoroot.tag != 'alpino_ds':
        raise Exception("source file is not an alpino file")
    sentencenode = alpinoroot.xpath('//sentence')[0]
    
    baseid = os.path.basename(alpinofile.replace('.xml',''))
    if not foliadoc:
        foliadoc = folia.Document(id=baseid)
        foliadoc.append(folia.Text(foliadoc, id=baseid+'.text'))        
    
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
    
    foliatextbody = foliadoc[-1]
    foliasentence = foliatextbody.append(folia.Sentence)
    
       
    #first pass, extract words
    alpinowords = sentencenode.text.split(' ')
    for alpinoword in alpinowords:
        foliasentence.append(folia.Word,alpinoword)
        
    #loop over lexical nodes
    for node in alpinoroot.xpath('//node'):
        if 'word' in node.attrib and 'pos' in node.attrib:
            index = int(node.attrib['begin'])
            assert alpinowords[index] == node.attrib['word']
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
                elif not (key in ('sense','pos','rel','postag','pt','frame','root','lemma','id','begin','end','word','index')): 
                    print >>sys.stderr, "WARNING: Ignored attribute " + key + "=\"" + value + "\" on node..."
    
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
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        else:            
            raise Exception("No such option: " + o)    
    
    try:
        alpinofile, foliafile = args
    except:
        usage()
        sys.exit(2)        
    
    if os.path.exists(foliafile):
        doc = folia.Document(file=foliafile)
    else:
        doc = None
    doc = alpino2folia(alpinofile, doc)
    doc.save(foliafile)
    
if __name__ == "__main__":
    main()
