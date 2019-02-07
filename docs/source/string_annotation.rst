.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _string_annotation:

String Annotation
==================================================================

.. foliaspec:annotationtype_description(string)
This is a form of higher-order annotation for selecting an arbitrary substring of a text, even untokenised, and allows further forms of higher-order annotation on the substring. It is also tied to a form of text markup annotation.

Specification
---------------

.. foliaspec:specification(string)
:Annotation Category: :ref:`higherorder_annotation_category`
:Declaration: ``<string-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Version History: since v0.9.1
:**Element**: ``<str>``
:API Class: ``String``
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
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<ph>`` (:ref:`phon_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<t>`` (:ref:`text_annotation`)
:Valid Context: ``<def>`` (:ref:`definition_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<figure>`` (:ref:`figure_annotation`), ``<head>`` (:ref:`head_annotation`), ``<list>`` (:ref:`list_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<term>`` (:ref:`term_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<w>`` (:ref:`token_annotation`)

Explanation
-------------

The ``<str>`` element is available in FoLiA to allow annotations on untokenised substrings. It is a higher-order
annotation element that refers to a substring of the text-content (``<t>``) element on the same level, but is specified
outside from it.

Explicitly denoting substrings in this fashion is needed when you want to associate further annotations with a
substring.  Consider the following example:


.. code-block:: xml

     <p xml:id="example.p.1">
        <t>Hello. This is a sentence. Bye!</t>
        <str xml:id="example.p.1.str.1">
            <t offset="0">Hello</t>
            <desc>This is a word of greeting</desc>
        </str>
     </p>

In substrings, using an offset attribute on the text-content element enables
substrings to be properly positioned with respect to their *parent* text.

The ``<str>`` element has a text markup (:ref:`textmarkup_annotation_category`) counterpart called ``<t-str>``. Both
share the same declaration. The text markup variant can be used in the scope of the text content itself and may be more intuitive, but it is also less flexible, as it does not allow further annotations in its scope and can not be used when substrings are overlapping, unlike ``<str>``. Consider the following example:

.. code-block:: xml

     <p xml:id="example.p.1">
        <t><t-str id="example.p.1.str.1">Hello</t-str>. This is a sentence. Bye!</t>
        <str xml:id="example.p.1.str.1">
            <t offset="0">Hello</t>
            <desc>This is a word of greeting</desc>
        </str>
     </p>

In the above example, the ``id`` parameter (distinct from ``xml:id``!) on ``<t-str>`` is a reference to the ``<str>``
element, showing how the two elements can be used in combination.

One of the features of ``<str>`` is that you can put :ref:`inline_annotation_category` in its scope, so you can
associate e.g. PoS tags and lemmas with substrings in special cases where you might need to do this. Do note that this is
**NOT** a substitute or alternative for proper tokenisation (:ref:`token_annotation`), nor :ref:`morphological_annotation`!

String elements are a form of higher-order annotation, they are similar to structure annotation but carry several
distinct properties. Unlike structure elements, substring order does not matter and substrings may overlap. The
difference between :ref:`token_annotation` (``<w>``) and string annotation (``<str>``) has to be clearly understood, the
former refers to actual tokens and supports further token annotation, the latter to untokenised or differently tokenised
substrings.The

Of course, the ``<str>`` elements themselves may carry a class, associated with a user-defined set.

Textclasses (advanced)
-------------------------

If you are familiar with :ref:`textclasses`, then it is good to know that this principle of course extends to within
substrings as well. Consider the following example with three text layers, from each of them the same substring has been extracted:


.. code-block:: xml

     <p xml:id="example.p.1">
        <t>Hello. This is a sentence. Bye!</t>
        <t class="normalised">Hello. This iz a sentence. Bye!</t>
        <t class="ocroutput">Hell0 Th1s iz a sentence, Bye1</t>

        <str xml:id="example.p.1.str.1">
            <t class="ocroutput" offset="0">Hell0</t>
        </str>

        <str xml:id="example.p.1.str.2">
            <t class="normalised" offset="0">Hello.</t>
        </str>

        <str xml:id="example.p.1.str.3">
            <t offset="0">Hello.</t>
        </str>
     </p>

Instead of three separate substrings, we can also opt for a single one. Which solution is right for you depends on your own use case:

.. code-block:: xml

     <p xml:id="example.p.1">
        <t>Hello. This is a sentence. Bye!</t>
        <t class="normalised">Hello. This iz a sentence. Bye!</t>
        <t class="ocroutput">Hell0 Th1s iz a sentence, Bye1</t>

        <str xml:id="example.p.1.str.1">
            <t class="ocroutput" offset="0">Hell0</t>
            <t class="normalised" offset="0">Hello</t>
            <t offset="0">Hello.</t>
        </str>
     </p>

Or, if you do want separate strings but you also want to make the relation between them very explicit, then you can
resort to :ref:`alignment_annotation` as shown in the next example:

.. code-block:: xml

 <p xml:id="example.p.1">
    <t>Hello. This is a sentence. Bye!</t>
    <t class="ocroutput">Hell0 Th1s iz a sentence, Bye1</t>

    <str xml:id="example.p.1.str.1">
        <t class="ocroutput" offset="0">Hell0</t>
        <alignment>
            <aref id="example.p.1.str.2" type="str" />
        </alignment>
    </str>

    <str xml:id="example.p.1.str.2">
        <t offset="0">Hello.</t>
        <alignment>
            <aref id="example.p.1.str.1" type="str" />
        </alignment>
    </str>
  </p>

The ``<str>`` element is powerful when combined with alignments, as this allows the user to
relate multiple alternative (pseudo-)tokenisations. This is also the limit as to what you can do with differing tokenisations in
FoLiA, as FoLiA only supports one authoritative tokenisation.

Example
-------------------------

The following examples combines various aspects discussed in this section:

.. literalinclude:: ../../examples/strings-alignments.2.0.0.folia.xml
    :linenos:
    :language: xml
