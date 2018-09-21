.. _alternative_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(alternative)
XXX

.. foliaspec:annotationtype_description(alternative)
XXX

Specification
---------------

.. foliaspec:specification(alternative)
XXX

.. foliaspec:specification_element(altlayers)
XXX

Introduction
-------------------------

The FoLiA format does not just allow for a single authoritative annotation per token; it allows the representation of
*alternative* annotations. There is a specific form for :ref:`inline_annotation` and a form for :ref:`span_annotation`;
both share the same declaration ``<alternative-annotation>`` with which a set may be associated.

Alternative Inline Annotation
---------------------------------

Alternative inline annotations are grouped within one or more ``<alt>``
elements. If multiple annotations are grouped together under the same
``<alt>`` element, then they are deemed *dependent* and form a single
set of alternatives.

Each alternative preferably is given a unique identifier. In the following example we see the Dutch word "bank" in the
sense of a sofa, alternatively we see two alternative annotations with a different sense and domain. Any annotation
element *within* an ``<alt>`` block by definition needs to be marked as non-authoritative by setting the mandatory
attribute ``auth="no"``. This facilitates the job of parsers and queriers.

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.1">
        <t>bank</t>
        <domain class="furniture" />
        <sense class="r_n-5918" confidence="1.0">
          <desc>furniture</desc>
        </sense>
        <alt xml:id="example.p.1.s.1.w.1.alt.1">
            <domain auth="no" class="finance" />
            <sense auth="no" class="r_n-5919" confidence="0.6">
                <desc>financial institution</desc>
            </sense>
        </alt>
        <alt xml:id="example.p.1.s.1.w.1.alt.2">
            <domain auth="no" class="geology" />
            <sense auth="no" class="r_n-5920" confidence="0.1">
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
            <domain auth="no" class="finance" />
            <sense auth="no" class="r_n-5919" confidence="0.6">
                <desc>financial institutioni</desc>
            </sense>
        </alt>
        <alt xml:id="example.p.1.s.1.w.1.alt.2">
            <domain auth="no" class="geology" />
            <sense auth="no" class="r_n-5920" confidence="0.1">
                <desc>river bank</desc>
            </sense>
        </alt>
        <alt xml:id="example.p.1.s.1.w.1.alt.2" exclusive="yes">
            <t>bank</t>
            <domain auth="no" class="navigation" />
            <sense auth="no" class="r_n-1234">
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
.. TODO: look at auth="no" usage

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
            <domain auth="no" class="finance" />
            <sense auth="no" class="r_n-5919" confidence="0.6">
                <desc>financial institution</desc>
            </sense>
        </alt>
        <alt xml:id="example.p.1.s.1.w.1.alt.2">
            <domain auth="no" class="geology" />
            <sense auth="no" class="r_n-5920" confidence="0.1">
                <desc>river bank</desc>
            </sense>
        </alt>
    </w>

Alternative Span Annotation
---------------------------------

With inline annotations one can specify an unbounded number of alternative
annotations. This functionality is available for :ref:`span_annotation` as well, but
due to the different nature of span annotations this happens in a slightly
different way.

Where we used ``<alt>`` for token annotations, we now use ``<altlayers>``
for span annotations. Under this element several alternative layers can be
presented. Analogous to ``<alt>``, any layers grouped together are assumed
to be somehow dependent. Multiple ``<altlayers>`` can be added to introduce
independent alternatives. Each alternative may be associated with a unique
identifier. The layers within ``<altlayers>`` need to be marked as
non-autoritative using ``auth="no"`` to facilitate the job for parsers.

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
           <chunking auth="no">
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


