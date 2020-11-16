.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _event_annotation:

Event Annotation
==================================================================

.. foliaspec:annotationtype_description(event)
Structural annotation type representing events, often used in new media contexts for things such as tweets, chat messages and forum posts (as defined by a user-defined set definition). Note that a more linguistic kind of event annotation can be accomplished with `Entity Annotation` or even `Time Segmentation` rather than this one.

Specification
---------------

.. foliaspec:specification(event)
:Annotation Category: :ref:`structure_annotation_category`
:Declaration: ``<event-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: since v0.7
:**Element**: ``<event>``
:API Class: ``Event`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Event.html>`_)
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
:Accepted Data: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<div>`` (:ref:`division_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<external>`` (:ref:`external_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<gap>`` (:ref:`gap_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<ph>`` (:ref:`phon_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<str>`` (:ref:`string_annotation`), ``<table>`` (:ref:`table_annotation`), ``<t>`` (:ref:`text_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)
:Valid Context: ``<div>`` (:ref:`division_annotation`), ``<event>`` (:ref:`event_annotation`), ``<head>`` (:ref:`head_annotation`), ``<list>`` (:ref:`list_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<term>`` (:ref:`term_annotation`)
:Feature subsets (extra attributes): * ``actor``
                                   * ``begindatetime``
                                   * ``enddatetime``

Explanation
-------------------------

Event structure,  though uncommon to regular written text, can be useful in
certain documents. Divisions, paragraphs, sentences, or even words can be
encapsulated in an event element to indicate they somehow form an event entity
of a particular class. This kind of structure annotation is especially useful
in dealing with computer-mediated communication such as chat logs, tweets, and internet fora, in
which chat turns, forum posts, and tweets can be demarcated as particular
events.

The event class predefines some feature subsets you can use (you can use these as XML attributes, see :ref:`features`
for more information on features); the subsets ``begindatetime`` and ``enddatetime`` can be
used express to the exact moment at which an event started or ended. Note that
this differs from the common ``datetime`` attribute, which would describe
the time at which the annotation was recorded, rather than when the event took
place! The ``actor`` subset is used to associate the person responsible for the event, i.e. the speaker or poster.

For more fine-grained control over timed events, for example within sentences.
It is recommended to use :ref:`timesegment_annotation`!

Example
---------

The following example shows a chat log composed of message events:

.. literalinclude:: ../../examples/events.2.0.0.folia.xml
    :linenos:
    :language: xml


