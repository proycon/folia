.. _span_annotation_category:

.. foliaspec:category_title(span)
Span Annotation
===================================================================

.. foliaspec:category_description(span)
This category encompasses (linguistic) annotation types that span one or more structural elements. Examples are (Named) Entities or Multi-word Expressions, Dependency Relations, and many others. FoLiA implements these as a stand-off layer that refers back to the structural elements (often words/tokens).

Span annotation elements are always embedded in a **layer** element, this is an element that groups span annotations of
a particular annotation type and set together. Each annotation type has its own layer element and the layer elements
themselves are embedded, inline, in a structural element. So, say you want to do named entity annotation (a form of span
annotation) over words, then *after* you defined the words, you can embed a layer (``<entities>``) containing the span
annotation elements (``<entity>`` in this example), which refer back to the words. Such a reference back is done with the ``wref``
element.

Consider the following example:

.. code-block:: xml

    <s xml:id="example.p.1.s.1">
      <t>The Dalai Lama greeted him.</t>
      <w xml:id="example.p.1.s.1.w.1"><t>The</t></w>
      <w xml:id="example.p.1.s.1.w.2"><t>Dalai</t></w>
      <w xml:id="example.p.1.s.1.w.3"><t>Lama</t></w>
      <w xml:id="example.p.1.s.1.w.4"><t>greeted</t></w>
      <w xml:id="example.p.1.s.1.w.5"><t>him</t></w>
      <w xml:id="example.p.1.s.1.w.6"><t>.</t></w>
      <entities>
        <entity xml:id="example.p.1.s.1.entity.1" class="per">
            <wref id="example.p.1.s.1.w.2" t="Dalai" />
            <wref id="example.p.1.s.1.w.3" t="Lama" />
        </entity>
      </entities>
    </s>

The next sentence may in turn have an ``<entities>`` layer as well. The design principle behind this is to keep
information, even when it concerns span annotations, as local as possible rather than spread out of the document. This
facilitates the job for streaming parsers and humans looking at the raw XML. Nevertheless, this is a convention which
most FoLiA libraries adhere to, but is not a strict requirement. So it is still possible and valid to place your layer at
any higher structural level, as long as all the elements you refer to are within its scope and all defined prior to the
layer itself.

.. note::

    As you might have seen, the ``wref`` element may carry a ``t`` attribute with the text of word/structure it refers to. This
    redundancy is merely to provide extra clarity to the person inspecting the XML and is not mandatory.

.. note::

    The ``wref`` elements refers to words/tokens or sub-token annotations such as morphemes and phonemes. We do not use it
    to refer to higher-level structural elements!

.. note::

    The order of the references should always correspond to the order of the tokens in the text. However, the references need
    not be strictly continuous; there may be gaps.

Depending on the type of span annotation, it is possible that the element may be nested. This is for example the case
for :ref:`syntax_annotation`, where the nesting of syntactic units allows the building of syntax trees. Span annotation
elements of a more complex nature may require or allow so-called **span role** elements. Span roles encapsulate
references to the words and ascribe a more defined meaning to the span, for instance to mark the head or dependent in a
dependency relation. Span role elements themselves never carry any classes and can only be used in the scope of a
certain span annotation element, not standalone. They can still carry :ref:`features`, though.

Annotation Types
-------------------

.. foliaspec:toc(span)
XXX
