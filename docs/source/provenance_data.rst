.. _provenance_data:

Provenance Data
========================

It is often desireable to know exactly what tools (and what versions thereof and even with what parameters) were invoked
in which order to produce a FoLiA document, this is called **provenance data**. In the metadata section, right after the
:ref:`annotation_declarations` FoLiA allows for a ``<provenance>`` block containing this information. It is not
mandatory but it is strongly recommended.

The ``<provenance>`` block defines one or more **processors**, processors are processes or entities that have processed
and often performend some kind of manipulation of the document, such as adding annotations. The processors are listed in
the order they were invoked. The :ref:`annotation_declarations` in turn link to these processors to tie a particular
annotation type and set to one or more processors.

A ``<processor>`` carries the following attributes:
   * ``xml:id`` -- The ID of the processor (mandatory), this is how it is referred to from the ``<annotator processor=".." />`` element in the :ref:`annotation_declarations` and from the ``processor`` attribute (part of the common FoLiA attributes) on individual annotations.
   * ``name`` -- The name identifies actual tool or human annotator
   * ``type`` -- Each processor contains a type:
        * ``auto`` - (default) - The processor is an automated tool that provided annotations
        * ``manual`` - The processor refers a manual annotator
        * ``generator`` - The processor indicates the FoLiA library used by the parent and sibling processors (unless sibling processes specify another generator in their scope)
        * ``datasource`` - The processor is a reference to a particular data source that was used by the parent processor
   * ``version`` -- (optional but strongly recommended) is the version of the processor aka tool
   * ``document_version``  -- The version of the document, refers to any label the user desires to indicate a version of the document, so the format is not predetermined and needs not be numeric.
   * ``command`` (optional) -- The exact command that was run
   * ``host`` (optional) -- The host on which the processor ran, this identifies individual systems on a network/cluster
   * ``user`` (optional) -- The user/executor which ran the processor, this identifies who ran an automated process rather than who the annotator was!
   * ``folia_version`` (optional)  - The folia version that was written
   * ``begindatetime`` (optional) -- Specifies when the process started, format is  ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
   * ``enddatetime`` (optional) -- Specifies when the process finished, format is  ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
   * ``resourcelink`` (optional) - The URI of any RDF resource describing this processor. This allows linking to the external world of linked open data from the provenance chain in FoLiA.
   * Additional custom metadata is allowed in the form of ``<meta>`` elements (just like with folia native metadata) inside the scope of a processor, FoLiA does not define the semantics of any such metadata, i.e. they are tool/application-specific and could for instance be used to specify tool parameters used.

First consider a fairly minimalistic example, note that we include the :ref:`annotation_declarations` as well with a link to the processor:

.. code-block:: xml

    <annotations>
      <token-annotation set="tokconfig-nl">
          <annotator processor="p0" />
      </token-annotation>
    </annotations>
    <provenance>
        <processor xml:id="p0" name="ucto" version="0.15" folia_version="2.0" command="ucto -Lnld" host="mhysa" user="proycon" begindatetime="2018-09-12T00:00:00" enddatetime="2018-09-12T00:00:10" document_version="1" />
    </provenance>

Individual annotations in the document can refer to this processor using the ``processor`` attribute:


.. code-block:: xml

    <w class="PUNCTUATION" processor="p0">
     <t>.</t>
    </w>

If there is only one ``<annotator>`` defined for a certain annotation type and set in the
:ref:`annotation_declarations`, then it is the default and no ``processor`` attribute is necessary.

One of the powerful features of processors is that they can be nested, this creates *subprocessors* and captures
situations where one processor invokes others as part of its operation. Subprocessors can also provide some extra
information on their parent processor, as they can for example state what FoLiA library was used (``type="generator"``)
or what data sources were used by the processor (``type="datasource"``).  Moreover, arbitrary metadata can be added to
any processor in the form of ``<meta>`` elements (just like with FoLiA's native :ref:`metadata`), FoLiA does not define
the semantics of any such metadata, i.e. they are tool/application-specific and could for instance be used to specify
tool parameters used. Note that whereas the order of the processors in the `<provenance>` block is strictly significant,
the order of subprocessors is not.

With all this in mind, we can expand our previous example:


.. code-block:: xml

    <provenance>
        <processor xml:id="p0" name="ucto" version="0.15" folia_version="2.0" command="ucto -Lnld" host="mhysa" user="proycon" begindatetime="2018-09-12T00:00:00" enddatetime="2018-09-12T00:00:10" document_version="1" />
            <meta id="config">tokconfig-nld</meta>
            <meta id="language">nld</meta>
            <processor xml:id="p0.1" name="libfolia" version="2.0" folia_version="2.0" type="generator" />
            <processor xml:id="p0.1" name="tokconfig-nld" version="2.0" folia_version="2.0" type="datasource" />
        </processor>
    </provenance>

Or consider the following example in which we have a tool that is an annotation environment in which human annotators
edit a FoLiA document and add/edit annotations:

.. code-block:: xml

    <provenance>
        <processor xml:id="p2" name="flat" version="0.8" folia_version="2.0" host="flat.science.ru.nl" begindatetime="2018-09-12T00:10:00" enddatetime="2018-09-12T00:20:00" document_version="3">
            <processor xml:id="p2.0" name="foliapy" version="2.0" folia_version="2.0" type="generator" />
            <processor xml:id="p2.1" name="proycon" type="manual" />
            <processor xml:id="p2.2" name="ko" type="manual" />
        </processor>
    </provenance>

From the :ref:`annotation_declarations`, we can then also refer directly to subprocessors. Moreover, a processor can be
referred to from multiple annotation types/sets:

.. code-block:: xml

    <annotations>
      ...
      <pos-annotation set="...">
          <annotator processor="p2.1" />
          <annotator processor="p2.2" />
      </pos-annotation>
      <lemma-annotation set="...">
          <annotator processor="p2.1" />
      </lemma-annotation>
      ...
    </annotations>

Of course, providing all this is not mandatory and requires the specific tool to actually supply this provenance data.
It is still possible to have FoLiA documents without provenance data at all.

The following example provides a small but complete FoLiA document with provenance data:

.. literalinclude:: ../../examples/provenance.2.0.0.folia.xml
    :linenos:
    :language: xml

And another more real-life example:

.. literalinclude:: ../../examples/pos-features-deep.2.0.0.folia.xml
    :linenos:
    :language: xml

.. seealso::
    :ref:`annotation_declarations`
    :ref:`set_definitions`
