.. _token_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(token)
Token Annotation
==================================================================

.. foliaspec:annotationtype_description(token)
This annotation type introduces a tokenisation layer for the document. The terms **token** and **word** are used interchangeably in FoLiA as FoLiA itself does not commit to a specific tokenisation paradigm. Tokenisation is a prerequisite for the majority of linguistic annotation types offered by FoLiA and it is one of the most fundamental types of Structure Annotation. The words/tokens are typically embedded in other types of structure elements, such as sentences or paragraphs.

Specification
---------------

.. foliaspec:specification(token)
:Element Name (primary): ``<w>``
:Declaration: ``<token-annotation set="..." />``
:Category: :ref:`structure_annotation_category`
:Accepted Data (as Annotation Types): :ref:`alignment_annotation`, :ref:`correction_annotation`, :ref:`metric_annotation`, :ref:`part_annotation`, :ref:`phon_annotation`, :ref:`string_annotation`, :ref:`text_annotation`
:Accepted Data (as FoLiA XML Elements): ``<alignment>``, ``<correction>``, ``<metric>``, ``<part>``, ``<ph>``, ``<str>``, ``<t>``
:Accepted Data (as API Classes): ``Alignment``, ``Correction``, ``Metric``, ``Part``, ``PhonContent``, ``String``, ``TextContent``
:Version History: Since the beginning

:Extra Attributes: ``space`` -- Indicates whether a space should be inserted after this token (value ``yes``, default if not specified) or not (value ``no``).

Description & Examples
-------------------------

Tokenisation is a prerequisite for most forms of linguistic annotation. The ``<w>`` element is FoLiA's basic token or
word (hence the element's name). This element occurs in the scope of wider structural elements such as ``<s>``
(:ref:`sentence_annotation`)


.. literalinclude:: ../examples/snippets/token.folia.xml
    :linenos:
    :language: xml


