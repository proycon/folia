<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcoi="http://lands.let.ru.nl/projects/d-coi/ns/1.0">

<xsl:output method="xml" encoding="UTF-8" indent="yes" cdata-section-elements="gap" />


<xsl:template match="/dcoi:DCOI">
<FoLiA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://ilk.uvt.nl/FoLiA folia.xsd" xmlns:imdi="http://www.mpi.nl/IMDI/Schema/IMDI" xml:id="{@xml:id}">
 <metadata>
  <annotations>
   <token-annotation />
  </annotations>
  <xsl:copy-of select="imdi:METATRANSCRIPT"/>
 </metadata>
 <xsl:apply-templates select="dcoi:text"/>
</FoLiA>
</xsl:template>

<xsl:template match="dcoi:text">
    <text xml:id="{@xml:id}">        
        <xsl:apply-templates />
    </text>
</xsl:template>

<xsl:template match="dcoi:gap">
<gap class="{@reason}" annotator="{@hand}">
    <desc><xsl:value-of select="desc" /></desc>
    <content><xsl:value-of select="content" /></content>
</gap>
</xsl:template>


<xsl:template match="dcoi:body">
    <body>
        <xsl:apply-templates select="dcoi:div|dcoi:div0|dcoi:div1|dcoi:div2|dcoi:div3|dcoi:div4|dcoi:div5|dcoi:div6|dcoi:div7"/>
    </body>
</xsl:template>

<xsl:template match="dcoi:div|dcoi:div0|dcoi:div1|dcoi:div2|dcoi:div3|dcoi:div4|dcoi:div5|dcoi:div6|dcoi:div7">
 <div>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </div>
</xsl:template>

<xsl:template match="dcoi:p">
 <p>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </p>
</xsl:template>

<xsl:template match="dcoi:head">
 <head>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </head>
</xsl:template>

<xsl:template match="dcoi:s">
 <s>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </s>
</xsl:template>

<xsl:template match="dcoi:w">
 <w>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <t><xsl:value-of select="."/></t>
  <xsl:if test="@pos">  
   <pos class="{@pos}" />
  </xsl:if>
  <xsl:if test="@lemma">  
   <lemma class="{@lemma}" />
  </xsl:if>
 </w>
</xsl:template>

</xsl:stylesheet>

