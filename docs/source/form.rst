.. _form:

Form
======================

In addition to the normal form of FoLiA XML, there is an additional *explicit* form. This form of XML serialisation is
functionally equivalent to the normal form, but any defaults that are implicit in the normal form are expressed
explicitly instead. Documents in either form can always be converted to eachother without any gain or loss of
information, it is just the accessibility of the certain information that is facilitated in explicit mode, at the cost
of redundancy, bigger filesize and higher memory footprint.

The reason for the existance of this explicit form is to help parsers, especially those not implementing the full FoLiA
logic. Parsers that can not deal with a document in normal form should themselves invoke ``foliavalidator --explicit`` to do
the conversion to explicit form prior to parsing it themselves.

The explicit form is declared by the attribute ``form="explicit"`` on the FoLiA root tag. When this form attribute is not set to explicit (or absent) altogether, behaviour is unchanged and normal form is used.

In explicit form, all defaults are made explicit:

-  All annotations that carry a set have a set attribute, sets never refer to aliases.
-  All annotations associated with a processor have an explicit processor attribute.
-  Layers themsleves carry a set attribute if the span elements within carry a set.
-  All text-content elements explicitly declare their class (so ``<t>`` will become ``<t class="current">``)
-  Predefined features/subsets are serialised explicitly using ``<feat>`` elements rather than as XML attributes.

Certain FoLiA internals are made explicit:

- All annotation elements get a ``typegroup`` attribute that makes explicit what kind of annotation element we are dealing with. Values are: *structure, inline, span, higherorder, textmarkup, content, layer*. So ``<w>`` becomes ``<w typegroup="structure">``, ``<pos>`` becomes ``<pos typegroup="inline">``. This allows for example xpath expressions like: give me the deepest structural ancestor.


