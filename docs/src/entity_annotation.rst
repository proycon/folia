.. _entity_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(entity)
XXX

.. foliaspec:annotationtype_description(entity)
XXX

Specification
---------------

.. foliaspec:specification(entity)
XXX

Explanation
-------------------------

.. note::

    Please first ensure you are familiar with the general principles of :ref:`span_annotation` to make sense of this annotation type.

The ``entities`` layer offers a generic solution to encode various types
of entities or *multi-word expressions*, including but not limited to named
entities. The set used determines the precise semantics behind the entities.

This annotation type, being the simplest of all span annotations, is much used in FoLiA.

It is recommended, but not required, for each entity to have a unique identifier.

Example
-------------------------

.. literalinclude:: ../examples/entities-deep.2.0.0.folia.xml
    :linenos:
    :language: xml


