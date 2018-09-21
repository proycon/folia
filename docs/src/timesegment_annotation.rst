.. _timesegment_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(timesegment)
XXX

.. foliaspec:annotationtype_description(timesegment)
XXX

Specification
---------------

.. foliaspec:specification(timesegment)
XXX

Explanation
-------------------------

FoLiA supports time segmentation using the ``<timing>`` layer and the
``<timesegment>`` span annotation element. This element is useful for
speech, but can also be used for event annotation. We already saw events as
structure annotation in :ref:`event_annotation`, but for more fine-grained
control of timing information a span annotation element in an offset layer is
more suited.

Time segments may also be nested. The predefined and optional
feature subset ``begindatetime`` and ``enddatetime`` can be used express
the exact moment at which an event started or ended. These too are set-defined
so the format shown here is just an example.

If you are only interested in a structural annotation of events, and a coarser level of
annotation suffices, then use :ref̋:`event_annotation`.

If used in a **speech context**, all the generic speech attributes become available
(See :ref:`speech`). This introduces ``begintime`` and
``endtime``, which are different from the ``begindatetime`` and
``enddatetime`` feature subsets introduced by this annotation type! The generic attributes ``begintime`` and
``endtime`` are not defined by a set, but specify a time location in
``HH:MM:SS.MMM`` format which may refer to the location in an associated audio
file. Audio files are associated using the ``src`` attribute, which is
inherited by all lower elements, so we put it on the sentence here.

.. seealso::

    * :ref:`event_annotation`
    * :ref:`speech`

Example
-------------------------

The following example illustrates the usage of time segmentation for event annotation:

.. literalinclude:: ../examples/timesegments-events.2.0.0.folia.xml
    :linenos:
    :language: xml

Example in a speech context
------------------------------

The following example illustrates the usage of time segmentation in a speech context. You have to be aware though, that
the ``begintime`` and ``endtime`` attributes can also be directly associated with any structure elements in a speech
context, making the use of this annotation type unnecessary or redundant if used this way.

.. literalinclude:: ../examples/timesegments-speech.2.0.0.folia.xml
    :linenos:
    :language: xml


