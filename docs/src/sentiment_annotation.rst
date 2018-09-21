.. _sentiment_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(sentiment)
XXX

.. foliaspec:annotationtype_description(sentiment)
XXX

Specification
---------------

.. foliaspec:specification(sentiment)
XXX

Explanation
-------------------------

.. note::

    Please first ensure you are familiar with the general principles of :ref:`span_annotation` to make sense of this annotation type.

Sentiment analysis marks subjective information such as sentiments or attitudes
expressed in text. The ``<sentiment>`` span annotation element is used to
this end. It is embedded in a ``<sentiments>`` layer.

The ``<sentiment>`` element takes the following span roles:

* ``<hd>`` -- (required) -- The head of the sentiment; expresses the actual sentiment, it covers word spans such as ``happy'', ``very satisfied'', ``highly dissappointed''.
* ``<source>`` -- (optional) -- The source/holder of the sentiment, assuming it is explicitly expressed in the text.
* ``<target>`` -- (optional) -- The target/recipient of the sentiment, assuming it is explicitly expressed in the text.

The following feature subsets are predefined (see :ref:`features`), whether they are actually used depends on the set, their values (classes) are set-dependent as well:

* ``polarity`` -- Expresses the whether the sentiment is positive, neutral or negative.
* ``strength`` -- Expresses the strength or intensity of the sentiment.

Besides these predefined features, FoLiA's feature mechanism can be used to associate other custom properties with any sentiment.

Example
-------------------------

.. literalinclude:: ../examples/sentiments.2.0.0.folia.xml
    :linenos:
    :language: xml


