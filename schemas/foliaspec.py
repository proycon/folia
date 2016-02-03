#!/usr/bin/env python3
#Generate library specification code (for either Python or C++) on the the basis of folia.yml
#Used by respectively pynlpl and libfolia
import sys
import yaml



spec = yaml.load(open('folia.yml','r'))

varmap_pynlpl = {
    'xmltag': 'XMLTAG',
    'required_attributes': 'REQUIRED_ATTRIBS',
    'optional_attributes': 'OPTIONAL_ATTRIBS',
    'occurrences': 'OCCURRENCES',
    'occurrences_per_set': 'OCCURRENCES_PER_SET',
    'accepted_data': 'ACCEPTED_DATA',
    'annotationtype': 'ANNOTATIONTYPE',
    'textdelimiter': 'TEXTDELIMITER',
    'printable': 'PRINTABLE',
    'speakable': 'SPEAKABLE',
    'xlink': 'XLINK',
    'authoritative': 'AUTH',
    'textcontainer': 'TEXTCONTAINER',
    'phoncontainer': 'PHONCONTAINER',
    'rootelement': 'ROOTELEMENT',
}

varmap_libfolia = {
    'xmltag': '_xmltag',
    'required_attributes': '_required_attributes',
    'optional_attributes': '_optional_attributes',
    'occurrences': '_occurences',
    'occurrences_per_set': '_occurrences_per_set',
    'accepted_data': '_accepted_data',
    'annotationtype': '_annotation_type',
    'textdelimiter': 'TEXTDELIMITER',
    'printable': 'PRINTABLE',
    'speakable': 'SPEAKABLE',
    'xlink': 'XLINK',
    'authoritative': '',
    'textcontainer': '',
    'phoncontainer': '',
    'rootelement': ''
}



def outputvar(var):
    if target == 'pynlpl':

        if var in varmap_pynlpl:
            libvar = varmap_pynlpl[var]
        else:
            libvar = var
        if libvar:
            if isinstance(spec[var], bool):
                if spec[var]:
                    print(libvar + ' = True')
                else:
                    print(libvar + ' = False')
            elif isinstance(spec[var], (int, float) ):
                print(libvar + ' = ' + str(spec[var]))
            else:
                print(libvar + ' = "' + spec[var] + '"')

    elif target == 'libfolia':

        if var in varmap_libfolia:
            libvar = varmap_libfolia[var]
        else:
            libvar = var

        if libvar:
            if isinstance(spec[var], bool):
                if spec[var]:
                    print(libvar + ' = true')
                else:
                    print(libvar + ' = false')
            elif isinstance(spec[var], int ):
                print(libvar + ' = ' + str(spec[var]) + ';')
            else:
                print(libvar + ' = "' + spec[var] + '";')

def outputdefaultproperties():
    if target == 'libfolia':
	for element in allelements:


out = {
    'foliaspec.py': open('foliaspec.py','w',encoding='utf-8'),
    'folia_properties.cxx': open('folia_properties.cxx','w',encoding='utf-8'),
    'folia_types.h': open('folia_types.h','w',encoding='utf-8'),
}



def outputblock(block, target, indent = ""):
    if target == 'python':
        commentsign = '#'
    elif target == 'c++':
        commentsign = '//'

    s = '' #the output
    if block == 'header'
        s += indent + commentsign + "This file was last updated according to the FoLiA specification for version " + str(spec['version']) + " on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ", using foliaspec.py"
        s += indent + commentsign + "Do not remove any foliaspec comments!!!"

    if block == 'attributes':
        if target == 'python':
            s += indent + "class Attrib:\n"
            s += indent + "    " +  ", ".join(spec['attributes']) + " = range(len( " + str(spec['attributes']) + "))" )
        elif target == 'c++':
            s += indent + "enum Attrib : int { NO_ATT=0, ")
            value = 1
            for attrib in spec['attributes']:
                s =  attrib + '=' + str(value) + ', ')
                value *= 2
            s += 'ALL='+str(value) + ' };'


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

