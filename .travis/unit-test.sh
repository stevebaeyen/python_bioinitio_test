#!/bin/bash

set -e
errors=0

# Run unit tests
python python_bioinitio_test/python_bioinitio_test_test.py || {
    echo "'python python/python_bioinitio_test/python_bioinitio_test_test.py' failed"
    let errors+=1
}

# Check program style
pylint -E python_bioinitio_test/*.py || {
    echo 'pylint -E python_bioinitio_test/*.py failed'
    let errors+=1
}

[ "$errors" -gt 0 ] && {
    echo "There were $errors errors found"
    exit 1
}

echo "Ok : Python specific tests"
