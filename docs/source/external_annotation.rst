.. _external_annotation:

External Annotation
===================================================================

.. foliaspec:annotationtype_description(external)
External annotation makes a reference to an external FoLiA document whose structure is inserted at the exact place the external element occurs.

Specification
---------------

.. foliaspec:specification(external)
XXX


Explanation
-------------------------

This annotation type type is used to split a larger document into multiple smaller ones, and link from the parent
document to the external child documents. It is a type of higher-order annotation that is inserted at a certain place in the
parent structure. The parent document would be functionally equivalent if the structure of the external child documents were
inserted at the point the ``<external>`` element occurs.

The ``<external>`` element is valid in most structural elements. It is **not** a mechanism to create stand-off
annotation documents. Each external document must also be a valid FoLiA document in its own right.

The ``src`` attribute can refer to a local file path (relative or absolute) or a remote URL.

Example
-------------------------

.. literalinclude:: ../../examples/external.2.4.0.folia.xml
    :linenos:
    :language: xml

