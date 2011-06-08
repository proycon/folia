<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcoi="http://lands.let.ru.nl/projects/d-coi/ns/1.0">

<xsl:output method="xml" encoding="UTF-8" indent="yes" />

<xsl:variable name="id" select="/ptext/@ref" />

<xsl:template match="/ptext">
<FoLiA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://ilk.uvt.nl/FoLiA folia.xsd" xmlns:imdi="http://www.mpi.nl/IMDI/Schema/IMDI">
 <xsl:attribute name="xml:id">
     <xsl:value-of select="$id" />
 </xsl:attribute>
 <metadata type="native">
  <!-- Native metadata should be removed and reference made to external CMDI file instead -->
  <annotations>
   <token-annotation />
   <pos-annotation set="http://ilk.uvt.nl/folia/sets/cgn" annotator="tadpole" annotatortype="auto" />
   <lemma-annotation set="http://ilk.uvt.nl/folia/sets/lemmas-nl" annotator="tadpole" annotatortype="auto" />
   <subjectivity-annotation set="http://ilk.uvt.nl/folia/sets/vu-dnc-subjectivity" />
   <div-annotation set="http://ilk.uvt.nl/folia/sets/vu-dnc-div" />
  </annotations>
  <meta id="corpus">VU-DNC</meta>
  <meta id="paper"><xsl:value-of select="@paper" /></meta>
  <meta id="reg"><xsl:value-of select="@news" /></meta>
  <meta id="subgenre"><xsl:value-of select="@subgenre" /></meta>
  <meta id="year"><xsl:value-of select="@year" /></meta>  
  <xsl:apply-templates select="header"/>
 </metadata>
 <xsl:apply-templates select="body"/> 
</FoLiA>
</xsl:template>

<xsl:template match="header">        
    <meta id="document"><xsl:value-of select="document" /></meta>
    <meta id="paper"><xsl:value-of select="paper" /></meta>
    <meta id="date"><xsl:value-of select="date" /></meta>
    <meta id="source"><xsl:value-of select="source" /></meta>
    <meta id="section"><xsl:value-of select="section" /></meta>
    <meta id="length"><xsl:value-of select="length" /></meta>
    <meta id="byline"><xsl:value-of select="byline" /></meta>
</xsl:template>

<xsl:template match="body">
    <text> 
        <xsl:attribute name="xml:id">
            <xsl:value-of select="$id" />
            <xsl:text>.text.1</xsl:text>
        </xsl:attribute>
        <div class="body">
            <xsl:apply-templates />    
        </div>        
    </text>
</xsl:template>

<xsl:template match="headline">
    <head>
        <xsl:apply-templates />            
    </head>
</xsl:template>

<xsl:template match="tail">
    <div class="tail">
        <xsl:apply-templates />       
    </div>
</xsl:template>

<xsl:template match="sent">
    <s>
        <xsl:attribute name="xml:id">
            <xsl:value-of select="$id" />
            <xsl:text>.s.</xsl:text>
            <xsl:value-of select="@id" />
        </xsl:attribute>
        <xsl:apply-templates />
    </s>
</xsl:template>

<xsl:template match="pau">
    <xsl:apply-templates />
</xsl:template>

<xsl:template match="DS">
    <quote>
        <xsl:apply-templates />        
    </quote>
</xsl:template>

<xsl:template match="pw">
    <w> <!-- TODO: grab ID of parent -->
        <t><xsl:value-of select="." /></t>
        <xsl:if test="@pos">
            <pos class="{@pos}" />
        </xsl:if>
        <xsl:if test="@lem">
            <lemma class="{@lem}" />
        </xsl:if>
        <xsl:if test="@subjcat">
            <subjectivity class="{@subjcat}">
                <xsl:if test="@subjscat">
                <feat subset="subcat" class="{@subjscat}" />
                </xsl:if>
                <xsl:if test="@subj-cond">
                <feat subset="cond" class="{@subj-cond}" />
                </xsl:if>
            </subjectivity>
        </xsl:if>
    </w>    
</xsl:template>

<xsl:template match="br">
    <whitespace />
</xsl:template>

</xsl:stylesheet>
