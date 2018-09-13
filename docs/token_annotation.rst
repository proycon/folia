.. _token_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(token)
Token Annotation
==================================================================

.. foliaspec:annotationtype_description(token)
This annotation type introduces a tokenisation layer for the document. The terms **token** and **word** are used interchangeably in FoLiA as FoLiA itself does not commit to a specific tokenisation paradigm. Tokenisation is a prerequisite for the majority of linguistic annotation types offered by FoLiA and it is one of the most fundamental types of Structure Annotation. The words/tokens are typically embedded in other types of structure elements, such as sentences or paragraphs.

Specification
---------------

.. foliaspec:specification(token)
:Element Name (primary): ``<w>``
:Category: :ref:`structure_annotation_category`
:Declaration: ``<token-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data (as Annotation Types): :ref:`alignment_annotation`, :ref:`correction_annotation`, :ref:`metric_annotation`, :ref:`part_annotation`, :ref:`phon_annotation`, :ref:`string_annotation`, :ref:`text_annotation`
:Accepted Data (as FoLiA XML Elements): ``<alignment>``, ``<correction>``, ``<metric>``, ``<part>``, ``<ph>``, ``<str>``, ``<t>``
:Accepted Data (as API Classes): ``Alignment``, ``Correction``, ``Metric``, ``Part``, ``PhonContent``, ``String``, ``TextContent``
:Valid Context (as Annotation Types): :ref:`definition_annotation`, :ref:`event_annotation`, :ref:`example_annotation`, :ref:`note_annotation`, :ref:`paragraph_annotation`, :ref:`sentence_annotation`, :ref:`term_annotation`, :ref:`utterance_annotation`
:Valid Context (as FoLiA XML Elements): ``<def>``, ``<event>``, ``<ex>``, ``<note>``, ``<p>``, ``<s>``, ``<term>``, ``<utt>``
:Valid Context (as API Classes): ``Definition``, ``Event``, ``Example``, ``Note``, ``Paragraph``, ``Sentence``, ``Term``, ``Utterance``
:Version History: Since the beginning

:Extra Attributes: ``space`` -- Indicates whether a space should be inserted after this token (value ``yes``, default if not specified) or not (value ``no``).

Description & Examples
-------------------------

Tokenisation is a prerequisite for most forms of linguistic annotation. The ``<w>`` element is FoLiA's basic token or
word (hence the element's name). This element occurs in the scope of wider structural elements such as ``<s>``
(:ref:`sentence_annotation`)


.. literalinclude:: ../examples/snippets/token.folia.xml
    :linenos:
    :language: xml


