Guidelines
=================

This section collects guidelines, tips, do's and don'ts and conventions in dealing with FoLiA documents.

For data creators/publishers
-------------------------------

1. **Always validate all FoLiA documents you create and intend to publish!**. Use one of the official validation tools
   (``foliavalidator`` and ``folialint``). See :ref:`validation`. This will already catch most of the issues that could
   arise out of not following these guidelines.
2. Never invent custom XML elements and attributes. If you really must, make sure they are in a different XML namespace.
   See :ref:`foreign_annotation`.
3. If you want to encode something and FoLiA does not seem to offer a good solution yet, or if you are simply unsure
   whether the solution you want to use is appropriate, contact the FoLiA developers on our `Issue tracker <https://github.com/proycon/folia/issues/>`_.
   FoLiA can be extended in collaboration. Do not simply add your own elements/attributes.
4. Mind the sets you use. Creating and publishing set definitions is recommended but not strictly mandatory for most uses. See :ref:`set_definitions`
5. Identifiers should never change: Once you assign an identifier to something and publish your data: do not change any
   identifier that is in use.
6. All annotation types you use must be declared, see :ref:`annotation_declarations`. Take care not to declare annotation types that you don't actually use in your document unless you have good reason to believe the annotation type will be added soon.

For developers
-----------------

1. Using a high-level FoLiA programming library, if available for your programming language, is strongly recommended over parsing/writing/querying the XML yourself, as it will
   make things a lot easier and save a lot of work!
2. Always use the latest version of FoLiA and its libraries.
3. Mind the sets you use. Actively check whether the sets uses in a document are in fact the ones your software handles,
   i.e. check the declarations (see :ref:`annotation_declarations`). For example, do not blindly assume any part-of-speech tag will be in your intended vocabulary. See
   :ref:`set_definitions`
4. Considering that FoLiA is vast, it is fine to only support a subset of a certain annotation types in your software,
   or not to support certain complexities such as :ref:`correction_annotation`. Just make sure to check the declarations
   based on which you can reject processing a document.
5. The structure of a text as represented in FoLiA documents can differ greatly between documents, as different types of
   documents (books,articles,papers,poetry,etc..) are structured differently. The annotation declaration in the metadata
   tell you what structural types you can encounter, but they don't convey precisely how these structures are nested. Unless you have
   very good reason to do so, do NOT assume your documents are neatly subdivided into e.g. only paragraphs and
   sentences. There may be lists, figures, divisions. Generally spoken, you'll often want to descend into the deepest
   structural nodes that have text.  The FoLiA libraries provide a high-level API for you to do this.

Conventions
-----------------------

Conventions are good practices that you will encounter and are encouraged to follow, but they remain just conventions
rather than strict guidelines.

1. Most FoLiA software assigns verbose identifiers for all elements. We use the the ID of the FoLiA
   document as the base identifier and then append the element type and sequence number, all delimited by dots. The IDs
   are cumulative in nature, so we get for instance ``example.p.1.s.2.w.3`` for the third word in the second sentence in
   the first paragraph of the document with ID ``example``. See :ref:`identifiers`
2. Adding metadata to your document is always encouraged.

