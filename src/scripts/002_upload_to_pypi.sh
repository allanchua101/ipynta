#!/bin/bash

cd ../

# Step 1: Create distribution directory
DIR="./dist"

python setup.py sdist

# Step 2: Upload to PyPi
echo "Uploading to PyPi!!!"
twine upload dist/*
