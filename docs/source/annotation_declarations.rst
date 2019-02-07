.. _annotation_declarations:

Annotation Declarations
==========================

Introduction
---------------

All annotation types that are used in a FoLiA document have to be *declared*. In the metadata block you will find the
``<annotations>`` block in which each annotation type that occurs in the document is mentioned, i.e. declared. So does
your document include Part of Speech tagging? Then there will be an entry declaring it does so, and linking to the set
definition used.

These declarations allow software to identify exactly what a FoLiA document consists of without needing to go through the entire
document, on the basis of this software can determine whether it can handle the document in the first place. You can for
instance imagine an NLP tool that does Named Entity Recognition but requires Part-of-Speech tags and Lemmas to do so,
feeding it a FoLiA document without such annotation layers would then be pointless and easy to detect.

Each annotation type has a specific XML element to use as declaration in the ``<annotations>`` block, these all end in
with the suffix ``-annotations`` and take the following attributes:

* ``set`` - The set should be a URL to a publicly hosted set definition that defines the vocabulary used (see
  :ref:`set_definitions`) with this particular annotation type. Sets are intentionally kept separate from FoLiA itself
  and can be created by anyone. FoLiA also allows for ad-hoc sets, these are sets that are not actually defined and they
  are therefore an arbitrary string rather than a URL. They allow for a more flexible use of FoLiA without full formal
  closure, but limit it to only shallow validation.
  Some annotation types also work without an associated vocabulary, and for some they are optional, on such declarations the ``set`` attribute is not used or optional.
* ``format`` - Set definitions can be stored in several formats, the format may be indicated (not mandatory) by the
  ``format`` attribute on each declaration, its value should be a MIME type.
* ``alias`` - This is an optional attribute that specifies an alias for the set, this is useful in case an annotation
  type occurs multiple times with distinct sets, in which case individual annotation needs to explicitly mention the set
  but referring to sets by long URLs gets cumbersome. In such cases annotations can use the alias instead of the full
  set URL. An alias has to be unique for the annotation type.

Within the scope of each annotation's declaration, you can declare one or more *annotators*, each annotator refers (by ID) to what we call a
``processor`` in the *provenance data*. These processors represent software tools or human annotators and carry
various attributes, e.g. the name of the annotator/tool. So this part of declaration identifies *who* or *what* performed the annotation. Consider the following example:

.. code-block:: xml

    <annotations>
        <token-annotation set="https://raw.githubusercontent.com/LanguageMachines/uctodata/master/setdefinitions/tokconfig-eng.foliaset.ttl">
            <annotator processor="p1.ucto"/>
        </token>
        <pos-annotation set="https://github.com/proycon/folia/blob/master/setdefinitions/cgn.foliaset.ttl">
            <annotator processor="p2.frog"/>
            <annotator processor="p3.proycon"/>
        </pos>
    </annotations>


The section :ref:`provenance_data` will explain in depth how the processors that the ``annotator`` elements refer to are
defined. If there is only one annotator declared, then this is the default for all annotations of this type and set, in
which case individual annotation instances need not refer to any processor. If there are multiple annotators, the
individual annotation instances should refer to a processor to disambiguate.

Provenance data is recommended but not required in FoLiA. A simpler mechanism from prior to FoLiA v2.0 is also still
available: If you do not refer to processors for a certain annotation type and set, then you can specify the following
*optional* attributes on your declaration to set a default annotator:

* ``annotator`` - The name of the default annotator (either human or software)
* ``annotatortype`` - Set to ``auto`` if the default annotator is automatic annotation by software or ``manual`` for human annotators


More about set definitions
---------------------------

A *set definition* (see :ref:`set_definitions`) specifies exactly what classes are allowed in a particular vocabulary.
It for example specifies exactly what part-of-speech tags exist. This information is necessary to validate the document
completely at its deepest level. If the sets point to URLs that do not exist or are not URLs at all, warnings will be
issued.  Validation can still proceed but with the notable exception that there is no deep validation of these sets, so
no full formal closure.

Though we recommend using and creating actual sets. FoLiA itself is rather agnostic about their existence for most
purposes. For deep validation, proper formalisation, and for certain applications they may be required; but as long as
they serve as proper *unique identifiers* you can get get away with non-existing sets. In this case, simply do not use a
URL but another arbitrary identification string.

If multiple sets are used for the same annotation type, which is perfectly valid, they each need a
separate declaration.

.. seealso::
    * :ref:`set_definitions`
    * :ref:`provenance_data`


