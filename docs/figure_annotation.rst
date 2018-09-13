.. _figure_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(figure)
XXX

.. foliaspec:annotationtype_description(figure)
XXX

Specification
---------------

Figure
~~~~~~~~~~

.. foliaspec:specification(figure)
XXX

:Extra Attributes: ``src`` -- Points to an image file (URL)

Caption
~~~~~~~~~~~

.. foliaspec:specification(caption)
XXX

Description & Examples
-------------------------

Even figures can be encoded in the FoLiA format, although the actual figure
itself can only be included as a mere reference to an external image file, but
including such a reference with the ``src`` attribute is optional.

Within the context of a figure, a ``caption`` element can be used.

The following example shows a figure and caption:

.. literalinclude:: ../examples/figure.2.0.0.folia.xml
    :linenos:
    :language: xml


