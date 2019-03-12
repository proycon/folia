.. _textmarkup_annotation_category:

Text Markup Annotation
===================================================================

.. foliaspec:category_description(textmarkup)
The text content element (``<t>``) allows within its scope elements of a this category; these are **Text Markup** elements, they always contain textual content and apply a certain markup to certain spans of the text. One of it's common uses is for styling (emphasis, underlines, etc.). Text markup elements may be nested.


Text markup elements may take sets and classes as most other elements, and any
of the remaining common FoLiA attributes may be freely associated with any of
the text-markup elements.

As text markup operates in the scope of the text content element, it is ideally
suited for untokenised text. You should, however, limit your usage of text
markup elements and only use them when other existing annotation elements do not
suffice, or for extra verbosity in addition to existing elements.

Each text-markup element, save for one exception, starts with ``<t-`` and
demands a declaration. The following subsections will discuss the various text
markup elements available.

Text markup elements may carry an optional identifier. However, it may happen that textual content is repeated on
multiple levels (see :ref:`text_annotation`), which implies the textual markup elements may also be repeated, but this
is not a strict requirement. However, if that is the case, only one of them may carry the customary ``xml:id``
attribute; duplicates may carry the ``id`` *reference* attribute (in the FoLiA namespace instead of the XML namespace!)
which is interpreted as a reference. Such an element should be identical to the one it refers to, and explicitly include
the value (if applicable) to facilitate the job of XML parsers. Certain elements may also use this ``id`` reference
attribute to refer to structural elements that cover the very same data. A markup element may thus take either
``xml:id`` or ``id`` (a reference to another element); they may never occur together.

FoLiA defines the following types of text markup annotation:

.. foliaspec:toc(textmarkup)
* :ref:`textmarkup_annotation_category` --
  The text content element (``<t>``) allows within its scope elements of a this category; these are **Text Markup** elements, they always contain textual content and apply a certain markup to certain spans of the text. One of it's common uses is for styling (emphasis, underlines, etc.). Text markup elements may be nested.
   - :ref:`style_annotation` -- ``<t-style>`` -- This is a text markup annotation type for applying styling to text. The actual styling is defined by the user-defined set definition and can for example included classes such as italics, bold, underline

.. foliaspec:begin:toctree(textmarkup,hidden)
.. toctree::
   :hidden:
   :maxdepth: 3

   style_annotation

.. foliaspec:end:toctree
