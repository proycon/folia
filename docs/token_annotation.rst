.. _token_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(token)
Word/Token Annotation
========================

.. foliaspec:annotationtype_description(token)
(description goes here)

Specification
---------------

.. foliaspec:specification(token)
(specification goes here)

:Extra Attributes: ``space`` -- Indicates whether a space should be inserted after this token (value ``yes``, default if not specified) or not (value ``no``).

Description & Examples
-------------------------

Tokenisation is a prerequisite for most forms of linguistic annotation. The ``<w>`` element is FoLiA's basic token or
word (hence the element's name). This element occurs in the scope of wider structural elements such as ``<s>``
(:ref:`sentence_annotation`)





.. literalinclude:: ../examples/snippets/token.folia.xml
    :linenos:
    :language: xml


