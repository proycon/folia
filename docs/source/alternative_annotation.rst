.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _alternative_annotation:

Alternative Annotation
==================================================================

.. foliaspec:annotationtype_description(alternative)
This form of higher-order annotation encapsulates alternative annotations, i.e. annotations that are posed as an alternative option rather than the authoratitive chosen annotation

Specification
---------------

.. foliaspec:specification(alternative)
:Annotation Category: :ref:`higherorder_annotation_category`
:Declaration: ``<alternative-annotation>`` *(note: there is no set associated with this annotation type)
:Version History: Since the beginning, may carry set and classes since v2.0
:**Element**: ``<alt>``
:API Class: ``Alternative``
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
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
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<morphology>`` (:ref:`morphological_annotation`), ``<phonology>`` (:ref:`phonological_annotation`)
:Valid Context: ``<def>`` (:ref:`definition_annotation`), ``<div>`` (:ref:`division_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<table>`` (:ref:`table_annotation`), ``<term>`` (:ref:`term_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)

.. foliaspec:specification_element(AlternativeLayers)
:**Element**: ``<altlayers>``
:API Class: ``AlternativeLayers``
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
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
:Valid Context: ``<def>`` (:ref:`definition_annotation`), ``<div>`` (:ref:`division_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<table>`` (:ref:`table_annotation`), ``<term>`` (:ref:`term_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)

Introduction
-------------------------

The FoLiA format does not just allow for a single authoritative annotation per token; it allows the representation of
*alternative* annotations. There is a specific form for :ref:`inline_annotation_category` and a form for :ref:`span_annotation_category`;
both share the same declaration ``<alternative-annotation>`` with which a set may be associated.

Alternative Inline Annotation
---------------------------------

Alternative inline annotations are grouped within one or more ``<alt>``
elements. If multiple annotations are grouped together under the same
``<alt>`` element, then they are deemed *dependent* and form a single
set of alternatives.

Each alternative preferably is given a unique identifier. In the following example we see the Dutch word "bank" in the
sense of a sofa, alternatively we see two alternative annotations with a different sense and domain.

.. DISCARDING THIS in v2 (issue #56)
.. Any annotation
.. element *within* an ``<alt>`` block by definition needs to be marked as non-authoritative by setting the mandatory
.. attribute ``auth="no"``. This facilitates the job of parsers and queriers.

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.1">
        <t>bank</t>
        <domain class="furniture" />
        <sense class="r_n-5918" confidence="1.0">
          <desc>furniture</desc>
        </sense>
        <alt xml:id="example.p.1.s.1.w.1.alt.1">
            <domain class="finance" />
            <sense class="r_n-5919" confidence="0.6">
                <desc>financial institution</desc>
            </sense>
        </alt>
        <alt xml:id="example.p.1.s.1.w.1.alt.2">
            <domain class="geology" />
            <sense class="r_n-5920" confidence="0.1">
                <desc>river bank</desc>
            </sense>
        </alt>
    </w>

Sometimes, an alternative is concerned only with a portion of the annotations.
By default, annotations not mentioned are applicable to the alternative as
well, unless the alternative is set as being *exclusive*. Consider the
following expanded example in which we added a part-of-speech tag and a lemma.

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.1">
        <t>bank</t>
        <domain class="furniture" />
        <sense class="r_n-5918" confidence="1.0">
          <desc>furniture</desc>
        </sense>
        <pos class="n" />
        <lemma class="bank" />
        <alt xml:id="example.p.1.s.1.w.1.alt.1">
            <domain class="finance" />
            <sense class="r_n-5919" confidence="0.6">
                <desc>financial institution</desc>
            </sense>
        </alt>
        <alt xml:id="example.p.1.s.1.w.1.alt.2">
            <domain class="geology" />
            <sense class="r_n-5920" confidence="0.1">
                <desc>river bank</desc>
            </sense>
        </alt>
        <alt xml:id="example.p.1.s.1.w.1.alt.2" exclusive="yes">
            <t>bank</t>
            <domain class="navigation" />
            <sense class="r_n-1234">
                <desc>to turn</desc>
            </sense>
            <pos class="v" />
            <lemma class="bank" />
        </alt>
    </w>

The first two alternatives are inclusive, which is the default. This means that
the pos tag ``n`` and the lemma ``bank`` apply to them as well. The last
alternative is set as exclusive, using the ``exclusive`` attribute. It has
been given a different pos tag and the lemma and even the text content has
necessarily been repeated even though it is equal to the higher-level annotation,
otherwise there would be no lemma nor text associated with the exclusive
alternative.

.. TODO: is exclusive implemented?
.. RESPONSE: It is now

.. TODO: look at auth="no" usage
.. RESPONSE: I'm discarding auth="no" from FoLiA v2.0 and making it an internal property only, no longer expressed (issue #56)

Alternatives can be used as a great way of postponing actual annotation, due to
their non-authoritative nature. When used in this way, they can be regarded as
*options*. They can be used even when there are no authoritative annotations
of the type.  Consider the following example in which domain and sense
annotations are presented as alternatives and there is no authoritative
annotation of these types whatsoever:

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.1">
        <t>bank</t>
        <alt xml:id="example.p.1.s.1.w.1.alt.1">
            <domain class="finance" />
            <sense class="r_n-5919" confidence="0.6">
                <desc>financial institution</desc>
            </sense>
        </alt>
        <alt xml:id="example.p.1.s.1.w.1.alt.2">
            <domain class="geology" />
            <sense class="r_n-5920" confidence="0.1">
                <desc>river bank</desc>
            </sense>
        </alt>
    </w>

Alternative Span Annotation
---------------------------------

With inline annotations one can specify an unbounded number of alternative
annotations. This functionality is available for :ref:`span_annotation_category` as well, but
due to the different nature of span annotations this happens in a slightly
different way.

Where we used ``<alt>`` for token annotations, we now use ``<altlayers>``
for span annotations. Under this element several alternative layers can be
presented. Analogous to ``<alt>``, any layers grouped together are assumed
to be somehow dependent. Multiple ``<altlayers>`` can be added to introduce
independent alternatives. Each alternative may be associated with a unique
identifier.

Below is an example of a sentence that is chunked in two ways:

.. code-block:: xml

    <s xml:id="example.p.1.s.1">
      <t>The Dalai Lama greeted him.</t>
      <w xml:id="example.p.1.s.1.w.1"><t>The</t></w>
      <w xml:id="example.p.1.s.1.w.2"><t>Dalai</t></w>
      <w xml:id="example.p.1.s.1.w.3"><t>Lama</t></w>
      <w xml:id="example.p.1.s.1.w.4"><t>greeted</t></w>
      <w xml:id="example.p.1.s.1.w.5"><t>him</t></w>
      <w xml:id="example.p.1.s.1.w.6"><t>.</t></w>
      <chunking>
        <chunk xml:id="example.p.1.s.1.chunk.1">
            <wref id="example.p.1.s.1.w.1" t="The" />
            <wref id="example.p.1.s.1.w.2" t="Dalai" />
            <wref id="example.p.1.s.1.w.3" t="Lama" />
        </chunk>
        <chunk xml:id="example.p.1.s.1.chunk.2">
            <wref id="example.p.1.s.1.w.4" t="greeted" />
        </chunk>
        <chunk xml:id="example.p.1.s.1.chunk.3">
            <wref id="example.p.1.s.1.w.5" t="him" />
            <wref id="example.p.1.s.1.w.6" t="." />
        </chunk>
      </chunking>
      <altlayers xml:id="example.p.1.s.1.alt.1">
           <chunking>
            <chunk xml:id="example.p.1.s.1.alt.1.chunk.1" confidence="0.001">
                <wref id="example.p.1.s.1.w.1" t="The" />
                <wref id="example.p.1.s.1.w.2" t="Dalai" />
            </chunk>
            <chunk xml:id="example.p.1.s.1.alt.1.chunk.2" confidence="0.001">
                <wref id="example.p.1.s.1.w.2" t="Lama" />
                <wref id="example.p.1.s.1.w.4" t="greeted" />
            </chunk>
            <chunk xml:id="example.p.1.s.1.alt.1.chunk.3" confidence="0.001">
                <wref id="example.p.1.s.1.w.5" t="him" />
                <wref id="example.p.1.s.1.w.6" t="." />
            </chunk>
          </chunking>
      </altlayers>
    </s>

The support for alternatives and the fact that multiple layers (including those
of different types) cannot be nested in a single inline structure, should make
clear why FoLiA uses a stand-off notation alongside an inline notation.


