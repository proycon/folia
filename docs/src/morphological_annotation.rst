.. _morphological_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(morphological)
XXX

.. foliaspec:annotationtype_description(morphological)
XXX

Specification
---------------

.. foliaspec:specification(morphological)
XXX

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

