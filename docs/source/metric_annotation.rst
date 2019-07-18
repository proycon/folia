.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _metric_annotation:

Metric Annotation
==================================================================

.. foliaspec:annotationtype_description(metric)
Metric Annotation is a form of higher-order annotation that allows annotation of some kind of measurement. The type of measurement is defined by the class, which in turn is defined by the set as always. The metric element has a ``value`` attribute that stores the actual measurement, the value is often numeric but this needs not be the case.

Specification
---------------

.. foliaspec:specification(metric)
:Annotation Category: :ref:`higherorder_annotation_category`
:Declaration: ``<metric-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: since v0.9
:**Element**: ``<metric>``
:API Class: ``Metric`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Metric.html>`_)
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
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`)
:Valid Context: ``<chunk>`` (:ref:`chunking_annotation`), ``<coreferencechain>`` (:ref:`coreference_annotation`), ``<coreferencelink>`` (:ref:`coreference_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<current>`` (:ref:`correction_annotation`), ``<def>`` (:ref:`definition_annotation`), ``<dependency>`` (:ref:`dependency_annotation`), ``<div>`` (:ref:`division_annotation`), ``<domain>`` (:ref:`domain_annotation`), ``<entity>`` (:ref:`entity_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<errordetection>`` (:ref:`errordetection_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<gap>`` (:ref:`gap_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<lang>`` (:ref:`lang_annotation`), ``<lemma>`` (:ref:`lemma_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<new>`` (:ref:`correction_annotation`), ``<note>`` (:ref:`note_annotation`), ``<observation>`` (:ref:`observation_annotation`), ``<original>`` (:ref:`correction_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<pos>`` (:ref:`pos_annotation`), ``<predicate>`` (:ref:`predicate_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<semrole>`` (:ref:`semrole_annotation`), ``<sense>`` (:ref:`sense_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<sentiment>`` (:ref:`sentiment_annotation`), ``<spanrelation>`` (:ref:`spanrelation_annotation`), ``<statement>`` (:ref:`statement_annotation`), ``<str>`` (:ref:`string_annotation`), ``<subjectivity>`` (:ref:`subjectivity_annotation`), ``<suggestion>`` (:ref:`correction_annotation`), ``<su>`` (:ref:`syntax_annotation`), ``<table>`` (:ref:`table_annotation`), ``<term>`` (:ref:`term_annotation`), ``<timesegment>`` (:ref:`timesegment_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)
:Feature subsets (extra attributes): * ``value``

Explanation
-------------------------

The ``<metric>`` element allows annotation of some kind of measurement. The type of
measurement is defined by the *class*, which in turn is user-defined by the set as
always. The metric element has a ``value`` attribute
that stores the actual measurement, the value is often numeric but this needs
not be the case. It is a higher-level annotation element
that may be used with any kind of annotation.

An example of measurements associated with a word/token:

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.2">
        <t>boot</t>
        <metric class="charlength" value="4" />
        <metric class="frequency" value="0.00232" />
    </w>

An example of measurements associated with a span annotation element:

.. code-block:: xml

    <su class="np">
        <wref id="..." />
        <wref id="..." />
        <metric class="length" value="2" />
    </su>

The next example demonstrates a full FoLiA document with metric annotation on a Figure, but it may be more appropriate to
use :ref:`submetadata` for this instead:

.. literalinclude:: ../../examples/figure-metric.2.0.0.folia.xml
    :linenos:
    :language: xml
