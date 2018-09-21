.. _semrole_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(semrole)
XXX

.. foliaspec:annotationtype_description(semrole)
XXX

Specification
---------------

.. foliaspec:specification(semrole)
XXX

Explanation
-------------------------

.. note::

    Please first ensure you are familiar with the general principles of :ref:`span_annotation` to make sense of this annotation type.

Semantic roles are usually embedded within the ``<predicate>`` span
annotation element (see :ref:`predicate_annotation`, since FoLiA v1.3). This is a *separate* span
annotation element, which itself may also take a class and has its own declaration. Such a class can for
instance be used to describe frame semantics, such as
`FrameNet <https://framenet.icsi.berkeley.edu/fndrupal/>`_.

Semantic roles without predicates are also allowed, but less expressive as
relations between the semantic roles are not explicit. The reverse also hold, you can do predicate annotation without
semantic role labelling.

.. seealso::

    :ref:`predicate_annotation`

Example
-------------------------

.. literalinclude:: ../examples/semroles.2.0.0.folia.xml
    :linenos:
    :language: xml


