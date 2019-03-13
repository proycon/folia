.. _foreign_annotation:

Foreign Annotation
==================================================================

It may happen that you want to include annotations inside your FoLiA that are not actually in FoLiA, but in some other
XML format. Though **this is very much discouraged**, even more so if FoLiA has proper facilities for your annotation needs,
it may in rare cases be needed; for example if FoLiA has no support yet for a particular advanced
type of annotation or if another scheme has already been in use and conversion is not an option. It is most
suitable for attaching further data to arbitrary elements, though for metadata :ref:`submetadata` should always be considered first!

The higher-order annotation element ``<foreign-data>`` can be used to accomplish
foreign annotations. It acts as a container in which annotation must be in a different XML namespace,
rather than the FoLiA namespace. The element is allowed almost
anywhere: inside structure annotation, inside inline/span annotation, inside
other higher annotation elements, but
**not** inside text content (``<t>``), phonetic content (``<ph>``) or text-markup
(``<t-*>``).

In the following example we attach an annotation in a custom fictitious XML format and namespace to a FoLiA word:

.. code-block:: xml

   <w xml:id="w.1">
      <t>Hello</t>
      <foreign-data xmlns:myformat="http://my.com/custom/format">
         <myformat:myannotation myattribute="myvalue" />
      </foreign-data>
   </w>

Foreign annotation does not need to be declared and, as can not be emphasised enough, should really only be used when no
proper FoLiA solution exists, and even in such cases it is preferable to contact the FoLiA developers and see if FoLiA
can be extended for your needs.. Be aware that generic FoLiA tools and libraries will usually not process the contents
of foreign-data, as it can contain anything by definition, and special-purpose tools need to be written for your
specific use case if you use foreign-data.
