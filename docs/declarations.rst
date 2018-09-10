Declarations
===============

Introduction
---------------

All annotation types that are used in a FoLiA document have to be *declared*. In the metadata block you will find the
``<annotations>`` block in which each annotation type that occurs in the document is mentioned, i.e. declared. So does
your document include Part of Speech tagging? Then there will be an entry declaring it does so, and linking to the set
definition used.

This allows software to identify exactly what a FoLiA document consists of without needing to go through the entire
document, on the basis of this software can determine whether it can handle the document in the first place. You can for
instance imagine an NLP tool that does Named Entity Recognition but requires Part-of-Speech tags and Lemmas to do so,
feeding it a FoLiA document without such annotation layers would then be pointless and easy to detect.
