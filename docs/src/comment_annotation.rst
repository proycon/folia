.. _comment_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(comment)
XXX

.. foliaspec:annotationtype_comment(comment)
XXX

Specification
---------------

.. foliaspec:specification(comment)
XXX

Explanation
-------------------------

Comments is a simple higher-order annotation element that may be used with any
annotation. It holds text that comments the annotation. Multiple comments are
allowed per annotation.

An alternative to these FoLiA-specific comments, which are considered actual
annotations, is standard XML comments. Standard XML comments, however, are not
considered actual annotations and most likely won't be interpreted by any
tools.

Example
-------------------------

Consider the following example in the context of :ref:`sense_annotation`.

.. literalinclude:: ../examples/sense.2.0.0.folia.xml
    :linenos:
    :language: xml


