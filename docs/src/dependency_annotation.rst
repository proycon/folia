.. _dependency_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(dependency)
XXX

.. foliaspec:annotationtype_description(dependency)
XXX

Specification
---------------

.. foliaspec:specification(dependency)
XXX

Explanation
-------------------------

.. note::

    Please first ensure you are familiar with the general principles of :ref:`span_annotation` to make sense of this annotation type.

Dependency relations are syntactic relations between spans of tokens. A dependency relation takes a particular class and
consists of a single head component and a single dependent component. In the
sample *"He sees"*, there is  syntactic dependency between the two words:
*"sees"* is the head, and *"He"* is the dependant, and the relation can be qualified as
something like *subject*, as the dependant is the subject of the head word.
Each dependency relation is explicitly noted in FoLiA.

The element ``<dependencies>`` introduces this annotation layer. Within it,
``<dependency>`` elements describe all dependency pairs.
The ``<dependency>`` element always contains two *span roles*: one
head element (``<hd>``) and one dependent element (``<dep>``). Within these span roles, the words
referenced in the usual stand-off fashion, using ``<wref>``.


Example
-------------------------

In the example below, we show a Dutch sentence parsed with the Alpino Parser.

For a better understanding, The following figure illustrates the syntactic parse with the dependency relations (blue).

.. image:: ../alpino.png
    :align: center

We show not only the dependency layer, but also the syntax layer (:ref:`syntax_annotation`)
to which it is related.

.. literalinclude:: ../examples/dependencies.2.0.0.folia.xml
    :linenos:
    :language: xml


