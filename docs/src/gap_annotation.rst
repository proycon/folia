.. _gap_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(gap)
XXX

.. foliaspec:annotationtype_description(gap)
XXX

Specification
---------------

Structure Element
~~~~~~~~~~~~~~~~~~~

.. foliaspec:specification(gap)
XXX

Text markup Element
~~~~~~~~~~~~~~~~~~~

.. foliaspec:specification_element(t-gap)
XXX

Explanation
-------------------------

Sometimes there are parts of a document you want to skip and not annotate, but include as is. For this purpose the
``<gap>`` element should be used. Gaps may have a particular class indicating the kind of gap it is, defined by a
user-defined set. Common omissions are for example front-matter and back-matter, text that is illegible/inaudible or in
a foreign language. Again, the semantics depend on your set.

Although a gap skips over content, you may still want to explicitly add the raw content, this is done with the ``<content>``
element (see :ref:`content_annotation`). As this concerns raw content, it can not be annotated any
further and we use XML CDATA type here to include it verbatim.

The following example shows the the use of ``<gap>``:

.. literalinclude:: ../examples/gaps.2.0.0.folia.xml
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

