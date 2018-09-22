.. _table_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(table)
XXX

.. foliaspec:annotationtype_description(table)
XXX

Specification
---------------

.. foliaspec:specification(table)
XXX

.. foliaspec:specification(tablehead)

XXX
.. foliaspec:specification(row)
XXX

.. foliaspec:specification(cell)
XXX

Explanation
-------------------------

Support for simple tables is provided in a fashion similar to HTML and TEI. The
element ``<table>`` introduces a table, within its scope ``row``
elements mark the various rows, ``<tablehead>`` marks the header of the
table and contains one or more rows. The rows themselves consist of
``<cell>`` elements, which in turn may contain other structural elements
such as words, sentences or even entire paragraphs.

Tables, rows and cells can all be assigned classes (in the same set).

Example
-------------------------

.. literalinclude:: ../examples/table.2.0.0.folia.xml
    :linenos:
    :language: xml


