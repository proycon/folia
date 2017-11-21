#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import argparse
import sys
from itertools import chain
from collections import Counter, defaultdict
try:
    from pynlpl.formats import folia
except:
    print("ERROR: pynlpl not found, please obtain PyNLPL from the Python Package Manager ($ sudo pip install pynlpl) or directly from github: $ git clone git://github.com/proycon/pynlpl.git",file=sys.stderr)
    sys.exit(2)



def is_structural(correction):
    for annotation in chain(correction.new(), correction.original()):
        if isinstance(annotation, folia.AbstractStructure):
            return True
    return False

def get_corrections(doc, Class, foliaset):
    """Get relevant corrections from document"""
    for correction in doc.select(folia.Correction):
        structural = is_structural(correction)

        #find targets, i.e. the original tokens this correction applies to
        targets = []
        if structural:
            #structural correction
            if correction.hasoriginal():
                for structure in correction.original():
                    if isinstance(structure, folia.AbstractStructureElement):
                        targets.append(structure)
            elif correction.hasoriginal(allowempty=True):
                #TODO: deal with insertions
                print("INSERTION found but not implemented yet",file=sys.stderr)
                pass
        elif issubclass(Class, folia.AbstractSpanAnnotation):
            #span annotation
            pass #defer until later
        else:
            #token annotation
            targets = [correction.ancestor(folia.AbstractStructureElement)]

        if correction.hasnew():
            annotations = []
            for annotation in correction.new():
                if isinstance(annotation, Class) and annotation.set == foliaset:
                    annotations.append(annotation)
                    if issubclass(Class, folia.AbstractSpanAnnotation):
                        targets += annotation.wrefs()
        elif correction.hasnew(allowempty=True) and structural:
            #TODO: deal with deletion
            print("DELETION found but not implemented yet",file=sys.stderr)
            pass

        yield annotations, targets, correction


def inter_annotator_agreement(docs, Class, foliaset, do_corrections=False, verbose=False):
    nr = len(docs)
    index = []
    for i, doc in enumerate(docs):
        index.append(defaultdict(list))
        if do_corrections:
            for annotations, targets, correction in get_corrections(doc, Class, foliaset):
                targets = tuple(targets) #make hashable
                index[i][targets].append( (annotations, correction) )
        else:
            for annotation in doc.select(Class, foliaset):
                if isinstance(annotation, folia.AbstractSpanAnnotation):
                    targets = annotation.wrefs() #TODO: distinguish span roles?
                else:
                    targets = [annotation.ancestor(folia.AbstractStructure)]
                targetids = tuple(( target.id for target in targets)) #tuple of IDs; hashable
                index[i][targetids].append( [annotation] )
                if verbose:
                    print("DOC #" + str(i+1) + " - Found annotation (" + str(annotation.cls) + ") on " + ", ".join(targetids),file=sys.stderr)

    #linking step: links annotations on the same things
    links = []
    linkedtargets = []
    for targets in index[0]:
        linkchain = []
        for i, doc in enumerate(docs):
            assert isinstance(doc, folia.Document)
            if i == 0: linkedtargets.append([ doc[targetid] for targetid in targets] )
            if targets not in index[i]:
                break
            else:
                linkchain.append(index[i][targets])
        if len(linkchain) == nr:
            links.append(linkchain)



    #evaluation step
    weakmatches = len(links) #match regardless of class

    strongmatches = 0 #match including class
    correctionmatches = 0 #match including correction class
    weakcorrections = 0 #correction *with* class
    strongcorrections = 0 #correction matches both for class and content
    #compute strong matches
    for target, linkchain in zip(linkedtargets, links):
        if do_corrections:
            values = [ get_value(annotation, Class) for annotation, correction in linkchain ]
            correctionmatch = all_equal([ correction.cls for annotation, correction in linkchain ])
            weakcorrections += int(correctionmatch)
        else:
            values = [ get_value(annotation, Class) for annotation in linkchain ]
        match = all_equal(values)
        strongmatches += int(match)
        if do_corrections:
            strongcorrections += int(match and correctionmatch)
        if verbose:
            if match:
                print("STRONG\t" + target.id + "\t" + get_value(annotation, Class))
            else:
                print("WEAK\t" + target.id + "\t" + "; ".join([ get_value(annotation, Class)] ))
            if do_corrections:
                if correctionmatch:
                    print("CORRECTION CLASS MATCHES: " + linkchain[0][1].cls)
                else:
                    print("CORRECTION CLASS DOES NOT MATCH: " + "; ".join([ correction.cls for _, correction in linkchain ]))

    #collect all possible targets (for normalisation)
    alltargets = set()
    for i in index:
        for target in index[i]:
            alltargets.add(hash(target))

    return strongmatches, weakmatches, len(alltargets), strongcorrections, weakcorrections

def all_equal(collection):
    iterator = iter(collection)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

def get_value(annotation, Class):
    if Class is folia.TextContent or Class is folia.PhonContent:
        return str(annotation)
    return annotation.cls

def main():
    parser = argparse.ArgumentParser(description="FoLiA Inter-Annotator Agreement: This tool computes inter-annotator agreement on two or more structurally equivalent FoLiA documents. Evaluation is expressed as accuracy on the total number of annotation targets (often words) and comes in two flavours: weak and strong. Weak checks only if the same items were marked and can be used as a measure of detection; strong checks if the assigned classes are equal amongst annotators.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    #parser.add_argument('--storeconst',dest='settype',help="", action='store_const',const='somevalue')
    parser.add_argument('-t','--type', type=str,help="Annotation type to consider", action='store',default="",required=True)
    parser.add_argument('-s','--set', type=str,help="Set definition (required if there is ambiguity in the document)", action='store',required=False)
    parser.add_argument('-c','--corrections', help="Use corrections", action='store_true',default="",required=False)
    parser.add_argument('-v','--verbose', help="Verbose, list all matches/mismatches", action='store_true',required=False)
    #parser.add_argument('-i','--number',dest="num", type=int,help="", action='store',default="",required=False)
    parser.add_argument('documents', nargs='+', help='FoLiA Documents')
    args = parser.parse_args()

    docs = []
    for docfile in args.documents:
        if args.verbose:
            print("Loading " + docfile,file=sys.stderr)
        docs.append( folia.Document(file=docfile))

    try:
        Type = folia.XML2CLASS[args.type]
    except KeyError:
        print("No such type: ", args.type,file=sys.stderr)

    foliaset = args.set
    if args.verbose:
        print("type=" + repr(Type),file=sys.stderr)
        print("set=" + repr(foliaset),file=sys.stderr)

    strongmatches, weakmatches, total, strongcorrections, weakcorrections  = inter_annotator_agreement(docs, Type, foliaset, args.corrections, args.verbose)
    if not total:
        print("strong\t0\t0")
        print("weak\t0\t0")
        print("total\t0")
    else:
        print("strong\t" + str(strongmatches) + "\t" + str(round(strongmatches/total,3)))
        print("weak\t" + str(weakmatches) + "\t" + str(round(weakmatches/total,3)))
        if args.corrections:
            print("strongcorrections\t" + str(strongcorrections) + "\t" + str(round(strongcorrections/total,3)))
            print("weakcorrections\t" + str(weakcorrections) + "\t" + str(round(weakcorrections/total,3)))
        print("total\t" + str(total))

if __name__ == "__main__":
    main()
