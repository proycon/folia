.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _rawcontent_annotation:

Raw Content
==================================================================

.. foliaspec:annotationtype_description(rawcontent)
This associates raw text content which can not carry any further annotation. It is used in the context of :ref:`gap_annotation`

Specification
---------------

.. foliaspec:specification(rawcontent)
:Annotation Category: :ref:`content_annotation_category`
:Declaration: ``<rawcontent-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: Since the beginning, but revised and made a proper annotation type in v2.0
:**Element**: ``<content>``
:API Class: ``Content`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Content.html>`_)
:Required Attributes: 
:Optional Attributes: * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`)
:Valid Context: ``<gap>`` (:ref:`gap_annotation`)

Explanation
-------------------------

The content element associates raw text content with an element, it is specifically used in the context of
:ref:`gap_annotation`. The content can carry no further annotations.

Example
-------------------------

.. literalinclude:: ../../examples/gaps.2.0.0.folia.xml
    :linenos:
    :language: xml


