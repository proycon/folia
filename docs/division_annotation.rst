.. _division_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(division)
Division Annotation
==================================================================

.. foliaspec:annotationtype_description(division)
Structure annotation representing some kind of division, typically used for chapters, sections, subsections (up to the set definition). Divisions may be nested at will, and may include almost all kinds of other structure elements.

Specification
---------------

.. foliaspec:specification(division)
:Element Name (primary): ``<div>``
:Category: :ref:`structure_annotation_category`
:Declaration: ``<division-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data (as Annotation Types): :ref:`alignment_annotation`, :ref:`correction_annotation`, :ref:`division_annotation`, :ref:`entry_annotation`, :ref:`event_annotation`, :ref:`example_annotation`, :ref:`figure_annotation`, :ref:`gap_annotation`, :ref:`linebreak_annotation`, :ref:`list_annotation`, :ref:`metric_annotation`, :ref:`note_annotation`, :ref:`paragraph_annotation`, :ref:`part_annotation`, :ref:`phon_annotation`, :ref:`sentence_annotation`, :ref:`table_annotation`, :ref:`text_annotation`, :ref:`utterance_annotation`, :ref:`whitespace_annotation`
:Accepted Data (as FoLiA XML Elements): ``<alignment>``, ``<correction>``, ``<div>``, ``<entry>``, ``<event>``, ``<ex>``, ``<figure>``, ``<gap>``, ``<br>``, ``<list>``, ``<metric>``, ``<note>``, ``<p>``, ``<part>``, ``<ph>``, ``<s>``, ``<table>``, ``<t>``, ``<utt>``, ``<whitespace>``
:Accepted Data (as API Classes): ``Alignment``, ``Correction``, ``Division``, ``Entry``, ``Event``, ``Example``, ``Figure``, ``Gap``, ``Linebreak``, ``List``, ``Metric``, ``Note``, ``Paragraph``, ``Part``, ``PhonContent``, ``Sentence``, ``Table``, ``TextContent``, ``Utterance``, ``Whitespace``
:Valid Context (as Annotation Types): :ref:`division_annotation`, :ref:`event_annotation`
:Valid Context (as FoLiA XML Elements): ``<div>``, ``<event>``
:Valid Context (as API Classes): ``Division``, ``Event``
:Version History: Since the beginning

Description & Examples
-------------------------

The structure element ``<div>`` is used to create divisions and subdivisions within a text.

Each division *may* be of a particular *class* pertaining to a *set* defining all possible classes, common classes for
this annotation type would be *chapter*, *section*, *subsection*. A set, however, is not mandatory for most types of
structure, so divisions may be
set-less.

Divisions and other structural units are often numbered, think for example of
chapters and sections. The number, as it was in the source document, can be
encoded in the *n* attribute of the structure annotation element.

Look at the following example, showing a full FoLiA document with structured
divisions. The declared set is a fictitious example:

.. literalinclude:: ../examples/snippets/division.folia.xml
    :linenos:
    :language: xml


