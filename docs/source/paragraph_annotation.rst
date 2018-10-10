.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _paragraph_annotation:

Paragraph Annotation
==================================================================

.. foliaspec:annotationtype_description(paragraph)
This annotation type introduces a tokenisation layer for the document. The terms **token** and **word** are used interchangeably in FoLiA as FoLiA itself does not commit to a specific tokenisation paradigm. Tokenisation is a prerequisite for the majority of linguistic annotation types offered by FoLiA and it is one of the most fundamental types of Structure Annotation. The words/tokens are typically embedded in other types of structure elements, such as sentences or paragraphs.

Specification
---------------

.. foliaspec:specification(paragraph)
XXX

Explanation & Examples
-------------------------

Paragraphs are a very common structural element and their use is encouraged. The following example shows a single paragraph within a structure of divisions with headers, it does not provide any deeper tokenisation.

.. literalinclude:: ../../examples/untokenised-structure.2.0.0.folia.xml
    :linenos:
    :language: xml

The next example shows a paragraph with sentences and tokenisation:

.. literalinclude:: ../../examples/tokens-structure.2.0.0.folia.xml
    :linenos:
    :language: xml
