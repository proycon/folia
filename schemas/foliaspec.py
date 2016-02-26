#!/usr/bin/env python3
#Generate library specification code (for either Python or C++) on the the basis of folia.yml
#Used by respectively pynlpl and libfolia
import sys
import datetime
import os
from collections import defaultdict
import yaml


#Load specification
spec = yaml.load(open('folia.yml','r'))


parents = defaultdict(set)

def getelements(d):
    global parents
    elements = []
    if 'elements' in d:
        for e in d['elements']:
            elements.append(e)
            children = getelements(e)
            elements += children
            for c in children:
                parents[c['class']].add(e['class'])
    return elements

elements = getelements(spec) #gathers all class names
elements.sort(key=lambda x: x['class'])
elementnames = [ e['class'] for e in elements ]


################################################################

def addfromparents(elementname, key, value):
    newvalue = set()
    for parent in parents[key]:
        newvalue |= addfromparents(parent, key, newvalue)
    return newvalue



def outputvar(var, value, target, declare = False):
    """Output a variable ``var`` with value ``value`` in the specified target language."""

    #do we need to quote the value? (bool)
    quote = var in ('version','namespace','TEXTDELIMITER','XMLTAG')  #these values are string literals rather than enums or classes, so yes

    if target == 'python':
        if value is None:
                return var + ' = None'
        elif isinstance(value, bool):
            if value:
                return var + ' = True'
            else:
                return var + ' = False'
        elif isinstance(value, (int, float) ):
            return var + ' = ' + str(value)
        elif isinstance(value, list):
            if all([ x in elementnames for x in value ]) or  all([ x in spec['attributes'] for x in value ]):
                return var + ' = (' + ', '.join(value) + ',)'

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
            if var in ('REQUIRED_ATTRIBS','OPTIONAL_ATTRIBS'):
                return var + ' = NO_ATT;'
            elif var == 'ANNOTATIONTYPE':
                return var + ' = AnnotationType::NO_ANN;'
            elif var in ('XMLTAG','TEXTDELIMITER'):
                return var + ' = "NONE"'
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
        elif isinstance(value, list):
            #list items are  enums or classes, never string literals
            if all([ x in elementnames for x in value ]):
                if declare:
                    typedeclarion = 'const set<ElementType> '
                    operator = '='
                else:
                    typedeclaration = ''
                    operator += '+='
                value = [ x + '_t' for x in value ]

                return typedeclaration + var + ' ' + operator + ' {' + ', '.join(value) + '};'
            elif all([ x in spec['attributes'] for x in value ]):
                return var + ' = ' + '|'.join(value)
            else:
                return typedeclaration + var + ' = { ' + ', '.join([ '"' + x + '"' for x in value]) + ', }'
        else:
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
        'annotationtype_string_map': 'A mapping from annotation types to strings (xml tag)',
        'string_annotationtype_map': 'A mapping from strings (xml tag) to annotation types',
        'structurescope': 'Structure scope above the sentence level, used by next() and previous() methods',
        'defaultproperties': 'Default properties which all elements inherit',
        'default_ignore': 'Default ignore list for the select() method, do not descend into these',
        'default_ignore_annotations': 'Default ignore list for token annotation',
        'default_ignore_structure': 'Default ignore list for structure annotation',
}

def outputblock(block, target, varname, indent = ""):
    """Output the template block (identified by ``block``) for the target language"""

    if target == 'python':
        commentsign = '#'
    elif target == 'c++':
        commentsign = '//'
    else:
        raise NotImplementedError("Unknown target language: " + target)

    if block in blockhelp:
        s = indent + commentsign + blockhelp[block]  #output what each block does
    else:
        s = ''

    if block == 'header':
        s += indent + commentsign + "This file was last updated according to the FoLiA specification for version " + str(spec['version']) + " on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ", using foliaspec.py"
        s += indent + commentsign + "Code blocks after a foliaspec comment (until the next newline) are automatically generated. **DO NOT EDIT THOSE** and **DO NOT REMOVE ANY FOLIASPEC COMMENTS** !!!"
    elif block == 'version_major':
        versionfields = [ int(x) for x in spec['version'].split('.') ]
        outputvar(varname, versionfields[0], target, True)
    elif block == 'version_minor':
        versionfields = [ int(x) for x in spec['version'].split('.') ]
        outputvar(varname, versionfields[1] if len(versionfields) > 1 else 0, target, True)
    elif block == 'version_sub' or block == 'version_rev':
        versionfields = [ int(x) for x in spec['version'].split('.') ]
        outputvar(varname, versionfields[2] if len(versionfields) > 2 else 0, target, True)
    elif block == 'attributes':
        if target == 'python':
            s += indent + "class Attrib:\n"
            s += indent + "    " +  ", ".join(spec['attributes']) + " = range(len( " + str(spec['attributes']) + "))"
        elif target == 'c++':
            s += indent + "enum Attrib : int { NO_ATT=0, "
            value = 1
            for attrib in spec['attributes']:
                s +=  attrib + '=' + str(value) + ', '
                value *= 2
            s += 'ALL='+str(value) + ' };'
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'annotationtype':
        if target == 'python':
            s += indent + "class AnnotationType:\n"
            s += indent + "    " +  ", ".join(spec['annotationtype']) + " = range(len( " + str(spec['annotationtype']) + "))"
        elif target == 'c++':
            s += indent + "enum AnnotationType : int { NO_ANN,"
            s += ", ".join(spec['annotationtype']) + ", LAST_ANN };\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'defaultproperties':
        if target == 'c++':
            s += indent + "properties DEFAULT_PROPERTIES;\n"
            s += indent + "DEFAULT_PROPERTIES.ELEMENT_ID = BASE;\n"
            s += indent + "DEFAULT_PROPERTIES.ACCEPTED_DATA.insert(XmlComment_t);\n"
            for prop, value in spec['defaultproperties'].items():
                if prop not in ('textcontainer','phoncontainer'): #these two are not yet handled in libfolia, filter out (MAYBE TODO, add it libfolia?)
                    s += indent + outputvar('DEFAULT_PROPERTIES.' + prop.upper(),  value, target) + '\n'
        elif target == 'python':
            for prop, value in spec['defaultproperties'].items():
                s += indent + outputvar(prop.upper(),  value, target) + '\n'
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
                    for prop, value in element['properties'].items():
                        if prop == 'accepted_data': value = tuple(addfromparents(element['class'],'accepted_data',value))
                        s += indent + outputvar(element['class'] + '.' + prop.upper(),  value, target) + '\n'
        elif target == 'c++':
            for element in elements:
                s += commentsign + "------ " + element['class'] + " -------\n"
                s += indent + element['class'] + '::PROPS.ELEMENT_ID = ' + element['class'] + '_t;\n'
                if 'properties' in element:
                    for prop, value in element['properties'].items():
                        if prop == 'accepted_data': value = tuple(addfromparents(element['class'],'accepted_data',value))
                        s += indent + outputvar(element['class'] + '::PROPS.' + prop.upper(),  value, target) + '\n'
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'annotationtype_string_map':
        if target == 'c++':
            s += indent + "const map<AnnotationType::AnnotationType,string> ant_s_map = {\n"
            s += indent + "  { AnnotationType::NO_ANN, \"NONE\" },\n"
            for element in elements:
                if 'properties' in element and 'xmltag' in element['properties'] and 'annotationtype' in element['properties']:
                    s += indent + "  { AnnotationType::" + element['properties']['annotationtype'] + ',  "' + element['properties']['xmltag'] + '" },\n'
            s += indent + "};\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'string_annotationtype_map':
        if target == 'c++':
            s += indent + "const map<string,AnnotationType::AnnotationType> s_ant_map = {\n"
            s += indent + "  { \"NONE\", AnnotationType::NO_ANN },\n"
            for element in elements:
                if 'properties' in element and 'xmltag' in element['properties'] and 'annotationtype' in element['properties']:
                    s += indent + '  { "' + element['properties']['xmltag'] + '", AnnotationType::' + element['properties']['annotationtype'] + ' },\n'
            s += indent + "};\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'elementtype_string_map':
        if target == 'c++':
            s += indent + "const map<ElementType,string> et_s_map = {\n"
            s += indent + "  { BASE, \"FoLiA\" },\n"
            for element in elements:
                if 'properties' in element and 'xmltag' in element['properties']:
                    s += indent + "  { " + element['class'] + '_t,  "' + element['properties']['xmltag'] + '" },\n'
            s += indent + "};\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'string_elementtype_map':
        if target == 'c++':
            s += indent + "const map<string,ElementType> s_et_map = {\n"
            s += indent + "  { \"FoLiA\", BASE },\n"
            for element in elements:
                if 'properties' in element and 'xmltag' in element['properties']:
                    s += indent + '  { "' + element['properties']['xmltag'] + '", ' + element['class'] + '_t  },\n'
            s += indent + "};\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'default_ignore':
        if target == 'c++':
            s += indent + "const set<ElementType> default_ignore = { " + ", ".join([ e + '_t' for e in spec['default_ignore'] ]) + " };\n"
        elif target == 'python':
            s += indent + "default_ignore = ( " + ", ".join(spec['default_ignore']) + ",)\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'default_ignore_annotations':
        if target == 'c++':
            s += indent + "const set<ElementType> default_ignore_annotations = { " + ", ".join([ e + '_t' for e in spec['default_ignore_annotations'] ]) + " };\n"
        elif target == 'python':
            s += indent + "default_ignore_annotations = ( " + ", ".join(spec['default_ignore_annotations']) + ",)\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block == 'default_ignore_structure':
        if target == 'c++':
            s += indent + "const set<ElementType> default_ignore_structure = { " + ", ".join([ e + '_t' for e in spec['default_ignore_structure'] ]) + " };\n"
        elif target == 'python':
            s += indent + "default_ignore_structure = ( " + ", ".join(spec['default_ignore_structure']) + ",)\n"
        else:
            raise NotImplementedError("Block " + block + " not implemented for " + target)
    elif block in spec:
        #simple variable blocks
        outputvar(varname, spec[block], target, True)
    else:
        raise Exception("No such block exists in foliaspec: " + block)


    if s and s[-1] != '\n': s += '\n'
    return s


def parser(filename):
    if filename[-2:] in ('.h','.c') or filename[-4:] in ('.cxx','.cpp','.hpp'):
        target = 'c++' #libfolia
        commentsign = '//'
    elif filename[-3] == '.py':
        target = 'python' #pynlpl.formats.folia
        commentsign = '#'
    else:
        raise Exception("No target language could be deduced from the filename " + filename)

    if not os.path.exists(filename):
        raise FileNotFoundError("File not found: " + filename)

    out = open(filename+'.foliaspec.out','w',encoding='utf-8')


    inblock = False
    blockname = blocktype = ""
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            strippedline = line.strip()
            if not inblock:
                if strippedline.startswith(commentsign + 'foliaspec:'):
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
                    out.write(outputblock(blockname, target, varname) + "\n")
                    inblock = False
                elif blocktype == 'explicit' and strippedline.startswith(commentsign + 'foliaspec:end:'):
                    out.write(outputblock(blockname, target, varname) + "\n")
                    inblock = False

    os.rename(filename+'.foliaspec.out', filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Syntax: foliaspec.py [filename] [filename].." ,file=sys.stderr)
        print("Filenames are Python or C++ files that may contain foliaspec instructions, the files will be updated according to the latest specification in folia.yml",file=sys.stderr)

    for filename in sys.argv[1:]:
        parser(filename)

