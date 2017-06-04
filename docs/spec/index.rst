FoLiA: Format for Linguistic Annotation
=======================================

Introduction
------------------

FoLiA, an acronym for **Format for Linguistic Annotation**, is a file format and data model to represent digitised
language resources enriched with a possibly wide variety of linguistic annotation, e.g. linguistically enriched textual
documents or transcriptions of speech. The format is intended to provide a standard for the storage and exchange of such
language resources, including corpora and promote interoperability amongst Natural Language Processing tools that use
the format.

Our aim is to introduce a single rich format that can accommodate a wide variety of linguistic annotation types through
a single generalised paradigm. We do not commit to any label/vocabulary set, language or linguistic theory.  This is always left to
the developer of the language resources, and provides maximum flexibility. We merely specify the broad category of annotation types.

* **Expressive**: The format is highly expressive, annotations can be expressed in great detail and with flexibility to the user's needs, without forcing unwanted details. Moreover, FoLiA has generalised support for representing annotation alternatives, and annotation metadata such as information on annotator, time of annotation, and annotation confidence.
* **Generic** - We apply the same paradigm to a wide variety of annotation types, assuring a uniform and consistent way of representing different annotation.
* **Formalised** - The format is formalised, and can be validated on both a shallow and a deep level (the latter including tagset validation), and easily machine parsable, for which tools are provided.
* **Practical** - FoLiA has been developed in a bottom-up fashion right alongside applications, programming libraries, and other toolkits and converters. Whilst the format is rich, we try to maintain it as simple and straightforward as possible, minimising the learning curve and making it easy to adopt FoLiA in practical applications.

The FoLiA format is XML-based and makes mixed-use of inline and stand-off annotation. XML is an inherently hierarchic
format and FoLiA does justice to this by utilising a hierarchic, inline, setup where possible. Inline annotation is used
for annotations pertaining to singular structural elements such as words/tokens, whilst stand-off annotation in separate
annotation layers is adopted for annotation types that span over multiple structural elements.

Generic Annotation Groups
---------------------------

FoLiA defines various XML elements to represent document structure and various annotations, we can divide these XML
elements into the following four generic annotation groups:

* **Structure Annotation** -- Elements to denote the structure of a document, e.g. division in paragraphs, sentences,
  words, sections like chapters, lists, tables, etc...
* **Token Annotation** -- Annotation elements pertaining to a single
  structural element (often a word/token, hence the name, but not necessarily so!). Examples in this category are: Part-of-Speech annotation, Lemmatisation
* **Span Annotation** -- Annotation elements that span multiple words/tokens/structural elements. These are defined in
  annotation layers. The annotation layers are embedded in any structural element (often a sentence) that covers the scope of the
  annotations. Examples in this category are: Named entity annotation, co-reference annotation, semantic roles,
  dependency relations.
* **Higher order Annotation** --  Annotations on annotations. This category subsumes various specialised annotation types that are
  considered annotations on annotations, such as **Alternative Annotations** and **Corrections**.

In each of these categories, FoLiA defines specific elements for specific annotation types.

Vocabulary sets
------------------

FoLiA specifically defines various types of annotation, but it never defines the vocabulary (aka label/tag sets) you can
use for those annotations. The vocabulary for, for instance, Part-of-Speech annotation can be defined by anyone in a
separate publicly available file known as a **Set Definition**. Anybody is free to create and host their own set
definitions on the internet. These set definitions are typically formulated according to a linked open data model (SKOS) and as-such
provide a semantic foundation. Each FoLiA document *declares* in its metadata section, what set definitions to use
(described by a URL pointing to a set definition file) for what annotation types. The individual labels inside a set are
called **classes** in the FoLiA paradigm. Classes in a Part-of-Speech tagset, for instance, could be ``Noun``, ``Verb``
or ``Adjective``, or a more symbolic version thereof (human readable labelling is exlusively done inside the set
definition, classes typically refer to more symbollic names, such as ``N``, ``V`` or ``ADJ`` in this case).

This vocabulary paradigm of independently defined sets and classes is a fundamental part of FoLiA and stretches accross all annotation types.

Validation
-------------

If you create FoLiA documents in any shape or form, it is of great importance that you validate whether they indeed conform to the FoLiA
specification; otherwise they can not be processed correctly by any FoLiA-aware software. Specific validator software is
provided to this end.

* A first level of validation is performed by comparing your document against the FoLiA schema (in RelaxNG), this gives you a
  good indication whether the document is formed corrected; but is not sufficient for full validation!
* For full validation, process the document using one of the provided validation tools. These tools make a distinction
  between **shallow validation** and **deep validation**, the distinction being that only in the latter case the validity of all used
  classes will be put to the test using the set definitions.

Common attributes
-------------------

Annotation elements in FoLiA carry a subset of so-called *common attributes*, these are common properties (represented
as XML attributes) that can be set on different annotations. The exact subset of mandatory or optional common attributes
differs slightly per element. We distinguish the following:


* ``xml:id`` -- The ID of the element
* ``set`` -- The set of the element (a URI linking to a set definition)
* ``class`` -- The class of the annotation
* ``annotator`` -- The name or ID of the system or human annotator that made the annotation.
* ``annotatortype`` -- ``manual`` for human annotators, or ``auto`` for automated systems.
* ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
* ``datetime`` --  The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
* ``n`` --  A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers.

The following extra common attributes apply in a speech context:

* ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
* ``begintime`` --  A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
* ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
* ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.

Document structure
----------------------




















Contents:

.. toctree::
    :maxdepth: 3
    :glob:

    *

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

