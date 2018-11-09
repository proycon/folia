.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _relation_annotation:

Relation Annotation
==================================================================

.. foliaspec:annotationtype_description(relation)
XXX

Specification
---------------

.. foliaspec:specification(relation)
XXX

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
block.

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

    For more complex many-to-many relations, see :ref:`complexrelation_annotation`, an extension of the current
    annotation type.

Translations
---------------

relation Annotation and :ref:`complexrelation_annotation` are an excellent tool for specifying translations. For situations in which relations seem overkill, a simple
multi-document mechanism is available. This mechanism is based purely on convention: It assumes that structural elements
that are translations simply share the same ID. This approach is quite feasible when used on higher-level structural
elements, such as divisions, paragraphs, events or entries.

Example
-------------------------

The following example shows relations within strings in a document (See also :ref:`string_annotation`):

.. literalinclude:: ../../examples/strings-relations.2.0.0.folia.xml
    :linenos:
    :language: xml


