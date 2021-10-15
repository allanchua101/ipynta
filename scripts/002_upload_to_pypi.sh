#!/bin/bash

cd ./src

# Step 1: Create distribution directory
DIR="./dist"

python setup.py sdist

# Step 2: Bump version of app
# TODO:

# Step 3: Upload to PyPi
echo "Uploading to PyPi!!!"
twine upload dist/*
