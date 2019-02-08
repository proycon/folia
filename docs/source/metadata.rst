.. _metadata:

Metadata
========================

FoLiA supports associating metadata with your document. An extensive and mandatory part of the metadata is the
:ref:`annotation_declarations` block (``<annotations>``), and optionally also the block for :ref:`provenance_data`
(``<provenance``). To associate other arbitrary metadata with a FoLiA document, there is FoLiA's native metadata system,
in which simple metadata fields can be defined and used at will through the ``<meta>`` element. The following example shows
document-wide metadata:

.. code-block:: xml

   <metadata type="native">
       <annotations>
       ..
       </annotations>
       <meta id="title">Title of my document</meta>
       <meta id="language">eng</meta>
   </metadata>

The native metadata format just offers a simple key-value store. You can define
fields with custom IDs. FoLiA itself does not predefine any, strictly speaking, although certain fields like
*language*, *title* and *author* are conventional and can be interpreted by some FoLiA-capable tools and libraries.

The native metadata format is deliberately limited, as various other formats
already tackle the metadata issue. FoLiA is able to operate with any other
metadata format, such as for example Dublin Core or for example CMDI. The
``type`` attribute specifies what metadata format is used. We see it was set
to ``native`` for FoLiA's native metadata format, for foreign formats it
can be set to any other string.

Foreign metadata can be stored in two ways:

* Externally in a different file
* Internally in the metadata block of the FoLiA document itself

When the metadata is stored externally in a different
file, a reference is made from the ``src`` attribute. As shown in the
following example:

.. code-block:: xml

   <metadata type="cmdi" src="/path/or/url/to/metadata.cmdi">
     <annotations>
     ..
     </annotations>
   </metadata>

If you want to store the metadata in the FoLiA document itself, then the
metadata must be places inside a ``<foreign-data>`` element. All elements
under foreign-data *must* be in another XML namespace, that is, not the default
FoLiA namespace. Consider the following example for Dublin Core:

.. code-block:: xml

   <metadata type="dc">
     <annotations>
     ..
     </annotations>
     <foreign-data xmlns:dc="http://purl.org/dc/elements/1.1/">
       <dc:identifier>mydoc</dc:identifier>
       <dc:format>text/xml</dc:format>
       <dc:type>Example</dc:type>
       <dc:contributor>proycon</dc:contributor>
       <dc:creator>proycon</dc:creator>
       <dc:language>en</dc:language>
       <dc:publisher>Radboud University</dc:publisher>
       <dc:rights>public Domain</dc:rights>
     </foreign-data>
   </metadata>

The namespace prefix and the type specified in the ``<metadata>``
element should match.

.. _submetadata:

Submetadata
-------------------

Whereas the metadata discussed in the previous section concerns document-wide metadata, i.e. metadata that is applicable
to the document as a whole, FoLiA also supports metadata on arbitrary parts of the document. This we call
*submetadata*. Within the ``<metadata>`` block, one can include one or more ``<submetadata>`` blocks. Like
``<metadata>``, a ``<submetadata>`` block carries a ``type`` attribute, a ``src`` attribute in case the
metadata is an external reference, and it may hold ``<meta>`` elements or ``<foreign-data>`` elements. It differs
from ``<metadata>`` in that it carries a mandatory ``xml:id`` attribute and *never* has an ``<annotations>`` or
``<provenance>`` block.  The ID is in turn used to back to the metadata from particular elements in the text. Such a reference is made using the
``metadata`` attribute, which is a common FoLiA attribute allowed on many elements. Consider the following example
(certain details are omitted for brevity):

.. code-block:: xml

   <FoLiA>
   <metadata>
    <annotations>...</annotations>
    <submetadata xml:id="metadata.1" type="native">
      <meta id="author">proycon</meta>
      <meta id="language">nld</meta>
    </submetadata>
    <submetadata xml:id="metadata.2" type="native">
      <meta id="author">Shakespeare</meta>
      <meta id="language">eng</meta>
    </submetadata>
   </metadata>
   <text>
    <p metadata="metadata.1">
      <t>Het volgende vers komt uit Hamlet:</t>
    </p>
    <p metadata="metadata.2">
     <s><t>To be, or not to be, that is the question:</t></s>
     <s><t>Whether 'tis nobler in the mind to suffer<br/>The slings and arrows of outrageous fortune,<br/>Or to take Arms against a Sea of troubles,<br/> And by opposing end them:</s></t>
    </p>
   </text>
   </FoLiA>

Since metadata can be associated with anything, any arbitrary sub-part of untokenised text can even be selected and
associated with the existing facilities ``<str>`` or ``t-str`` (see :ref:`string_annotation`). Some redundancy
occurs only at places where structural boundaries are crossed (the metadata attribute might have to be repeated on
multiple structural elements if there is no catch-all structure).

Submetadata is inherited (recursively), i.e. it is not necessary to explicitly assign the ``metadata`` attribute to the children
of an element that already has such an assignment.
