#!/usr/bin/env python3
#Generate library specification code (for either Python or C++) on the the basis of folia.yml
#Used by respectively pynlpl and libfolia

from __future__ import print_function, unicode_literals, division, absolute_import

import sys
import datetime
import os
from collections import defaultdict
import yaml



skip_properties = {
    'c++': ('textcontainer','phoncontainer','primaryelement'), #these are not handled in libfolia, or handled differently, don't output these in the source
}

#Load specification
specfiles= [  os.path.join(os.path.dirname(__file__) ,'../schemas/folia.yml'), 'folia.yml' ]
spec = None
for specfile in specfiles:
    spec = yaml.load(open(specfile,'r'))
    break

if spec is None:
    print("FoLiA Specification file folia.yml could not be found in " + ", ".join(specfiles) ,file=sys.stderr)


parents = defaultdict(list)

elementdict = {} #flat (unnested) dictionary

def getelements(d):
    elements = []
    if 'elements' in d:
        for e in d['elements']:
            elementdict[e['class']] = e
            elements.append(e)
            children = getelements(e)
            elements += children
            for c in children:
                if e['class'] not in parents[c['class']]:
                    parents[c['class']].append(e['class'])
    return elements

elements = getelements(spec) #gathers all class names
elements.sort(key=lambda x: x['class'])
elementnames = [ e['class'] for e in elements ]


################################################################

def addfromparents(elementname, key):
    value = set(spec['defaultproperties']['accepted_data'])
    if 'properties' in elementdict[elementname] and key in elementdict[elementname]['properties'] and elementdict[elementname]['properties'][key]:
        value |= set(elementdict[elementname]['properties'][key])
    else:
        value |= set()
    for parent in parents[elementname]:
        value |= addfromparents(parent, key)
    return value



def outputvar(var, value, target, declare = False):
    """Output a variable ``var`` with value ``value`` in the specified target language."""

    #do we need to quote the value? (bool)
    varname = var.split('.')[-1]

    if isinstance(value, str) and varname.upper() in ('ACCEPTED_DATA','REQUIRED_DATA','REQUIRED_ATTRIBS', 'OPTIONAL_ATTRIBS','ANNOTATIONTYPE'):
        quote = False
    else:
        quote = True


    if isinstance(value, str):
        value = value.replace("\n","\\n").replace("\t","\\t")

    if target == 'python':
        if varname == 'ANNOTATIONTYPE' and isinstance(value,str):
            value = 'AnnotationType.' + value

        if value is None:
                return var + ' = None'
        elif isinstance(value, bool):
            if value:
                return var + ' = True'
            else:
                return var + ' = False'
        elif isinstance(value, (int, float) ):
            return var + ' = ' + str(value)
        elif isinstance(value, (list,tuple,set) ):
            if varname in ('ACCEPTED_DATA','REQUIRED_DATA') or  all([ x in elementnames for x in value ]):
                return var + ' = (' + ', '.join(value) + ',)'
            elif all([ x in spec['attributes'] for x in value ]):
                return var + ' = (' + ', '.join(['Attrib.' + x for x in value]) + ',)'

            if len(value) == 0:
                return var + ' = ()'

            #list items are  enums or classes, never string literals
            if quote:
                return var + ' = (' + ', '.join([ '"' + x + '"' for x in value]) + ',)'
            else:
                return var + ' = (' + ', '.join(value) + ',)'
        else:
            if quote:
                return var + ' = "' + value  + '"'
            else:
                return var + ' = ' + value
    elif target == 'c++':
        typedeclaration = ''
        if value is None:
            if declare: raise NotImplementedError("Declare not supported for None values")
            if varname in ('REQUIRED_ATTRIBS','OPTIONAL_ATTRIBS'):
                return var + ' = NO_ATT;'
            elif varname == 'ANNOTATIONTYPE':
                return var + ' = AnnotationType::NO_ANN;'
            elif varname in ('XMLTAG','TEXTDELIMITER'):
                return var + ' = "NONE";'
            elif varname  == 'REQUIRED_DATA':
                return var + ' = {};'
            elif varname  == 'SUBSET':
                return var + ' = "";'
            else:
                raise NotImplementedError("Don't know how to handle None for " + var)
        elif isinstance(value, bool):
            if declare: typedeclaration = 'const bool '
            if value:
                return typedeclaration + var + ' = true;'
            else:
                return typedeclaration + var + ' = false;'
        elif isinstance(value, int ):
            if declare: typedeclaration = 'const int '
            return typedeclaration + var + ' = ' + str(value) + ';'
        elif isinstance(value, float ):
            if declare: typedeclaration = 'const double '
            return typedeclaration + var + ' = ' + str(value) + ';'
        elif isinstance(value, (list,tuple,set)):
            #list items are  enums or classes, never string literals
            if varname in ('ACCEPTED_DATA','REQUIRED_DATA') or  all([ x in elementnames for x in value ]):
                if declare:
                    typedeclarion = 'const set<ElementType> '
                    operator = '='
                else:
                    typedeclaration = ''
                    operator = '+='
                value = [ x + '_t' for x in value ]
                return typedeclaration + var + ' ' + operator + ' {' + ', '.join(value) + '};'
            elif all([ x in spec['attributes'] for x in value ]):
                return var + ' = ' + '|'.join(value) + ';'
            else:
                return typedeclaration + var + ' = { ' + ', '.join([ '"' + x + '"' for x in value if x]) + ', };'
        else:
            if varname == 'ANNOTATIONTYPE':
                value = "AnnotationType::" + value

            if quote:
                if declare: typedeclaration = 'const string '
                return typedeclaration + var + ' = "' + value+ '";'
            else:
                if declare: typedeclaration = 'const auto '
                return typedeclaration + var + ' = ' + value+ ';'

#concise description for all available template blocks
blockhelp = {
        'namespace': 'The FoLiA XML namespace',
        'version': 'The FoLiA version',
        'version_major': 'The FoLiA version (major)',
        'version_minor': 'The FoLiA version (minor)',
        'version_sub': 'The FoLiA version (sub/rev)',
        'attributes': 'Defines all common FoLiA attributes (as part of the Attrib enumeration)',
        'annotationtype': 'Defines all annotation types (as part of the AnnotationType enumeration)',
        'instantiateelementproperties': 'Instantiates all element properties for the first time, setting them to the default properties',
        'setelementproperties': 'Sets all element properties for all elements',
        'annotationtype_string_map': 'A mapping from annotation types to strings',
        'string_annotationtype_map': 'A mapping from strings to annotation types',
        'annotationtype_xml_map': 'A mapping from annotation types to xml tags (strings)',
        'structurescope': 'Structure scope above the sentence level, used by next() and previous() methods',
        'defaultproperties': 'Default properties which all elements inherit',
        'default_ignore': 'Default ignore list for the select() method, do not descend into these',
        'default_ignore_annotations': 'Default ignore list for token annotation',
        'default_ignore_structure': 'Default ignore list for structure annotation',
}

def setelementproperties_cpp(element,indent, defer,done):
    commentsign = "//"
    target = 'c++'
    s = commentsign + "------ " + element['class'] + " -------\n"
    if element['class'] in parents:
        for parent in parents[element['class']]:
            if parent not in done:
                defer[parent].append(element)
                return None
            else:
                s += indent + element['class'] + '::PROPS = ' + parent + '::PROPS;\n'
            break
    s += indent + element['class'] + '::PROPS.ELEMENT_ID = ' + element['class'] + '_t;\n'
    if 'properties' in element:
        for prop, value in sorted(element['properties'].items()):
            if target not in skip_properties or prop not in skip_properties[target]:
                if prop == 'xmltag':
                    if 'Feature' in parents[element['class']] and 'subset' in element['properties'] and element['properties']['subset']:
                        value = element['properties']['subset']
                elif prop == 'accepted_data':
                    value = tuple(sorted(addfromparents(element['class'],'accepted_data')))
                    if ('textcontainer' in element['properties'] and element['properties']['textcontainer']) or ('phoncontainer' in element['properties'] and element['properties']['phoncontainer']):
                        value += ('XmlText',)
                    if 'WordReference' in value:
                        value += ('Word','Morpheme','Phoneme')
                s += indent + outputvar(element['class'] + '::PROPS.' + prop.upper(),  value, target) + '\n'
    done[element['class']] = True
    return s

def flattenclasses(candidates):
    done = {}
    resolved = set()
    for c in candidates:
        for child, parentlist in parents.items():
            if c in parentlist:
                if child not in done and child not in candidates:
                    candidates.append(child)
        if c[:8] != 'Abstract':
            resolved.add(c)
    return resolved




def outputblock(block, target, varname, indent = ""):
    """Output the template block (identified by ``block``) for the target language"""

    if target == 'python':
        commentsign = '#'
    elif target == 'c++':
        commentsign = '//'
    else:
        raise NotImplementedError("Unknown target language: " + target)

    if block in blockhelp:
        s = indent + commentsign + blockhelp[block] + "\n" #output what each block does
    else:
        s = ''

    if block == 'header':
        s += indent + commentsign + "This file was last updated according to the FoLiA specification for version " + str(spec['version']) + " on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ", using foliaspec.py\n"
        s += indent + commentsign + "Code blocks after a foliaspec comment (until the next newline) are automatically generated. **DO NOT EDIT THOSE** and **DO NOT REMOVE ANY FOLIASPEC COMMENTS** !!!"
    elif block == 'version_major':
        versionfields = [ int(x) for x in spec['version'].split('.') ]
        s += indent + outputvar(varname, versionfields[0], target, True)
    elif block == 'version_minor':
        versionfields = [ int(x) for x in spec['version'].split('.') ]
        s += indent + outputvar(varname, versionfields[1] if len(versionfields) > 1 else 0, target, True)
    elif block == 'version_sub' or block == 'version_rev':
        versionfields = [ int(x) for x in spec['version'].split('.') ]
        s += indent + outputvar(varname, versionfields[2] if len(versionfields) > 2 else 0, target, True)
    elif block == 'attributes':
        if target == 'python':
            s += indent + "class Attrib:\n"
            s += indent + "    " +  ", ".join(spec['attributes']) + " = range(" + str(len(spec['attributes'])) + ")"
        elif target == 'c++':
            s += indent + "enum Attrib : int { NO_ATT=0, "
            value = 1
            for attrib in spec['attributes']:
                s +=  attrib + '=' + str(value) + ', '
                value *= 2
            s += 'ALL='+str(value) + ' };'
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'elementtype':
        if target == 'c++':
            s += indent + "enum ElementType : unsigned int { BASE=0,"
            s += ", ".join([ e + '_t' for e in elementnames]) + ", PlaceHolder_t, XmlComment_t, XmlText_t,  LastElement };\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'annotationtype':
        if target == 'python':
            s += indent + "class AnnotationType:\n"
            s += indent + "    " +  ", ".join(spec['annotationtype']) + " = range(" + str(len(spec['annotationtype'])) + ")"
        elif target == 'c++':
            s += indent + "enum AnnotationType : int { NO_ANN,"
            s += ", ".join(spec['annotationtype']) + ", LAST_ANN };\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'defaultproperties':
        if target == 'c++':
            s += indent + "ELEMENT_ID = BASE;\n"
            s += indent + "ACCEPTED_DATA.insert(XmlComment_t);\n"
            for prop, value in sorted(spec['defaultproperties'].items()):
                if target not in skip_properties or prop not in skip_properties[target]:
                    s += indent + outputvar( prop.upper(),  value, target) + '\n'
        elif target == 'python':
            for prop, value in sorted(spec['defaultproperties'].items()):
                s += indent + outputvar('AbstractElement.' + prop.upper(),  value, target) + '\n'
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'instantiateelementproperties':
        if target == 'c++':
            for element in elements:
                s += indent + "properties " + element['class'] + '::PROPS = DEFAULT_PROPERTIES;\n'
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'setelementproperties':
        if target == 'python':
            for element in elements:
                s += commentsign + "------ " + element['class'] + " -------\n"
                if 'properties' in element:
                    for prop, value in sorted(element['properties'].items()):
                        if prop == 'accepted_data':
                            value = tuple(sorted(addfromparents(element['class'],'accepted_data')))
                        s += indent + outputvar(element['class'] + '.' + prop.upper(),  value, target) + '\n'
        elif target == 'c++':
            done = {}
            defer = defaultdict(list) #defer output of some elements until parent elements are processed:  hook => deferred_elements
            for element in elements:
                output = setelementproperties_cpp(element,indent, defer,done)
                if output:
                    s += output
                    if element['class'] in defer:
                        for deferred in defer[element['class']]:
                            s += setelementproperties_cpp(deferred,indent, defer,done)

        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'annotationtype_string_map':
        if target == 'c++':
            s += indent + "const map<AnnotationType::AnnotationType,string> ant_s_map = {\n"
            s += indent + "  { AnnotationType::NO_ANN, \"NONE\" },\n"
            done = {}
            for element in elements:
                if 'properties' in element and  'annotationtype' in element['properties'] and element['properties']['annotationtype'] not in done:
                    #if 'primaryelement' in element['properties'] and not element['properties']['primaryelement']: continue #not primary, skip
                    s += indent + "  { AnnotationType::" + element['properties']['annotationtype'] + ',  "' + element['properties']['annotationtype'].lower() + '" },\n'
                    done[element['properties']['annotationtype']] = True #prevent duplicates
            s += indent + "};\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'string_annotationtype_map':
        if target == 'c++':
            s += indent + "const map<string,AnnotationType::AnnotationType> s_ant_map = {\n"
            s += indent + "  { \"NONE\", AnnotationType::NO_ANN },\n"
            done = {}
            for element in elements:
                if 'properties' in element and  'annotationtype' in element['properties'] and element['properties']['annotationtype'] not in done:
                    s += indent + '  { "' + element['properties']['annotationtype'].lower() + '", AnnotationType::' + element['properties']['annotationtype'] + ' },\n'
                    done[element['properties']['annotationtype']] = True #prevent duplicates
            s += indent + "};\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'annotationtype_xml_map':
        if target == 'python':
            s += indent + "ANNOTATIONTYPE2XML = {\n"
            for element in elements:
                if 'properties' in element and 'xmltag' in element['properties'] and element['properties']['xmltag'] and 'annotationtype' in element['properties']:
                    if 'primaryelement' in element['properties'] and not element['properties']['primaryelement']: continue #not primary, skip
                    s += indent + "    AnnotationType." + element['properties']['annotationtype'] + ':  "' + element['properties']['xmltag'] + '" ,\n'
            s += indent + "}"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'elementtype_string_map':
        if target == 'c++':
            s += indent + "const map<ElementType,string> et_s_map = {\n"
            s += indent + "  { BASE, \"FoLiA\" },\n"
            for element in elements:
                if 'properties' in element and 'xmltag' in element['properties'] and element['properties']['xmltag']:
                    s += indent + "  { " + element['class'] + '_t,  "' + element['properties']['xmltag'] + '" },\n'
                elif 'properties' in element and 'subset' in element['properties'] and element['properties']['subset']:
                    if element['class'] == 'HeadFeature':
                        s += indent + "  { HeadFeature_t,  \"headfeature\" },\n"
                    else:
                        s += indent + "  { " + element['class'] + '_t,  "' + element['properties']['subset'] + '" },\n'
                else:
                    s += indent + "  { " + element['class'] + '_t,  "_' + element['class'] + '" },\n'
            s += indent + '  { PlaceHolder_t, "_PlaceHolder" },\n'
            s += indent + '  { XmlComment_t, "_XmlComment" },\n'
            s += indent + '  { XmlText_t, "_XmlText" }\n'
            s += indent + "};\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'string_elementtype_map':
        if target == 'c++':
            s += indent + "const map<string,ElementType> s_et_map = {\n"
            s += indent + "  { \"FoLiA\", BASE },\n"
            for element in elements:
                if 'properties' in element and 'xmltag' in element['properties'] and element['properties']['xmltag']:
                    s += indent + '  { "' + element['properties']['xmltag'] + '", ' + element['class'] + '_t  },\n'
                elif 'properties' in element and 'subset' in element['properties'] and element['properties']['subset']:
                    if element['class'] == 'HeadFeature':
                        s += indent + "  { \"headfeature\", HeadFeature_t },\n"
                    else:
                        s += indent + '  { "' + element['properties']['subset'] + '", ' + element['class'] + '_t  },\n'
                else:
                    s += indent + '  { "_' + element['class'] + '", ' + element['class'] + '_t  },\n'
            s += indent + '  { "_PlaceHolder", PlaceHolder_t  },\n'
            s += indent + '  { "_XmlComment", XmlComment_t  },\n'
            s += indent + '  { "_XmlText", XmlText_t  }\n'
            s += indent + "};\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'string_class_map':
        if target == 'python':
            s += indent + "XML2CLASS = {\n"
            for element in elements:
                if 'properties' in element and 'xmltag' in element['properties'] and element['properties']['xmltag']:
                    s += indent + '    "' + element['properties']['xmltag'] + '": ' + element['class'] + ',\n'
            s += indent + "}\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'annotationtype_layerclass_map':
        if target == 'python':
            s += indent + "ANNOTATIONTYPE2LAYERCLASS = {\n"
            for element in elements:
                if element['class'].endswith('Layer'):
                    if 'properties' in element and 'xmltag' in element['properties'] and element['properties']['xmltag'] and 'annotationtype' in element['properties']:
                        s += indent + "    AnnotationType." + element['properties']['annotationtype'] + ':  ' + element['class'] + ' ,\n'
            s += indent + "}"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'default_ignore':
        if target == 'c++':
            s += indent + "const set<ElementType> default_ignore = { " + ", ".join([ e + '_t' for e in sorted(flattenclasses(spec['default_ignore'])) ]) + " };\n"
        elif target == 'python':
            s += indent + "default_ignore = ( " + ", ".join(spec['default_ignore']) + ",)\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'default_ignore_annotations':
        if target == 'c++':
            s += indent + "const set<ElementType> default_ignore_annotations = { " + ", ".join([ e + '_t' for e in sorted(flattenclasses(spec['default_ignore_annotations'])) ]) + " };\n"
        elif target == 'python':
            s += indent + "default_ignore_annotations = ( " + ", ".join(spec['default_ignore_annotations']) + ",)\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'default_ignore_structure':
        if target == 'c++':
            s += indent + "const set<ElementType> default_ignore_structure = { " + ", ".join([ e + '_t' for e in sorted(flattenclasses(spec['default_ignore_structure'])) ]) + " };\n"
        elif target == 'python':
            s += indent + "default_ignore_structure = ( " + ", ".join(spec['default_ignore_structure']) + ",)\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'typehierarchy':
        if target == 'c++':
            s += indent + "static const map<ElementType, set<ElementType> > typeHierarchy = { "
            for child, parentset in sorted(parents.items()):
                s += indent + "   { " + child + '_t' + ", { " + ",".join([p + '_t' for p in parentset ]) + " } },\n"
            s += indent + "   { PlaceHolder_t , { Word_t, AbstractStructureElement_t } }\n"
            s += indent + "};\n";
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'attributefeatures':
        if target == 'c++':
            l = []
            for element in elements:
                if 'properties' in element and 'subset' in element['properties'] and element['properties']['subset']:
                    if element['class'] == 'HeadFeature':
                        l.append("headfeature")
                    else:
                        l.append(element['properties']['subset'])
            l.sort()
            s += indent + "const set<string> AttributeFeatures = { " + ", ".join([ '"' + x + '"' for x in l ]) + " };\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block in spec:
        #simple variable blocks
        s += indent + outputvar(varname, spec[block], target, True)
    else:
        raise Exception("No such block exists in foliaspec: " + block)


    if s and s[-1] != '\n': s += '\n'
    return s


def parser(filename):
    if filename[-2:] in ('.h','.c') or filename[-4:] in ('.cxx','.cpp','.hpp'):
        target = 'c++' #libfolia
        commentsign = '//'
    elif filename[-3:] == '.py':
        target = 'python' #pynlpl.formats.folia
        commentsign = '#'
    else:
        raise Exception("No target language could be deduced from the filename " + filename)

    if not os.path.exists(filename):
        raise FileNotFoundError("File not found: " + filename)

    out = open(filename+'.foliaspec.out','w',encoding='utf-8')


    inblock = False
    blockname = blocktype = ""
    indent = ""
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            strippedline = line.strip()
            if not inblock:
                if strippedline.startswith(commentsign + 'foliaspec:'):
                    indent = line.find(strippedline) * ' '
                    fields = strippedline[len(commentsign):].split(':')
                    if fields[1] in ('begin','start'):
                        blocktype = 'explicit'
                        blockname = fields[2]
                        try:
                            varname = fields[3]
                        except:
                            varname = blockname
                    elif len(fields) >= 2:
                        blocktype = 'implicit'
                        blockname = fields[1]
                        try:
                            varname = fields[2]
                        except:
                            varname = blockname
                    else:
                        raise Exception("Syntax error: " + strippedline)
                    inblock = True
                    out.write(line)
                elif strippedline.split(' ')[-1].startswith(commentsign + 'foliaspec:'):
                    fields = strippedline.split(' ')[-1][len(commentsign):].split(':')
                    blocktype = 'line'
                    blockname = fields[1]
                    try:
                        varname = fields[2]
                    except:
                        varname = blockname
                    if varname != blockname:
                        out.write( outputblock(blockname, target, varname) + " " + commentsign + "foliaspec:" + blockname + ":" + varname + "\n")
                    else:
                        out.write( outputblock(blockname, target, varname) + " " + commentsign + "foliaspec:" + blockname + "\n")
                else:
                    out.write(line)
            else:
                if not strippedline and blocktype == 'implicit':
                    out.write(outputblock(blockname, target, varname,indent) + "\n")
                    inblock = False
                elif blocktype == 'explicit' and strippedline.startswith(commentsign + 'foliaspec:end:'):
                    out.write(outputblock(blockname, target, varname,indent) + "\n" + commentsign + "foliaspec:end:" + blockname + "\n")
                    inblock = False

    os.rename(filename+'.foliaspec.out', filename)

def usage():
    print("Syntax: foliaspec.py [filename] [filename] ..etc.." ,file=sys.stderr)
    print("Filenames are Python or C++ files that may contain foliaspec instructions, the files will be updated according to the latest specification in folia.yml",file=sys.stderr)
    sys.exit(0)

def main():
    if len(sys.argv) == 1:
        usage()

    for filename in sys.argv[1:]:
        if filename in ('-h', '--help'):
            usage()
        elif filename in ('-v', '--version'):
            print("FoLiA specification is at version v" + spec['version'],file=sys.stderr)
            sys.exit(0)

        parser(filename)

if __name__ == '__main__':
    main()
