.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _etymology_annotation:

Etymology Annotation
==================================================================

.. foliaspec:annotationtype_description(etymology)

Specification
---------------

.. foliaspec:specification(etymology)

Explanation
-------------------------

In etymology annotation, you can associate words or morphemes with their historical roots. The classes usually correspond to some kind of lexical ID in an etymological database.

You can use :ref:`description_annotation` to optionally associate a human readable description with the etymology annotation (or any other annotation for that matter), or alternatively leave it up to the etymological set definition.

The sets are, as always, user-defined and may correspond for instance with particular historical languages or language groups. The below example illustrates this, and multiple sets are used for multiple etymological annotations.


Example
-------------------------

The following example shows sense annotations:

.. literalinclude:: ../../examples/etymology.2.5.2.folia.xml
    :linenos:
    :language: xml


