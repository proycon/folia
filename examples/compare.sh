# /bin/sh

OK="\033[1;32m OK  \033[0m"
PROBLEM="\033[1;31m DISAGREE \033[0m"

for file in *.xml tests/*.xml erroneous/*.xml
do
    folialint --nooutput $file >& /dev/null
    lintstat=$?
    foliavalidator $file >& /dev/null
    valstat=$?
    if [ $lintstat != $valstat ]
    then
	echo -e $file $PROBLEM folialint=$lintstat foliavalidator=$valstat
    else
	echo -e $file $OK
    fi
done
