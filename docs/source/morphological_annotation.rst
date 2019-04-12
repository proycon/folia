.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _morphological_annotation:

Morphological Annotation
==================================================================

.. foliaspec:annotationtype_description(morphological)
Morphological Annotation allows splitting a word/token into morphemes, morphemes itself may be nested. It is embedded within a layer ``morphology`` which can be embedded within word/tokens.

Specification
---------------

.. foliaspec:specification(morphological)
:Annotation Category: :ref:`subtoken_annotation_category`
:Declaration: ``<morphological-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: Heavily revised since v0.9
:**Element**: ``<morpheme>``
:API Class: ``Morpheme`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Morpheme>`_)
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
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
:Accepted Data: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<part>`` (:ref:`part_annotation`), ``<ph>`` (:ref:`phon_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<str>`` (:ref:`string_annotation`), ``<t>`` (:ref:`text_annotation`)
:Valid Context: ``<morpheme>`` (:ref:`morphological_annotation`), ``<morphology>`` (:ref:`morphological_annotation`)
:Feature subsets (extra attributes): * ``function``

Explanation
-------------------------

Tokens can be further segmented into morphemes, a form of structure annotation.
Morphemes behave much like ``<w>`` elements (tokens). Moreover, morphemes
can be referred to from within in span annotation using ``<wref>``, allowing
spans to be defined not only over whole words/tokens but also parts thereof.
The element for morphemes is ``<morpheme>``, and can only occur within
``<w>`` elements. Recall that ``<t>`` elements can contain references to
higher-level ``<t>`` elements. In such cases, the ``offset`` attribute
is used to designate the offset index in the word's associated text element
(``<t>``)` (zero being right at the start of the text). Morphemes may do
this.

Furthermore, a morpheme may take a class in a user-defined set, referring to its type.

Morphemes are grouped in a ``morphology`` layer, in turn embedded in a word, this is analogous to
:ref:`span_annotation_category`.

Consider the following example:

.. code-block:: xml

    <w xml:id="example.p.4.s.2.w.4">
        <t>leest</t>
        <lemma class="lezen" />
        <morphology>
            <morpheme class="stem" function="lexical">
                <t offset="0">lees</t>
            </morpheme>
            <morpheme class="suffix" function="inflexional">
                <t offset="4">t</t>
            </morpheme>
        </morphology>
    </w>

There is a predefined *feature subset* (see :ref:`features`) which you can use with morphemes, it is called ``function``
and denotes the function of the morpheme, the class it takes is defined by the particular set used.

Morphemes allow the same kinds of inline annotation just as words do. We can for instance bind lemma annotation to the
morpheme representing the word's stem rather than only to the entire word:

.. code-block:: xml

    <w xml:id="example.p.4.s.2.w.4">
        <t>leest</t>
        <lemma class="lezen" />
        <morphology>
            <morpheme xml:id="example.p.4.s.2.w.4.m.1" class="stem"
             function="lexical">
                <lemma class="lezen" />
                <t offset="0">lees</t>
            </morpheme>
            <morpheme xml:id="example.p.4.s.2.w.4.m.2" class="suffix"
             function="inflexional">
                <t offset="4">t</t>
            </morpheme>
        </morphology>
    </w>

Similarly, consider the Spanish word or phrase "Dámelo" (give it to me),
written as one entity. If this has not been split during tokenisation, but left
as a single token, you can annotate its morphemes, as all morphemes allow token
annotation to be placed within their scope:

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.1">
        <t>dámelo</t>
        <morphology>
            <morpheme class="stem">
                <t offset="0">dá</t>
                <lemma class="dar" />
                <pos class="v" />
            </morpheme>
            <morpheme class="suffix">
                <t offset="2">me</t>
                <lemma class="me" />
                <pos class="pron" />
            </morpheme>
            <morpheme class="suffix">
                <t offset="4">lo</t>
                <lemma class="lo" />
                <pos class="pron" />
            </morpheme>
        </morphology>
    </w>

Unlike words, but similar to :ref:`syntax_annotation`, morphemes may also be nested, as they can be expressed on multiple levels:

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.1">
        <t>comfortable</t>
        <morphology>
            <morpheme class="base">
                <t offset="0">comfort</t>
                <morpheme class="prefix">
                    <t offset="0">com</t>
                </morpheme>
                <morpheme class="morph">
                    <t offset="3">fort</t>
                </morpheme>
            </morpheme>
            <morpheme class="suffix">
                <t offset="7">able</t>
            </morpheme>
        </morphology>
    </w>


The next example will illustrate how morphemes can be referred to in span
annotation. Here we have a morpheme, and not the entire word, which forms a
named entity:

.. code-block:: xml

    <w xml:id="example.p.4.s.2.w.4">
        <t>CDA-voorzitter</t>
        <morphemes>
            <morpheme xml:id="example.p.4.s.2.w.1.m.1">
                <t offset="0">CDA</t>
            </morpheme>
        </morphemes>
        <entities>
            <entity xml:id="entity.1" class="organisation">
                <wref id="example.p.4.s.2.w.1.m.1" t="CDA" />
            </entity>
        </entities>
    </w>

The same approach can be followed for other kinds of span annotation. Note that
the span annotation layer (``<entities>`` in the example) may be embedded on
various levels. Most commonly on sentence level, but also on word level,
paragraph level or the global text level.

