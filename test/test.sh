#!/bin/bash

FAILURE=0
for f in ../examples/*.folia.xml; do
    echo "Validating $(basename $f) against RelaxNG schema..."
    xmllint --relaxng ../schemas/folia.rng $f > /dev/null
    if [ $? -ne 0 ]; then
        echo "...FAILED" >&2
        FAILURE=1
    else
        echo "...OK" >&2
    fi
done

exit $FAILURE
