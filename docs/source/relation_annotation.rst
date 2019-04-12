.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _relation_annotation:

Relation Annotation
==================================================================

.. foliaspec:annotationtype_description(relation)
FoLiA provides a facility to relate arbitrary parts of your document with other parts of your document, or even with parts of other FoLiA documents or external resources, even in other formats. It thus allows linking resources together. Within this context, the ``xref`` element is used to refer to the linked FoLiA elements.

Specification
---------------

.. foliaspec:specification(relation)
:Annotation Category: :ref:`higherorder_annotation_category`
:Declaration: ``<relation-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: Revised since v0.8, renamed from alignment in v2.0
:**Element**: ``<relation>``
:API Class: ``Relation`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Relation>`_)
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
                      * ``xlink:href`` -- Turns this element into a hyperlink to the specified URL
                      * ``xlink:type`` -- The type of link (you'll want to use ``simple`` in almost all cases).
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<metric>`` (:ref:`metric_annotation`)
:Valid Context: ``<chunk>`` (:ref:`chunking_annotation`), ``<coreferencechain>`` (:ref:`coreference_annotation`), ``<coreferencelink>`` (:ref:`coreference_annotation`), ``<def>`` (:ref:`definition_annotation`), ``<dependency>`` (:ref:`dependency_annotation`), ``<div>`` (:ref:`division_annotation`), ``<entity>`` (:ref:`entity_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<note>`` (:ref:`note_annotation`), ``<observation>`` (:ref:`observation_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<predicate>`` (:ref:`predicate_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<semrole>`` (:ref:`semrole_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<sentiment>`` (:ref:`sentiment_annotation`), ``<spanrelation>`` (:ref:`spanrelation_annotation`), ``<statement>`` (:ref:`statement_annotation`), ``<str>`` (:ref:`string_annotation`), ``<su>`` (:ref:`syntax_annotation`), ``<table>`` (:ref:`table_annotation`), ``<term>`` (:ref:`term_annotation`), ``<timesegment>`` (:ref:`timesegment_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)

Explanation
-------------------------

.. note::

    In versions of FoLiA prior to 2.0, this annotation type was called *alignments*

FoLiA provides a facility to link parts of your document with other parts of your document, or even with parts of other
FoLiA documents or external resources. These are called *relations* and are implemented using the ``<relation>``
element.  Within this context, the ``<xref>`` element is  used to cross-link to the related FoLiA elements.

Consider the two following aligned sentences from excerpts of two
**separate** FoLiA documents in different languages:

.. code-block:: xml

    <s xml:id="example-english.p.1.s.1">
      <t>The Dalai Lama greeted him.</t>
      <relation class="french-translation" xlink:href="doc-french.xml"
        xlink:type="simple">
         <xref id="doc-french.p.1.s.1" t="Le Dalai Lama le saluait."
         type="s" />
      </relation>
    </s>

.. code-block:: xml

    <s xml:id="example-french.p.1.s.1">
      <t>Le Dalai Lama le saluait.</t>
      <relation class="english-translation" xlink:href="doc-english.xml"
        xlink:type="simple">
          <xref id="doc-english.p.1.s.1" t="The Dalai Lama greeted him."
           type="s" />
      </relation>
      <relation class="dutch-translation" xlink:href="doc-dutch.xml"
         xlink:type="simple">
          <xref id="doc-dutch.p.1.s.1" t="De Dalai Lama begroette hem."
           type="s" />
      </relation>
    </s>

It is the job of the ``<relation>`` element to point to the relevant
resource, whereas the ``<xref>`` element points to a specific point
*inside* the referenced resource. The ``xlink:href`` attribute is
used to link to the target document, if any. If the relation is within the
same document then it should simply be omitted. The ``type`` attribute on
``<xref>`` specifies the type of element the relation points too, i.e. its
value is equal to the tagname it points to. The ``t`` attribute to the
``<xref>`` element is merely optional and this overhead is added simply to
facilitate the job of limited FoLiA parsers and provides a quick reference to
the target text for both parsers and human users.

Although the above example has a single relation reference (``<xref>``), it
is not forbidden to specify multiple references within the ``<relation>``
block, effectively referring to a span of multiple elements at the target.

By default, relations are between FoLiA documents. It is, however, also
possible to point to resources in different formats. This has to be made
explicit using the ``format`` attribute on the ``<relation>`` element.
The value of the ``format`` attribute is a MIME type and defaults to
``text/folia+xml`` (naming follows RFC 3032). In the following example
align a section (``<div>``) with the original HTML document from which the
FoLiA document is arrived, and where the section is expressed with an HTML anchor
(``<a>``) tag.

.. code-block:: xml

    <div class="section">
     <t>lorum ipsum etc.</t>
     <relation class="original" xlink:href="http://somewhere/original.html"
        xlink:type="simple" format="text/html">
        <xref id="section2" type="a" />
     </relation>
    </div>

.. seealso::

    For more complex many-to-many relations, see :ref:`spanrelation_annotation`, an extension of the current
    annotation type.

Translations
---------------

relation Annotation and :ref:`spanrelation_annotation` are an excellent tool for specifying translations. For situations in which relations seem overkill, a simple
multi-document mechanism is available. This mechanism is based purely on convention: It assumes that structural elements
that are translations simply share the same ID. This approach is quite feasible when used on higher-level structural
elements, such as divisions, paragraphs, events or entries.

Example
-------------------------

The following example shows relations within strings in a document (See also :ref:`string_annotation`):

.. literalinclude:: ../../examples/string-relations.2.0.0.folia.xml
    :linenos:
    :language: xml


