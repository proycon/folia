.. _pos_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(pos)
Part-of-Speech Annotation
==================================================================

.. foliaspec:annotationtype_description(pos)
Part-of-Speech Annotation, one of the most common types of linguistic annotation. Assigns a lexical class to words.

Specification
---------------

.. foliaspec:specification(pos)
:Annotation Category: :ref:`inline_annotation_category`
:Declaration: ``<pos-annotation set="...">``
:Version History: Since the beginning
:**Element**: ``<pos>``
:API Class: ``PosAnnotation``
:Required Attributes: * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
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
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<metric>`` (:ref:`metric_annotation`)
:Valid Context: 
:Feature subsets (extra attributes): * ``head``

Explanation & Examples
-------------------------

Part-of-Speech annotation allows the annotation of lexical categories using the
``pos`` element. The following example shows a simple part-of-speech annotation. In this example , we declare PoS annotation to use the
tagset from the brown corpus (although we do not have an actual set definition for it).

.. literalinclude:: ../../examples/pos.2.0.0.folia.xml
    :linenos:
    :language: xml

Lexical annotation can take more complex forms than assignment of a single part-of-speech tag. There may for example be
numerous features associated with the part-of-speech tag, such as gender, number, case, tense, mood, etc... FoLiA
introduces a special paradigm for dealing with such features. This is described in :ref:`features`, please ensure you
are familiar with this before reading the remainder of this section.

Two scenarios can be envisioned, one in
which the class of the ``pos`` element encodes all features, and one in
which it is the foundation upon which is expanded. Which one is used is
entirely up to the defined set.

Option one:

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.2">
        <t>boot</t>
        <pos head="N" class="N(singular)">
            <feat subset="number" class="singular" />
            <feat subset="gender" class="none" />
            <feat subset="case" class="none" />
        </pos>
    </w>

In FoLiA, this attribute ``head`` is a *predefined subset* for PoS-annotation, i.e. the subset is commonly used and has
clear semantics; however, it still needs to be defined in the set definition. We can use such *predefined subsets* as
XML attributes.

Option two:

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.2">
        <t>boot</t>
        <pos class="N">
            <feat subset="number" class="singular" />
            <feat subset="gender" class="none" />
            <feat subset="case" class="none" />
        </pos>
    </w>

The last examples demonstrates a full FoLiA document with part-of-speech tagging with features:

.. literalinclude:: ../../examples/pos-features-deep.2.0.0.folia.xml
    :linenos:
    :language: xml


