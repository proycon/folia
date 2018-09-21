.. _statement_annotation:
.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. foliaspec:annotationtype_title(statement)
XXX

.. foliaspec:annotationtype_description(statement)
XXX

Specification
---------------

.. foliaspec:specification(statement)
XXX

Explanation
-------------------------

The span annotation element ``<statement>`` allows to decompose statements into the source of the statement, the content
of the statement, and the way these relate, provided these are made explicit in the text. It can be used to annotate
attribution (who said what etc). The element is used in a ``<statements>`` layer and takes the following span roles:

* ``<hd>`` -- (required) -- The head of the statement is the actual content of the statement; this role spans the words containing the statement.
* ``<source>`` -- (optional) -- The source/holder of the statement, assuming it is explicitly expressed in the text.
* ``<relation>`` -- (optional) -- The relation between the source of the statement and the statement, this usually encompasses verbs like "to say", "to think", or prepositional phrases such as "according to".

Example
-------------------------

.. literalinclude:: ../examples/statement.folia.xml
    :linenos:
    :language: xml


