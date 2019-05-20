.. _set_definitions:

Set Definitions (Vocabulary)
==============================

Introduction
---------------

The sets and classes used by the various linguistic annotation types are never defined in the FoLiA documents
themselves, but externally in **set definitions**.

By using set definitions, a FoLiA document can be validated on a deep level, i.e.  the validity of the used classes can
be tested. Set definitions provide semantics to the FoLiA documents that use them and are an integral part of FoLiA.
When set definitions are absent, validation can only be conducted on a shallow level that is agnostic about all sets and
the classes therein.

Recall that all sets that are used need to be declared in the :ref:`annotation_declarations` section in the document
header and that they point to URLs holding a FoLiA set definitions. If no set definition files are associated, then a
full in-depth validation cannot take place.

The role of FoLiA Set Definitions is:

* to define which classes are valid in a set
* to define which subsets and classes are valid in :ref:`features` in a set
* to constrain which subsets and classes may co-occur in an annotation of the set
* to allow enumeration over classes and subsets
* to assign human-readable labels to symbolic classes
* to relate classes to external resources defining them (data category registries, linked data)
* to define a hierarchy/taxonomy of classes

Prior to FoLiA v1.4, set definitions were stored in a simple custom XML format,
distinct from FoLiA itself, which we call the legacy format and which is still
supported for backward compatibility. Since FoLiA v1.4 however, we strongly
prefer and recommend to store the set definitions as RDF [RDF_], i.e. the
technology that powers the semantic web. In this way, set definitions provide a
formal semantic layer for FoLiA.

Set definitions may be stored in various common RDF serialisation formats. The
format can be indicated on the declarations in the document metadata using the
``format`` attribute, recognised values are:

* ``application/rdf+xml`` -- XML for RDF (assumed for ``rdf.xml`` or ``rdf`` extensions
* ``text/turtle`` -- `Turtle <https://www.w3.org/TeamSubmission/turtle/>`_ (for RDF) (assumed for ``ttl`` extensions)
* ``text/n3`` -- Notation 3 (for RDF) (assumed for ``n3`` extensions)
* ``application/foliaset+xml`` - Legacy FoLiA Set Definition format (XML) (assumed for ``xml`` extensions and in most other cases)

FoLiA applications should attempt to autodetect the format based on the extension.
Not all applications may be able to deal with all formats/serialisations, however.

In this documentation, we will use the Turtle format for RDF, alongside our
older legacy format. In all cases, FoLiA requires that only one set is defined
per file, any other defined sets must be subsets of the primary set.  In our
legacy XML format, an otherwise empty set definition would look like this:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <set
     xmlns="http://ilk.uvt.nl/folia"
     xml:id="your-set-id" type="closed" label="Human readable label for your set">
    </set>

Note that the legacy XML format takes an XML namespace that is always the same
(the FoLiA namespace).

In RDF, FoLiA Set Definitions follow a particular model. The model we use is a
small superset of the SKOS model. SKOS is a W3C standard for the representation
of Simple Knowledge Organization Systems [SKOS]_. Not everything can be
expressed in the SKOS model, so we have some extensions to it which are
formally defined in our set definition schema at
https://raw.githubusercontent.com/proycon/folia/master/schemas/foliasetdefinition.ttl.
The RDF namespace for our extension is
``http://folia.science.ru.nl/setdefinition#``, for which we use the prefix
``fsd:`` generally, though this is mere convention.

Some familiarity with RDF and Turtle is recommended for this
chapter, but it is also still possible to work with the XML legacy format,
which is a bit more concise and simple, and automatically convert it to Turtle
format using our superset of the SKOS model.

Your own set definitions typically has its own RDF namespace, which in
Turtle syntax is defined by the ``@base`` directive at the top of your set
definition.

.. warning::

    Never reuse the SKOS or FoLiA Set Definition namespaces!

.. code-block:: turtle

    @base <http://your/namespace/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix fsd: <http://folia.science.ru.nl/setdefinition#> .

SKOS uses a different terminology than we do, which may be the source
of some confusion. We attempt to map the terms in the following table:

+------------------+--------------+----------------------+
| Our term         | SKOS         | SKOS class           |
+==================+==============+======================+
| Set/Subset       | Collection   | ``skos:Collection``  |
| ID               | Notation     | ``skos:notation``    |
+------------------+--------------+----------------------+

After this preamble, we can define a set as follows:

.. code-block:: turtle

    <#your-set-id>
        a skos:Collection ;
        skos:notation	"your-set-id" ;
        skos:prefLabel	"Human readable label for your set" ;
        fsd:open	false .

The first two lines state that ``http://your/namespace/#your-set-i`` is
*a* [#ftype]_ SKOS Collection, which is what we use for FoLiA Sets. The ``skos:notation``
property corresponds to the ID of the Set, only one is allowed [#fnotation]_ .

A set can be either open or closed (default), an open set allows any classes,
even if they are not defined. This can be used for open vocabularies. The
``fsd:open`` property is used to indicate this, it is not part of SKOS but
an extension of ours, hence the different namespace prefix.

.. rubric:: References

.. [RDF] Richard Cyganiak, David Wood and Markus Lanthaler (2014). RDF 1.1 Concepts and Abstract Syntax `(website) <https://www.w3.org/TR/rdf11-concepts/>`_
.. [SKOS] Alistair Miles & Sean Bechhofer (2009). SKOS: Simple Knowledge Organization System Reference `(website) <https://www.w3.org/TR/2009/REC-skos-reference-20090818/>`_

.. rubric:: Footnotes

.. [#ftype] the *a* in Turtle syntax is shorthand for ``rdf:type``
.. [#fnotation] Technically, SKOS allows multiple, but we restrict it for Set Definitions.

Classes
----------------

A set (collection in SKOS terms) consists of classes (concepts in SKOS
terms). Consider a simple part-of-speech set with three classes. First we
define the set and refer to all the classes it contains:

.. code-block:: turtle

    <#simplepos>
        a skos:Collection ;
        skos:notation	"simplepos" ;
        skos:prefLabel "A simple part of speech set" ;
        skos:member <#N> , <#V> , <#A> ;

Then we define the classes:

.. code-block:: turtle

    <#N>
        a skos:Concept ;
        skos:notation	"N" ;
        skos:prefLabel "Noun" .

    <#V>
        a skos:Concept ;
        skos:notation	"V" ;
        skos:prefLabel "Verb" .

    <#A>
        a skos:Concept ;
        skos:notation	"A" ;
        skos:prefLabel "Adjective" .

The **ID** (``skos:notation``) of the class is mandatory for FoLiA
Set Definitions and determines a value the ``class`` attribute
may take in the FoLiA document, for elements of this set. The
``skos:prefLabel`` property, both on the set itself as well as the classes, carries a human
readable description for presentational purposes, this is optional but highly
recommended.

In our legacy set definition format this is fairly straightforward and more concise:

.. code-block:: xml

    <set
      xmlns="http://ilk.uvt.nl/folia"
      xml:id="simplepos" type="closed"
      label="Simple Part-of-Speech">
      <class xml:id="N" label="Noun" />
      <class xml:id="V" label="Verb" />
      <class xml:id="A" label="Adjective" />
    </set>


Class Hierarchy
--------------------

In FoLiA Set Definitions, classes can be nested to create more complex
hierarchies or taxonomy trees, in which both nodes and leaves act as valid
classes.  This is best illustrated in our legacy XML format first. Consider the
following set definition for named entities, in which the *location* class
has been extended into more fine-grained subclasses.

.. code-block:: xml

    <set xml:id="namedentities" type="closed">
      <class xml:id="per" label="Person" />
      <class xml:id="org" label="Organisation" />
      <class xml:id="loc" label="Location">
        <class xml:id="loc.country" label="Country" />
        <class xml:id="loc.street" label="Street" />
        <class xml:id="loc.building" label="Building">
          <class xml:id="loc.building.hospital" label="Hospital" />
          <class xml:id="loc.building.church" label="Church" />
          <class xml:id="loc.building.station" label="Station" />
        </class>
      </class>
    </set>

In the SKOS model, this is more verbose as the hierarchy has to be modelled
explicitly using the ``skos:broader`` property, as shown in the following excerpt:

.. code-block:: turtle

    <#namedentities>
        a skos:Collection ;
        skos:member <#loc> , <#loc.country> .

    <#loc>
        a skos:Concept ;
        skos:notation	"loc" ;
        skos:prefLabel "Location" .

    <#loc.country>
        a skos:Concept ;
        skos:notation	"loc.country" ;
        skos:prefLabel "Country" ;
        skos:broader <#loc> .

It is recommended, but not mandatory, to set the class ID
(``skos:notation``) of any nested classes
to represent a full path, as a full path makes substring queries possible.
FoLiA, however, does not dictate this and neither does it prescribe a delimiter
for such paths, so the period in the above example (``loc.country``) is merely a convention. Each
ID, however, does have to be unique in the entire set.

Subsets
----------

.. toctree::
    :hidden:

    features

The section on :ref:`features` introduced subsets. Please ensure you are familiar with this notion before continuing
with the current section.

Subset can be defined in a similar fashion to sets. Consider the legacy XML format first:

.. code-block:: xml

    <set xml:id="simplepos" type="closed">
      <class xml:id="N" label="Noun" />
      <class xml:id="V" label="Verb" />
      <class xml:id="A" label="Adjective" />
      <subset xml:id="gender" class="closed">
          <class xml:id="m" label="Masculine" />
          <class xml:id="f" label="Feminine" />
          <class xml:id="n" label="Neuter" />
      </subset>
    </set>

In RDF, subsets are defined as SKOS Collections, just like the primary set. The primary set refers to the subsets using
the same ``skos:member`` relation as is used for classes/concepts.

.. code-block:: turtle

    <#simplepos>
        a skos:Collection ;
        skos:member <#N> , <#V> , <#A> , <#gender> .

    <#gender>
        a skos:Collection ;
        skos:notation	"gender" ;
        skos:member <#gender.m> .

    <#gender.m>
        a skos:Concept ;
        skos:notation	"m" ;
        skos:prefLabel "Location" ;

Note that in this example, we prefixed the resource name for the class
(``#gender.m`` instead of ``#m``). This is just a recommended
convention as URIs have to be unique and we may want to re-use the ``m``
ID in other subsets as well. The ID in the ``skos:notation`` property does not need to
carry this prefix, as it needs only be unique within the subset. This property
always determines how it is referenced from the FoLiA document, so we would still get
``<feat subset="gender" class="m" />``

Constraints
------------

It is possible to define constriants on which subsets can be used with which classes and which classes within subsets
can be combined, though SKOS has no mechanism to express such constraints. We introduce our own resources and properties
to define to define constraints, in the namespace of our extension ( ``http://folia.science.ru.nl/setdefinition#``, with
prefix ``fsd:`` in this documentation).

The core of the constraints is the ``fsd:constrain`` relation which can be made between any subset (``skos:Collection``)
and class (``skos:Concept``). Consider the following Part-of-Speech tag example in which we constrain the subset
*gender* to only occur with nouns:

.. code-block:: turtle

   <#simplepos>
        a skos:Collection ;
        skos:member <#N> .

   example:N a skos:Concept ;
       skos:notation "N" ;
       skos:prefLabel "Noun" .

   example:gender a skos:Collection ;
       skos:member example:masculine, example:feminine, example:neuter ;
       fsd:constrain example:N .

The same can be expressed in our legacy format as follows. Note that we left out the definition for the three genders in
the RDF example for brevity.

.. code-block:: xml

    <set xml:id="simplepos" type="closed">
       <class xml:id="N" label="Noun" />
       <subset xml:id="gender" type="closed">
         <class xml:id="masculine" label="masculine" />
         <class xml:id="feminine" label="feminine" />
         <class xml:id="neuter" label="neuter" />
         <constrain id="N" />
       </subset>
    </set>

Multiple constrain relations may be specified, but one has to be aware that this then counts as a conjunction or
intersection.  What we often see instead when multiple relations is the use of a ``fsd:Constraint`` class, which acts as
a collection of contrain relations and can explicitly express the *type* (``fsd:constraintType``) of matching to apply to the constraints. The type be any of the following:

* ``"any"`` - Only of of the constrain relations must match for the constraint to pass
* ``"all"`` - All constrain relations must match for the constraint to pass
* ``"none"`` - None of the constrain relations must match for the constraint to pass

The
other main purpose of the ``fsd:Constraint`` class is to avoid repetition, as it allows a complex contraint to be
referenced from multiple locations. Consider the following example, first in our legacy format:

.. code-block:: xml

    <set xml:id="simplepos" type="closed">
       <class xml:id="N" label="Noun" />
       <class xml:id="A" label="Adjective" />
       <class xml:id="V" label="Verb" />
       <subset xml:id="gender" type="closed">
         <class xml:id="masculine" label="masculine" />
         <class xml:id="feminine" label="feminine" />
         <class xml:id="neuter" label="neuter" />
         <constrain id="constraint.1" />
       </subset>
       <subset xml:id="case" type="closed">
         <class xml:id="nom" label="nominative" />
         <class xml:id="gen" label="geninitive" />
         <class xml:id="dat" label="dative" />
         <class xml:id="acc" label="accusative" />
         <constrain id="constraint.1" />
       </subset>
       <constraint xml:id="constraint.1" type="any">
         <constrain id="N" />
         <constrain id="A" />
       </constraint>
    </set>

In RDF, the constraint would be formulated as follows:

.. code-block:: turtle

   example:constraint.1 a fsd:Constraint ;
       fsd:constraintType "any" ;
       fsd:constrain example:N ;
       fsd:constrain example:A .

A ``fsd::constrain`` relation may be used within sets (``skos:Collection``), classes (``skos:Concept``) as well as
constraints (``fsd:Constraint``). Similary, a ``fsd:constrain`` relation may point to either of the three. All this
combined allows for complex nesting logic.


SKOS
---------

SKOS allows for more expressions to be made, and of course the full power of
open linked data is available up to be used with FoLiA Set Definitions. The
previous subsections layed out the minimal requirements for FoLiA Set
Definitions using the SKOS model.

The use of ``skos:OrderedCollection`` is currently not supported yet,
``skos:Collection`` is mandatory. Ordering of classes (SKOS Concepts) can
currently be indicated through a separate ``fsd:sequenceNumber`` property.

FoLiA Set Definitions must be *complete*, that is to say that all sets
(SKOS collections) and classes (SKOS concepts) must be fully defined in one and
the same set definition file.

.. note::

    The file need not be static but can be dynamically generated server-side; which must be *publicly* available from a
    URL. A set definition must contain one and only one primary set (SKOS collection), all other sets must be subsets
    (SKOS collections that are a member of the primary set, no deeper nesting is supported).

.. seealso::

   * :ref:`annotation_declarations`
   * :ref:`features`

