#!/bin/bash

FAILURE=0


echo "Running validator..." >&2
foliavalidator example.xml
if [ $? -ne 0 ]; then
    echo "...FAILED" >&2
    FAILURE=1
else
    echo "...OK" >&2
fi

echo "Running validator (2)..." >&2
foliavalidator test.xml
if [ $? -ne 0 ]; then
    echo "...FAILED" >&2
    FAILURE=1
else
    echo "...OK" >&2
fi

echo "Running folia2txt" >&2
folia2txt test.xml > test.tmp
if [ $? -ne 0 ]; then
    echo "...FAILED" >&2
    FAILURE=1
else
    diff test.tmp test.txt > test.diff
    if [ $? -ne 0 ]; then
        echo "...FAILED" >&2
        FAILURE=0
        cat test.diff
    else
        echo "...OK" >&2
    fi
fi

echo "Running folia2columns" >&2
folia2columns -c id,text,pos,lemma test.xml > test.tmp
if [ $? -ne 0 ]; then
    echo "...FAILED" >&2
    FAILURE=1
else
    diff test.tmp test.columns.txt > test.diff
    if [ $? -ne 0 ]; then
        echo "...FAILED" >&2
        FAILURE=1
        cat test.diff
    else
        echo "...OK" >&2
    fi
fi


echo "Running folia2annotatedtxt" >&2
folia2annotatedtxt -c id,text,pos,lemma test.xml > test.tmp
if [ $? -ne 0 ]; then
    echo "...FAILED" >&2
    FAILURE=1
else
    diff test.tmp test.annotated.txt > test.diff
    if [ $? -ne 0 ]; then
        echo "...FAILED" >&2
        FAILURE=1
        cat test.diff
    else
        echo "...OK" >&2
    fi
fi

#echo "Running folia2html" >&2
#folia2html test.xml > test.tmp
#if [ $? -ne 0 ]; then
#    echo "...FAILED" >&2
#    FAILURE=1
#else
#    diff test.tmp test.html > test.diff
#    if [ $? -ne 0 ]; then
#        echo "...FAILED" >&2
#        FAILURE=1
#        cat test.diff
#    else
#        echo "...OK" >&2
#    fi
#fi


echo "Running foliaquery" >&2
foliaquery --text "zin" test.xml > test.tmp
if [ $? -ne 0 ]; then
    echo "...FAILED" >&2
    FAILURE=1
else
    diff test.tmp test.query1 > test.diff
    if [ $? -ne 0 ]; then
        echo "...FAILED" >&2
        FAILURE=1
        cat test.diff
    else
        echo "...OK" >&2
    fi
fi

echo "Running foliaquery (2)" >&2
foliaquery --pos "{(A|T).*} {N\(.*}" test.xml > test.tmp
if [ $? -ne 0 ]; then
    echo "...FAILED" >&2
    FAILURE=1
else
    diff test.tmp test.query2 > test.diff
    if [ $? -ne 0 ]; then
        echo "...FAILED" >&2
        FAILURE=1
        cat test.diff
    else
        echo "...OK" >&2
    fi
fi

exit $FAILURE


