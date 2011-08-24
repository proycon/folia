<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns="http://ilk.uvt.nl/folia" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcoi="http://lands.let.ru.nl/projects/d-coi/ns/1.0" xmlns:folia="http://ilk.uvt.nl/folia">

<xsl:output method="xml" encoding="UTF-8" indent="yes" />

<xsl:variable name="id" select="/ptext/@ref" />

<xsl:template match="/ptext">
<FoLiA xmlns="http://ilk.uvt.nl/folia" version="0.5.1" generator="vudnc2folia.xsl">
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
   <division-annotation set="http://ilk.uvt.nl/folia/sets/vu-dnc-div" />
  </annotations>
  <meta id="corpus">VU-DNC</meta>
  <xsl:if test="@paper"><meta id="paper"><xsl:value-of select="@paper" /></meta></xsl:if>
  <xsl:if test="@reg"><meta id="reg"><xsl:value-of select="@news" /></meta></xsl:if>
  <xsl:if test="@subgenre"><meta id="subgenre"><xsl:value-of select="@subgenre" /></meta></xsl:if>
  <xsl:if test="@year"><meta id="year"><xsl:value-of select="@year" /></meta></xsl:if>
  <xsl:apply-templates select="header"/>
 </metadata>
 <xsl:apply-templates select="body"/> 
</FoLiA>
</xsl:template>

<xsl:template match="header">        
    <xsl:if test="paper"><meta id="paper"><xsl:value-of select="paper" /></meta></xsl:if>
    <xsl:if test="date"><meta id="date"><xsl:value-of select="date" /></meta></xsl:if>
    <xsl:if test="dateline"><meta id="dateline"><xsl:value-of select="dateline" /></meta></xsl:if>
    <xsl:if test="source"><meta id="source"><xsl:value-of select="source" /></meta></xsl:if>
    <xsl:if test="section"><meta id="section"><xsl:value-of select="section" /></meta></xsl:if>
    <xsl:if test="length"><meta id="length"><xsl:value-of select="length" /></meta></xsl:if>
    <xsl:if test="byline"><meta id="byline"><xsl:value-of select="byline" /></meta></xsl:if>
</xsl:template>

<xsl:template match="body">
    <text> 
        <xsl:attribute name="xml:id">
            <xsl:value-of select="$id" />
            <xsl:text>.text.1</xsl:text>
        </xsl:attribute>
        <div class="body">
            <xsl:attribute name="xml:id">
                <xsl:value-of select="$id" />
                <xsl:text>.body</xsl:text>
            </xsl:attribute>                 
            <xsl:if test="headline">
                    <head>
                        <xsl:attribute name="xml:id">
                            <xsl:value-of select="$id" />
                            <xsl:text>.headline</xsl:text>
                        </xsl:attribute>                         
                        <xsl:apply-templates select="headline/*" />    
                    </head>
            </xsl:if>
            <xsl:apply-templates select="sent" />    
        </div>        
        <xsl:if test="tail">
            <div class="tail">
                    <xsl:attribute name="xml:id">
                        <xsl:value-of select="$id" />
                        <xsl:text>.tail</xsl:text>
                    </xsl:attribute>     
                 <xsl:apply-templates select="tail/*" />  
            </div>
        </xsl:if>        
    </text>
</xsl:template>

<xsl:template match="sent">
    <xsl:variable name="sid">
        <xsl:value-of select="$id" />
        <xsl:text>.s.</xsl:text>
        <xsl:value-of select="@id" />
    </xsl:variable>
    <s>
        <xsl:attribute name="xml:id">
            <xsl:value-of select="$sid" />
        </xsl:attribute>        
        <xsl:for-each select="pau/*">
            <xsl:if test="local-name(.) = 'DS'">
                <xsl:call-template name="quote">
                    <xsl:with-param name="localid">
                        <xsl:value-of select="$sid" />
                        <xsl:text>.quote.</xsl:text>
                        <xsl:number />                        
                    </xsl:with-param>
                </xsl:call-template>
            </xsl:if>
            <xsl:if test="local-name(.) = 'pw'">
                <xsl:call-template name="word">
                    <xsl:with-param name="localid">
                        <xsl:value-of select="$sid" />
                        <xsl:text>.w.</xsl:text>
                        <xsl:number />                        
                    </xsl:with-param>
                </xsl:call-template>
            </xsl:if>            
        </xsl:for-each>
    </s>
</xsl:template>


<xsl:template name="quote">
    <xsl:param name="localid" />
    <quote>
        <xsl:attribute name="xml:id">
            <xsl:value-of select="$localid" />
        </xsl:attribute>      
        <xsl:for-each select="pw">
            <xsl:if test="local-name(.) = 'pw'">
                <xsl:call-template name="word">
                    <xsl:with-param name="localid">
                        <xsl:value-of select="$localid" />
                        <xsl:text>.w.</xsl:text>
                        <xsl:number />                        
                    </xsl:with-param>
                </xsl:call-template>
            </xsl:if>  
        </xsl:for-each>
    </quote>
</xsl:template>



<xsl:template name="word">
    <xsl:param name="localid" />
    <w>
        <xsl:attribute name="xml:id">
            <xsl:value-of select="$localid" />
        </xsl:attribute> 
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
