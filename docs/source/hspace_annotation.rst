.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _hspace_annotation:

Horizontal Whitespace
==================================================================

.. foliaspec:annotationtype_description(hspace)
Markup annotation introducing horizontal whitespace

.. note::

    Do not confuse this with the ``<whitespace>`` structure element and ``<t-whitespace>`` markup element that are used for *vertical* whitespace, see
    :ref:`whitespace_annotation`.

Specification
---------------

.. foliaspec:specification(hspace)
:Annotation Category: :ref:`textmarkup_annotation_category`
:Declaration: ``<hspace-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: Since the v2.5.0
:**Element**: ``<t-hspace>``
:API Class: ``TextMarkupHSpace`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.TextMarkupHSpace.html>`_)
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
                      * ``xlink:href`` -- Turns this element into a hyperlink to the specified URL
                      * ``xlink:type`` -- The type of link (you'll want to use ``simple`` in almost all cases).
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<br>`` (:ref:`linebreak_annotation`)
:Valid Context: 

Description & Examples
-------------------------

If normal spacing is not enough and you need to express **horizontal** whitespace explicitly, then you can use the
``<t-hspace>`` element.

.. code-block:: xml

   <t>To be<t-hspace class="long" />or not to be</t>

The vocabulary is defined by your set definition and you can assign your own size-interpretation. Tools that are not
aware of your vocabulary should simply render a single space.

An alternative to ``t-hspace`` is to use the ``xml:space="preserve"`` attribute as described in
:ref:`preserving_whitespace`, but the use of ``<t-hspace>`` is preferred.

The last section in this example shows horizontal whitespace:

.. literalinclude:: ../../examples/whitespace-linebreaks.2.5.0.folia.xml
    :linenos:
    :language: xml
