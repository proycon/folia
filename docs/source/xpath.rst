.. _xpath:

XPath
==========

Considering the fact that FoLiA is an XML-based format, XPath and its
derivatives are available as tools for searching in a FoLiA document.


Some common XPath queries are listed below, note that for the sake of brevity
and readability the namespace prefix is omitted. In actual situations you will
have to specify the FoLiA namespace with each element, as XPath unfortunately
has no notion of a default namespace.

* XPath query for all paragraphs: ``//p``
* XPath query for all sentences: ``//s``
* XPath query for all words/tokens: ``//w``
* XPath query for all words with lemma X: ``//w[.//lemma[@class="X"]``

This seems simple, but there are important caveats. When formulating XPath queries, however, one needs to be well aware
of how FoLiA works, as XPath is a generic tool that can not take care of specific FoLiA ideosyncracies for you, unlike
:ref:`fql` or the FoLiA programming libraries. These simple queries will be insufficient when dealing with a document containing
:ref:`correction_annotation`, :ref:`alternative_annotation` or even :ref:`quote_annotation`. You can rely on the
:ref:`annotation_declarations` to know whether this is the case. To formulate queries that work in all cases, you need
to be aware of the exceptions.

For example, if we query all words as ``//w`` in a document that contains structural corrections, we also get the
original words prior to correction. If we query for lemmas as ``//lemma[@class="X"]`` and our document has alternative
annotations, we may end up also getting lemmas that were specified as an alternative. This is of course fine if this is
what you want, but you need to be aware of it. A construct you will often see in FoLiA XPath Queries is
``not(ancestor-or-self::*/X)``, where X is a particular FoLiA element.

Consider the following more thought-out and more generic queries:

* XPath query for the text of all words/tokens: `//w//t[not(ancestor-or-self::*/original) and
  not(ancestor-or-self::*/suggestion) and not(ancestor-or-self::*/alt) and  not(ancestor-or-self::*/morpheme) and not(ancestor-or-self::*/str) and
  not(@class)]//text()``
    * Explanation: The ``not(@class)`` predicate is important here
    and makes sure to select only the ``current`` text content element in case there are
    multiple text content elements in different classes. (See :ref:`text_annotation`). The
    ``not(ancestor-or-self::*/morpheme`` makes sure morphemes are
    excluded, ``not(ancestor-or-self::*/str``) makes sure strings are
    excluded, ``not(ancestor-or-self::*/alt``) makes sure alternatives are excluded.
* XPath query for all words with PoS-tag A in set S: ``//w[.//pos[@set="S" and @class="A" and not(ancestor-or-self::*/original) and not(ancestor-or-self::*/suggestion) and not(ancestor-or-self::*/str) and not(ancestor-or-self(::*/morpheme)] ].``
    * Note: This query assumes the set attribute was set explicitly, i.e. there are multiple possible sets in the document for this annotation type. If there is only one set for this annotation type, it would be the default and only appear in the header's annotation declarations.
* XPath query to select all alternative PoS tags for all words: ``//w/alt/pos``
* XPath query for to obtain sentences except those in quotes: ``//s[not(ancestor::quote]``
    * Explanation: When selecting sentences, you often do not want sub-sentences that are part of a quote, since they may overlap with the larger sentence they form a part of.

When selecting text elements ``t``, you generally want to add ``not(@class)`` to the constraint, to select only the text
content elements that have not been assigned an alternative class. Recall that multiple text content may be present,
bearing another class. Omitting this constraint will prevent you from properly retrieving the current text of a
document, as it will also retrieve all this differently typed text content.

Before you release XPath queries on FoLiA documents, make sure to first parse the declarations present in the
:ref:`annotation_declarations`.  Verify that the annotation type with the desired set you are looking for is actually
present, otherwise you need not bother running a query at all. Note that the XPath expression differs based on whether
there is only one set defined for the sought annotation type, or if there are multiple. In the former case, you cannot
use the ``@set`` attribute to select, and in the latter case, you must.

As crafting good XPath queries is not trivial and requires knowledge of FoLiA, higher level abstractions are available
in the form  :ref:`fql`, or the use of dedicated FoLiA libraries.

