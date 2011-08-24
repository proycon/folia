<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns="http://www.w3.org/1999/xhtml" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:imdi="http://www.mpi.nl/IMDI/Schema/IMDI" xmlns:folia="http://ilk.uvt.nl/folia">

<xsl:output method="html" encoding="UTF-8" omit-xml-declaration="yes" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" indent="yes" />

<xsl:template match="/folia:FoLiA">
  <xsl:apply-templates select="folia:text" />    
</xsl:template>



<xsl:template match="/folia:FoLiA/folia:text">
 <div class="text">
   <xsl:choose>
   <xsl:when test="/folia:div">
    <xsl:apply-templates select="/folia:div" />
   </xsl:when>
   <xsl:when test="//folia:p">
    <xsl:apply-templates select="//folia:p|//folia:head" />
   </xsl:when>
   <xsl:when test="//folia:s">
    <xsl:apply-templates select="//folia:s|//folia:head" />
   </xsl:when> 
   <xsl:otherwise>
    <span class="error">No content found in this text!</span>
   </xsl:otherwise>
  </xsl:choose>
 </div>
</xsl:template>

<xsl:template match="folia:div">
 <div class="div">
   <xsl:choose>
   <xsl:when test="/folia:div">
    <xsl:apply-templates select="/folia:div" />
   </xsl:when>
   <xsl:when test="//folia:p">
    <xsl:apply-templates select="//folia:p|//folia:head" />
   </xsl:when>
   <xsl:when test="//folia:s">
    <xsl:apply-templates select="//folia:s|//folia:head" />
   </xsl:when> 
   </xsl:choose>
 </div>
</xsl:template>

<xsl:template match="folia:p">
 <p id="{@xml:id}">
  <xsl:apply-templates select="folia:s" />
 </p>
</xsl:template>


<xsl:template match="folia:head">
 <h1>
  <xsl:apply-templates select="folia:s" />
 </h1>
</xsl:template>

<xsl:template match="folia:s">
 <span id="{@xml:id}" class="s"><xsl:apply-templates select=".//folia:w" /></span>
</xsl:template>

<xsl:template match="folia:w">
<xsl:if test="not(ancestor::folia:original) and not(ancestor::folia:suggestion)">
<span id="{@xml:id}" class="word"><xsl:value-of select="folia:t"/></span>
<xsl:choose>
   <xsl:when test="@space = 'no'"></xsl:when>
   <xsl:otherwise>
    <xsl:text> </xsl:text>
   </xsl:otherwise>
</xsl:choose>
</xsl:if>
</xsl:template>

</xsl:stylesheet>

