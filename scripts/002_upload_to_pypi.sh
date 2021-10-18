#!/bin/bash
set -e

DIST_DIR="./dist"

cd ../src

# Step 1: Remove old distribution directory
rm -rf $DIST_DIR

# Step 1: Create distribution directory

python setup.py sdist

# Step 2: Bump version of app
# TODO:

# Step 3: Upload to PyPi
echo "Uploading to PyPi!!!"
twine upload dist/*
