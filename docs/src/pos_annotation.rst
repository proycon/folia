.. _pos_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(pos)
XXX

.. foliaspec:annotationtype_description(pos)
XXX

Specification
---------------

.. foliaspec:specification(pos)
XXX

Explanation & Examples
-------------------------

Part-of-Speech annotation allows the annotation of lexical categories using the
``pos`` element. The following example shows a simple part-of-speech annotation. In this example , we declare PoS annotation to use the
tagset from the brown corpus (although we do not have an actual set definition for it).

.. literalinclude:: ../examples/pos.2.0.0.folia.xml
    :linenos:
    :language: xml

Lexical annotation can take more complex forms than assignment of a single part-of-speech tag. There may for example be
numerous features associated with the part-of-speech tag, such as gender, number, case, tense, mood, etc... FoLiA
introduces a special paradigm for dealing with such features. This is described in :ref:`features`, please ensure you
are familiar with this before reading the remainder of this section.

Two scenarios can be envisioned, one in
which the class of the ``pos`` element encodes all features, and one in
which it is the foundation upon which is expanded. Which one is used is
entirely up to the defined set.

Option one:

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.2">
        <t>boot</t>
        <pos head="N" class="N(singular)">
            <feat subset="number" class="singular" />
            <feat subset="gender" class="none" />
            <feat subset="case" class="none" />
        </pos>
    </w>

In FoLiA, this attribute ``head`` is a *predefined subset* for PoS-annotation, i.e. the subset is commonly used and has
clear semantics; however, it still needs to be defined in the set definition. We can use such *predefined subsets* as
XML attributes.

Option two:

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.2">
        <t>boot</t>
        <pos class="N">
            <feat subset="number" class="singular" />
            <feat subset="gender" class="none" />
            <feat subset="case" class="none" />
        </pos>
    </w>

The last examples demonstrates a full FoLiA document with part-of-speech tagging with features:

.. literalinclude:: ../examples/pos-features.2.0.0.folia.xml
    :linenos:
    :language: xml


