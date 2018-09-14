.. _reference_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(reference)
XXX

.. foliaspec:annotationtype_description(reference)
XXX

Specification
---------------

.. foliaspec:specification(reference)
XXX

:Extra Attributes: * ``id`` -- The ID of the element to link to
                   * ``type`` (optional) -- The type of the element that is being linked to (e.g. ``note``)

Description & Examples
-------------------------

FoLiA allows for things like footnotes and bibliography entry using :ref:`note_annotation`. In this section we show that
you can make references to these notes using the ``<ref>`` element, this is a structure element, which implies that the references are
explicitly present in the text. The ``<ref>`` element, however, carries an extra higher-order annotation function:

.. code-block:: xml
    <s>
      <t>We demonstrated this earlier.</t>
    </s>
    <ref id="mynote" />

Another example in tokenised data, and now we add the \emph{optional} \texttt{type}
attribute, which holds the type of the FoLiA element that is referred to:

.. code-block:: xml

    <s>
      <w><t>We</t></w>
      <w><t>demonstrated</t></w>
      <w><t>this</t></w>
      <w><t>earlier</t></w>
      <w><t>.</t></w>
      <ref id="mynote" type="note" />
    </s>

You can optionally make explicit the symbol used for the reference. When no
textual content is provided, whatever program renders the FoLiA document may assign its own
numbering or symbol.

.. code-block:: xml

    <s>
      <t>We demonstrated this earlier.</t>
    </s>
    <ref id="mynote" type="note"><t>1</t></ref>

This is often needed for bibliographical references:

.. code-block:: xml

    <s>
      <t>We demonstrated this earlier.</t>
    </s>
    <ref id="bib.1" type="note"><t>(van Gompel et al, 2014)</t></ref>

As a structure element, the ``<ref>`` element may contain other structure
elements such as words (:ref:`token_annotation`) or even sentences (:ref:`sentence_annotation`) or
paragraphs (:ref:`paragraph_annotation`), which can in turn contain further linguistic
annotations.

Although we framed this section in the context of notes, the ``<ref>`` element is
more general and can be used whereever you need to explicitly refer to other *structure
elements*. Common targets are figures, tables, divisions (sections, chapters,
etc).

Being a structure element, the note reference itself may carry an ID as well.
Note that the ID attribute without the xml namespace always indicates a reference
in FoLiA:

.. code-block:: xml
    <s><t>We demonstrated this earlier.</t></s>
    <ref xml:id="myreference" id="mynote" />

The difference between the reference element and the higher-order alignments
(:ref:`alignment_annotations`) needs to be clearly understood. Alignments lay
relations between annotations of any kind and thus pertain strongly to
linguistic annotation, whereas this reference element is a structural element
that is explicitly shown in the text and draws a reference that is explicitly
reflected in the text.

External references can also be made with the ``<ref>`` element, which
effectively makes it a valid tool for *hyperlinking*. This is
done by setting the ``xlink:href`` to point to the external resource and
by setting the ``format`` attribute to the format of the external
resource. The format is understood to be a MIME type and its value defaults to
``text/folia+xml``. When an external reference is made, the ``id``
attribute is optional and points to an element inside the external resource.

.. code-block:: xml
    <s>
      <w><t>We</t></w>
      <w><t>demonstrated</t></w>
      <w><t>this</t></w>
      <ref xlink:href="http://somewhere" xlink:type="simple"
        format="text/html" id="section2">
        <w><t>here</t></w>
      </ref>
      <w><t>.</t></w>
    </s>

This method of hyperlinking can be contrasted to the one described in
:ref:`hyperlinks`. The ``<ref>`` element offers a highly semantic way of
hyperlinking, whereas the other method is more of a text-markup or stylistic
nature.


.. literalinclude:: ../examples/note-reference.2.0.0.folia.xml
    :linenos:
    :language: xml


