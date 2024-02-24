#!/bin/bash

# Set the path to your Python interpreter
PYTHON_EXECUTABLE=python3

# Set the path where you want to create the virtual environment
VENV_DIR=env

# Set the path to your main.py file
MAIN_SCRIPT=main.py

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Run main.py
$PYTHON_EXECUTABLE $MAIN_SCRIPT

# Deactivate the virtual environment
deactivate
