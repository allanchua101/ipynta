#!/bin/bash

cd ../..

# Step 1: Setup virtual environment
if [ -d "./venv" ]; then
  echo "Virtual environment already configured..."
else
  echo "Creating our virtual environment.."
  python3 -m venv venv
fi

# Step 2: Activate virtual environment
echo "Activating virtual environment..."
source ./venv/bin/activate

# Step 3: Install latest pip
echo "Upgrading pip environment..."
pip3 install --upgrade pip

# Step 4: Install package dependencies
echo "Installing package dependencies..."
python3 -m pip install -r requirements.txt

cd ./src

# Step 5: Create distribution directory
DIR="./dist"

if [ -d "$DIR" ]; then
  echo "Distribution directory already exists..."
else
  echo "Creating our distribution directory..."
  python setup.py sdist
fi
