#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function, unicode_literals, division, absolute_import

import argparse
import sys
import json
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



def evaluate(docs, Class, foliaset, do_corrections=False, verbose=False):
    nr = len(docs)
    index = []
    for i, doc in enumerate(docs):
        index.append(defaultdict(list))
        if do_corrections:
            for annotations, targets, correction in get_corrections(doc, Class, foliaset):
                targetids = tuple(( target.id for target in targets)) #tuple of IDs; hashable
                for annotation in annotations:
                    index[i][targetids].append( (annotation, correction) )
                    if verbose:
                        print("DOC #" + str(i+1) + " - Found annotation (" + str(annotation.cls) + ") on " + ", ".join(targetids) + " (in correction " + repr(correction) + ")",file=sys.stderr)
        else:
            for annotation in doc.select(Class, foliaset):
                if isinstance(annotation, folia.AbstractSpanAnnotation):
                    targets = annotation.wrefs() #TODO: distinguish span roles?
                else:
                    targets = [annotation.ancestor(folia.AbstractStructure)]
                targetids = tuple(( target.id for target in targets)) #tuple of IDs; hashable
                index[i][targetids].append( annotation )
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

    #collect all possible targets (for normalisation)
    alltargetids = set()
    for i in range(0,nr):
        for targetids in index[i].keys():
            alltargetids.add(targetids)

    evaluation = {
        'foundtargets': len(links),
        'totaltargets': len(alltargetids),
        'value': {'matches': 0, 'misses':0},
        'correctionclass': {'matches': 0, 'misses':0},
        'correction': {'matches': 0, 'misses':0}
    }

    #compute strong matches
    for targets, linkchain in zip(linkedtargets, links):
        #targets example: [<pynlpl.formats.folia.Word object at 0x7fa7dfcadfd0>, <pynlpl.formats.folia.Word object at 0x7fa7dfcc00b8>]
        #linkchain example: [[<pynlpl.formats.folia.Entity object at 0x7fa7dfcc0be0>], [<pynlpl.formats.folia.Entity object at 0x7fa7df7a9630>]]
        #                    ^-- outer index corresponds to doc seq
        #annotations are wrapped in (annotation, correction) tuples if do_corrections is true

        evaluator = Evaluator()

        for annotations in linkchain:
            evaluator.evaluate(docs, linkchain, Class, do_corrections)

        targets_label = " & ".join([ target.id for target in targets])
        for value in evaluator.value_matches:
            print("[VALUE MATCHES]\t" + targets_label + "\t" + value)
        for value in evaluator.value_misses:
            print("[VALUE MISSED]\t" + targets_label + "\t" + value)

        if do_corrections:
            for correctionclass in evaluator.correctionclass_matches:
                print("[CORRECTION CLASS MATCHES]\t" + targets_label + "\t" + correctionclass)
            for correctionclass in evaluator.correctionclass_misses:
                print("[CORRECTION CLASS MISSED]\t" + targets_label + "\t" + correctionclass)
            for correctionclass, value in evaluator.correction_matches:
                print("[CORRECTION MATCHES]\t" + targets_label + "\t" + correctionclass + "\t" + value)
            for correctionclass, value in evaluator.value_misses:
                print("[CORRECTION MISSED]\t" + targets_label + "\t" + correctionclass + "\t" + value)

        evaluation['value']['matches'] += len(evaluator.value_matches)
        evaluation['value']['misses'] += len(evaluator.value_misses)
        evaluation['correctionclass']['matches'] += len(evaluator.correctionclass_matches)
        evaluation['correctionclass']['misses']  += len(evaluator.correctionclass_misses)
        evaluation['correction']['matches']  += len(evaluator.correction_matches)
        evaluation['correction']['misses']   += len(evaluator.correction_misses)

    return evaluation


def iter_linkchain(linkchain, do_corrections):
    for i, annotations in enumerate(linkchain):
        if do_corrections:
            iterator = annotations
        else:
            iterator = [ (annotation, None) for annotation in annotations ]
        for annotation, correction in iterator:
            yield i, annotation, correction

class Evaluator:
    def __init__(self):
        self.value_matches = []
        self.value_misses = []

        self.correctionclass_matches = []
        self.correctionclass_misses = []

        self.correction_matches = []
        self.correction_misses = []

    def evaluate(self, docs, linkchain, Class, do_corrections):
        #first parameter will be output!

        values = defaultdict(set) #abstraction over annotation classes or text content (depending on annotation type)

        correctionclasses = defaultdict(set) #with corrections
        corrections = defaultdict(set)  #full corrections; values and correctionclasses
        for docnr, annotation, correction in iter_linkchain(linkchain, do_corrections):
            value = get_value(annotation, Class) #gets class or text depending on annotation type
            values[value].add(docnr)
            if do_corrections and correction:
                correctionclasses[correction.cls].add(docnr)
                corrections[(correction.cls, value)].add(docnr)


        for value, docset in values.items():
            if len(docset) == len(docs):
                self.value_matches.append(value)
            else:
                self.value_misses.append(value)

        if do_corrections:
            for correctionclass, docset in correctionclasses.items():
                if len(docset) == len(docs):
                    self.correctionclass_matches.append(correctionclass)
                else:
                    self.correctionclass_misses.append(correctionclass)

            for correction, docset in corrections.items():
                if len(docset) == len(docs):
                    self.correction_matches.append(correction)
                else:
                    self.correction_misses.append(correction)


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

    evaluation = evaluate(docs, Type, foliaset, args.corrections, args.verbose)
    print(json.dumps(evaluation))

if __name__ == "__main__":
    main()
