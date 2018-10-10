.. _phon_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE phonetic BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

Phonetic Content
==================

.. foliaspec:annotationtype_description(phon)
This is the phonetic analogy to text content (``<t>``) and allows associating a phonetic transcription with any structural element, it is often used in a speech context. Note that for actual segmentation into phonemes, FoLiA has another related type: ``Phonological Annotation``

Specification
---------------

.. foliaspec:specification(phon)
:Annotation Category: :ref:`content_annotation_category`
:Declaration: ``<phon-annotation set="...">`` *(note: ``set`` is optional for this annotation type)*
:Version History: Since v0.12
:**Element**: ``<ph>``
:API Class: ``PhonContent``
:Required Attributes: 
:Optional Attributes: * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`)
:Valid Context: ``<def>`` (:ref:`definition_annotation`), ``<div>`` (:ref:`division_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<head>`` (:ref:`head_annotation`), ``<list>`` (:ref:`list_annotation`), ``<morpheme>`` (:ref:`morphological_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<phoneme>`` (:ref:`phonological_annotation`), ``<ref>`` (:ref:`reference_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<str>`` (:ref:`string_annotation`), ``<term>`` (:ref:`term_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<w>`` (:ref:`token_annotation`)

Explanation
-------------------------

Written text is always contained in the text content element (``<t>``, see :ref:`text_content`), for
phonology there is a similar counterpart that behaves almost identically: ``<ph>``. This element
holds a phonetic or phonological transcription. It is used in a very similar fashion:

.. code-block:: xml

    <utt src="helloworld.mp3"  begintime="..." endtime="...">
        <ph>helˈoʊ wɝːld</ph>
        <w xml:id="example.utt.1.w.1" begintime="..." endtime="...">
            <ph>helˈoʊ</ph>
        </w>
        <w xml:id="example.utt.1.w.2" begintime="..." endtime="...">
            <ph>wɝːld</ph>
        </w>
    </utt>

Like the :ref:`text_annotation`, the ``<ph>`` element supports the ``offset`` attribute, referring to the offset in the
phonetic transcription for the parent structure. The first index being zero. It also support multiple classes (analogous
to text classes), the implicit default and *predefined* class being ``current``. You could imagine using this for different notation systems (IPA
, SAMPA, pinyin, etc...).

Phonetic transcription and text content can also go together without problem:

.. code-block:: xml

    <utt>
        <ph>helˈoʊ wɝːld</ph>
        <t>hello world</t>
        <w xml:id="example.utt.1.w.1">
            <ph offset="0">helˈoʊ</ph>
            <t offset="0">hello</t>
        </w>
        <w xml:id="example.utt.1.w.2">
            <ph offset="8">wɝːld</ph>
            <t offset="6">world</t>
        </w>
    </utt>

.. note::

 You should still use the normal :ref:`text_annotation` for a normal textual transcription of the speech. This
 annotation type is reserved for phonetic/phonological transcriptions.

.. TODO: there is no counterpart for the textclass attribute for phonetic content

.. seealso::

    If you want to actually do segmentation into *phonemes*, see :ref:`phonological_annotation`.
