.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _gap_annotation:

Gap Annotation
==================================================================

.. foliaspec:annotationtype_description(gap)
Sometimes there are parts of a document you want to skip and not annotate at all, but include as is. This is where gap annotation comes in, the user-defined set may indicate the kind of gap. Common omissions in books are for example front-matter and back-matter, i.e. the cover.

Specification
---------------

Structure Element
~~~~~~~~~~~~~~~~~~~

.. foliaspec:specification(gap)
:Annotation Category: :ref:`higherorder_annotation_category`
:Declaration: ``<gap-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: Since the beginning
:**Element**: ``<gap>``
:API Class: ``Gap`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Gap.html>`_)
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<content>`` (:ref:`rawcontent_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<part>`` (:ref:`part_annotation`)
:Valid Context: ``<div>`` (:ref:`division_annotation`), ``<event>`` (:ref:`event_annotation`), ``<head>`` (:ref:`head_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<term>`` (:ref:`term_annotation`), ``<utt>`` (:ref:`utterance_annotation`)

Text markup Element
~~~~~~~~~~~~~~~~~~~

.. foliaspec:specification_element(TextMarkupGap)
:**Element**: ``<t-gap>``
:API Class: ``TextMarkupGap`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.TextMarkupGap.html>`_)
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
                      * ``xlink:href`` -- Turns this element into a hyperlink to the specified URL
                      * ``xlink:type`` -- The type of link (you'll want to use ``simple`` in almost all cases).
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<br>`` (:ref:`linebreak_annotation`)
:Valid Context: 

Explanation
-------------------------

Sometimes there are parts of a document you want to skip and not annotate, but include as is. For this purpose the
``<gap>`` element should be used. Gaps may have a particular class indicating the kind of gap it is, defined by a
user-defined set. Common omissions are for example front-matter and back-matter, text that is illegible/inaudible or in
a foreign language. Again, the semantics depend on your set.

Although a gap skips over content, you may still want to explicitly add the raw content, this is done with the ``<content>``
element (see :ref:`rawcontent_annotation`). As this concerns raw content, it can not be annotated any
further and we use XML CDATA type here to include it verbatim.

The following example shows the the use of ``<gap>``:

.. literalinclude:: ../../examples/gaps.2.0.0.folia.xml
    :linenos:
    :language: xml

The gap element comes in two flavours, there is not just the aforementioned structural elements but there is also a text
markup element (see :ref:`textmarkup_annotation_category`). This is the text markup element ``<t-gap>`` and it offers a
more fine-grained variant for use in untokenised text.  It indicates a gap in the textual content and is also shown in
the above example.  Either text is not available or there is a deliberate blank for, for example, fill-in exercises. It
is recommended to provide a textual value when possible, but this is not required.

If you find that you want to mark your whole
text content as being a ``<t-gap>``, then this is a sure sign you should use the
structural element ``<gap>`` instead.

.. note::

    Both elements are the same annotation type so share the same declaration.



Text Redundancy
~~~~~~~~~~~~~~~~~~

In cases of *text redundancy* (see :ref:`text_annotation`), the ``<t-gap>`` element may take an
ID reference attribute that refers to a ``gap`` element, as shown in the following
example:

.. code-block:: xml

    <s>
      <t>to <t-gap id="gap.1" class="fillin">be</t-gap> or not to be</t>
      <w><t>to</t></w>
      <gap xml:id="gap.1" class="fillin"><content>be</content></gap>
      <w><t>or</t></w>
      <w><t>not</t></w>
      <w><t>to</t></w>
      <w><t>be</t></w>
    </s>

