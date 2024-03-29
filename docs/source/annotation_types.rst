.. _annotation_types:

Annotation Types
==================

FoLiA defines various XML elements to represent document structure and various annotations, we can divide these XML
elements into several generic annotation groups. In each of these categories, FoLiA defines specific elements for
specific annotation types. This is a deliberate limit on the extensibility of FoLiA in favour of specificity; i.e. you
can't just add your own annotation type. If a particular annotation type is not properly accommodated yet, contact the
FoLiA developers and we will see how we can extend FoLiA.

For good measure, we again emphasise that this is a limitation on annotation types only, not on the vocabulary the
annotation types make use of, which is deliberately separated from the FoLiA standard itself. The next section will
elaborate on this.

Below are the categories and underlying annotation types, you can click each for exhaustive information (but please
finish this introductory chapter first):

.. DO NOT EDIT ANYTHING IN THE TABLE OF CONTENTS BLOCK! IT IS AUTO-GENERATED BY foliaspec!

.. foliaspec:toc
* :ref:`structure_annotation_category` --
  This category encompasses annotation types that define the structure of a document, e.g. paragraphs, sentences, words, sections like chapters, lists, tables, etc... These types are not strictly considered linguistic annotation and equivalents are also commonly found in other document formats such as HTML, TEI, MarkDown, LaTeX, and others. For FoLiA it provides the necessary structural basis that linguistic annotation can build on.
   - :ref:`token_annotation` -- ``<w>`` -- This annotation type introduces a tokenisation layer for the document. The terms **token** and **word** are used interchangeably in FoLiA as FoLiA itself does not commit to a specific tokenisation paradigm. Tokenisation is a prerequisite for the majority of linguistic annotation types offered by FoLiA and it is one of the most fundamental types of Structure Annotation. The words/tokens are typically embedded in other types of structure elements, such as sentences or paragraphs.
   - :ref:`division_annotation` -- ``<div>`` -- Structure annotation representing some kind of division, typically used for chapters, sections, subsections (up to the set definition). Divisions may be nested at will, and may include almost all kinds of other structure elements.
   - :ref:`paragraph_annotation` -- ``<p>`` -- Represents a paragraph and holds further structure annotation such as sentences.
   - :ref:`head_annotation` -- ``<head>`` -- The ``head`` element is used to provide a header or title for the structure element in which it is embedded, usually a division (``<div>``)
   - :ref:`list_annotation` -- ``<list>`` -- Structure annotation for enumeration/itemisation, e.g. bulleted lists.
   - :ref:`figure_annotation` -- ``<figure>`` -- Structure annotation for including pictures, optionally captioned, in documents.
   - :ref:`whitespace_annotation` -- ``<whitespace>`` -- Structure annotation introducing vertical whitespace
   - :ref:`linebreak_annotation` -- ``<br>`` -- Structure annotation representing a single linebreak and with special facilities to denote pagebreaks.
   - :ref:`sentence_annotation` -- ``<s>`` -- Structure annotation representing a sentence. Sentence detection is a common stage in NLP alongside tokenisation.
   - :ref:`event_annotation` -- ``<event>`` -- Structural annotation type representing events, often used in new media contexts for things such as tweets, chat messages and forum posts (as defined by a user-defined set definition). Note that a more linguistic kind of event annotation can be accomplished with `Entity Annotation` or even `Time Segmentation` rather than this one.
   - :ref:`quote_annotation` -- ``<quote>`` -- Structural annotation used to explicitly mark quoted speech, i.e. that what is reported to be said and appears in the text in some form of quotation marks.
   - :ref:`note_annotation` -- ``<note>`` -- Structural annotation used for notes, such as footnotes or warnings or notice blocks.
   - :ref:`reference_annotation` -- ``<ref>`` -- Structural annotation for referring to other annotation types. Used e.g. for referring to bibliography entries (citations) and footnotes.
   - :ref:`table_annotation` -- ``<table>`` -- Structural annotation type for creating a simple tabular environment, i.e. a table with rows, columns and cells and an optional header.
   - :ref:`part_annotation` -- ``<part>`` -- The structure element ``part`` is a fairly abstract structure element that should only be used when a more specific structure element is not available. Most notably, the part element should never be used for representation of morphemes or phonemes! Part can be used to divide a larger structure element, such as a division, or a paragraph into arbitrary subparts.
   - :ref:`utterance_annotation` -- ``<utt>`` -- An utterance is a structure element that may consist of words or sentences, which in turn may contain words. The opposite is also true, a sentence may consist of multiple utterances. Utterances are often used in the absence of sentences in a speech context, where neat grammatical sentences can not always be distinguished.
   - :ref:`entry_annotation` -- ``<entry>`` -- FoLiA has a set of structure elements that can be used to represent collections such as glossaries, dictionaries, thesauri, and wordnets. `Entry annotation` defines the entries in such collections, `Term annotation` defines the terms, and `Definition Annotation` provides the definitions.
   - :ref:`term_annotation` -- ``<term>`` -- FoLiA has a set of structure elements that can be used to represent collections such as glossaries, dictionaries, thesauri, and wordnets. `Entry annotation` defines the entries in such collections, `Term annotation` defines the terms, and `Definition Annotation` provides the definitions.
   - :ref:`definition_annotation` -- ``<def>`` -- FoLiA has a set of structure elements that can be used to represent collections such as glossaries, dictionaries, thesauri, and wordnets. `Entry annotation` defines the entries in such collections, `Term annotation` defines the terms, and `Definition Annotation` provides the definitions.
   - :ref:`example_annotation` -- ``<ex>`` -- FoLiA has a set of structure elements that can be used to represent collections such as glossaries, dictionaries, thesauri, and wordnets. `Examples annotation` defines examples in such collections.
   - :ref:`hiddentoken_annotation` -- ``<hiddenw>`` -- This annotation type allows for a hidden token layer in the document. Hidden tokens are ignored for most intents and purposes but may serve a purpose when annotations on implicit tokens is required, for example as targets for syntactic movement annotation.
* :ref:`content_annotation_category` --
  This category groups text content and phonetic content, the former being one of the most frequent elements in FoLiA and used to associate text (or a phonetic transcription) with a structural element.
   - :ref:`text_annotation` -- ``<t>`` -- Text annotation associates actual textual content with structural elements, without it a document would be textless. FoLiA treats it as an annotation like any other.
   - :ref:`phon_annotation` -- ``<ph>`` -- This is the phonetic analogy to text content (``<t>``) and allows associating a phonetic transcription with any structural element, it is often used in a speech context. Note that for actual segmentation into phonemes, FoLiA has another related type: ``Phonological Annotation``
   - :ref:`rawcontent_annotation` -- ``<content>`` -- This associates raw text content which can not carry any further annotation. It is used in the context of :ref:`gap_annotation`
* :ref:`inline_annotation_category` --
  This category encompasses (linguistic) annotation types describing a single structural element. Examples are Part-of-Speech Annotation or Lemmatisation, which often describe a single token.
   - :ref:`pos_annotation` -- ``<pos>`` -- Part-of-Speech Annotation, one of the most common types of linguistic annotation. Assigns a lexical class to words.
   - :ref:`lemma_annotation` -- ``<lemma>`` -- Lemma Annotation, one of the most common types of linguistic annotation. Represents the canonical form of a word.
   - :ref:`domain_annotation` -- ``<domain>`` -- Domain/topic Annotation. A form of inline annotation used to assign a certain domain or topic to a structure element.
   - :ref:`sense_annotation` -- ``<sense>`` -- Sense Annotation allows to assign a lexical semantic sense to a word.
   - :ref:`errordetection_annotation` -- ``<errordetection>`` -- This annotation type is deprecated in favour of `Observation Annotation` and only exists for backward compatibility.
   - :ref:`subjectivity_annotation` -- ``<subjectivity>`` -- This annotation type is deprecated in favour of `Sentiment Annotation` and only exists for backward compatibility.
   - :ref:`lang_annotation` -- ``<lang>`` -- Language Annotation simply identifies the language a part of the text is in. Though this information is often part of the metadata, this form is considered an actual annotation.
* :ref:`span_annotation_category` --
  This category encompasses (linguistic) annotation types that span one or more structural elements. Examples are (Named) Entities or Multi-word Expressions, Dependency Relations, and many others. FoLiA implements these as a stand-off layer that refers back to the structural elements (often words/tokens). The layer itself is embedded in a structural level of a wider scope (such as a sentence).
   - :ref:`syntax_annotation` -- ``<su>`` -- Assign grammatical categories to spans of words. Syntactic units are nestable and allow representation of complete syntax trees that are usually the result of consistuency parsing.
   - :ref:`chunking_annotation` -- ``<chunk>`` -- Assigns shallow grammatical categories to spans of words. Unlike syntax annotation, chunks are not nestable. They are often produced by a process called Shallow Parsing, or alternatively, chunking.
   - :ref:`entity_annotation` -- ``<entity>`` -- Entity annotation is a broad and common category in FoLiA. It is used for specifying all kinds of multi-word expressions, including but not limited to named entities. The set definition used determines the vocabulary and therefore the precise nature of the entity annotation.
   - :ref:`dependency_annotation` -- ``<dependency>`` -- Dependency relations are syntactic relations between spans of tokens. A dependency relation takes a particular class and consists of a single head component and a single dependent component.
   - :ref:`timesegment_annotation` -- ``<timesegment>`` -- FoLiA supports time segmentation to allow for more fine-grained control of timing information by associating spans of words/tokens with exact timestamps. It can provide a more linguistic alternative to `Event Annotation`.
   - :ref:`coreference_annotation` -- ``<coreferencechain>`` -- Relations between words that refer to the same referent (anaphora) are expressed in FoLiA using Coreference Annotation. The co-reference relations are expressed by specifying the entire chain in which all links are coreferent.
   - :ref:`semrole_annotation` -- ``<semrole>`` -- This span annotation type allows for the expression of semantic roles, or thematic roles. It is often used together with `Predicate Annotation`
   - :ref:`predicate_annotation` -- ``<predicate>`` -- Allows annotation of predicates, this annotation type is usually used together with Semantic Role Annotation. The types of predicates are defined by a user-defined set definition.
   - :ref:`observation_annotation` -- ``<observation>`` -- Observation annotation is used to make an observation pertaining to one or more word tokens.  Observations offer a an external qualification on part of a text. The qualification is expressed by the class, in turn defined by a set. The precise semantics of the observation depends on the user-defined set.
   - :ref:`sentiment_annotation` -- ``<sentiment>`` -- Sentiment analysis marks subjective information such as sentiments or attitudes expressed in text. The sentiments/attitudes are defined by a user-defined set definition.
   - :ref:`statement_annotation` -- ``<statement>`` -- Statement annotation, sometimes also refered to as attribution, allows to decompose statements into the source of the statement, the content of the statement, and the way these relate, provided these are made explicit in the text.
   - :ref:`modality_annotation` -- ``<modality>`` -- Modality annotation is used to describe the relationship between cue word(s) and the scope it covers. It is primarily used for the annotation of negation, but also for the annotation of factuality, certainty and truthfulness:.
* :ref:`subtoken_annotation_category` --
  This category contains morphological annotation and phonological annotation, i.e. the segmentation of a word into morphemes and phonemes, and recursively so if desired. It is a special category that mixes characteristics from structure annotation (the ``morpheme`` and ``phoneme`` elements are very structure-like) and also from span annotation, as morphemes and phonemes are embedded in an annotation layer and refer back to the text/phonetic content they apply to. Like words/tokens, these elements may also be referenced from ``wref`` elements.
   - :ref:`morphological_annotation` -- ``<morpheme>`` -- Morphological Annotation allows splitting a word/token into morphemes, morphemes itself may be nested. It is embedded within a layer ``morphology`` which can be embedded within word/tokens.
   - :ref:`phonological_annotation` -- ``<phoneme>`` -- The smallest unit of annotatable speech in FoLiA is the phoneme level. The phoneme element is a form of structure annotation used for phonemes.  Alike to morphology, it is embedded within a layer ``phonology`` which can be embedded within word/tokens.
* :ref:`textmarkup_annotation_category` --
  The text content element (``<t>``) allows within its scope elements of a this category; these are **Text Markup** elements, they always contain textual content and apply a certain markup to certain spans of the text. One of it's common uses is for styling (emphasis, underlines, etc.). Text markup elements may be nested.
   - :ref:`style_annotation` -- ``<t-style>`` -- This is a text markup annotation type for applying styling to text. The actual styling is defined by the user-defined set definition and can for example included classes such as italics, bold, underline
   - :ref:`hyphenation_annotation` -- ``<t-hbr>`` -- This is a text-markup annotation form that indicates where in the original text a linebreak was inserted and a word was hyphenised.
   - :ref:`hspace_annotation` -- ``<t-hspace>`` -- Markup annotation introducing horizontal whitespace
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


.. for sphinx TOC discovery:


.. toctree::
    :maxdepth: 3
    :includehidden:
    :hidden:
    :glob:

    *annotation_category
