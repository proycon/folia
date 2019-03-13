.. _subtoken_annotation_category:

Subtoken Annotation
===================================================================

.. foliaspec:category_description(subtoken)
This category contains morphological annotation and phonological annotation, i.e. the segmentation of a word into morphemes and phonemes, and recursively so if desired. It is a special category that mixes characteristics from structure annotation (the ``morpheme`` and ``phoneme`` elements are very structure-like) and also from span annotation, as morphemes and phonemes are embedded in an annotation layer and refer back to the text/phonetic content they apply to. Like words/tokens, these elements may also be referenced from ``wref`` elements.

FoLiA defines the following types of subtoken annotation:

.. foliaspec:toc(subtoken)
* :ref:`subtoken_annotation_category` --
  This category contains morphological annotation and phonological annotation, i.e. the segmentation of a word into morphemes and phonemes, and recursively so if desired. It is a special category that mixes characteristics from structure annotation (the ``morpheme`` and ``phoneme`` elements are very structure-like) and also from span annotation, as morphemes and phonemes are embedded in an annotation layer and refer back to the text/phonetic content they apply to. Like words/tokens, these elements may also be referenced from ``wref`` elements.
   - :ref:`morphological_annotation` -- ``<morpheme>`` -- Morphological Annotation allows splitting a word/token into morphemes, morphemes itself may be nested. It is embedded within a layer ``morphology`` which can be embedded within word/tokens.
   - :ref:`phonological_annotation` -- ``<phoneme>`` -- The smallest unit of annotatable speech in FoLiA is the phoneme level. The phoneme element is a form of structure annotation used for phonemes.  Alike to morphology, it is embedded within a layer ``phonology`` which can be embedded within word/tokens.

.. foliaspec:begin:toctree(subtoken,hidden)
.. toctree::
   :hidden:
   :maxdepth: 3

   morphological_annotation
   phonological_annotation

.. foliaspec:end:toctree
