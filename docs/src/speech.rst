.. _speech:

Speech
===========

FoLiA is also suited for annotation of speech data. The following additional
generic FoLiA attributes are available for *all* structure annotation elements in
a speech context:

.. foliaspec:attributes_doc(speech)
XXX

Speech generally asks for a different document structure than text documents. The top-level element for speech-centred
resources is ``speech``, rather than ``text``. Most elements described in the section on text structure may be used
under ``speech`` as well; such as :ref:`division_annotation`, :ref:`sentence_annotation`, :ref:`token_annotation`.
Notions such as paragraphs, tables and figures make less sense in a speech context.

In a speech context, you can use :ref:`utterance_annotation` as an alternative or complement to
:ref:`sentence_annotation`, as it is often more logical to segment speech into utterances than grammatically sound
sentences.

For non-speech events, you can use :ref:`event_annotation`. Consider the following small example, with
speech-context attributes associated:

.. code-block:: xml

    <event class="cough" src="soundclip.mp3" begintime="..." endtime="..." />

If you want to associate timing information and the use of ``begintime`` and ``endtime`` on structural elements is
insufficient for your needs, then look into :ref:`timesegment_annotation`.

.. TODO: phonetic content
.. TODO: phononological annotation
