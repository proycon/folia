.. _coreference_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(coreference)
XXX

.. foliaspec:annotationtype_description(coreference)
XXX

Specification
---------------

.. foliaspec:specification(coreference)
XXX

Explanation
-------------------------

.. note::

    Please first ensure you are familiar with the general principles of :ref:`span_annotation` to make sense of this annotation type.

Relations between words that refer to the same referent are expressed in FoLiA
using the ``<coreferencechain>`` span annotation element and the ``<coreferencelink>``
span role within it for each instance.

The co-reference relations are expressed by specifying the entire chain in which all links are coreferent.
The head of a coreferent may optionally be marked with the ``<hd>``
element, another span role.

As always, this annotation layer itself may be embedded on whatever level is preferred. The following example uses
paragraph level, but you can for instance also embed it at sentence level or a global text level:

The ``coreferencelink`` may take three attributes, which are actually
predefined feature subsets (See :ref:`features`), their values depend
on the set used and are thus user-definable and never predefined:

.. as suggested by Orphee De Clerq:

* ``modality`` - A subset that can be used to indicate that there is modality or negation in this coreference link.
* ``time``  - A subset used to indicate a time dependency. An example of a time dependency is seen in the sentence: *"Bert De Graeve, until recently CEO, will now take up a position as CFO"*. Here
"Bert De Graeve", "CEO"  and "CFO" would all be part of the same coreference chain, and the second coreferencelink ("CEO") can be marked as being in the past using the "time" attribute.
* ``level`` - A subset used that can indicate the level on which the coreference holds. A possible value suggestion could be ``sense``, indicating that only on sense-level there is a coreference relation, as opposed to an actual reference.

Example
-------------------------

.. literalinclude:: ../examples/coreferences.2.0.0.folia.xml
    :linenos:
    :language: xml


