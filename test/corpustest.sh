#!/bin/bash

if [ -z "$1" ]; then
    echo "Expected a directory" >&2
    exit 2
fi

DIR=$1

FAILURE=0

for doc in $DIR/*.xml; do

    echo "Processing $doc">&2

    echo "    Validating using RelaxNG stylesheet..." >&2
    xmllint --relaxng ../schemas/folia.rng "$doc" >/dev/null
    if [ $? -ne 0 ]; then
        echo "...FAILED" >&2
        FAILURE=1
    else
        echo "...OK" >&2
    fi

    echo "    Running foliavalidator..." >&2
    foliavalidator "$doc" >/dev/null
    if [ $? -ne 0 ]; then
        echo "...FAILED" >&2
        FAILURE=1
    else
        echo "...OK" >&2
    fi

    echo "    Running folialint..." >&2
    folialint "$doc" >/dev/null
    if [ $? -ne 0 ]; then
        echo "...FAILED" >&2
        FAILURE=1
    else
        echo "...OK" >&2
    fi

done

exit $FAILURE
