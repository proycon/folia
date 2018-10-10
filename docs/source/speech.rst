.. _speech:

Speech
===========

FoLiA is also suited for annotation of speech data. The following additional
generic FoLiA attributes are available for *all* structure annotation elements in
a speech context:

.. foliaspec:attributes_doc(speech)
* ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
* ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
* ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
* ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.

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

Speech has its counterpart to text, in the form of a phonetic or phonological transcription, i.e. a representation of
the speech as it was pronounced/recorded. FoLiA has a separate content element for this, see :ref:`phon_annotation`. You
should still use the normal :ref:`text_annotation` for a normal textual transcription of the speech.

For further segmentation of speech into phonemes, you can use :ref:`phonological_annotation`.

