.. _linebreak_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(linebreak)
XXX

.. foliaspec:annotationtype_description(linebreak)
XXX

Specification
---------------

.. foliaspec:specification(linebreak)
XXX

:Extra Attributes: * ``newpage`` -- Can be set to ``yes`` to indicate that the break is not just a linebreak, but also a pagebreak (defaults to ``no``)
                   * ``pagenr`` -- The number of the page after the break
                   * ``linenr`` -- The number of the line after the break

Description & Examples
-------------------------

Linebreaks play a double role, they are a structure element as well as a text markup element, the latter implies that you
may also use ``<br/>`` *within* the scope of text content, so within a ``<t>`` element.

The difference between ``br`` and ``whitespace`` is that the former specifies that only a linebreak was present, not
forcing any vertical whitespace between the lines, whilst the latter actually generates an empty space, which would
comparable to two successive ``br`` statements. Both elements can be used inside various structural elements, such as
divisions, paragraphs, headers, and sentences.


.. literalinclude:: ../examples/whitespace-linebreaks.folia.xml
    :linenos:
    :language: xml


