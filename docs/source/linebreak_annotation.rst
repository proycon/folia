.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _linebreak_annotation:

Linebreak
==================================================================

.. foliaspec:annotationtype_description(linebreak)
Structure annotation representing a single linebreak and with special facilities to denote pagebreaks.

Specification
---------------

.. foliaspec:specification(linebreak)
:Annotation Category: :ref:`structure_annotation_category`
:Declaration: ``<linebreak-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: Since the beginning
:**Element**: ``<br>``
:API Class: ``Linebreak`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Linebreak.html>`_)
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numbers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
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
                      * ``tag`` -- Contains a space separated list of processing tags associated with the element. A processing tag carries arbitrary user-defined information that may aid in processing a document. It may carry cues on how a specific tool should treat a specific element. The tag vocabulary is specific to the tool that processes the document. Tags carry no instrinsic meaning for the data representation and should not be used except to inform/aid processors in their task. Processors are encouraged to clean up the tags they use. Ideally, published FoLiA documents at the end of a processing pipeline carry no further tags. For encoding actual data, use ``class`` and optionally features instead.
                      * ``xlink:href`` -- Turns this element into a hyperlink to the specified URL
                      * ``xlink:type`` -- The type of link (you'll want to use ``simple`` in almost all cases).
:Accepted Data: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<external>`` (:ref:`external_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<part>`` (:ref:`part_annotation`), ``<relation>`` (:ref:`relation_annotation`)
:Valid Context: ``<def>`` (:ref:`definition_annotation`), ``<div>`` (:ref:`division_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<head>`` (:ref:`head_annotation`), ``<t-hbr>`` (:ref:`hyphenation_annotation`), ``<list>`` (:ref:`list_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<table>`` (:ref:`table_annotation`), ``<term>`` (:ref:`term_annotation`), ``<t>`` (:ref:`text_annotation`), ``<t-correction>`` (:ref:`correction_annotation`), ``<t-error>`` (:ref:`errordetection_annotation`), ``<t-gap>`` (:ref:`gap_annotation`), ``<t-hspace>`` (:ref:`hspace_annotation`), ``<t-lang>`` (:ref:`lang_annotation`), ``<t-ref>`` (:ref:`reference_annotation`), ``<t-str>`` (:ref:`string_annotation`), ``<t-style>`` (:ref:`style_annotation`), ``<t-whitespace>`` (:ref:`whitespace_annotation`)

:Extra Attributes: * ``newpage`` -- Can be set to ``yes`` to indicate that the break is not just a linebreak, but also a pagebreak (defaults to ``no``)
                   * ``pagenr`` -- The number of the page after the break
                   * ``linenr`` -- The number of the line after the break

Description & Examples
-------------------------

Linebreaks play a double role, they are a structure element as well as a text markup element, the latter implies that you
may also use ``<br/>`` *within* the scope of text content, so within a ``<t>`` element.

The difference between ``br`` and ``whitespace`` is that the former specifies that only a linebreak was present, not
forcing any vertical whitespace between the lines, whilst the latter actually generates an empty space, which would
comparable to two successive ``br`` statements. Both elements can be used inside various structural elements, such as
divisions, paragraphs, headers, and sentences. Note that the example below also contains an example of
:ref:`hyphenation_annotation`, which is a special softer kind of linebreak.

.. literalinclude:: ../../examples/whitespace-linebreaks.2.5.0.folia.xml
    :linenos:
    :language: xml

You can use ``<br/>`` also in the context of :ref:`textmarkup_annotation_category`, as in the following example:

.. literalinclude:: ../../examples/style.2.0.0.folia.xml
    :linenos:
    :language: xml
