#!/usr/bin/env python
#-*- coding:utf-8 -*-


from pynlpl.formats import folia

print "Generating Relax NG schema"
folia.relaxng('folia.rng')

print "Validating example document"
folia.validate('example.xml')
