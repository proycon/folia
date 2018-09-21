.. _observation_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(observation)
XXX

.. foliaspec:annotationtype_description(observation)
XXX

Specification
---------------

.. foliaspec:specification(observation)
XXX

Explanation
-------------------------

.. note::

    Please first ensure you are familiar with the general principles of :ref:`span_annotation` to make sense of this annotation type.

The ``<observation>`` element is a span annotation element that makes an observation
pertaining to one or more word tokens. It is embedded in an
``observations`` layer.

Observations offer a an external qualification on part of a text. The
qualification is expressed by the class, in turn defined by a set. The precise
semantics of the observation depends on the user-defined set.

The element may for example act to mark errors in the text or to capture observations from teachers/proofreaders.

Example
-------------------------

.. literalinclude:: ../examples/observations.2.0.0.folia.xml
    :linenos:
    :language: xml


