.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _metric_annotation:

Metric Annotation
==================================================================

.. foliaspec:annotationtype_description(metric)
XXX

Specification
---------------

.. foliaspec:specification(metric)
XXX

Explanation
-------------------------

The ``<metric>`` element allows annotation of some kind of measurement. The type of
measurement is defined by the *class*, which in turn is user-defined by the set as
always. The metric element has a ``value`` attribute
that stores the actual measurement, the value is often numeric but this needs
not be the case. It is a higher-level annotation element
that may be used with any kind of annotation.

An example of measurements associated with a word/token:

.. code-block:: xml

    <w xml:id="example.p.1.s.1.w.2">
        <t>boot</t>
        <metric class="charlength" value="4" />
        <metric class="frequency" value="0.00232" />
    </w>

An example of measurements associated with a span annotation element:

.. code-block:: xml

    <su class="np">
        <wref id="..." />
        <wref id="..." />
        <metric class="length" value="2" />
    </su>

