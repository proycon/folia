.. _hyperlinks:

Hyperlinks
====================================================

Hyperlinks are ubiquitous in documents from the web and are therefore supported
in FoLiA as well. A hyperlink can be defined as a pointer from a span of text to an
external resource. In FoLiA, this method is therefore implemented as a simple property
on :ref:`text_annotation` itself. Text content elements (``<t>``) as well as any Text Markup
elements that may be contained therein (``<t-*>``), may act as a hyperlink. The link
itself is implemented through XLink semantics:

.. code-block:: xml

   <s>
    <w><t>The</t></w>
    <w><t>FoLiA</t></w>
    <w><t>website</t></w>
    <w><t>is</t></w>
    <w><t xlink:type="simple" xlink:href="https://proycon.github.io/folia">here</t></w>
    <w><t>.</t></w>
   </s>

Or on a substring (see :ref:`string_annotation`) in untokenised text:

.. code-block:: xml

   <s>
    <t>The FoLiA website is <t-str xlink:type="simple"
    xlink:href="https://proycon.github.io/folia">here</t-str>.</t>
   </s>

Before using this, make sure to investigate :ref:`reference_annotation` as
well. There we describe a more semantic way of hyperlinking, which uses
references (``<ref>`` elements) that are actual structure elements. The
hyperlinking method described in this section is of a more text-mark-up or stylistic
nature. Actual references are usually preferred when applicable.

Another notion of linking is implemented using FoLiA's *relations* (:ref:`relation_annotation`).  Relations are actual
higher-order annotations that can link anything but it needs not be reflected in the actual text, whereas the hyperlinks
described here and the references of :ref:`reference_annotation` do always show in the text.

