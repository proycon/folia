.. _external_annotation:

External Annotation
===================================================================

.. foliaspec:annotationtype_description(external)
External annotation makes a reference to an external FoLiA document whose structure is inserted at the exact place the external element occurs.

Specification
---------------

.. foliaspec:specification(external)
:Annotation Category: :ref:`higherorder_annotation_category`
:Declaration: ``<external-annotation>`` *(note: there is never a set associated with this annotation type)
:Version History: Since v2.4.0
:**Element**: ``<external>``
:API Class: ``External`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.External.html>`_)
:Required Attributes: * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numbers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``tag`` -- Contains a space separated list of processing tags associated with the element. A processing tag carries arbitrary user-defined information that may aid in processing a document. It may carry cues on how a specific tool should treat a specific element. The tag vocabulary is specific to the tool that processes the document. Tags carry no instrinsic meaning for the data representation and should not be used except to inform/aid processors in their task. Processors are encouraged to clean up the tags they use. Ideally, published FoLiA documents at the end of a processing pipeline carry no further tags. For encoding actual data, use ``class`` and optionally features instead.
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`)
:Valid Context: ``<def>`` (:ref:`definition_annotation`), ``<div>`` (:ref:`division_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<table>`` (:ref:`table_annotation`), ``<term>`` (:ref:`term_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)


Explanation
-------------------------

This annotation type type is used to split a larger document into multiple smaller ones, and link from the parent
document to the external child documents. It is a type of higher-order annotation that is inserted at a certain place in the
parent structure. The parent document would be functionally equivalent if the structure of the external child documents were
inserted at the point the ``<external>`` element occurs.

The ``<external>`` element is valid in most structural elements. It is **not** a mechanism to create stand-off
annotation documents. Each external document must also be a valid FoLiA document in its own right.

The ``src`` attribute can refer to a local file path (relative or absolute) or a remote URL.

Example
-------------------------

.. literalinclude:: ../../examples/external.2.4.0.folia.xml
    :linenos:
    :language: xml

