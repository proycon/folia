.. _phonological_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(phonological)
XXX

.. foliaspec:annotationtype_description(phonological)
XXX

Specification
---------------

.. foliaspec:specification(phonological)
XXX

Explanation & Example
-------------------------

The smallest unit of annotatable speech in FoLiA is the phoneme level. The
``<phoneme>`` element is a form of subtoken annotation used for phonemes.

Very much alike to morphology, it is embedded within a layer ``<phonology>`` which can
be used within word/token elements (``<w>``) or directly within higher structure such as utterances (``<utt>``)
if no words are distinguished:


.. code-block:: xml

    <utt>
      <w xml:id="word" src="book.wav">
        <t>book</t>
        <ph>bʊk</ph>
        <phonology>
          <phoneme begintime="..."  endtime="...">
              <ph>b</ph>
          </phoneme>
          <phoneme begintime="..." endtime="...">
              <ph>ʊ</ph>
          </phoneme>
          <phoneme begintime="..." endtime="...">
              <ph>k</ph>
          </phoneme>
        </phonology>
      </w>
    </utt>


