#!/bin/bash

cd ../

echo "Uploading to PyPi!!!"
twine upload dist/*
