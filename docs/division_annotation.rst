.. _division_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(division)
XXX

.. foliaspec:annotationtype_description(division)
XXX

Specification
---------------

.. foliaspec:specification(division)
XXX

Description & Examples
-------------------------

The structure element ``div`` is used to create divisions and subdivisions within a text.

Each division *may* be of
a particular \emph{class} pertaining to a \emph{set} defining all possible classes.

Divisions and other structural units are often numbered, think for example of
chapters and sections. The number, as it was in the source document, can be
encoded in the \texttt{n} attribute of the structure annotation element.

Look at the following example, showing a full FoLiA document with structured
divisions. The declared set is a fictitious example:

.. literalinclude:: ../examples/snippets/division.folia.xml
    :linenos:
    :language: xml


