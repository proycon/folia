.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _hspace_annotation:

Horizontal Whitespace
==================================================================

.. foliaspec:annotationtype_description(hspace)
Markup annotation introducing horizontal whitespace

.. note::

    Do not confuse this with the ``<whitespace>`` structure element and ``<t-whitespace>`` markup element that are used for *vertical* whitespace, see
    :ref:`whitespace_annotation`.

Specification
---------------

.. foliaspec:specification(hspace)
XXX

Description & Examples
-------------------------

If normal spacing is not enough and you need to express **horizontal** whitespace explicitly, then you can use the
``<t-hspace>`` element.

.. code-block:: xml

   <t>To be<t-hspace class="long" />or not to be</t>

The vocabulary is defined by your set definition and you can assign your own size-interpretation. Tools that are not
aware of your vocabulary should simply render a single space.

An alternative to ``t-hspace`` is to use the ``xml:space="preserve"`` attribute as described in
:ref:`preserving_whitespace`, but the use of ``<t-hspace>`` is preferred.
