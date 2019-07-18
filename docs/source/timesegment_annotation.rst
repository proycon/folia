.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _timesegment_annotation:

Time Segmentation
==================================================================

.. foliaspec:annotationtype_description(timesegment)
FoLiA supports time segmentation to allow for more fine-grained control of timing information by associating spans of words/tokens with exact timestamps. It can provide a more linguistic alternative to `Event Annotation`.

Specification
---------------

.. foliaspec:specification(timesegment)
:Annotation Category: :ref:`span_annotation_category`
:Declaration: ``<timesegment-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: Since v0.8 but renamed since v0.9
:**Element**: ``<timesegment>``
:API Class: ``TimeSegment`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.TimeSegment.html>`_)
:Layer Element: ``<timing>``
:Span Role Elements: 
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
:Valid Context: ``<timing>`` (:ref:`timesegment_annotation`)
:Feature subsets (extra attributes): * ``actor``
                                   * ``begindatetime``
                                   * ``enddatetime``

Explanation
-------------------------

FoLiA supports time segmentation using the ``<timing>`` layer and the
``<timesegment>`` span annotation element. This element is useful for
speech, but can also be used for event annotation. We already saw events as
structure annotation in :ref:`event_annotation`, but for more fine-grained
control of timing information a span annotation element in an offset layer is
more suited.

Time segments may also be nested. The predefined and optional
feature subset ``begindatetime`` and ``enddatetime`` can be used express
the exact moment at which an event started or ended. These too are set-defined
so the format shown here is just an example.

If you are only interested in a structural annotation of events, and a coarser level of
annotation suffices, then use :ref̋:`event_annotation`.

If used in a **speech context**, all the generic speech attributes become available
(See :ref:`speech`). This introduces ``begintime`` and
``endtime``, which are different from the ``begindatetime`` and
``enddatetime`` feature subsets introduced by this annotation type! The generic attributes ``begintime`` and
``endtime`` are not defined by a set, but specify a time location in
``HH:MM:SS.MMM`` format which may refer to the location in an associated audio
file. Audio files are associated using the ``src`` attribute, which is
inherited by all lower elements, so we put it on the sentence here.

.. seealso::

    * :ref:`event_annotation`
    * :ref:`speech`

Example
-------------------------

The following example illustrates the usage of time segmentation for event annotation:

.. literalinclude:: ../../examples/timesegments-events.2.0.0.folia.xml
    :linenos:
    :language: xml

Example in a speech context
------------------------------

The following example illustrates the usage of time segmentation in a speech context. You have to be aware though, that
the ``begintime`` and ``endtime`` attributes can also be directly associated with any structure elements in a speech
context, making the use of this annotation type unnecessary or redundant if used this way.

.. literalinclude:: ../../examples/timesegments-speech.2.0.0.folia.xml
    :linenos:
    :language: xml


