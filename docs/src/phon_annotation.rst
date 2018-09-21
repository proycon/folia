.. _phon_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE phonetic BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

Phonetic Content
==================

.. foliaspec:annotationtype_description(phonetic)
XXX

Specification
---------------

.. foliaspec:specification(phonetic)
XXX

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

.. TODO: there is no counterpart for the textclass attribute for phonetic content

.. seealso::

    If you want to actually do segmentation into *phonemes*, see :ref:`phonological_annotation`.
