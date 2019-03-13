.. _content_annotation_category:

Content Annotation
===================================================================

.. foliaspec:category_description(content)
This category groups text content and phonetic content, the former being one of the most frequent elements in FoLiA and used to associate text (or a phonetic transcription) with a structural element.

FoLiA defines the following types of content annotation:

.. foliaspec:toc(content)
* :ref:`content_annotation_category` --
  This category groups text content and phonetic content, the former being one of the most frequent elements in FoLiA and used to associate text (or a phonetic transcription) with a structural element.
   - :ref:`text_annotation` -- ``<t>`` -- Text annotation associates actual textual content with structural elements, without it a document would be textless. FoLiA treats it as an annotation like any other.
   - :ref:`phon_annotation` -- ``<ph>`` -- This is the phonetic analogy to text content (``<t>``) and allows associating a phonetic transcription with any structural element, it is often used in a speech context. Note that for actual segmentation into phonemes, FoLiA has another related type: ``Phonological Annotation``
   - :ref:`rawcontent_annotation` -- ``<content>`` -- This associates raw text content which can not carry any further annotation. It is used in the context of :ref:`gap_annotation`

.. foliaspec:begin:toctree(content,hidden)
.. toctree::
   :hidden:
   :maxdepth: 3

   text_annotation
   phon_annotation
   rawcontent_annotation

.. foliaspec:end:toctree
