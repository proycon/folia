#! /usr/bin/env python
# -*- coding: utf8 -*-

import os
from setuptools import setup, find_packages



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "FoLiA-tools",
    version = "0.9.0.8",
    author = "Maarten van Gompel",
    author_email = "proycon@anaproy.nl",
    description = ("FoLiA-tools contains various Python-based command line tools for working with FoLiA XML (Format for Linguistic Annotation)"),
    license = "GPL",
    keywords = "nlp computational_linguistics search linguistics toolkit folia pynlpl",
    url = "https://github.com/proycon/folia",
    packages=['foliatools'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 2.6",
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    entry_points = {
        'console_scripts': [
            'folia2txt = foliatools.folia2txt:main',
            'foliafreqlist = foliatools.foliafreqlist:main',
            'foliavalidator = foliatools.foliavalidator:main',
            'folia2columns = foliatools.folia2columns:main',
            'folia2dcoi = foliatools.folia2dcoi:main',
            'folia2html = foliatools.folia2html:main',
	    'foliaquery = foliatools.foliaquery:main',
	    'foliatextcontent = foliatools.foliatextcontent:main',
            'dcoi2folia = foliatools.dcoi2folia:main', 
        ]
    },
    #include_package_data=True,
    package_data = {'foliatools': ['*.xsl'] },
    install_requires=['pynlpl >= 0.5.4.1', 'lxml >= 2.2']
)
