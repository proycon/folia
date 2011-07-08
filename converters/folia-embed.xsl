<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns="http://www.w3.org/1999/xhtml" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:imdi="http://www.mpi.nl/IMDI/Schema/IMDI" xmlns:folia="http://ilk.uvt.nl/folia">

<xsl:output method="html" encoding="UTF-8" omit-xml-declaration="yes" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" indent="yes" cdata-section-elements="script"/>


<xsl:template match="/folia:FoLiA">
  <xsl:apply-templates select="folia:text" />    
</xsl:template>



<xsl:template match="folia:text">
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
  <xsl:apply-templates />
 </div>
</xsl:template>

<xsl:template match="folia:p">
 <p>
  <xsl:apply-templates />
 </p>
</xsl:template>


<xsl:template match="folia:head">
 <h1>
  <xsl:apply-templates />
 </h1>
</xsl:template>

<xsl:template match="folia:s">
 <span class="s">
  <xsl:apply-templates />
 </span>
</xsl:template>

<xsl:template match="folia:w">
 <span id="{@xml:id}" class="word">
        <xsl:value-of select="folia:t"/>
 </span>
 <xsl:text> </xsl:text> <!-- TODO: implement @nospace check -->
</xsl:template>

</xsl:stylesheet>
