.. _whitespace_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(whitespace)
XXX

.. foliaspec:annotationtype_description(whitespace)
XXX

Specification
---------------

.. foliaspec:specification(whitespace)
XXX

Description & Examples
-------------------------

Sometimes you may want to explicitly specify vertical whitespace, rather than repeat multiple linebreaks
(:ref:`Linebreak Annotation`), the `whitespace` element accomplishes this. Note that using `p` to denote paragraphs is always strongly preferred
over using `whitespace` to mark their boundaries, this element should be used sparingly!

The difference between ``br`` and ``whitespace`` is that the former specifies that only a linebreak was present, not
forcing any vertical whitespace between the lines, whilst the latter actually generates an empty space, which would
comparable to two successive ``br`` statements. Both elements can be used inside various structural elements, such as
divisions, paragraphs, headers, and sentences.

