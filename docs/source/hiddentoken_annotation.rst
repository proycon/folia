.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _hiddentoken_annotation:

Hidden Token Annotation
==================================================================

.. foliaspec:annotationtype_description(token)
XXX

Specification
---------------

.. foliaspec:specification(token)
XXX

Explanation
-------------------------

Hidden tokens are tokens that are explicitly not part of the original text. They are either implied or tokens that act
as a dummy for further linguistic annotation. Hidden tokens are are valid target for any form of span annotation through
the ``<wref>`` element (see :ref:`span_annotation_category`_). They are structure elements so may appear interleaved
with the normal tokenisation layer, for which the order is significant.

Example
------------

The following example shows syntactic movement annotation which makes use of a hidden token for an implicit subject.

.. literalinclude:: ../../examples/syntactic-movement.2.0.0.folia.xml
    :linenos:
    :language: xml



