.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _hyphenation_annotation:

Hyphenation
==================================================================

.. foliaspec:annotationtype_description(hyphenation)
This is a text-markup annotation form that indicates where in the original text a linebreak was inserted and a word was hyphenised.

Specification
---------------

.. foliaspec:specification(hyphenation)
:Annotation Category: :ref:`textmarkup_annotation_category`
:Declaration: ``<hyphenation-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Version History: Since v2.0
:**Element**: ``<t-hbr>``
:API Class: ``Hyphbreak``
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
                      * ``xlink:href`` -- Turns this element into a hyperlink to the specified URL
                      * ``xlink:type`` -- The type of link (you'll want to use ``simple`` in almost all cases).
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<br>`` (:ref:`linebreak_annotation`)
:Valid Context: 

:Extra Attributes: * ``newpage`` -- Can be set to ``yes`` to indicate that the break is not just a linebreak, but also a pagebreak (defaults to ``no``)
                   * ``pagenr`` -- The number of the page after the break
                   * ``linenr`` -- The number of the line after the break

Description & Examples
-------------------------

Hyphenation breaks are a text markup element that indicate where in the original text a word was broken up for
line-wrapping purposes.

The difference between ``t-hbr`` and ``br`` (:ref:`linebreak_annotation`) is that the hyphenised break is a softer
break, only there for page formatting purposes. The hyphen symbol is by definition implied in its usage, so should never
be explicitly incorporated in the text content. For most intents and purposes, a word with a hyphenised break can be
considered semantically identical to a word without one. The following example demonstrates hyphenation in the last
division, alongside the more classical linebreak:

.. literalinclude:: ../../examples/whitespace-linebreaks.2.0.0.folia.xml
    :linenos:
    :language: xml

