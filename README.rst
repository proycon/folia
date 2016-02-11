FoLiA: Format for Linguistic Annotation
=======================================

.. image:: https://travis-ci.org/proycon/folia.svg?branch=master
    :target: https://travis-ci.org/proycon/folia

.. image:: http://applejack.science.ru.nl/lamabadge.php/folia
   :target: http://applejack.science.ru.nl/languagemachines/

*by Maarten van Gompel, Radboud University Nijmegen*

https://proycon.github.io/folia

FoLiA is an XML-based annotation format, suitable for the representation
of linguistically annotated language resources. FoLiA’s intended use is
as a format for storing and/or exchanging language resources, including
corpora. Our aim is to introduce a single rich format that can
accommodate a wide variety of linguistic annotation types through a
single generalised paradigm. We do not commit to any label set, language
or linguistic theory. This is always left to the developer of the
language resource, and provides maximum flexibility.

XML is an inherently hierarchic format. FoLiA does justice to this by
maximally utilising a hierarchic, inline, setup. We inherit from the
D-Coi format, which posits to be loosely based on a minimal subset of
TEI. Because of the introduction of a new and much broader paradigm,
FoLiA is not backwards-compatible with D-Coi, i.e. validators for D-Coi
will not accept FoLiA XML. It is however easy to convert FoLiA to less
complex or verbose formats such as the D-Coi format, or plain-text.
Converters are provided.

The main characteristics of FoLiA are:

-  **Generalised paradigm** - We use a generalised paradigm, with as few
   ad-hoc provisions for annotation types as possible.
-  **Expressivity** - The format is highly expressive, annotations can
   be expressed in great detail and with flexibility to the user’s
   needs, without forcing unwanted details. Moreover, FoLiA has
   generalised support for representing annotation alternatives, and
   annotation metadata such as information on annotator, time of
   annotation, and annotation confidence.
-  **Extensible** - Due to the generalised paradigm and the fact that
   the format does not commit to any label set, FoLiA is fairly easily
   extensible.
-  **Formalised** - The format is formalised, and can be validated on
   both a shallow and a deep level (the latter including tagset
   validation), and easily machine parsable, for which tools are
   provided.
-  **Practical** - FoLiA has been developed in a bottom-up fashion right
   alongside applications, libraries, and other toolkits and converters.
   Whilst the format is rich, we try to maintain it as simple and
   straightforward as possible, minimising the learning curve and making
   it easy to adopt FoLiA in practical applications.

The FoLiA format makes mixed-use of inline and stand-off annotation.
Inline annotation is used for annotations pertaining to single tokens,
whilst stand-off annotation in a separate annotation layers is adopted
for annotation types that span over multiple tokens. This provides FoLiA
with the necessary flexibility and extensibility to deal with various
kinds of annotations.

Notable features are:

-  XML-based, UTF-8 encoded
-  Language and tagset independent
-  Can encode both tokenised as well as untokenised text + partial
   reconstructability of untokenised form even after tokenisation.
-  Generalised paradigm, extensible and flexible
-  Provenance support for all linguistic annotations: annotator, type
   (automatic or manual), time.
-  Used by various software projects and corpora, especially in the
   Dutch-Flemish NLP community

Resources
---------

-  `Website <http://proycon.github.io/folia>`_
-  `Documentation <http://github.com/proycon/folia/blob/master/docs/folia.pdf?raw=true>`__
-  `RelaxNG schema <http://github.com/proycon/folia/blob/master/schemas/folia.rng>`__
-  **Example** of a FoLiA document (with in-browser visualisation
   through XSL, use view source for XML):
   http://proycon.github.io/folia/example.xml
-  **FoLiA library for Python**: ``pynlpl.formats.folia`` (`source <http://github.com/proycon/pynlpl/blob/master/formats/folia.py>`__, `documentation <https://pythonhosted.org/PyNLPl/folia.html>`__)
-  **C++ Library**: ``libfolia`` (`download <http://ilk.uvt.nl/folia/download-libfolia.php>`__, *by Ko van der Sloot (Tilburg University)*

Publications
------------

-  Maarten van Gompel & Martin Reynaert (2014). **FoLiA: A practical XML
   format for linguistic annotation - a descriptive and comparative
   study;** Computational Linguistics in the Netherlands Journal;
   3:63-81; 2013.
-  Maarten van Gompel (2014). **FoLiA: Format for Linguistic Annotation.
   Documentation.** Language and Speech Technology Technical Report
   Series LST-14-01. Radboud University Nijmegen.


FoLiA Tools
=================

A number of command-line tools are readily available for working with FoLiA, to various ends. The following tools are currently available:

- ``foliavalidator`` -- Tests if documents are valid FoLiA XML. **Always use this to test your documents if you produce your own FoLiA documents!**
- ``foliaquery`` -- Advanced query tool that searches FoLiA documents for a specified pattern, or modifies a document according to the query. Supports FQL (FoLiA Query Language) and CQL (Corpus Query Language).
- ``folia2txt`` -- Convert FoLiA XML to plain text (pure text, without any annotations)
- ``folia2annotatedtxt`` -- Like above, but produces output simple
  token annotations inline, by appending them directly to the word using a specific delimiter.
- ``folia2columns`` -- This conversion tool reads a FoLiA XML document
  and produces a simple columned output format (including CSV) in which each token appears on one line. Note that only simple token annotations are supported and a lot of FoLiA data can not be intuitively expressed in a simple columned format!
- ``folia2html`` -- Converts a FoLiA document to a semi-interactive HTML document, with limited support for certain token annotations.
- ``folia2dcoi`` -- Convert FoLiA XML to D-Coi XML (only for annotations supported by D-Coi)
- ``alpino2folia`` -- Convert Alpino-DS XML to FoLiA XML
- ``dcoi2folia`` -- Convert D-Coi XML to FoLiA XML
- ``rst2folia`` -- Convert ReStructuredText, a lightweight non-intrusive text markup language, to FoLiA, using `docutils <http://docutils.sourceforge.net/>`_.

All of these tools are written in Python, and thus require a Python (2.7, 3 or higher) installation to run. More tools are added as time progresses. 

Installation
---------------

The FoLiA tools are published to the Python Package Index and can be installed effortlessly using \texttt{pip}, from the command-line, type::
 
  $ pip install folia-tools

Add ``sudo`` to install it globally on your system, if you install locally, we strongly
recommend you use virtualenv to make a self-contained Python environment.

If ``pip`` is not yet available, install it as follows:

On Debian/Ubuntu-based systems::

  $ sudo apt-get install python-pip

On RedHat-based systems::

  $ yum install python-pip

On Arch Linux systems::

  $ pacman -Syu python-pip

On Mac OS X and Windows we recommend you install `Anaconda <http://continuum.io/>`_ or another Python distribution.

Alternatively, you can use ``easy_install``. The FoLiA tools can also be
obtained from `github <https://github.com/proycon/folia>`_, and once
downloaded and extracted, can be installed using ``python setup.py
install``.

Usage
-------

To obtain help regarding the usage of any of the available FoLiA tools, please pass the $-h$ option on the command line to the tool you intend to use. This will provide a summary on available options and usage examples. Most of the tools can run on both a single FoLiA document, as well as a whole directory of documents, allowing also for recursion. The tools generally take one or more file names or directory names as parameters.

More?
-----

Please consult the FoLiA website at http://proycon.github.io/folia for more!
