#! /usr/bin/env python
# -*- coding: utf8 -*-

import sys
import subprocess
import os.path
try:
    from pynlpl.formats import folia
except ImportError:
    print >>sys.stderr,"PyNLPL is required to run this script, obtain it from https://github.com/proycon/pynlpl and either install it or make sure the pynlpl/ dir is symlinked from the directory this script is in."
    sys.exit(3)

xsltfile = 'folia.rng'

if __name__ == '__main__':    
    try:
        foliadir = sys.argv[1]    
    except:
        print >>sys.stderr,"Syntax: folia_validator.py file-or-directory"
        sys.exit(2)
    
            
    maxtasksperchild = 10
    if os.path.isdir(foliadir):
        files = folia.CorpusFiles(foliadir, 'xml',"",lambda x: True)
    elif os.path.isfile(foliadir):
        files = [foliadir]
    else:
        print >>sys.stderr,"ERROR: No such file or directory: " + foliadir
        sys.exit(1)
    valid = errors = 0
    for filename in files:
        print "Shallow FoLiA validation on " + filename + ":",
        try:
            output = subprocess.check_output('xsltproc ' + xsltfile + ' ' + filename + ' > /dev/null', shell=True,stderr=subprocess.STDOUT)
            valid += 1
            print "OK" 
        except subprocess.CalledProcessError as e:            
            errors += 1
            f = open(filename.replace('.xml','.err'),'w')
            f.write(e.output)
            f.close()
            print "ERRORS (inspect " + filename.replace('.xml','.err') + " for details)"
            print >>sys.stderr, "File " + filename + " did not validate! (inspect " + filename.replace('.xml','.err') + " for details)" 

    print "All done."
    print "Valid:  " + str(valid)
    print "Errors: " + str(errors)
    
