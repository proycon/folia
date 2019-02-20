
.. _span_annotation_category:

Span Annotation
===================================================================

.. foliaspec:category_description(span)
This category encompasses (linguistic) annotation types that span one or more structural elements. Examples are (Named) Entities or Multi-word Expressions, Dependency Relations, and many others. FoLiA implements these as a stand-off layer that refers back to the structural elements (often words/tokens). The layer itself is embedded in a structural level of a wider scope (such as a sentence).

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

FoLiA defines the following types of span annotation:

.. foliaspec:toc(span)
* :ref:`span_annotation_category` -- This category encompasses (linguistic) annotation types that span one or more structural elements. Examples are (Named) Entities or Multi-word Expressions, Dependency Relations, and many others. FoLiA implements these as a stand-off layer that refers back to the structural elements (often words/tokens). The layer itself is embedded in a structural level of a wider scope (such as a sentence).
   - :ref:`syntax_annotation` -- ``<su>`` -- Assign grammatical categories to spans of words. Syntactic units are nestable and allow representation of complete syntax trees that are usually the result of consistuency parsing.
   - :ref:`chunking_annotation` -- ``<chunk>`` -- Assigns shallow grammatical categories to spans of words. Unlike syntax annotation, chunks are not nestable. They are often produced by a process called Shallow Parsing, or alternatively, chunking.
   - :ref:`entity_annotation` -- ``<entity>`` -- Entity annotation is a broad and common category in FoLiA. It is used for specifying all kinds of multi-word expressions, including but not limited to named entities. The set definition used determines the vocabulary and therefore the precise nature of the entity annotation.
   - :ref:`dependency_annotation` -- ``<dependency>`` -- Dependency relations are syntactic relations between spans of tokens. A dependency relation takes a particular class and consists of a single head component and a single dependent component.
   - :ref:`timesegment_annotation` -- ``<timesegment>`` -- FoLiA supports time segmentation to allow for more fine-grained control of timing information by associating spans of words/tokens with exact timestamps. It can provide a more linguistic alternative to `Event Annotation`.
   - :ref:`coreference_annotation` -- ``<coreferencechain>`` -- Relations between words that refer to the same referent (anaphora) are expressed in FoLiA using Coreference Annotation. The co-reference relations are expressed by specifying the entire chain in which all links are coreferent.
   - :ref:`semrole_annotation` -- ``<semrole>`` -- This span annotation type allows for the expression of semantic roles, or thematic roles. It is often used together with `Predicate Annotation`
   - :ref:`predicate_annotation` -- ``<predicate>`` -- Allows annotation of predicates, this annotation type is usually used together with Semantic Role Annotation. The types of predicates are defined by a user-defined set definition.
   - :ref:`observation_annotation` -- ``<observation>`` -- Observation annotation is used to make an observation pertaining to one or more word tokens.  Observations offer a an external qualification on part of a text. The qualification is expressed by the class, in turn defined by a set. The precise semantics of the observation depends on the user-defined set.
   - :ref:`sentiment_annotation` -- ``<sentiment>`` -- Sentiment analysis marks subjective information such as sentiments or attitudes expressed in text. The sentiments/attitudes are defined by a user-defined set definition.
   - :ref:`statement_annotation` -- ``<statement>`` -- Statement annotation, sometimes also refered to as attribution, allows to decompose statements into the source of the statement, the content of the statement, and the way these relate, provided these are made explicit in the text.

.. foliaspec:begin:toctree(span,hidden)
.. toctree::
   :hidden:
   :maxdepth: 3

   syntax_annotation
   chunking_annotation
   entity_annotation
   dependency_annotation
   timesegment_annotation
   coreference_annotation
   semrole_annotation
   predicate_annotation
   observation_annotation
   sentiment_annotation
   statement_annotation

.. foliaspec:end:toctree

.. _group_annotations:

Group Annotations: Inline Annotations on Span Annotations
----------------------------------------------------------

It is possible to directly apply inline annotations (see :ref:`inline_annotation_category`) to span annotations, which allows for example to assign a
part-of-speech tag or lemma directly to an entity, rather than to a word (``<w>``) as is customary. This functionality, however, needs to be explicitly enabled by adding the ``groupannotations=yes`` attribute to the declaration, as it adds extra complexity to a FoLiA document and in this way informs parsers to be aware of this.


