.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _spanrelation_annotation:

Span Relation Annotation
==================================================================

.. foliaspec:annotationtype_description(spanrelation)
Span relations are a stand-off extension of relation annotation that allows for more complex relations, such as word alignments that include many-to-one, one-to-many or many-to-many alignments. One of its uses is in the alignment of multiple translations of (parts) of a text.

Specification
---------------

.. foliaspec:specification(spanrelation)
:Annotation Category: :ref:`higherorder_annotation_category`
:Declaration: ``<spanrelation-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: since v0.8, renamed from complexalignment in v2.0
:**Element**: ``<spanrelation>``
:API Class: ``SpanRelation`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.SpanRelation.html>`_)
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
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<relation>`` (:ref:`relation_annotation`)
:Valid Context: ``<spanrelations>`` (:ref:`spanrelation_annotation`)

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

