.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _correction_annotation:

Correction Annotation
==================================================================

.. foliaspec:annotationtype_description(correction)
Corrections are one of the most complex annotation types in FoLiA. Corrections can be applied not just over text, but over any type of structure annotation, inline annotation or span annotation. Corrections explicitly preserve the original, and recursively so if corrections are done over other corrections.

Specification
---------------

.. foliaspec:specification(correction)
:Annotation Category: :ref:`higherorder_annotation_category`
:Declaration: ``<correction-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Version History: Since v0.4
:**Element**: ``<correction>``
:API Class: ``Correction``
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
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<errordetection>`` (:ref:`errordetection_annotation`), ``<metric>`` (:ref:`metric_annotation`)
:Valid Context: ``<alt>`` (:ref:`alternative_annotation`), ``<chunking>`` (:ref:`chunking_annotation`), ``<coreferences>`` (:ref:`coreference_annotation`), ``<def>`` (:ref:`definition_annotation`), ``<dependencies>`` (:ref:`dependency_annotation`), ``<div>`` (:ref:`division_annotation`), ``<entities>`` (:ref:`entity_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<head>`` (:ref:`head_annotation`), ``<t-hbr>`` (:ref:`hyphenation_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<list>`` (:ref:`list_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<morphology>`` (:ref:`morphological_annotation`), ``<note>`` (:ref:`note_annotation`), ``<observations>`` (:ref:`observation_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<phonology>`` (:ref:`phonological_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<semroles>`` (:ref:`semrole_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<sentiments>`` (:ref:`sentiment_annotation`), ``<spanrelations>`` (:ref:`spanrelation_annotation`), ``<statements>`` (:ref:`statement_annotation`), ``<str>`` (:ref:`string_annotation`), ``<syntax>`` (:ref:`syntax_annotation`), ``<table>`` (:ref:`table_annotation`), ``<term>`` (:ref:`term_annotation`), ``<timing>`` (:ref:`timesegment_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)

Explanation & Examples
-------------------------

Correction annotation is arguably one of the most complex annotation forms in FoLiA. It is a form of
:ref:`higherorder_annotation_category` which allows to annotate corrections on many types of annotation, including correction of text (i.e. spelling correction), of :ref:`inline_annotation_category`, :ref:`span_annotation_category` and even over :ref:`structure_annotation_category`.

All corrections are annotated using the ``<correction>`` element. The following example shows a
spelling correction of the misspelled word *treee* to its corrected form *tree*.


.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.1">
        <correction xml:id="TEST-000000001.p.1.s.1.w.1.c.1"
         class="spelling">
            <new>
                <t>tree</t>
            </new>
            <original>
                <t>treee</t>
            </original>
        </correction>
    </w>

The class indicates the kind of correction, according to a user-defined set definition (see :ref:`set_definitions`). The
``<new>`` element holds the actual content of the correction. The
``<original>`` element holds the content prior to correction.  In this example, what we are
correcting is the actual textual content (:ref:`text_annotation`, ``<t>``).

Corrections can be nested and we want to retain a full back-log. The following
example illustrates the word *treee* that has been first mis-corrected to
*three* and subsequently corrected again to *tree*:

.. literalinclude:: ../../examples/corrections-spelling-nested.2.0.0.folia.xml
    :linenos:
    :language: xml

In the examples above what we corrected was the actual textual content
(``<t>``). However, it is also possible to correct other annotations in exactly the same way.
The next example corrects a part-of-speech tag:

.. literalinclude:: ../../examples/corrections-pos.2.0.0.folia.xml
    :linenos:
    :language: xml

Error detection
------------------

.. seealso::

    The correction of an error implies the detection of an error. In some cases,
    detection comes without correction and without suggestions for correction, for instance when the generation of
    correction suggestions is postponed to a later processing stage. You can use :ref:`observation_annotation` to mark
    errors.

Suggestions for correction
------------------------------

The ``<correction>`` element can also be used in such situations in which you want to
list *suggestions for correction*, but not yet commit to any single one. You may
for example want to postpone this actual selection to another module or human
annotator. The output of a speller check is typically a suggestion for
correction. Recall that the actual correction is always included in the ``<new>``
tag, non-committing suggestions are included in the ``<suggestion>`` tag. All
suggestions may take an ID and may specify an annotator/processor.

Suggestions never take sets or classes by themselves, the class and set pertain
to the correction as a whole, and apply to all suggestions within. This implies
that you will need *multiple* correction elements if you want to make suggestions
of very distinct types. The following example shows two suggestions for
spelling correction:

.. literalinclude:: ../../examples/corrections-spelling-suggestions.2.0.0.folia.xml
    :linenos:
    :language: xml

In the situation above we have a possible correction with two suggestions, none
of which has been selected yet. The actual text remains unmodified so there are
no ``<new>`` or ``<original>`` tags.

When an actual correction is made, the correction element changes. It may still
retain the list of suggestions. In the following example, a human annotator
named John Doe took one of the suggestions and made the actual correction:

.. code-block:: xml

    <w>
        <correction xml:id="example.correction.1" class="spelling" processor="johndoe">
            <new>
                <t>tree</t>
            </new>
            <suggestion confidence="0.8" processor="spellingcorrector">
                <t>tree</t>
            </suggestion>
            <suggestion confidence="0.2" processor="spellingcorrector">
                <t>three</t>
            </suggestion>
            <original>
                <t>treee</t>
            </original>
        </correction>
    </w>

Structural corrections: Merges, splits and swaps
----------------------------------------------------

Sometimes in the context of spelling correction, one wants to merge multiple tokens into one single new token, or the
other way around; split one token into multiple new ones. The FoLiA format does not allow you to simply create new
tokens and reassign identifiers. Identifiers are by definition permanent and should never change, as this would break
backward compatibility. So such a change is therefore by definition a correction, and one uses the ``<correction>``
element to merge and split tokens.

We will first demonstrate a merge of two tokens (*on line*) into one
(*online*). The original tokens are always retained within the ``<original>``
element. First a peek at the XML prior to merging:

.. code-block:: xml

    <s xml:id="example.p.1.s.1">
        <w xml:id="example.p.1.s.1.w.1">
            <t>on</t>
        </w>
        <w xml:id="example.p.1.s.1.w.2">
            <t>line</t>
        </w>
    </s>

And after merging:

.. code-block:: xml

    <s xml:id="example.p.1.s.1">
     <correction xml:id="example.p.1.s.1.c.1" class="merge">
        <new>
            <w xml:id="example.p.1.s.1.w.1-2">
                <t>online</t>
            </w>
        </new>
        <original>
            <w xml:id="example.p.1.s.1.w.1">
                <t>on</t>
            </w>
            <w xml:id="example.p.1.s.1.w.2">
                <t>line</t>
            </w>
        </original>
     </correction>
    </s>

Note that the correction element here is a member of the sentence (``<s>``),
rather than the word token (``<w>``) as in all previous examples.  The
class, as always, is just a fictitious example and users can assign their own
according to their own sets.

Now we will look at a split, the reverse of the above situation. Prior to
splitting, assume we have:

.. code-block:: xml

    <s xml:id="example.p.1.s.1">
     <w xml:id="example.p.1.s.1.w.1">
        <t>online</t>
     </w>
    </s>

After splitting:

.. code-block:: xml

    <s xml:id="example.p.1.s.1">
     <correction xml:id="example.p.1.s.1.c.1" class="split">
        <new>
            <w xml:id="example.p.1.s.1.w.1_1">
                <t>on</t>
            </w>
            <w xml:id="example.p.1.s.1.w.1_2">
                <t>line</t>
            </w>
        </new>
        <original>
            <w xml:id="example.p.1.s.1.w.1">
                <t>online</t>
            </w>
        </original>
     </correction>
    </s>

The same principle as used for merges and splits can also be used for performing *swap* corrections:

.. code-block:: xml

    <s xml:id="example.p.1.s.1">
     <correction xml:id="example.p.1.s.1.c.1" class="swap">
        <new>
            <w xml:id="example.p.1.s.1.w.2_1">
                <t>on</t>
            </w>
            <w xml:id="example.p.1.s.1.w.1_2">
                <t>line</t>
            </w>
        </new>
        <original auth="no">
            <w xml:id="example.p.1.s.1.w.1">
                <t>line</t>
            </w>
            <w xml:id="example.p.1.s.1.w.2">
                <t>on</t>
            </w>
        </original>
     </correction>
    </s>

Note that in such a swap situation, the identifiers of the swapped tokens
tokens are new. They are essentially copies of the originals. Likewise, any
token annotations you want to preserve explicitly need to be copies.

Insertions and Deletions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Insertions are words that are omitted in the original and have to be inserted in
correction, while deletions are words that are erroneously inserted in the
original and have to be removed in correction. FoLiA deals with these in a
similar way to merges, splits and swaps. For deletions, the  ``<new>``
element is simply empty. In the following example the word *the* was
duplicated and removed in correction:


.. code-block:: xml

    <s xml:id="example.p.1.s.1">
     <w xml:id="example.p.1.s.1.w.1">
        <t>the</t>
     </w>
     <correction xml:id="example.p.1.s.1.c.1" class="duplicate">
        <new/>
        <original>
            <w xml:id="example.p.1.s.1.w.2">
                <t>the</t>
            </w>
        </original>
     </correction>
     <w xml:id="example.p.1.s.1.w.3">
        <t>man</t>
     </w>
    </s>

For insertions, the ``<original>`` element is empty:

.. code-block:: xml

    <s xml:id="example.p.1.s.1">
     <w xml:id="example.p.1.s.1.w.1">
        <t>the</t>
     </w>
     <correction xml:id="example.p.1.s.1.c.1" class="duplicate">
        <new>
            <w xml:id="example.p.1.s.1.w.1_1">
                <t>old</t>
            </w>
        </new>
        <original />
     </correction>
     <w xml:id="example.p.1.s.1.w.2">
        <t>man</t>
     </w>
    </s>

Although we limited our discussion to merges, splits, insertions and deletions
applied to words/tokens, they may be applied to any other structural element
just as well.

Suggestions for correction: structural changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The earlier described suggestions for correction can be extended to merges,
splits, insertions and deletions as well. This is done by embedding the newly
suggested structure in ``<suggestion>`` elements. The current version of the
structure is moved to within the scope of a ``<current>`` element.

We illustrate the splitting of online to on line as a suggestion for
correction:

.. code-block:: xml

    <s xml:id="example.p.1.s.1">
     <correction xml:id="example.p.1.s.1.c.1" class="split">
        <current>
            <w xml:id="example.p.1.s.1.w.1">
                <t>online</t>
            </w>
        </current>
        <suggestion>
            <w xml:id="example.p.1.s.1.w.1_1">
                <t>on</t>
            </w>
            <w xml:id="example.p.1.s.1.w.1_2">
                <t>line</t>
            </w>
        </suggestion>
     </correction>
    </s>

Special cases are insertions and deletions. In case of suggested insertions, the current
element is empty (but always present!), in case of deletions, the suggestion
element is empty (but always present!).

For non-structural suggestions for correction, we simply have multiple
correction elements if there are suggestions for correction of different
classes. When structural changes are proposed, however, this is not possible,
as there can be only one ``<current>`` element. The remedy here is to nest
corrections, a current element may hold a correction with its own current
element, and so on.

We can use suggestions for correction on any structural level; so we can for
instance embed entire sentences or paragraphs within a suggestion. However,
this quickly becomes very verbose and redundant as all the lower levels are
copied for each suggestion. Common structural changes, as we have seen, are
splits and merges. The ``<suggestion>`` element has a special additional
facility to signal splits and merges, using the ``split`` and
``merge`` attribute, the value of which points to the ID (or IDs, space
delimited) of the elements to split or merge with. When applied to sentences, splits
and merges often coincide with an insertion of punctuation (for a sentence
split), or deletion of redundant punctuation (for a sentence merge). The
following two examples illustrate both these cases:

.. code-block:: xml

  <p xml:id="correctionexample.p.2">
      <s xml:id="correctionexample.p.2.s.1">
          <w xml:id="correctionexample.p.2.s.1.w.1"><t>I</t></w>
          <w xml:id="correctionexample.p.2.s.1.w.2"><t>think</t></w>
          <correction xml:id="correctionexample.p.2.correction.1" class="redundantpunctuation">
              <suggestion merge="correctionexample.p.2.s.2" />
              <current>
                  <w xml:id="correctionexample.p.2.s.1.w.3"><t>.</t></w>
              </current>
          </correction>
      </s>
      <s xml:id="correctionexample.p.2.s.2">
          <w xml:id="correctionexample.p.2.s.2.w.1"><t>and</t></w>
          <w xml:id="correctionexample.p.2.s.2.w.2"><t>therefore</t></w>
          <w xml:id="correctionexample.p.2.s.2.w.3"><t>I</t></w>
          <w xml:id="correctionexample.p.2.s.2.w.4"><t>am</t></w>
          <w xml:id="correctionexample.p.2.s.2.w.5"><t>.</t></w>
      </s>
  </p>

.. code-block:: xml

  <p xml:id="correctionexample.p.2">
      <s xml:id="correctionexample.p.2.s.1">
          <w xml:id="correctionexample.p.2.s.1.w.1"><t>I</t></w>
          <w xml:id="correctionexample.p.2.s.1.w.2"><t>go</t></w>
          <w xml:id="correctionexample.p.2.s.1.w.3"><t>home</t></w>
          <correction xml:id="correctionexample.p.2.correction.1" class="missingpunctuation">
              <suggestion split="correctionexample.p.2.s.1">
                  <w xml:id="correctionexample.p.2.s.1.w.3a"><t>.</t></w>
              </suggestion>
              <current />
          </correction>
          <w xml:id="correctionexample.p.2.s.1.w.4">
            <t>you</t>
            <correction xml:id="correctionexample.p.2.correction.2" class="capitalizationerror">
              <suggestion>
                <t>You</t>
              </suggestion>
            </correction>
          </w>
          <w xml:id="correctionexample.p.2.s.1.w.5"><t>welcome</t></w>
          <w xml:id="correctionexample.p.2.s.1.w.6"><t>me</t></w>
          <w xml:id="correctionexample.p.2.s.1.w.7"><t>.</t></w>
      </s>
  </p>

In the second example, we also add an additional non-structural suggestion for correction,
suggesting to capitalize the first word of what is suggested to become a new sentence.

