.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _text_annotation:

Text Annotation
==================================================================

.. foliaspec:annotationtype_description(text)
Text annotation associates actual textual content with structural elements, without it a document would be textless. FoLiA treats it as an annotation like any other.

Specification
---------------

.. foliaspec:specification(text)
:Annotation Category: :ref:`content_annotation_category`
:Declaration: ``<text-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: Since the beginning, revised since v0.6
:**Element**: ``<t>``
:API Class: ``TextContent`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.TextContent.html>`_)
:Required Attributes: 
:Optional Attributes: * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``tag`` -- Contains a space separated list of processing tags associated with the element. A processing tag carries arbitrary user-defined information that may aid in processing a document. It may carry cues on how a specific tool should treat a specific element. The tag vocabulary is specific to the tool that processes the document. Tags carry no instrinsic meaning for the data representation and should not be used except to inform/aid processors in their task. Processors are encouraged to clean up the tags they use. Ideally, published FoLiA documents at the end of a processing pipeline carry no further tags. For encoding actual data, use ``class`` and optionally features instead.
                      * ``xlink:href`` -- Turns this element into a hyperlink to the specified URL
                      * ``xlink:type`` -- The type of link (you'll want to use ``simple`` in almost all cases).
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<br>`` (:ref:`linebreak_annotation`)
:Valid Context: ``<current>`` (:ref:`correction_annotation`), ``<def>`` (:ref:`definition_annotation`), ``<div>`` (:ref:`division_annotation`), ``<entry>`` (:ref:`entry_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<list>`` (:ref:`list_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<new>`` (:ref:`correction_annotation`), ``<note>`` (:ref:`note_annotation`), ``<original>`` (:ref:`correction_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<str>`` (:ref:`string_annotation`), ``<suggestion>`` (:ref:`correction_annotation`), ``<term>`` (:ref:`term_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<w>`` (:ref:`token_annotation`)

Explanation
-------------------------

Text is considered an annotation like any other rather than a given in FoLiA, but it is ubiquitous in almost all FoLiA
documents, as a document without text is a rare occurrence. Text content is always represented by the ``<t>`` element
and can be associated with :ref:`structure_annotation_category` and :ref:`subtoken_annotation_category`. Consider text
associated with a words in a sentence:

.. code-block:: xml

    <s xml:id="s.1">
        <w xml:id="s.1.w.1">
            <t>Hello</t>
        </w>
        <w xml:id="s.1.w.2">
            <t>world</t>
        </w>
    </s>

FoLiA is not just a format for holding tokenised text, although tokenisation is a prerequisite for most all kinds of
linguistic annotation. We can associate text content with a sentence as such:

.. code-block:: xml

    <s xml:id="s.1">
        <t>Hello world</t>
    </s>

Untokenised FoLiA documents with text on higher structural levels are in fact common input to FoLiA-aware tokenisers.

As FoLiA's representation of structure is hierarchical, you can nest various structure elements, but at the same time you
can also associate text with structure elements on different levels, so specifying text on *both* the sentence and word
level is valid too:

.. code-block:: xml

    <s xml:id="s.1">
        <t>Hello world</t>
        <w xml:id="s.1.w.1">
            <t>Hello</t>
        </w>
        <w xml:id="s.1.w.2">
            <t>world</t>
        </w>
    </s>

We call the association of text content on multiple structural levels **text redundancy**, it has its uses in preserving the untokenised
original text, and facilating the job for parsers and tools.

If this kind of redundancy is used (it is not mandatory!), you may optionally
point back to the text content of its parent structure element by specifying the ``offset``
attribute:

.. code-block:: xml

 <p xml:id="example.p.1">
    <t>This is a paragraph containing only one sentence.</t>
    <s xml:id="example.p.1.s.1">
        <t offset="0">This is a paragraph containing only one sentence.</t>
        <w xml:id="example.p.1.s.1.w.1">
        	<t offset="0">This</t>
        </w>
        <w xml:id="example.p.1.s.1.w.2">
        	<t offset="5">is</t>
        </w>
        ...
        <w xml:id="example.p.1.s.1.w.8" space="no">
        	<t offset="40">sentence</t>
        </w>
        <w xml:id="example.p.1.s.1.w.9">
        	<t offset="48">.</t>
        </w>
    </s>
 </p>


.. note::

    Offsets in FoLiA are always zero indexed (i.e, the first offset is zero, not one) and count unicode codepoints (as opposed to bytes).
    Offsets always refer to a specific `normalized form <http://www.unicode.org/reports/tr15/`_ of the text:  Unicode Normal Form Composed (NFC). This affects how certain characters (notably those with diacritics) are encoded. FoLiA libraries should take care of this for you automatically.


Offsets can be used to refer back from deeper text-content elements. This does imply
that there are some challenges to solve: First of all, by default, the offset
refers to the first structural parent of whatever text-supporting element the text
content (``<t>``) is a member of. If a level is missing we have to
explicitly specify this reference using the ``ref`` attribute. We show this in the following example, where
there is no text content for the sentence, and we refer directly to the paragraph's text:

.. code-block:: xml

 <p xml:id="example.p.1">
    <t>Hello. This is a sentence. Bye!</t>
    <s xml:id="example.p.1.s.1">
        <w xml:id="example.p.1.s.1.w.1">
         <t ref="example.p.1" offset="7">This</t>
        </w>
        <w xml:id="example.p.1.s.1.w.2">
         <t ref="example.p.1" offset="12">is</t>
        </w>
        <w xml:id="example.p.1.s.1.w.3">
         <t ref="example.p.1" offset="15">a</t>
        </w>
        <w xml:id="example.p.1.s.1.w.4" space="no">
         <t ref="example.p.1" offset="17">sentence</t>
        </w>
        <w xml:id="example.p.1.s.1.w.5">
         <t ref="example.p.1" offset="25">.</t>
        </w>
    </s>
 </p>

Text content is by default expected to be untokenised for higher-level structure; in ``w`` structure elements it by
definition is tokenised, as that is precisely what provides the tokenisation layer. Text content elements may *never* be
empty nor contain only whitespace or non-printable characters, in such circumstances you simply omit the text-content
element altogether.

The notion of text redundancy can be useful but also creates room for error, the text on a higher level may not
correspond with the text on a deeper level, as in the following *erroneous example*:

.. code-block:: xml

    <s xml:id="s.1">
        <t>Goodbye world</t>
        <w xml:id="s.1.w.1">
            <t>Hello</t>
        </w>
        <w xml:id="s.1.w.2">
            <t>world</t>
        </w>
    </s>

FoLiA validators (since version 1.5) will not accept this and produce a *text consistency error*, so this is invalid
FoLiA and should be rejected. Similar text consistency errors occur if you specify offsets that are incorrect.

Whitespace
--------------------------

Leading and trailing whitespace within a text content element is not significant (since version 2.4.1 but with backward
effect). Double whitespace is collapsed to a single. As whitespace we consider spaces, tabs, newlines and carriage returns, so all of the following snippets have the identical text ``to be or not to be`` and the offset for ``To`` is 0:

.. code-block:: xml

   <t>To be or not to be</t>

   <t> To be or not to be</t>

   <t>     To be or not to be</t>

   <t>To be or not to be </t>

   <t>
    To be or not to be</t>

   <t>
    To be     or not to be</t>

   <t>To be
      or not to be</t>

   <t>
    To
    be
    or
    not
    to
    be</t>

This same principle applies to :ref:`textmarkup_annotation_category`, the following three are semantically identical:

.. code-block:: xml

    <t>To <t-style class="bold">be</t-style> or not to be</t>

    <t>To <t-style class="bold"> be </t-style> or not to be</t>

    <t>
       To
       <t-style class="bold">be</t-style>
       or not to be
    </t>

If you want to encode linebreaks, you need to explicitly use :ref:`linebreak_annotation` (``<br/>``), as otherwise it will not be significant:

.. code-block:: xml

   <t>To be<br/>
      or not to be</t>

Whitespace before explicit linebreaks is insignificant (since FoLiA v2.5.1), so the following two examples are identical to the one above:

.. code-block:: xml

   <t>To be  <br/>
      or not to be</t>

.. code-block:: xml

   <t>
      To be
      <br/>
      or not to be
   </t>


As mentioned before, empty text is explicitly forbidden in FoLiA. All of the following are identical semantically, and all will
produce an empty text error:

.. code-block:: xml

    <t></t>

    <t/>

    <t>   </t>

    <t>
    </t>

The rule here is, empty text is no text at all, so you should omit the ``<t>`` element entirely in such cases.


.. note::

    The rules regarding whitespace prior to FoLiA v2.5 and v2.4.1 were different and not as well-defined yet.

    * prior to FoLiA v2.4.1 all whitespace and linebreaks were interpreted as significant
    * since FoLiA v2.4.1 leading and trailing whitespace was stripped, but not all whitespace was collapsed yet.

    FoLiA validators will be forgiving when checking the text consistency and offsets in older FoLiA documents. The new
    rules will be applied first, but fallbacks wil test again older rules in such cases, retaining backward
    compatibility.

.. note::

    FoLiA (since v2.5) and TEI are comparable in the way they treat XML whitespace. TEI has an `elaborate article <https://wiki.tei-c.org/index.php/XML_Whitespace>`_ on the subject that may provide further insight.

.. _preserving_whitespace:

Preserving whitespace (advanced)
-------------------------------------

What if you **DO** explicitly want to encode a double space, an initial space or a trailing space? Though generally not
recommended, this may be needed if you want to stay true to the untokenised original in a very strict sense. The
You can set the ``xml:space="preserve"`` attribute on any text content or text markup element to indicate that you want
to preserve the spaces as-is. Consider the following distinct examples:

.. code-block:: xml

   <t>To be or not to be</t>

   <t xml:space="preserve">To be     or not to be</t>

Without ``xml:space="preserve"``, the texts would be identical. This attribute is automatically inherited by child elements, you will need to set ``xml:space="default"`` if you want to revert to the normal behaviour when nesting text markup.

Note that even when preserving spaces, FoLiA does not accept empty (whitespace-only) text nodes.

Instead of using ``xml:space="preserve"``, you are encouraged to use the more explicit :ref:`hspace_annotation` using
the ``<t-hspace/>`` element:

.. code-block:: xml

   <t>To be<t-hspace class="long" />or not to be</t>

.. note::

    FoLiA does not accept XML CDATA in text content or text markup elements. It will be treated as it if were normal
    text. CDATA only makes sense when used with :ref:`gap_annotation`.

.. _textclasses:

Text classes (advanced)
--------------------------

It is possible to associate **multiple text content elements** with the same
structural element, and thus associating multiple texts with the same element. You may
wonder what could possibly be the point of such extra complexity. But there is
a clear use case when dealing with for example corrections, or wanting to
associate the text version just after a processing step such as
Optical Character Recognition or any another kind of normalisation.

Text annotation, like most forms of annotations in FoLiA, is bound to the same paradigm of sets and classes. You can
assign a ``class`` to your text content. And FoLiA allows you to associate multiple text content elements of different
classes in the same structural element. Text content that has no explicitly associated class obtains the ``current`` class by
default and is the only situation in which FoLiA actually predefines a class for a set. We call it ``current`` because
it is considered the most current and up-to-date text layer, and the default unless explicitly specified otherwise. We
allow you to omit it as it is so common and for most FoLiA documents you will not make use of multiple text classes and
only use a single one.

Like all annotations, text annotation needs to be explicitly declared, declaring a ``set`` is only needed if you assign
custom classes, otherwise a built-in set that defines ``current`` will be used automatically.

Orthographical corrections (see also :ref:`correction_annotation`) are challenging because they can be applied to text content and
thus change the text. Corrections are often applied on the token level, but you may want them
propagated to the text content of sentences or paragraphs whilst at the same time wanting to retain the text how it
originally was. This can be accomplished by introducing text content of a different class.

Below is an example illustrating the usage of multiple classes, three to be precise: the default ``current`` class
showing the normal text, an ``original`` class showing text prior to correction, and a ``ocroutput`` class showing the text as
produced by an OCR engine. To show the flexibility, offsets are added, but these
are of course always optional. Note that when an offset is specified, it always refers to a text-content element of the
same class! We first give an example where the correction is implicit:

.. code-block:: xml

 <p xml:id="example.p.1">
    <t>Hello. This is a sentence. Bye!</t>
    <t class="original">Hello. This iz a sentence. Bye!</t>
    <t class="ocroutput">Hell0 Th1s iz a sentence, Bye1</t>
    <s xml:id="example.p.1.s.1">
        <t offset="7">This is a sentence.</t>
        <t class="original" offset="7">This is a sentence.</t>
        <t class="ocroutput" offset="6">Th1s iz a sentence,</t>
        <w xml:id="example.p.1.s.1.w.1">
         <t offset="0">This</t>
         <t class="ocroutput" offset="0">Th1s</t>
        </w>
        <w xml:id="example.p.1.s.1.w.2">
           <t offset="5">is</t>
           <t offset="5" class="original">iz</t>
           <t offset="5" class="ocroutput">iz</t>
        </w>
        <w xml:id="example.p.1.s.1.w.3">
         <t offset="8">a</t>
         <t offset="8" class="original">a</t>
         <t offset="8" class="ocroutput">a</t>
        </w>
        <w xml:id="example.p.1.s.1.w.4" space="no">
         <t offset="10">sentence</t>
        </w>
        <w xml:id="example.p.1.s.1.w.5">
         <t offset="48">.</t>
         <t offset="48" class="original">.</t>
         <t offset="48" class="ocroutput">,</t>
        </w>
    </s>
 </p>

Next, we give an example in which the correction is explicit, making use of :ref:`correction_annotation`, which is one of the most complex
annotation types in FoLiA. We leave out the ocr text class:


.. code-block:: xml

    <p xml:id="example.p.1">
      <t>Hello. This is a sentence. Bye!</t>
      <t class="original">Hello. This iz a sentence. Bye!</t>
      <s xml:id="example.p.1.s.1">
        <t offset="7">This is a sentence.</t>
        <t class="original" offset="7">This is a sentence.</t>
        <w xml:id="example.p.1.s.1.w.1">
          <t offset="0">This</t>
        </w>
        <w xml:id="example.p.1.s.1.w.2">
          <correction>
          <new>
            <t offset="5">is</t>
          </new>
          <original>
            <t offset="5" class="original">iz</t>
          </original>
          </correction>
        </w>
        <w xml:id="example.p.1.s.1.w.3">
          <t offset="8">a</t>
        </w>
        <w xml:id="example.p.1.s.1.w.4" space="no">
          <t offset="10">sentence</t>
        </w>
        <w xml:id="example.p.1.s.1.w.5">
          <t offset="48">.</t>
        </w>
      </s>
    </p>


.. seealso::

    * :ref:`correction_annotation`
    * :ref:`string_annotation`

.. _textclass_attribute:

Text class attribute (advanced)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So as we have just seen, FoLiA allows for multiple text content elements on the same structural elements, these other text
content elements must carry a different class. This indicates an alternative text for the same element and is used for
instance for pre-OCR vs. post-OCR or pre-normalisation vs. post-normalisation distinctions, or for
transliterations.

When adding linguistic annotations on a structure element that has multiple text representations, it may be desirable
to explicitly state which text class was used in establishing the annotation. This is done with the ``textclass``
attribute on any token or span annotation element. By default, this attribute is omitted, which implies it points to the
default ``current`` text class.

Consider the following Part-of-Speech and lemma annotation on a word with two text classes, one representing the spelling as it
occurs in the document, and one representing a more contemporary spelling. The following example makes it explicit that
the PoS and lemma annotations are based on the latter text class.

.. code-block:: xml

     <w class="WORD" xml:id="s.1.w.3">
          <t>aengename</t>
          <t class="contemporary">aangename</t>
          <pos class="ADJ" textclass="contemporary" />
          <lemma class="aangenaam" textclass="contemporary" />
     </w>

Note that if you want to add another PoS annotation or lemma that is derived from another textclass, you will need to
add those as an *alternative* (See :ref:`alternative_annotation`), as the usual restrictions apply, there can be
only one of each of a given set.

For span annotation, you can apply the ``textclass`` attribute in a similar fashion:

.. code-block:: xml

    <entities>
      <entity class="per" textclass="contemporary">
        <wref id="s.1.w.5" t="John"/>
        <wref id="s.1.w.6" t="Doe"/>
      </entity>
    </entities>

