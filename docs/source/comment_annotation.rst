.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _comment_annotation:

Comment Annotation
==================================================================

.. foliaspec:annotationtype_description(comment)
This is a form of higher-order annotation that allows you to associate comments with almost all other annotation elements

Specification
---------------

.. foliaspec:specification(comment)
:Annotation Category: :ref:`higherorder_annotation_category`
:Declaration: ``<comment-annotation>`` *(note: there is never a set associated with this annotation type)
:Version History: Since v1.3
:**Element**: ``<comment>``
:API Class: ``Comment`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Comment.html>`_)
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numbers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``tag`` -- Contains a space separated list of processing tags associated with the element. A processing tag carries arbitrary user-defined information that may aid in processing a document. It may carry cues on how a specific tool should treat a specific element. The tag vocabulary is specific to the tool that processes the document. Tags carry no instrinsic meaning for the data representation and should not be used except to inform/aid processors in their task. Processors are encouraged to clean up the tags they use. Ideally, published FoLiA documents at the end of a processing pipeline carry no further tags. For encoding actual data, use ``class`` and optionally features instead.
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`)
:Valid Context: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<chunk>`` (:ref:`chunking_annotation`), ``<chunking>`` (:ref:`chunking_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<content>`` (:ref:`rawcontent_annotation`), ``<coreferencechain>`` (:ref:`coreference_annotation`), ``<coreferences>`` (:ref:`coreference_annotation`), ``<coreferencelink>`` (:ref:`coreference_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<current>`` (:ref:`correction_annotation`), ``<def>`` (:ref:`definition_annotation`), ``<dependencies>`` (:ref:`dependency_annotation`), ``<dependency>`` (:ref:`dependency_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<div>`` (:ref:`division_annotation`), ``<domain>`` (:ref:`domain_annotation`), ``<entities>`` (:ref:`entity_annotation`), ``<entity>`` (:ref:`entity_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<errordetection>`` (:ref:`errordetection_annotation`), ``<etymology>`` (:ref:`etymology_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<external>`` (:ref:`external_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<gap>`` (:ref:`gap_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<t-hbr>`` (:ref:`hyphenation_annotation`), ``<lang>`` (:ref:`lang_annotation`), ``<lemma>`` (:ref:`lemma_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<modalities>`` (:ref:`modality_annotation`), ``<modality>`` (:ref:`modality_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<morphology>`` (:ref:`morphological_annotation`), ``<new>`` (:ref:`correction_annotation`), ``<note>`` (:ref:`note_annotation`), ``<observation>`` (:ref:`observation_annotation`), ``<observations>`` (:ref:`observation_annotation`), ``<original>`` (:ref:`correction_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<ph>`` (:ref:`phon_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<phonology>`` (:ref:`phonological_annotation`), ``<pos>`` (:ref:`pos_annotation`), ``<predicate>`` (:ref:`predicate_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<semrole>`` (:ref:`semrole_annotation`), ``<semroles>`` (:ref:`semrole_annotation`), ``<sense>`` (:ref:`sense_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<sentiment>`` (:ref:`sentiment_annotation`), ``<sentiments>`` (:ref:`sentiment_annotation`), ``<spanrelation>`` (:ref:`spanrelation_annotation`), ``<spanrelations>`` (:ref:`spanrelation_annotation`), ``<statement>`` (:ref:`statement_annotation`), ``<statements>`` (:ref:`statement_annotation`), ``<str>`` (:ref:`string_annotation`), ``<subjectivity>`` (:ref:`subjectivity_annotation`), ``<suggestion>`` (:ref:`correction_annotation`), ``<su>`` (:ref:`syntax_annotation`), ``<syntax>`` (:ref:`syntax_annotation`), ``<table>`` (:ref:`table_annotation`), ``<term>`` (:ref:`term_annotation`), ``<t>`` (:ref:`text_annotation`), ``<t-correction>`` (:ref:`correction_annotation`), ``<t-error>`` (:ref:`errordetection_annotation`), ``<t-gap>`` (:ref:`gap_annotation`), ``<t-hspace>`` (:ref:`hspace_annotation`), ``<t-lang>`` (:ref:`lang_annotation`), ``<t-ref>`` (:ref:`reference_annotation`), ``<t-str>`` (:ref:`string_annotation`), ``<t-style>`` (:ref:`style_annotation`), ``<t-whitespace>`` (:ref:`whitespace_annotation`), ``<timesegment>`` (:ref:`timesegment_annotation`), ``<timing>`` (:ref:`timesegment_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)

Explanation
-------------------------

Comments is a simple higher-order annotation element that may be used with any
annotation. It holds text that comments the annotation. Multiple comments are
allowed per annotation.

An alternative to these FoLiA-specific comments, which are considered actual
annotations, is standard XML comments. Standard XML comments, however, are not
considered actual annotations and most likely won't be interpreted by any
tools.

Example
-------------------------

Consider the following example in the context of :ref:`sense_annotation`.

.. literalinclude:: ../../examples/sense.2.0.0.folia.xml
    :linenos:
    :language: xml


