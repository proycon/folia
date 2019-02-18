.. _fql:

FoLiA Query Language (FQL)
=============================

.. todo:: DOCUMENT PROVENANCE

Whereas XPath is a very generic query language, the FoLiA Query Language (FQL)
is a very specific language, designed purely for FoLiA. It allows advanced querying and
document editing.

FQL statements are separated by newlines and encoded in UTF-8. The expressions
are case sensitive, all keywords are in upper case, all element names and
attributes in lower case.

FQL is also strict about parentheses, they are generally either required or forbidden
for an expression. Parentheses usually indicate a sub-expression, and it is also used in
boolean logic.

As a general rule, it is more efficient to do a single big query than multiple
standalone queries.

Note that for readability, queries may have been split on multiple lines
in the presentation here, whereas in reality they should be on one.

Global variables
-------------------

* ``SET variable$=$value`` - Sets global variables that apply to all statements that follow. String values need to be in double quotes. Available variables are:
  * ``processor`` - The ID of the processor
  * ``annotator`` - The name of the annotator (the use of ``processor`` is preferred!)
  * ``annotatortype`` - The type of the annotator, can be *auto* or *manual* (the use of ``processor`` is preferred!)


Usually your queries on a particular annotation type are limited to one
specific set. To prevent having to enter the set explicitly in your queries,
you can set defaults. The annotation type corresponds to a FoLiA element::

    DEFAULTSET entity https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/namedentitycorrection.foliaset.xml

If the FoLiA document only has one set of that type anyway, then this is not even
necessary and the default will be automatically set.

Provenance
----------------

To make use of FoLiA's ability to register :ref:`provenance_data`, you need to define a processor as follows::

    PROCESSOR id = "p0" name = "mytool" type = "auto"

If you do not specify an ID manually one will be generated automatically. If the ID already exists, the existing one
will be selected and modified. Any subsequent queries will be made using this processor.

To add subprocessors under the currently selected processor, use ``PROCESSOR SUB`` instead of ``PROCESSOR``. The
subprocessor will again be automatically selected for all subsequent queries (except if it has ``type = "generator"``). Example::

    PROCESSOR name = "annotationtool" type = "auto"
    PROCESSOR SUB name = "john doe" type = "manual"

You can select the parent processor again with the ``PROCESSOR PARENT`` directive, or if you know the ID you can always
use ``PROCESSOR id = "id"``, be aware that multiple calls to ``PROCESSOR SUB``
would cause ever deeper nesting. To deselect a processor, use ``PROCESSOR NONE``.


Declarations
----------------

All annotation types in FoLiA need to be declared. FQL does this for you automatically. If you make an edit of a
previously undeclared set, it will be declared for you. These default declarations will never assign default annotators
or annotator types, and if a *PROCESSOR* statement was issued earlier, it will use that processor.

Explicit declarations are possible using the *DECLARE* keyword followed by
the annotation type you want to declare, this represented the tag of the
respective FoLiA annotation element::

    DECLARE entity OF "https://github.com/proycon/folia/blob/master/setdefinitions/namedentities.foliaset.xml"

The *WITH* clause is optional, the set following the *OF* keyword is mandatory for annotation types where you use a set.

Declarations may be chained, i.e. multiple *DECLARE* statements may be issued
on one line, as well as prepended to action statements (see next section).


.. note::

    If you don't intend to use FoLiA v2's provenance mechanism, i.e. processors, then you can declare default annotators
    and annotator types the old way::

        DECLARE entity OF "https://github.com/proycon/folia/blob/master/setdefinitions/namedentities.foliaset.xml"
        WITH annotator = "me" annotatortype = "manual"

    Note that the statement must be on one single line, it is split here only for ease of
    presentation.





.. _fel_actions:

Actions
----------

The core part of an FQL statement consists of an action verb, the following are
available:

* ``SELECT <focus expression> [<target expression>]`` - Selects an annotation
* ``DELETE <focus expression> [<target expression>]`` - Deletes an annotation
* ``EDIT <focus expression> [<assignment expression>]`` ``[<target expression>]`` - Edits an existing annotation
* ``ADD <focus expression> <assignment expression> <target expression>`` - Adds an annotation (to the target expression)
* ``APPEND <focus expression> <assignment expression> <target expression>`` - Inserts an annotation after the target expression
* ``PREPEND <focus expression> <assignment expression> <target expression>`` - Inserts an annotation before the target expression

Following the action verb is the focus expression, this starts with an
annotation type, which is equal to the FoLiA XML element tag. The set is
specified using ``OF <set>`` and/or the ID with ``ID <id>``. An example::

    pos OF "http://some.domain/some.folia.set.xml"

If an annotation type is already declared and there is only one in document, or
if the *DEFAULTSET* statement was used earlier, then the *OF* statement can
be omitted and will be implied and detected automatically. If it is ambiguous,
an error will be raised (rather than applying the query regardless of set).

To further filter a the focus, the expression may consist of a *WHERE* clause
that filters on one or more FoLiA attributes:

* ``class``
* ``annotator``
* ``annotatortype``
* ``n``
* ``confidence``
* ``src``
* ``speaker``
* ``begintime``
* ``endtime``

The following keywords are also available on when the elements contains text
and/or phonetic/phonological content:

* ``text``
* ``phon``

The *WHERE* statement requires an operator (``=``,``!=``,``>``,``<``,``<=``,``>=``,``CONTAINS``,``MATCHES``), the *AND*,
*OR* and *NOT* operators are available (along with parentheses) for
grouping and boolean logic. The operators must never be glued to the attribute
name or the value, but have spaces left and right.

We can now show some examples of full FQL queries with some operators:

* ``SELECT pos OF "http://some.domain/some.folia.set.xml"``
* ``SELECT pos WHERE class = "n" AND annotator = "johndoe"``
* ``DELETE pos WHERE class = "n" AND annotator != "johndoe"``
* ``DELETE pos WHERE class = "n" AND annotator CONTAINS "john"``
* ``DELETE pos WHERE class = "n" AND annotator MATCHES "^john$"``

The *ADD* and *EDIT* change actual attributes, this is done in the
*assignment expression* that starts with the *WITH* keyword. It applies to
all the common FoLiA attributes like the *WHERE* keyword, but has no operator or
boolean logic, as it is a pure assignment function.

SELECT and DELETE only support WHERE, EDIT supports both WHERE and WITH, if
both are use they than WHERE is always before WITH. the ADD action supports only WITH. If
an EDIT is done on an annotation that can not be found, and there is no WHERE
clause, then it will fall back to ADD.

Here is an *EDIT* query that changes all nouns in the document to verbs (assuming a particular set):

* ``EDIT pos WHERE class = "n" WITH class "v" AND annotator = "johndoe"``

The query is fairly crude as it still lacks a *target expression*: A \emph{target
expression} determines what elements the focus is applied to, rather than to
the document as a whole, it starts with the keyword *FOR* and is followed by
either an annotation type (i.e. a FoLiA XML element tag) *or* the ID of an
element. The target expression also determines what elements will be returned.
More on this in a later section.

The following FQL query shows how to get the part of speech tag for a
word::

    SELECT pos FOR ID mydocument.word.3

Or for all words::

    SELECT pos FOR w

The *ADD* action almost always requires a target expression::

    ADD pos WITH class "n" FOR ID mydocument.word.3

Multiple targets may be specified, comma delimited::

    ADD pos WITH class "n" FOR ID mydocument.word.3  , ID myword.document.word.25

The target expression can again contain a *WHERE* filter::

    SELECT pos FOR w WHERE class != "PUNCT"

Target expressions, starting with the *FOR* keyword, can be nested::

    SELECT pos FOR w WHERE class != "PUNCT" FOR event WHERE class = "tweet"

You may also use the SELECT keyword without focus expression, but only with a target expression. This is particularly useful when you want to return multiple distinct elements, for instance by ID::

    SELECT FOR ID mydocument.word.3 , ID myword.document.word.25

The *SELECT* keyword can also be used with the special *ALL* selector that selects all elemens in the scope, the following two statement are identical and will return all elements in the document::

    SELECT ALL
    SELECT FOR ALL

It can be used at deeper levels too, the following will return everything under all words::

    SELECT ALL FOR w

Target expressions are vital for span annotation, the keyword *SPAN* indicates
that the target is a span (to do multiple spans at once, repeat the SPAN
keyword again), the operator ``&`` is used for consecutive spans, whereas ``,``
is used for disjoint spans::

    ADD entity WITH class "person" FOR SPAN ID mydocument.word.3 & ID myword.document.word.25

This works with filters too, the ``&`` operator enforced a single consecutive span::

    ADD entity WITH class "person" FOR SPAN w WHERE text = "John" & w WHERE text = "Doe"

Remember we can do multiple at once::

    ADD entity WITH class "person" FOR SPAN w WHERE text = "John" & w WHERE text = "Doe"
    SPAN w WHERE text = "Jane" & w WHERE text = "Doe"

The *HAS* keyword enables you to descend down in the document tree to
siblings.  Consider the following example that changes the part of speech tag
to "verb", for all occurrences of words that have lemma "fly". The parentheses
are mandatory for a *HAS* statement::

    EDIT pos OF "someposset" WITH class = "v" FOR w WHERE (lemma OF "somelemmaset" HAS class "fly")

Target expressions can be former with either *FOR* or with *IN*, the
difference is that *IN* is much stricter, the element has to be a direct
child of the element in the *IN* statement, whereas *FOR* may skip
intermediate elements. In analogy with XPath, *FOR* corresponds to \texttt{//} and
*IN* corresponds to ``/``. *FOR* and *IN* may be nested and mixed at
will. The following query would most likely not yield any results because there are
likely to be paragraphs and/or sentences between the wod and event structures::

    SELECT pos FOR w WHERE class != "PUNCT" IN event WHERE class = "tweet"

Multiple actions can be combined, all share the same target expressions::

    ADD pos WITH class "n" ADD lemma WITH class "house" FOR w WHERE text = "house" OR text = "houses"

It is also possible to nest actions, use parentheses for this, the nesting
occurs after any WHERE and WITH statements::

    ADD w ID mydoc.sentence.1.word.1 (ADD t WITH text "house" ADD pos WITH class "n") FOR ID mydoc.sentence.1

Though explicitly specified here, IDs will be automatically generated when necessary and not specified.

The *ADD* action has two cousins: *APPEND* and *PREPEND*.
Instead of adding something in the scope of the target expression, they either append
or prepend an element, so the inserted element will be a sibling::

    APPEND w (ADD t WITH text "house") FOR w WHERE text = "the"

This above query appends/inserts the word "house" after every definite article.

Text
---------

Our previous examples mostly focussed on part-of-speech annotation. In this
section we look at text content, which in FoLiA is an annotation element too
(t).

Here we change the text of a word::

    EDIT t WITH text = "house" FOR ID mydoc.word.45

Here we edit or add (recall that EDIT falls back to ADD when not found and
there is no further selector) a lemma and check on text content::

    EDIT lemma WITH class "house" FOR w WHERE text = "house" OR text = "houses"

You can use WHERE text on all elements, it will cover both explicit text
content as well as implicit text content, i.e. inferred from child elements. If
you want to be really explicit you can do::

    EDIT lemma WITH class "house" FOR w WHERE (t HAS text = "house")

*Advanced*:

Such syntax is required when covering texts with custom classes, such as
OCRed or otherwise pre-normalised text. Consider the following OCR correction::

    ADD t WITH text = "spell" FOR w WHERE (t HAS text = "5pe11" AND class = "OCR" )


Query Response
--------------------

We have shown how to do queries but not yet said anything on how the response is
returned. This is regulated using the *RETURN* keyword:

* ``RETURN focus`` (default)
* ``RETURN parent`` - Returns the parent of the focus
* ``RETURN target`` or ``RETURN inner-target``
* ``RETURN outer-target``
* ``RETURN ancestor-target``

The default focus mode just returns the focus. Sometimes, however, you may want
more context and may want to return the target expression instead. In the
following example returning only the pos-tag would not be so interesting, you
are most likely interested in the word to which it applies::

    SELECT pos WHERE class = "n" FOR w RETURN target

When there are nested FOR/IN loops, you can specify whether you want to return
the inner one (highest granularity, default) or the outer one (widest scope).
You can also decide to return the first common structural ancestor of the
(outer) targets, which may be specially useful in combination with the *SPAN}
keyword.

The return type can be set using the *FORMAT* statement:

* ``FORMAT xml`` - Returns FoLiA XML, the response is contained in a simple ``<results><result/></results>`` structure.
* ``FORMAT single-xml`` - Like above, but returns pure unwrapped FoLiA XML and therefore only works if the response only contains one element. An error will be raised otherwise.
* ``FORMAT json`` - Returns JSON list
* ``FORMAT single-json`` - Like above, but returns a single element rather than a list. An error will be raised if the response contains multiple.
* ``FORMAT python`` - Returns a Python object, can only be used when directly querying the FQL library without the document server
* ``FORMAT flat`` -  Returns a parsed format optimised for FLAT. This is a JSON reply containing an HTML skeleton of structure elements (key html), parsed annotations (key annotations). If the query returns a full FoLiA document, then the JSON object will include parsed set definitions, (key setdefinitions), and declarations.

The *RETURN* statement may be used standalone or appended to a query, in
which case it applies to all subsequent queries. The same applies to the
*FORMAT* statement, though an error will be raised if distinct formats are
requested in the same HTTP request.

When context is returned in *target* mode, this can get quite big, you may
constrain the type of elements returned by using the *REQUEST* keyword, it
takes the names of FoLiA XML elements. It can be used standalone so it applies
to all subsequent queries::

    REQUEST w,t,pos,lemma

..or after a query::

    SELECT pos FOR w WHERE class!="PUNCT" FOR event WHERE class="tweet" REQUEST w,pos,lemma

Two special uses of request are ``REQUEST ALL`` (default) and ``REQUEST NOTHING``, the latter may be useful in combination with *ADD*, *EDIT* and
*DELETE*, by default it will return the updated state of the document.

Note that if you set REQUEST wrong you may quickly end up with empty results.

Span Annotation
--------------------

Selecting span annotations is identical to token annotation. You may be aware
that in FoLiA span annotation elements are technically stored in a separate
stand-off layers, but you can forget this fact when composing FQL queries and can
access them right from the elements they apply to.

The following query selects all named entities (of an actual rather than a
fictitious set for a change) of people that have the name John::

    SELECT entity OF "https://github.com/proycon/folia/blob/master/setdefinitions/namedentities.foliaset.xml"
    WHERE class = "person" FOR w WHERE text = "John"

Or consider the selection of noun-phrase syntactic units (su) that contain the
word house::

    SELECT su WHERE class = "np" FOR w WHERE text CONTAINS "house"

Note that if the *SPAN} keyword were used here, the selection would be
exclusively constrained to single words "John"::

    SELECT entity WHERE class = "person" FOR SPAN w WHERE text = "John"

We can use that construct to select all people named John Doe for instance::

    SELECT entity WHERE class = "person" FOR SPAN w WHERE text = "John" & w WHERE text = "Doe"

Span annotations like syntactic units are typically nested trees, a tree query
such as "//pp/np/adj" can be represented as follows. Recall that the *IN*
statement starts a target expression like *FOR*, but is stricter on the
hierarchy, which is what we would want here::

    SELECT su WHERE class = "adj" IN su WHERE class = "np" IN su WHERE class = "pp"

In such instances we may be most interested in obtaining the full PP::

    SELECT su WHERE class = "adj" IN su WHERE class = "np" IN su WHERE class = "pp" RETURN outer-target

The *EDIT* action is not limited to editing attributes, sometimes you
want to alter the element of a span. A separate *RESPAN* keyword (without
FOR/IN/WITH) accomplishes this. It takes the keyword *RESPAN* which behaves the
same as a *FOR SPAN* target expression and represents the new scope of the
span, the normal target expression represents the old scope::

    EDIT entity WHERE class= "person" RESPAN ID word.1 & ID word.2 FOR SPAN ID word.1 & ID word.2 & ID word.3

*WITH* statements can be used still too, they always preceed *RESPAN*::

    EDIT entity WHERE class= "person" WITH class="location" RESPAN ID word.1 & ID word.2 FOR SPAN ID word.1 & ID word.2 & ID word.3


Corrections and Alternatives
--------------------------------

Both FoLiA and FQL have explicit support for corrections and alternatives on
annotations. A correction is not a blunt substitute of an annotation of any
type, but the original is preserved as well. Similarly, an alternative
annotation is one that exists alongside the actual annotation of the same type
and set, and is not authoritative.

The following example is a correction but not in the FoLiA sense, it bluntly changes part-of-speech
annotation of all occurrences of the word *fly* from *n* to *v*, for example to
correct erroneous tagger output::

    EDIT pos WITH class "v" WHERE class = "n" FOR w WHERE text = "fly"

Now we do the same but as an explicit correction::

    EDIT pos WITH class "v" WHERE class = "n" (AS CORRECTION OF "some/correctionset" WITH class "wrongpos")
    FOR w WHERE text = "fly"

Another example in a spelling correction context, we correct the misspelling
*concous* to *conscious*::

    EDIT t WITH text "conscious" (AS CORRECTION OF "some/correctionset" WITH class "spellingerror")
    FOR w WHERE text = "concous"

The *AS CORRECTION* keyword (always in a separate block within parentheses) is used to
initiate a correction. The correction is itself part of a set with a class that
indicates the type of correction.

Alternatives are simpler, but follow the same principle::

    EDIT pos WITH class "v" WHERE class = "n" (AS ALTERNATIVE) FOR w WHERE text = "fly"

Confidence scores are often associationed with alternatives::

    EDIT pos WITH class "v" WHERE class = "n" (AS ALTERNATIVE WITH confidence 0.6)
    FOR w WHERE text = "fly"

The *AS* clause is also used to select alternatives rather than the
authoritative form, this will get all alternative pos tags for words with the
text "fly"::

    SELECT pos (AS ALTERNATIVE) FOR w WHERE text = "fly"

If you want the authoritative tag as well, you can chain the actions. The
same target expression (FOR..) always applies to all chained actions, but the AS clause
applies only to the action in the scope of which it appears::

    SELECT pos SELECT pos (AS ALTERNATIVE) FOR w WHERE text = "fly"

Filters on the alternative themselves may be applied as expected using the WHERE clause::

    SELECT pos (AS ALTERNATIVE WHERE confidence > 0.6) FOR w WHERE text = "fly"

Note that filtering on the attributes of the annotation itself is outside of the scope of
the AS clause::

    SELECT pos WHERE class = "n" (AS ALTERNATIVE WHERE confidence > 0.6) FOR w WHERE text = "fly"

Corrections by definition are authoritative, so no special syntax is needed to
obtain them. Assuming the part of speech tag is corrected, this will
correctly obtain it, no AS clause is necessary::

    SELECT pos FOR w WHERE text = "fly"

Adding *AS CORRECTION* will only enforce to return those that were actually
corrected::

    SELECT pos (AS CORRECTION) FOR w WHERE text = "fly"

However, if you want to obtain the original prior to correction, you can do so
using *AS CORRECTION ORIGINAL*::

    SELECT pos (AS CORRECTION ORIGINAL) FOR w WHERE text = "fly"

FoLiA does not just distinguish corrections, but also supports suggestions for
correction. Envision a spelling checker suggesting output for misspelled
words, but leaving it up to the user which of the suggestions to accept.
Suggestions are not authoritative and can be obtained in a similar fashion
by using the *SUGGESTION* keyword::

    SELECT pos (AS CORRECTION SUGGESTION) FOR w WHERE text = "fly"

Note that *AS CORRECTION* may take the *OF* keyword to
specify the correction set, they may also take a *WHERE* clause to filter::

    SELECT t (AS CORRECTION OF "some/correctionset" WHERE class = "confusible") FOR w

The *SUGGESTION* keyword can take a WHERE filter too::

    SELECT t (AS CORRECTION OF "some/correctionset" WHERE class = "confusible" SUGGESTION WHERE confidence > 0.5) FOR w

To add a suggestion for correction rather than an actual authoritative
correction, you can do::

    EDIT pos (AS CORRECTION OF "some/correctionset" WITH class "poscorrection" SUGGESTION class "n") FOR w ID some.word.1

The absence of a WITH statement in the action clause indicates that this is
purely a suggestion. The actual suggestion follows the *SUGGESTION*
keyword.

Any attributes associated with the suggestion can be set with a *WITH*
statement after the suggestion::

    EDIT pos (AS CORRECTION OF "some/correctionset" WITH class "poscorrection" SUGGESTION class "n" WITH confidence 0.8) FOR w ID some.word.1

Even if a *WITH* statement is present for the action, making it an actual
correction, you can still add suggestions::

    EDIT pos WITH class "v" (AS CORRECTION OF "some/correctionset" WITH class "poscorrection" SUGGESTION class "n" WITH confidence 0.8) FOR w ID some.word.1

The *SUGGESTION* keyword can be chaineed to add multiple suggestions at once::

    EDIT pos (AS CORRECTION OF "some/correctionset" WITH class "poscorrection"
    SUGGESTION class "n" WITH confidence 0.8
    SUGGESTION class "v" wITH confidence 0.2) FOR w ID some.word.1

Another example in a spelling correction context::

    EDIT t (AS CORRECTION OF "some/correctionset" WITH class "spellingerror"
    SUGGESTION text "conscious" WITH confidence 0.8 SUGGESTION text "couscous" WITH confidence 0.2)
    FOR w WHERE text = "concous"

A similar construction is available for alternatives as well. First we
establish that the following two statements are identical::

    EDIT pos WHERE class = "n" WITH class "v" (AS ALTERNATIVE WITH confidence 0.6) FOR w WHERE text = "fly"
    EDIT pos WHERE class = "n" (AS ALTERNATIVE class "v" WITH confidence 0.6) FOR w WHERE text = "fly"

Specifying multiple alternatives is then done by simply adding enother
*ALTERNATIVE* clause::

    EDIT pos (AS ALTERNATIVE class "v" WITH confidence 0.6 ALTERNATIVE class "n" WITH confidence 0.4 ) FOR w WHERE text = "fly"

When a correction is made on an element, all annotations below it (recursively) are left
intact, i.e. they are copied from the original element to the new correct element. The
same applies to suggestions.  Moreover, all references to the original element,
from for instance span annotation elements, will be made into references to the
new corrected elements.

This is not always what you want, if you want the correction not to have any
annotations inherited from the original, simply use *AS BARE CORRECTION* instead of *AS
CORRECTION*.

You can also use *AS CORRECTION* with *ADD* and *DELETE*.

The most complex kind of corrections are splits and merges. A split separates a
structure element such as a word into multiple, a merge unifies multiple
structure elements into one.

In FQL, this is achieved through substitution, using the action *SUBSTITUTE*::

    SUBSTITUTE w WITH text "together" FOR SPAN w WHERE text="to" & w WHERE text="gether"

Subactions are common with SUBSTITUTE, the following is equivalent to the above::

    SUBSTITUTE w (ADD t WITH text "together") FOR SPAN w WHERE text="to" & w WHERE text="gether"

To perform a split into multiple substitutes, simply chain the SUBSTITUTE
clause::

    SUBSTITUTE w WITH text "each" SUBSTITUTE w WITH TEXT "other" FOR w WHERE text="eachother"

Like *ADD*, both *SUBSTITUTE* may take assignments (*WITH*), but no filters (*WHERE*).

You may have noticed that the merge and split examples were not corrections in
the FoLiA-sense; the originals are removed and not preserved. Let's make it
into proper corrections::

    SUBSTITUTE w WITH text "together"
    (AS CORRECTION OF "some/correctionset" WITH class "spliterror")
    FOR SPAN w WHERE text="to" & w WHERE text="gether"

And a split::

    SUBSTITUTE w WITH text "each" SUBSTITUTE w WITH text "other"
    (AS CORRECTION OF "some/correctionset WITH class "runonerror")
    FOR w WHERE text="eachother"

To make this into a suggestion for correction instead, use the *SUGGESTION}
folloed by  *SUBSTITUTE*,  inside the *AS* clause, where the chain of substitute statements has to be enclosed in parentheses::

    SUBSTITUTE (AS CORRECTION OF "some/correctionset" WITH class "runonerror" SUGGESTION (SUBTITUTE w WITH text "each" SUBSTITUTE w WITH text "other") )
    FOR w WHERE text="eachother"


Dealing with context
------------------------

We have seen that with the *FOR* keyword we can move to bigger elements in the FoLiA
document, and with the *HAS* keyword we can move to siblings. There are
several *context keywords* that give us all the tools we need to peek at the
context. Like *HAS* expressions, these need always be enclosed in
parentheses.

For instance, consider a part-of-speech tagging scenario. If we have a word where
the left neighbour is a determiner, and the right neighbour a noun, we can be
pretty sure the word under our consideration (our target expression) is an
adjective. Let's add the pos tag::

    EDIT pos WITH class = "adj" FOR w WHERE (PREVIOUS w WHERE (pos HAS class == "det")) AND (NEXT w WHERE (pos HAS class == "n"))

You may append a number directly to the *PREVIOUS*/*NEXT* modifier if
you're interested in further context, or you may use
*LEFTCONTEXT*/*RIGHTCONTEXT*/*CONTEXT* if you don't care at what position
something occurs::

    EDIT pos WITH class = "adj" FOR w WHERE (PREVIOUS2 w WHERE (pos HAS class == "det")) AND (PREVIOUS w WHERE (pos HAS class == "adj")) AND (RIGHTCONTEXT w WHERE (pos HAS class == "n"))

Instead of the *NEXT* and *PREVIOUS* keywords, a target expression can be used with the *SPAN* keyword and  the *&* operator::

    SELECT FOR SPAN w WHERE text = "the" & w WHERE (pos HAS class == "adj") & w WHERE text = "house"

Within a *SPAN* keyword, an *expansion expression* can be used to select
any number, or a certain number, of elements. You can do this by appending
curly braces after the element name (but not attached to it) and specifying the
minimum and maximum number of elements. The following expression selects from
zero up to three adjectives between the words *the* and *house*::

    SELECT FOR SPAN w WHERE text = "the" & w {0,3} WHERE (pos HAS class == "adj") & w WHERE text = "house"

If you specify only a single number in the curly braces, it will require that
exact number of elements. To match at least one word up to an unlimited number,
use an expansion expression such as ``{1,}``

If you are now perhaps tempted to use the FoLiA document server and FQL for searching through
large corpora in real-time, then be advised that this is not a good idea. It will be prohibitively
slow on large datasets as this requires smart indexing, which this document
server does not provide. You can therefore not do this real-time, but perhaps
only as a first step to build an actual search index.

Other modifiers are PARENT and and ANCESTOR. PARENT will at most go one element
up, whereas ANCESTOR will go on to the largest element::

    SELECT lemma FOR w WHERE (PARENT s WHERE  text CONTAINS "wine")

Instead of *PARENT*, the use of a nested *FOR* is preferred and more efficient::

    SELECT lemma FOR w FOR s WHERE text CONTAINS "wine"

Let's revisit syntax trees for a bit now we know how to obtain context. Imagine
we want an NP to the left of a PP::

    SELECT su WHERE class = "np" AND (NEXT su WHERE class = "pp")

... and where the whole thing is part of a VP::

    SELECT su WHERE class = "np" AND (NEXT su WHERE class = "pp") IN su WHERE class = "vp"

... and return that whole tree rather than just the NP we were looking for::

    SELECT su WHERE class = "np" AND (NEXT su WHERE class = "pp") IN su WHERE class = "vp" RETURN target


.. _fql_shortcuts:

Shortcuts
-----------

Classes are prevalent all throughout FoLiA, it is very common to want to select
on classes. To select words with pos tag ``n`` for example you can do::

    SELECT w WHERE (pos HAS class = "n")

Because this is so common, there is a shortcut. Specify the annotation type
directly preceeded by a colon, and a HAS statement that matches on class will
automatically be constructed::

    SELECT w WHERE :pos = "n"

The two statements are completely equivalent.

Another third alternative to obtain the same result set is to use a target
expression::

    SELECT pos WHERE class = "n" FOR w RETURN target

This illustrates that there are often multiple ways of obtaining the same
result set. Due to lazy evaluation in the FQL library, there is not much
difference performance-wise.

Another kind of shortcut exists for setting text on structural elements. The
explicit procedure to add a word goes as follows::

    ADD w (ADD t WITH text "hello") IN ID some.sentence

The shortcut is::

    ADD w WITH text "hello" IN ID some.sentence
