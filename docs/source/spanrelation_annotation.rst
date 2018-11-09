.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _spanrelation_annotation:

Span Relation Annotation
==================================================================

.. foliaspec:annotationtype_description(spanrelation)
XXX

Specification
---------------

.. foliaspec:specification(spanrelation)
XXX

Explanation & Examples
-------------------------

Please ensure you are familiar with :ref:`relation_annotation` first, as this is an extension for that annotation type.

.. note::

    In versions of FoLiA prior to 2.0, this annotation type was called *complex alignments*

Under span relations we count more complex relations such as many-to-one, one-to-many and many-to-many relations between
arbitrary elements.  The element ``<spanrelation>`` behaves similarly to a span annotation element, operating in a
stand-off fashion. This element groups ``<relation>`` elements together, effectively creating a many-to-many relation.
The following example illustrates an example similar to the one above. All this takes place within the
``<spanrelations>`` annotation layer.

Consider the following example:

.. literalinclude:: ../../examples/spanrelations.2.0.0.folia.xml
    :linenos:
    :language: xml

Here ``<xref>`` is used instead of the ``<wref>`` element we know from :ref:`span_annotation_category`.
as despite similarities relations are technically not exactly span annotation elements. You can in
fact relate to anything that can carry an ID, within the same document and across
multiple documents. Moreover, the notion of relations is not limited to just
words, and it can be used for more than specifying translations.

The first ``<relation>`` element has no xlink reference, and therefore
simply refers to the current document. The second relation element links to
the foreign document. This notation is powerful as it allows you to specify a
large number of relations in a concise matter. Consider the next example in
which we added German and Italian, effectively specifying what can be perceived
as 16 relationships over four different documents:

.. code-block:: xml

    <s xml:id="example-english.p.1.s.1">
      <t>The Dalai Lama greeted him.</t>
      <w xml:id="example-english.p.1.s.1.w.1"><t>The</t></w>
      <w xml:id="example-english.p.1.s.1.w.2"><t>Dalai</t></w>
      <w xml:id="example-english.p.1.s.1.w.3"><t>Lama</t></w>
      <w xml:id="example-english.p.1.s.1.w.4"><t>greeted</t></w>
      <w xml:id="example-english.p.1.s.1.w.5"><t>him</t></w>
      <w xml:id="example-english.p.1.s.1.w.6"><t>.</t></w>
      <spanrelations>
        <spanrelation>
          <relation class="english-translation">
            <xref id="example-english.p.1.s.1.w.2" t="Dalai" type="w"/>
            <xref id="example-english.p.1.s.1.w.3" t="Lama" type="w"/>
          </relation>
          <relation class="french-translation"
           xlink:href="doc-french.xml"
           xlink:type="simple">
            <xref id="example-french.p.1.s.1.w.2" t="Dalai" type="w"/>
            <xref id="example-french.p.1.s.1.w.3" t="Lama" type="w"/>
          </relation>
          <relation class="german-translation"
           xlink:href="doc-german.xml"
           xlink:type="simple">
            <xref id="example-german.p.1.s.1.w.2" t="Dalai" type="w"/>
            <xref id="example-german.p.1.s.1.w.3" t="Lama" type="w"/>
          </relation>
          <relation class="italian-translation"
           xlink:href="doc-italian.xml"
           xlink:type="simple">
            <xref id="example-italian.p.1.s.1.w.2" t="Dalai" type="w"/>
            <xref id="example-italian.p.1.s.1.w.3" t="Lama" type="w"/>
          </relation>
        </spanrelation>
      </spanrelations>
    </s>

Now you can even envision a FoLiA document that does not hold actual content,
but acts merely as a document containing all relations between for example
different translations of the document. Allowing for all relations to be
contained in a single document rather than having to be made explicit in each
language version.

The ``<spanrelation>`` element itself may also take a set, which is
*independent* from the alignment set. They therefore also have two separate
declarations.

