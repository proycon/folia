.. _inline_annotation_category:

Inline Annotation
===================================================================

.. foliaspec:category_description(inline)
This category encompasses (linguistic) annotation types describing a single structural element. Examples are Part-of-Speech Annotation or Lemmatisation, which often describe a single token.

These annotation types are encoded in an inline fashion in FoLiA, i.e. they appear within the structural element to
which they apply (often words/tokens but not necessarily so) and make use of the hierarchical nature of XML.

Annotation Types
-------------------

.. foliaspec:toc(inline)
* :ref:`inline_annotation_category` -- This category encompasses (linguistic) annotation types describing a single structural element. Examples are Part-of-Speech Annotation or Lemmatisation, which often describe a single token.
   - :ref:`pos_annotation` -- ``<pos>`` -- Part-of-Speech Annotation, one of the most common types of linguistic annotation. Assigns a lexical class to words.
   - :ref:`lemma_annotation` -- ``<lemma>`` -- Lemma Annotation, one of the most common types of linguistic annotation. Represents the canonical form of a word.
   - :ref:`domain_annotation` -- ``<domain>`` -- Domain/topic Annotation. A form of inline annotation used to assign a certain domain or topic to a structure element.
   - :ref:`sense_annotation` -- ``<sense>`` -- Sense Annotation allows to assign a lexical semantic sense to a word.
   - :ref:`errordetection_annotation` -- ``<errordetection>`` -- This annotation type is deprecated in favour of `Observation Annotation` and only exists for backward compatibility.
   - :ref:`subjectivity_annotation` -- ``<subjectivity>`` -- This annotation type is deprecated in favour of `Sentiment Annotation` and only exists for backward compatibility.
   - :ref:`lang_annotation` -- ``<lang>`` -- Language Annotation simply identifies the language a part of the text is in. Though this information is often part of the metadata, this form is considered an actual annotation.

.. foliaspec:begin:toctree(inline,hidden)
.. toctree::
   :hidden:
   :maxdepth: 3

   pos_annotation
   lemma_annotation
   domain_annotation
   sense_annotation
   errordetection_annotation
   subjectivity_annotation
   lang_annotation

.. foliaspec:end:toctree
