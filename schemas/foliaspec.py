#!/usr/bin/env python3
#Generate library specification code (for either Python or C++) on the the basis of folia.yml
#Used by respectively pynlpl and libfolia
import sys
import datetime
import os
import yaml


#Load specification
spec = yaml.load(open('folia.yml','r'))

elements = getelements(spec) #gathers all class names
elements.sort(key=lambda x: x['class'])
elementnames = [ e['class'] for e in elements ]

def getelements(d):
    elements = []
    if 'elements' in d:
        for e in d['elements']:
            elements.append(e)
            elements += getelements(e)

    return elements

################################################################

def outputvar(var, value, target, declare = False):
    quote = var in ('version','namespace','TEXTDELIMITER','XMLTAG')  #values are string literals rather than enums or classes

    if target == 'python':
        if isinstance(value, bool):
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
        if isinstance(value, bool):
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


def outputblock(block, target, indent = ""):
    if target == 'python':
        commentsign = '#'
    elif target == 'c++':
        commentsign = '//'

    s = '' #the output
    if block == 'header':
        s += indent + commentsign + "This file was last updated according to the FoLiA specification for version " + str(spec['version']) + " on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ", using foliaspec.py"
        s += indent + commentsign + "Do not remove any foliaspec comments!!!"

    elif block == 'attributes':
        if target == 'python':
            s += indent + "class Attrib:\n"
            s += indent + "    " +  ", ".join(spec['attributes']) + " = range(len( " + str(spec['attributes']) + "))"
        elif target == 'c++':
            s += indent + "enum Attrib : int { NO_ATT=0, "
            value = 1
            for attrib in spec['attributes']:
                s =  attrib + '=' + str(value) + ', '
                value *= 2
            s += 'ALL='+str(value) + ' };'
    elif block == 'annotationtype':
        if target == 'python':
            s += indent + "class AnnotationType:\n"
            s += indent + "    " +  ", ".join(spec['annotationtype']) + " = range(len( " + str(spec['annotationtype']) + "))"
        elif target == 'c++':
            s += indent + "enum AnnotationType : int { NO_ANN, "
            s += indent + ", ".join(spec['annotationtype']) + ", LAST_ANN };"
    elif block == 'initelementproperties':
        if target == 'c++':
            for element in elements:
                s += indent + "properties " + element['class'] + '::PROPS = DEFAULT_PROPERTIES;\n'
    elif block == 'setelementproperties':
        if target == 'python':
            for element in elements:
                s += commentsign + "------ " + element['class'] + " -------\n"
                if 'properties' in element:
                    for prop, value in element['properties'].items:
                        s += indent + outputvar(element['class'] + '.' + prop.upper(),  value, target) + '\n'
        elif target == 'c++':
            for element in elements:
                s += commentsign + "------ " + element['class'] + " -------\n"
                s += indent + element['class'] + '::PROPS.ELEMENT_ID = ' + element['class'] + '_t;\n'
                if 'properties' in element:
                    for prop, value in element['properties'].items:
                        s += indent + outputvar(element['class'] + '::PROPS.' + prop.upper(),  value, target) + '\n'
    else:
        if block in spec:
            outputvar(block, spec[block], target, True, quote)
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
                    if len(fields) == 3 and field[1] in ('begin','start'):
                        blocktype = 'explicit'
                        blockname = field[2]
                    elif len(fields) == 2:
                        blocktype = 'implicit'
                        blockname = field[1]
                    else:
                        raise Exception("Syntax error: " + strippedline)
                    inblock = True
                    out.write(line)
                elif strippedline.split(' ')[-1].startswith(comment + 'foliaspec:'):
                    fields = strippedline.split(' ')[-1][len(commentsign):].split(':')
                    blocktype = 'line'
                    blockname = field[1]
                    out.write( outputblock(blockname, target) + " " + commentsign + "foliaspec:" + blockname + "\n")
                else:
                    out.write(line)
            else:
                if not strippedline and blocktype == 'implicit':
                    out.write(outputblock(blockname, target) + "\n")
                    inblock = False
                elif blocktype == 'explicit' and strippedline.startswith(commentsign + 'foliaspec:end:'):
                    out.write(outputblock(blockname, target) + "\n")
                    inblock = False

    os.rename(filename+'.foliaspec.out', filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Syntax: foliaspec.py [filename] [filename].." ,file=sys.stderr)
        print("Filenames are Python or C++ files containing foliaspec instructions, the files will be updated according to the latest specification in folia.yml",file=sys.stderr)

    for filename in sys.argv[1:]:
        parser(filename)

