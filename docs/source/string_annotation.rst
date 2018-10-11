.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _string_annotation:

String Annotation
==================================================================

.. foliaspec:annotationtype_description(string)
XXX

Specification
---------------

.. foliaspec:specification(string)
XXX

Explanation
-------------

The ``<str>`` element is available in FoLiA to allow annotations on untokenised substrings. It is a higher-order
annotation element that refers to a substring of the text-content (``<t>``) element on the same level, but is specified
outside from it.

Explicitly denoting substrings in this fashion is needed when you want to associate further annotations with a
substring.  Consider the following example:


.. code-block:: xml

     <p xml:id="example.p.1">
        <t>Hello. This is a sentence. Bye!</t>
        <str xml:id="example.p.1.str.1">
            <t offset="0">Hello</t>
            <desc>This is a word of greeting</desc>
        </str>
     </p>

In substrings, using an offset attribute on the text-content element enables
substrings to be properly positioned with respect to their *parent* text.

The ``<str>`` element has a text markup (:ref:`textmarkup_annotation_category`) counterpart called ``<t-str>``. Both
share the same declaration. The text markup variant can be used in the scope of the text content itself and may be more intuitive, but it is also less flexible, as it does not allow further annotations in its scope and can not be used when substrings are overlapping, unlike ``<str>``. Consider the following example:

.. code-block:: xml

     <p xml:id="example.p.1">
        <t><t-str id="example.p.1.str.1">Hello</t-str>. This is a sentence. Bye!</t>
        <str xml:id="example.p.1.str.1">
            <t offset="0">Hello</t>
            <desc>This is a word of greeting</desc>
        </str>
     </p>

In the above example, the ``id`` parameter (distinct from ``xml:id``!) on ``<t-str>`` is a reference to the ``<str>``
element, showing how the two elements can be used in combination.

One of the features of ``<str>`` is that you can put :ref:`inline_annotation_category` in its scope, so you can
associate e.g. PoS tags and lemmas with substrings in special cases where you might need to do this. Do not that this is
**NOT** a substitute or alternative for proper tokenisation (:ref:`token_annotation`), nor :ref:`morphological_annotation`!

String elements are a form of higher-order annotation, they are similar to structure annotation but carry several
distinct properties. Unlike structure elements, substring order does not matter and substrings may overlap. The
difference between :ref:`token_annotation` (``<w>``) and string annotation (``<str>``) has to be clearly understood, the
former refers to actual tokens and supports further token annotation, the latter to untokenised or differently tokenised
substrings.The

Of course, the ``<str>`` elements themselves may carry a class, associated with a user-defined set.

Textclasses (advanced)
-------------------------

If you are familiar with :ref:`textclasses`, then it is good to know that this principle of course extends to within
substrings as well. Consider the following example with three text layers, from each of them the same substring has been extracted:


.. code-block:: xml

     <p xml:id="example.p.1">
        <t>Hello. This is a sentence. Bye!</t>
        <t class="normalised">Hello. This iz a sentence. Bye!</t>
        <t class="ocroutput">Hell0 Th1s iz a sentence, Bye1</t>

        <str xml:id="example.p.1.str.1">
            <t class="ocroutput" offset="0">Hell0</t>
        </str>

        <str xml:id="example.p.1.str.2">
            <t class="normalised" offset="0">Hello.</t>
        </str>

        <str xml:id="example.p.1.str.3">
            <t offset="0">Hello.</t>
        </str>
     </p>

Instead of three seperate substrings, we can also opt for a single one. Which solution is right for you depends on your own use case:

.. code-block:: xml

     <p xml:id="example.p.1">
        <t>Hello. This is a sentence. Bye!</t>
        <t class="normalised">Hello. This iz a sentence. Bye!</t>
        <t class="ocroutput">Hell0 Th1s iz a sentence, Bye1</t>

        <str xml:id="example.p.1.str.1">
            <t class="ocroutput" offset="0">Hell0</t>
            <t class="normalised" offset="0">Hello</t>
            <t offset="0">Hello.</t>
        </str>
     </p>

Or, if you do want seperate strings but you also want to make the relation between them very explicit, then you can
resort to :ref:`alignment_annotation` as shown in the next example:

.. code-block:: xml

 <p xml:id="example.p.1">
    <t>Hello. This is a sentence. Bye!</t>
    <t class="ocroutput">Hell0 Th1s iz a sentence, Bye1</t>

    <str xml:id="example.p.1.str.1">
        <t class="ocroutput" offset="0">Hell0</t>
        <alignment>
            <aref id="example.p.1.str.2" type="str" />
        </alignment>
    </str>

    <str xml:id="example.p.1.str.2">
        <t offset="0">Hello.</t>
        <alignment>
            <aref id="example.p.1.str.1" type="str" />
        </alignment>
    </str>
  </p>

The ``<str>`` element is powerful when combined with alignments, as this allows the user to
relate multiple alternative (pseudo-)tokenisations. This is also the limit as to what you can do with differing tokenisations in
FoLiA, as FoLiA only supports one authoritative tokenisation.

Example
-------------------------

The following examples combines various aspects discussed in this section:

.. literalinclude:: ../../examples/strings-alignments.2.0.0.folia.xml
    :linenos:
    :language: xml
