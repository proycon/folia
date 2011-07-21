<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:imdi="http://www.mpi.nl/IMDI/Schema/IMDI" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://lands.let.ru.nl/projects/d-coi/ns/1.0"  xmlns:dcoi="http://lands.let.ru.nl/projects/d-coi/ns/1.0" xmlns:folia="http://ilk.uvt.nl/folia">


<!--
FoLiA to D-Coi Conversion stylesheet
    by Maarten van Gompel
    Induction of Linguistic Knowledge Research group
    Tilburg University
    
    http://ilk.uvt.nl/folia
    http://github.com/proycon/folia
    
    version 0.5.2
    
    Usage with xsltproc: 
     $ xsltproc folia2dcoi.xsl foliadocument.xml
     
    Conversion considers only elements that are supported in D-Coi,
    other information will be lost in conversion!!
    
    Licensed under the GNU General Public License v3
-->

<xsl:output method="xml" encoding="UTF-8" indent="yes" cdata-section-elements="gap" />

<xsl:template match="/folia:FoLiA">
<DCOI>
 <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
 </xsl:if>
 <xsl:copy-of select="folia:metadata/imdi:METATRANSCRIPT"/>
 <xsl:apply-templates select="folia:text"/>
</DCOI>
</xsl:template>


<xsl:template match="folia:text">
<body>
  <text>
    <xsl:if test="@xml:id">
        <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
    </xsl:if>        
    <xsl:apply-templates />
  </text>
</body>    
</xsl:template>

<xsl:template match="folia:gap">
<gap reason="{@class}" hand="{@annotator}">
    <xsl:if test="folia:desc">
        <desc><xsl:value-of select="folia:desc" /></desc>
    </xsl:if>
    <xsl:if test="folia:content">
        <content><xsl:value-of select="folia:content" /></content>
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
 <w><xsl:if test="@xml:id"><xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute></xsl:if><xsl:if test="folia:pos"><xsl:attribute name="pos"><xsl:value-of select="folia:pos/@class" /></xsl:attribute></xsl:if><xsl:if test="folia:lemma"><xsl:attribute name="lemma"><xsl:value-of select="folia:lemma/@class" /></xsl:attribute></xsl:if><xsl:value-of select="folia:t"/></w>
</xsl:template>

<xsl:template match="folia:list">
 <list>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </list>
</xsl:template>

<xsl:template match="folia:listitem">
 <item>
  <xsl:if test="@xml:id">
   <xsl:attribute name="xml:id"><xsl:value-of select="@xml:id" /></xsl:attribute>
  </xsl:if>
  <xsl:apply-templates />
 </item>
</xsl:template>



<xsl:template match="*">
  <xsl:comment>
    <xsl:value-of select="concat('[CONVERSION FROM FOLIA WARNING] Element from original not processed: ',name())"/>
  </xsl:comment>
</xsl:template>

</xsl:stylesheet>
