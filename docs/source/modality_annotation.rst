.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _modality_annotation:

Modality Annotation
==================================================================

.. foliaspec:annotationtype_description(modality)
Modality is usually defined as the expression of the speaker's opinion and of his attitude towards what he is saying (Palmer,  1986). This annotation type is used for the annotation of sentiments, certainty, negation and  truthfulness. The modalities are defined by a user-defined set definition.

.. note::

   This annotation type has overlap with sentiment annotation (:ref:`_sentiment_annotation`). Modality annotation is now
   preferred over sentiment annotation, as it is more generic.

Specification
---------------

.. foliaspec:specification(modality)
:Annotation Category: :ref:`span_annotation_category`
:Declaration: ``<modality-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: since v2.4.0
:**Element**: ``<modality>``
:API Class: ``modality`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.modality.html>`_)
:Layer Element: ``<modalities>``
:Span Role Elements: ``<hd>`` (``Headspan``), ``<source>`` (``Source``), ``<target>`` (``Target``)
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
                      * ``textclass`` -- Refers to the text class this annotation is based on. This is an advanced attribute, if not specified, it defaults to ``current``. See :ref:`textclass_attribute`.
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<relation>`` (:ref:`relation_annotation`)
:Valid Context: ``<modalities>`` (:ref:`modality_annotation`)
:Feature subsets (extra attributes): * ``polarity``
                                     * ``strength``

Explanation
-------------------------

.. note::

    Please first ensure you are familiar with the general principles of :ref:`span_annotation_category` to make sense of this annotation type.

Modality analysis marks things such as sentiments, truthfulness, negation, doubt. The ``<modality>`` span annotation element is used to
this end. It is embedded in a ``<modalities>`` layer.

The ``<modalities>`` element takes the following span roles:

* ``<cue>`` -- (required) -- The cue or trigger of the modality. In case of sentiments, this expresses the actual sentiment and could cover word spans such as "happy", "very satisfied", "highly dissappointed". This may also be nested inside ``<scope>``.
* ``<scope>`` -- (optional) -- The scope of the modality. In case of negation for example, this covers the text that is negated.
* ``<source>`` -- (optional) -- The source/holder of the modality, assuming it is explicitly expressed in the text. This may also be nested inside ``<scope>``.
* ``<target>`` -- (optional) -- The target/recipient of the modality, assuming it is explicitly expressed in the text. This may also be nested inside ``<scope>``.

The following feature subsets are predefined (see :ref:`features`), whether they are actually used depends on the set, their values (classes) are set-dependent as well:

* ``polarity`` -- Expresses the whether the sentiment is positive, neutral or negative.
* ``strength`` -- Expresses the strength or intensity of the sentiment.

Besides these predefined features, FoLiA's feature mechanism can be used to associate other custom properties with any sentiment.

Example
-------------------------

.. literalinclude:: ../../examples/modality-sentiments.2.4.0.folia.xml
    :linenos:
    :language: xml


