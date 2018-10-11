.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _complexalignment_annotation:

Complex Alignment Annotation
==================================================================

.. foliaspec:annotationtype_description(complexalignment)
XXX

Specification
---------------

.. foliaspec:specification(complexalignment)
XXX

Explanation & Examples
-------------------------

Please ensure you are familiar with :ref:`alignment_annotation` first, as this is an extension for that annotation type.

Under complex alignments we count many-to-one, one-to-many and many-to-many alignments between elements (such as words).
The element ``<complexalignment>`` behaves similarly to a
span annotation element. This element groups ``<alignment>`` elements
together, effectively creating a many-to-many alignment. The following example
illustrates an example similar to the one above. All this takes place within
the ``<complexalignments>`` annotation layer.

Consider the following example:

.. literalinclude:: ../../examples/complexalignments.2.0.0.folia.xml
    :linenos:
    :language: xml

Here ``<aref>`` is used instead of the ``<wref>`` element we know from :ref:`span_annotation_category`.
as despite similarities alignments are technically not exactly span annotation elements. You can in
fact align anything that can carry an ID, within the same document and across
multiple documents. Moreover, the notion of alignments is not limited to just
words, and it can be used for more than specifying translations.

The first ``<alignment>`` element has no xlink reference, and therefore
simply refers to the current document. The second alignment element links to
the foreign document. This notation is powerful as it allows you to specify a
large number of alignments in a concise matter. Consider the next example in
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
      <complexalignments>
        <complexalignment>
          <alignment class="english-translation">
            <aref id="example-english.p.1.s.1.w.2" t="Dalai" type="w"/>
            <aref id="example-english.p.1.s.1.w.3" t="Lama" type="w"/>
          </alignment>
          <alignment class="french-translation"
           xlink:href="doc-french.xml"
           xlink:type="simple">
            <aref id="example-french.p.1.s.1.w.2" t="Dalai" type="w"/>
            <aref id="example-french.p.1.s.1.w.3" t="Lama" type="w"/>
          </alignment>
          <alignment class="german-translation"
           xlink:href="doc-german.xml"
           xlink:type="simple">
            <aref id="example-german.p.1.s.1.w.2" t="Dalai" type="w"/>
            <aref id="example-german.p.1.s.1.w.3" t="Lama" type="w"/>
          </alignment>
          <alignment class="italian-translation"
           xlink:href="doc-italian.xml"
           xlink:type="simple">
            <aref id="example-italian.p.1.s.1.w.2" t="Dalai" type="w"/>
            <aref id="example-italian.p.1.s.1.w.3" t="Lama" type="w"/>
          </alignment>
        </complexalignment>
      </complexalignments>
    </s>

Now you can even envision a FoLiA document that does not hold actual content,
but acts merely as a document containing all alignments between for example
different translations of the document. Allowing for all relations to be
contained in a single document rather than having to be made explicit in each
language version.

The ``<complexalignment>`` element itself may also take a set, which is
*independent* from the alignment set. They therefore also have two separate
declarations.

