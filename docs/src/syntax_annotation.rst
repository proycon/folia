.. _syntax_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(syntax)
XXX

.. foliaspec:annotationtype_description(syntax)
XXX

Specification
---------------

.. foliaspec:specification(syntax)
XXX

Explanation
-------------------------

.. note::

    Please first ensure you are familiar with the general principles of :ref:`span_annotation` to make sense of this annotation type.

Syntax annotation allows representation of a syntax tree, commonly the result of *constituency parsing*. This is a
nested form of span annotation, in which nodes in the tree are represented by ``<su>`` (syntactic unit) elements. Each
syntactic unit may carry a class in a user-defined set, determining the vocabulary of the syntax annotation.

It is recommended for each syntactic unit to have a unique identifier.

.. seealso::

    For dependency parsing, see :ref:`dependency_parsing` instead.

Example
-------------------------

.. literalinclude:: ../examples/syntax.2.0.0.folia.xml
    :linenos:
    :language: xml


