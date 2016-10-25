#!/usr/bin/env python3
#Generate library specification code (for either Python or C++) on the the basis of folia.yml
#Used by respectively pynlpl and libfolia

from __future__ import print_function, unicode_literals, division, absolute_import

import sys
import os
import json
import yaml

#Load specification
specfiles= [  os.path.join(os.path.dirname(__file__) ,'../schemas/folia.yml'), 'folia.yml' ]
spec = None
for specfile in specfiles:
    spec = yaml.load(open(specfile,'r'))
    break

if spec is None:
    print("FoLiA Specification file folia.yml could not be found in " + ", ".join(specfiles) ,file=sys.stderr)

def main(var=None):
    try:
        var = sys.argv[1]
        if var[0] == '-': var = None
    except:
        var = None
    if var:
        print(var + ' = ' + json.dumps(spec, sort_keys=True, indent=4) + ';')
    else:
        print(json.dumps(spec, sort_keys=True, indent=4))

if __name__ == '__main__':
    main()
