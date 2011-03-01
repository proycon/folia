<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:imdi="http://www.mpi.nl/IMDI/Schema/IMDI">

<xsl:output method="html" encoding="UTF-8" omit-xml-declaration="yes" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" indent="yes" cdata-section-elements="script"/>

<xsl:template match="/FoLiA">
    <html>
        <head>
            <xsl:choose>
             <xsl:when test="/FoLiA/metadata/imdi:METATRANSCRIPT/imdi:Session/imdi:Title">
                <title><xsl:value-of select="/FoLiA/metadata/imdi:METATRANSCRIPT/imdi:Session/imdi:Title"/></title>
             </xsl:when>
             <xsl:otherwise>
                <title><xsl:value-of select="@xml:id"/></title>
             </xsl:otherwise>
            </xsl:choose>            
        </head>
        <body>
            <xsl:apply-templates select="//p" />
        </body>
    </html>
</xsl:template>


<xsl:template match="//p">
 <p>
  <xsl:apply-templates select="s" />
 </p>
</xsl:template>


<xsl:template match="s">
 <span class="s">
  <xsl:apply-templates select="w" />
 </span>
</xsl:template>

<xsl:template match="w">
 <span class="w"><xsl:value-of select="t"/></span>
</xsl:template>


</xsl:stylesheet>
