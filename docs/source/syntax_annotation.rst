.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _syntax_annotation:

Syntactic Annotation
==================================================================

.. foliaspec:annotationtype_description(syntax)
Assign grammatical categories to spans of words. Syntactic units are nestable and allow representation of complete syntax trees that are usually the result of consistuency parsing.

Specification
---------------

.. foliaspec:specification(syntax)
:Annotation Category: :ref:`span_annotation_category`
:Declaration: ``<syntax-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Version History: Since the beginning
:**Element**: ``<su>``
:API Class: ``SyntacticUnit``
:Layer Element: syntax
:Span Role Elements: 
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
                      * ``textclass`` -- Refers to the text class this annotation is based on. This is an advanced attribute, if not specified, it defaults to ``current``. See :ref:`textclass_attribute`.
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<su>`` (:ref:`syntax_annotation`)
:Valid Context: ``<su>`` (:ref:`syntax_annotation`), ``<syntax>`` (:ref:`syntax_annotation`)

Explanation
-------------------------

.. note::

    Please first ensure you are familiar with the general principles of :ref:`span_annotation_category` to make sense of this annotation type.

Syntax annotation allows representation of a syntax tree, commonly the result of *constituency parsing*. This is a
nested form of span annotation, in which nodes in the tree are represented by ``<su>`` (syntactic unit) elements. Each
syntactic unit may carry a class in a user-defined set, determining the vocabulary of the syntax annotation.

It is recommended for each syntactic unit to have a unique identifier.

.. seealso::

    For dependency parsing, see :ref:`dependency_annotation` instead.

Example
-------------------------

.. literalinclude:: ../../examples/syntax.2.0.0.folia.xml
    :linenos:
    :language: xml


