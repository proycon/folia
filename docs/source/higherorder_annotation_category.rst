.. _higherorder_annotation_category:

Higher-order Annotation
===================================================================

.. foliaspec:category_description(higherorder)
Higher-order Annotation groups a very diverse set of annotation types that are considered *annotations on annotations*

FoLiA defines the following types of higher-order annotation:

.. foliaspec:toc(higherorder)
* :ref:`higherorder_annotation_category` --
  Higher-order Annotation groups a very diverse set of annotation types that are considered *annotations on annotations*
   - :ref:`correction_annotation` -- ``<correction>`` -- Corrections are one of the most complex annotation types in FoLiA. Corrections can be applied not just over text, but over any type of structure annotation, inline annotation or span annotation. Corrections explicitly preserve the original, and recursively so if corrections are done over other corrections.
   - :ref:`gap_annotation` -- ``<gap>`` -- Sometimes there are parts of a document you want to skip and not annotate at all, but include as is. This is where gap annotation comes in, the user-defined set may indicate the kind of gap. Common omissions in books are for example front-matter and back-matter, i.e. the cover.
   - :ref:`relation_annotation` -- ``<relation>`` -- FoLiA provides a facility to relate arbitrary parts of your document with other parts of your document, or even with parts of other FoLiA documents or external resources, even in other formats. It thus allows linking resources together. Within this context, the ``xref`` element is used to refer to the linked FoLiA elements.
   - :ref:`spanrelation_annotation` -- ``<spanrelation>`` -- Span relations are a stand-off extension of relation annotation that allows for more complex relations, such as word alignments that include many-to-one, one-to-many or many-to-many alignments. One of its uses is in the alignment of multiple translations of (parts) of a text.
   - :ref:`metric_annotation` -- ``<metric>`` -- Metric Annotation is a form of higher-order annotation that allows annotation of some kind of measurement. The type of measurement is defined by the class, which in turn is defined by the set as always. The metric element has a ``value`` attribute that stores the actual measurement, the value is often numeric but this needs not be the case.
   - :ref:`string_annotation` -- ``<str>`` -- This is a form of higher-order annotation for selecting an arbitrary substring of a text, even untokenised, and allows further forms of higher-order annotation on the substring. It is also tied to a form of text markup annotation.
   - :ref:`alternative_annotation` -- ``<alt>`` -- This form of higher-order annotation encapsulates alternative annotations, i.e. annotations that are posed as an alternative option rather than the authoratitive chosen annotation
   - :ref:`comment_annotation` -- ``<comment>`` -- This is a form of higher-order annotation that allows you to associate comments with almost all other annotation elements
   - :ref:`description_annotation` -- ``<desc>`` -- This is a form of higher-order annotation that allows you to associate descriptions with almost all other annotation elements
   - :ref:`external_annotation` -- ``<external>`` -- External annotation makes a reference to an external FoLiA document whose structure is inserted at the exact place the external element occurs.

.. foliaspec:begin:toctree(higherorder,hidden)
.. toctree::
   :hidden:
   :maxdepth: 3

   correction_annotation
   gap_annotation
   relation_annotation
   spanrelation_annotation
   metric_annotation
   string_annotation
   alternative_annotation
   comment_annotation
   description_annotation
   external_annotation

.. foliaspec:end:toctree
