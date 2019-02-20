.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _hyphenation_annotation:

Hyphenation
==================================================================

.. foliaspec:annotationtype_description(hyphenation)
Structure annotation representing a single linebreak and with special facilities to denote pagebreaks.

Specification
---------------

.. foliaspec:specification(hyphbreak)
XXX

:Extra Attributes: * ``newpage`` -- Can be set to ``yes`` to indicate that the break is not just a linebreak, but also a pagebreak (defaults to ``no``)
                   * ``pagenr`` -- The number of the page after the break
                   * ``linenr`` -- The number of the line after the break

Description & Examples
-------------------------

Hyphenation breaks are a text markup element that indicate where in the original text a word was broken up for
line-wrapping purposes.

The difference between ``t-hbr`` and ``br`` (:ref:`linebreak_annotation`) is that the hyphenised break is a softer
break, only there for page formatting purposes. The hyphen symbol is by definition implied in its usage, so should never
be explicitly incorporated in the text content. For most intents and purposes, a word with a hyphenised break can be
considered semantically identical to a word without one. The following example demonstrates hyphenation in the last
division, alongside the more classical linebreak:

.. literalinclude:: ../../examples/whitespace-linebreaks.2.0.0.folia.xml
    :linenos:
    :language: xml

