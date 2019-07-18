.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _part_annotation:

Part Annotation
==================================================================

.. foliaspec:annotationtype_description(part)
The structure element ``part`` is a fairly abstract structure element that should only be used when a more specific structure element is not available. Most notably, the part element should never be used for representation of morphemes or phonemes! Part can be used to divide a larger structure element, such as a division, or a paragraph into arbitrary subparts.

Specification
---------------

.. foliaspec:specification(part)
:Annotation Category: :ref:`structure_annotation_category`
:Declaration: ``<part-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: since v0.11.2
:**Element**: ``<part>``
:API Class: ``Part`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Part.html>`_)
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
                      * ``space`` -- This attribute indicates whether spacing should be inserted after this element (it's default value is always ``yes``, so it does not need to be specified in that case), but if tokens or other structural elements are glued together then the value should be set to ``no``. This allows for reconstruction of the detokenised original text.
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<part>`` (:ref:`part_annotation`), ``<ph>`` (:ref:`phon_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<t>`` (:ref:`text_annotation`)
:Valid Context: ``<def>`` (:ref:`definition_annotation`), ``<div>`` (:ref:`division_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<gap>`` (:ref:`gap_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<table>`` (:ref:`table_annotation`), ``<term>`` (:ref:`term_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)

Explanation
-------------------------

Part can be used to divide a larger structure element, such as a division, or a
paragraph into arbitrary subparts.

.. code-block:: xml

   <p>
     <part xml:id="p.1.part.1">
       <t>First part of the paragraph.</t>
     </part>
     <part xml:id="p.2.part.2">
       <t>Last part of the paragraph.</t>
     </part>
   </p>

The part element may seem alike to the division element, but divisions are typically used
for text blocks larger than a paragraph, typically correspondings to chapters,
sections or subsections and often carrying a ``<head>`` element. Do not use
parts for these structures!

The part element, on the other hand, is more abstract and plays a role on
a deeper level. It can be embedded within paragraphs, sentences, and most other
structure elements, even words, though we have to again emphasize **it should not
be used for morphology**, always use :ref:`morphological_annotation` for that!

Contact the FoLiA authors if you find yourself using part and you feel a
more specific FoLiA element is missing.
