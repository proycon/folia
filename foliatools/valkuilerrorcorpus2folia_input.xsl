<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:folia="http://ilk.uvt.nl/folia" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcoi="http://lands.let.ru.nl/projects/d-coi/ns/1.0" xmlns:imdi="http://www.mpi.nl/IMDI/Schema/IMDI">

<!--
Valkuil Foutencorpus to FoLiA Conversion stylesheet
    by Maarten van Gompel
    Induction of Linguistic Knowledge Research group
    Tilburg University
    
    http://ilk.uvt.nl/folia
    http://github.com/proycon/folia

    version 0.1 
    
    Note: this is a LIMITED conversion, it does not deal with any joins/splits and multiple corrections on the same token!
    
    Licensed under the GNU General Public License v3
-->

<xsl:output method="xml" encoding="UTF-8" indent="yes" cdata-section-elements="gap" />


<xsl:template match="/dcoi:DCOI">
<FoLiA xmlns="http://ilk.uvt.nl/folia">
 <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
 </xsl:if>      
 <metadata type="imdi">
  <annotations>
   <token-annotation annotator="ilktok" annotatortype="auto" />
   <pos-annotation annotator="tadpole" annotatortype="auto" set="http://ilk.uvt.nl/folia/sets/cgn"/>
   <lemma-annotation annotator="tadpole" annotatortype="auto" set="http://ilk.uvt.nl/folia/sets/lemmas-nl"/>
   <correction-annotation annotator="unknown" annotatortype="manual" set="valkuilset"/>
  </annotations>
  <xsl:copy-of select="imdi:METATRANSCRIPT"/>
 </metadata>
 <xsl:apply-templates select="dcoi:text"/>
</FoLiA>
</xsl:template>

<xsl:template match="dcoi:text">
    <text xmlns="http://ilk.uvt.nl/folia">  
        <xsl:if test="@xml:id">
            <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
        </xsl:if>      
        <xsl:apply-templates />
    </text>
</xsl:template>

<xsl:template match="dcoi:gap">
<gap xmlns="http://ilk.uvt.nl/folia" class="{@reason}" annotator="{@hand}">
    <xsl:if test="desc/.">
    <desc><xsl:value-of select="desc" /></desc>
    </xsl:if>
    <xsl:if test="content/.">
    <content><xsl:value-of select="content" /></content>
    </xsl:if>
</gap>
</xsl:template>


<xsl:template match="dcoi:body">
    <xsl:apply-templates />
</xsl:template>

<xsl:template match="dcoi:div|dcoi:div0|dcoi:div1|dcoi:div2|dcoi:div3|dcoi:div4|dcoi:div5|dcoi:div6|dcoi:div7">
 <div xmlns="http://ilk.uvt.nl/folia">
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </div>
</xsl:template>

<xsl:template match="dcoi:p">
 <p xmlns="http://ilk.uvt.nl/folia">
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </p>
</xsl:template>

<xsl:template match="dcoi:head">
 <head xmlns="http://ilk.uvt.nl/folia">
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </head>
</xsl:template>

<xsl:template match="dcoi:s">
 <s xmlns="http://ilk.uvt.nl/folia">
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </s>
</xsl:template>

<xsl:template match="dcoi:w">
 <w xmlns="http://ilk.uvt.nl/folia">
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>  
    <xsl:choose>
    <xsl:when test="@original">
	  <t><xsl:value-of select="@original"/></t>
    </xsl:when>
    <xsl:otherwise>
     <t><xsl:value-of select="."/></t>
    </xsl:otherwise>
    </xsl:choose>  
   <xsl:if test="@pos">  
   <pos class="{@pos}" />
  </xsl:if>
  <xsl:if test="@lemma">  
   <lemma class="{@lemma}" />
  </xsl:if>
 </w>
</xsl:template>


<xsl:template match="dcoi:list">
 <list xmlns="http://ilk.uvt.nl/folia">
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </list>
</xsl:template>


<xsl:template match="dcoi:item">
 <listitem xmlns="http://ilk.uvt.nl/folia">
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:if test="@n">
   <xsl:attribute name="n"><xsl:value-of select="@n" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </listitem>
</xsl:template>

<xsl:template match="dcoi:label">
 <label xmlns="http://ilk.uvt.nl/folia"> 
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </label>
</xsl:template>

<xsl:template match="dcoi:figure">
 <figure xmlns="http://ilk.uvt.nl/folia">
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </figure>
</xsl:template>

<xsl:template match="dcoi:figDesc">
 <desc xmlns="http://ilk.uvt.nl/folia"><xsl:value-of select="." /></desc>
</xsl:template>

<xsl:template match="*">
  <xsl:comment>
    <xsl:value-of select="concat('[CONVERSION TO FOLIA WARNING] Element from original not processed: ',name())"/>
  </xsl:comment>
</xsl:template>

</xsl:stylesheet>
