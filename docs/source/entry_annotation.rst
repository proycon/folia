.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _entry_annotation:

Entry Annotation
==================================================================

.. foliaspec:annotationtype_description(entry)
FoLiA has a set of structure elements that can be used to represent collections such as glossaries, dictionaries, thesauri, and wordnets. `Entry annotation` defines the entries in such collections, `Term annotation` defines the terms, and `Definition Annotation` provides the definitions.

In this documentation we cover all four annotation types, as they are intimately connected.

Specification
---------------

.. foliaspec:specification(entry)
:Annotation Category: :ref:`structure_annotation_category`
:Declaration: ``<entry-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Version History: since v0.12
:**Element**: ``<entry>``
:API Class: ``Entry``
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``space`` -- This attribute indicates whether spacing should be inserted after this element (it's default value is always ``yes``, so it does not need to be specified in that case), but if tokens or other structural elements are glued together then the value should be set to ``no``. This allows for reconstruction of the detokenised original text. 
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<def>`` (:ref:`definition_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<part>`` (:ref:`part_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<str>`` (:ref:`string_annotation`), ``<term>`` (:ref:`term_annotation`), ``<t>`` (:ref:`text_annotation`)
:Valid Context: ``<div>`` (:ref:`division_annotation`), ``<event>`` (:ref:`event_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<s>`` (:ref:`sentence_annotation`)

.. foliaspec:specification(term)
:Annotation Category: :ref:`structure_annotation_category`
:Declaration: ``<term-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Version History: since v0.12
:**Element**: ``<term>``
:API Class: ``Term``
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``space`` -- This attribute indicates whether spacing should be inserted after this element (it's default value is always ``yes``, so it does not need to be specified in that case), but if tokens or other structural elements are glued together then the value should be set to ``no``. This allows for reconstruction of the detokenised original text. 
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<event>`` (:ref:`event_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<gap>`` (:ref:`gap_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<ph>`` (:ref:`phon_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<str>`` (:ref:`string_annotation`), ``<table>`` (:ref:`table_annotation`), ``<t>`` (:ref:`text_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)
:Valid Context: ``<entry>`` (:ref:`entry_annotation`)

.. foliaspec:specification(definition)
:Annotation Category: :ref:`structure_annotation_category`
:Declaration: ``<definition-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Version History: since v0.12
:**Element**: ``<def>``
:API Class: ``Definition``
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``space`` -- This attribute indicates whether spacing should be inserted after this element (it's default value is always ``yes``, so it does not need to be specified in that case), but if tokens or other structural elements are glued together then the value should be set to ``no``. This allows for reconstruction of the detokenised original text. 
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<ph>`` (:ref:`phon_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<str>`` (:ref:`string_annotation`), ``<table>`` (:ref:`table_annotation`), ``<t>`` (:ref:`text_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)
:Valid Context: ``<entry>`` (:ref:`entry_annotation`)

.. foliaspec:specification(example)
:Annotation Category: :ref:`structure_annotation_category`
:Declaration: ``<example-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Version History: since v0.12
:**Element**: ``<ex>``
:API Class: ``Example``
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``space`` -- This attribute indicates whether spacing should be inserted after this element (it's default value is always ``yes``, so it does not need to be specified in that case), but if tokens or other structural elements are glued together then the value should be set to ``no``. This allows for reconstruction of the detokenised original text. 
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<ph>`` (:ref:`phon_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<str>`` (:ref:`string_annotation`), ``<table>`` (:ref:`table_annotation`), ``<t>`` (:ref:`text_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)
:Valid Context: ``<div>`` (:ref:`division_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<event>`` (:ref:`event_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<s>`` (:ref:`sentence_annotation`)

Explanation
-------------------------

Collections such as glossaries, dictionaries, thesauri and wordnets have in common that they consist of a set of
entries, which is represented in FoLiA by the ``<entry>`` element, and each entry is identified by one or more terms,
represented by the ``<term>`` element within an entry.

Terms need not be words, but a wide variety of structural elements can be used
as the term. Within the entry, these terms can subsequently be associated with
one or more definitions, using the ``<def>`` element, or with examples,
using the ``<ex>`` element.

The ``<term>``, ``<def>`` and ``<ex>`` elements can all take sets and
classes, and thus need to be declared. The ``<entry>`` elements themselves
are simple containers and can contain multiple
terms if they are deemed dependent or related, such as in case of morphological
variants such as verb conjugations and declensions. The elements ``<term>``
and ``<def>`` can only be used within an ``<entry>``. The ``<ex>``
element, however, can also be used standalone in different contexts.

In FoLiA, linguistic annotations are associated with the structure element
within the term itself. This is where a glossary can for instance obtain
part-of-speech or lexical semantic sense information, to name just a few
examples.

Below you see an example of a glossary entry, the sense set used comes from WordNet. The other sets are fictitious.

.. code-block:: xml

   <entry xml:id="entry.1">
    <term xml:id="entry.1.term.1">
     <w xml:id="entry.1.term.1.w.1">
       <t>house</t>
       <pos class="n">
         <feat subset="number" class="sing" />
       </pos>
       <lemma class="house" />
       <sense class="house\%1:06:00::">
     </w>
    </term>
    <term xml:id="entry.1.term.2">
     <w xml:id="entry.1.term.2.w.1">
       <t>houses/t>
       <pos class="n">
         <feat subset="number" class="plural" />
       </pos>
       <lemma class="house" />
       <sense class="house\%1:06:00::">
     </w>
    </term>
    <def xml:id="entry.1.def.1" class="sensedescription">
     <p xml:id="entry.1.def.1.p.1">
       <t>A dwelling, place of residence</t>
     </p>
    </def>
    <ex>
     <s xml:id="entry.1.ex.1.s.1>
       <t>My house was constructed ten years ago.</t>
     </s>
    </ex>
   </entry>

Other semantic senses would be represented as separate entries.

The definitions (``<def>``) are a generic element that can be used for
multiple types of definition. As always, the set is not predefined and purely
fictitious in our examples, giving the user flexibility. Definitions are for
instance suited for dictionaries:

.. code-block:: xml

   <entry xml:id="entry.1">
    <term xml:id="entry.1.term.1">
     <w xml:id="entry.1.term.1.w.1">
       <t>house</t>
       <pos set="englishpos" class="n">
         <feat subset="number" class="sing" />
       </pos>
       <lemma set="englishlemma" class="house" />
       <sense set="englishsense" class="house\%1:06:00::">
     </w>
    </term>
    <def xml:id="entry.1.def.1" class="translation-es">
     <w xml:id="entry.1.def.1.w.1">
       <t>casa</t>
       <pos set="spanishpos"  class="n">
         <feat subset="number" class="sing" />
       </pos>
       <lemma set="spanishlemma" class="casa" />
     </w>
    </def>
   </entry>

Or for etymological definitions:

.. code-block:: xml

    <def xml:id="entry.1.def.2" class="etymology">
     <p xml:id="entry.1.def.2.p.1">
      <t>Old English hus "dwelling, shelter, house," from Proto-Germanic *husan
    (cognates: Old Norse, Old Frisian hus, Dutch huis, German Haus), of unknown
    origin, perhaps connected to the root of hide (v.) [OED]. In Gothic only in
    gudhus "temple," literally "god-house;" the usual word for "house" in Gothic
    being razn.  </t>
     </p>
    </def>


The following two samples illustrate a dictionary distributed over multiple
FoLiA files, using :ref:`relation_annotation` to link the two:

English part, ``doc-english.xml`` (excerpt):

.. code-block:: xml

   <entry xml:id="en-entry.1">
    <term xml:id="en-entry.1.term.1">
     <w xml:id="en-entry.1.term.1.w.1">
       <t>house</t>
       <pos set="englishpos" class="n">
         <feat subset="number" class="sing" />
       </pos>
       <lemma set="englishlemma" class="house" />
       <sense set="englishsense" class="house\%1:06:00::">
     </w>
    </term>
    <relation class="translation-es" xlink:href="doc-spanish.xml"
       xlink:type="simple">
         <xref id="es-entry.1" type="entry" />
    </relation>
   </entry>

Spanish part, ``doc-spanish.xml`` (excerpt):

.. code-block:: xml

   <entry xml:id="es-entry.1">
    <term xml:id="es-entry.1.def.1" class="translation-es">
     <w xml:id="entry.1.def.1.w.1">
       <t>casa</t>
       <pos set="spanishpos"  class="n">
         <feat subset="number" class="sing" />
       </pos>
       <lemma set="spanishlemma" class="casa" />
     </w>
    </term>
    <relation class="translation-en" xlink:href="doc-english.xml"
       xlink:type="simple">
         <xref id="en-entry.1" type="entry" />
    </relation>
   </entry>


For simple multilingual documents, explicit relations may be too much hassle,
For situations where this seems overkill, a simple multi-document
mechanism is available. This mechanism is based purely on convention: It
assumes that structural elements that are translations simply share the same
ID. This approach is quite feasible when used on higher-level structural
elements, such as divisions, paragraphs, events or entries.
