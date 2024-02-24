#!/bin/bash

# Set the path to your Python interpreter
PYTHON_EXECUTABLE=python3

# Set the path where you want to create the virtual environment
VENV_DIR=env

# Set the path to your requirements.txt file
REQUIREMENTS_FILE=requirements.txt

# Create a virtual environment
$PYTHON_EXECUTABLE -m venv $VENV_DIR

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Install requirements
pip install -r $REQUIREMENTS_FILE

echo "Virtual environment created and activated. Requirements installed."
