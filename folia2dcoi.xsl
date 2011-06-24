<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:imdi="http://www.mpi.nl/IMDI/Schema/IMDI" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://lands.let.ru.nl/projects/d-coi/ns/1.0"  xmlns:dcoi="http://lands.let.ru.nl/projects/d-coi/ns/1.0" xmlns:folia="http://ilk.uvt.nl/folia">

<xsl:output method="xml" encoding="UTF-8" indent="yes" cdata-section-elements="gap" />

<xsl:template match="/folia:FoLiA">
<DCOI xml:id="{@xml:id}"></DCOI>
 <xsl:copy-of select="metadata/imdi:METATRANSCRIPT"/>
 <xsl:apply-templates select="folia:text"/>
</DCOI>
</xsl:template>


<xsl:template match="folia:text">
<body>
  <text xml:id="{@xml:id}">        
    <xsl:apply-templates />
  </text>
</body>    
</xsl:template>

<xsl:template match="folia:gap">
<gap reason="{@class}" hand="{@annotator}">
    <xsl:if test="desc">
        <desc><xsl:value-of select="desc" /></desc>
    </xsl:if>
    <xsl:if test="content">
        <content><xsl:value-of select="content" /></content>
    </xsl:if>
</gap>
</xsl:template>


<xsl:template match="folia:div">
 <div>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </div>
</xsl:template>

<xsl:template match="folia:p">
 <p>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </p>
</xsl:template>

<xsl:template match="folia:head">
 <head>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </head>
</xsl:template>

<xsl:template match="folia:s">
 <s>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </s>
</xsl:template>

<xsl:template match="folia:w">
 <w xml:id="@xml:id"><xsl:if test="pos"><xsl:attribute name="pos"><xsl:value-of select="pos/@class" /></xsl:attribute></xsl:if><xsl:if test="lemma"><xsl:attribute name="lemma"><xsl:value-of select="lemma/@class" /></xsl:attribute></xsl:if><xsl:value-of select="t"/></w>
</xsl:template>

</xsl:stylesheet>
