.. _sense_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(sense)
XXX

.. foliaspec:annotationtype_description(sense)
XXX

Specification
---------------

.. foliaspec:specification(sense)
XXX

Explanation
-------------------------

In semantic sense annotation, the classes will correspond to some kind of lexical unit ID or synset ID.
In vocabularies that make an explicit distinction between lexical units and
synonym sets (synsets), you can use the ``synset`` *predefined subset* for notation of the
latter. A simpler alternative is to just use two different sets similtaneously (two ``sense`` annotations per item).

You can use :ref:`description_annotation` to optionally associate a human readable description with the sense annotation (or any other annotation for that matter).

Example
-------------------------

The following example shows sense annotations:

.. literalinclude:: ../examples/sense.2.0.0.folia.xml
    :linenos:
    :language: xml


