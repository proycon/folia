.. _structure_annotation_category:

Structure Annotation
===================================================================

.. foliaspec:category_description(structure)
This category encompasses annotation types that define the structure of a document, e.g. paragraphs, sentences, words, sections like chapters, lists, tables, etc... These types are not strictly considered linguistic annotation and equivalents are also commonly found in other document formats such as HTML, TEI, MarkDown, LaTeX, and others. For FoLiA it provides the necessary structural basis that linguistic annotation can build on.

FoLiA defines the following types of structure annotation:

.. foliaspec:toc(structure)
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

.. foliaspec:begin:toctree(structure,hidden)
.. toctree::
   :hidden:
   :maxdepth: 3

   token_annotation
   division_annotation
   paragraph_annotation
   head_annotation
   list_annotation
   figure_annotation
   whitespace_annotation
   linebreak_annotation
   sentence_annotation
   event_annotation
   quote_annotation
   note_annotation
   reference_annotation
   table_annotation
   part_annotation
   utterance_annotation
   entry_annotation
   term_annotation
   definition_annotation
   example_annotation
   hiddentoken_annotation

.. foliaspec:end:toctree
