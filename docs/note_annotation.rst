.. _note_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(note)
XXX

.. foliaspec:annotationtype_description(note)
XXX

Specification
---------------

.. foliaspec:specification(note)
XXX

:Set Definitions: You can use any of the following existing set definitions or simply create your own:
                  * `https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/notes.foliaset.xml`_

Explanation
-------------------------

The structure element ``<note>`` allows for notes to be included in FoLiA
documents. A footnote or a bibliographical reference is an example of a
note. The notes form an integral part of the text. For notes that are merely
descriptive comments on the text or its annotations, rather than a part of it,
use ``<desc>`` or ``<comment>`` instead. Notes themselves can contain all the
usual forms of annotations.

The place of a note in the text is where it will appear. References to the note
are made using a specific tag, ``<ref>``, discussed in :ref:`reference_annotation`.

Example
---------

.. literalinclude:: ../examples/note_ref.2.0.0.folia.xml
    :linenos:
    :language: xml


