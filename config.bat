@echo off

REM Set the path to your Python interpreter
set PYTHON_EXECUTABLE=python

REM Set the path where you want to create the virtual environment
set VENV_DIR=env

REM Set the path to your requirements.txt file
set REQUIREMENTS_FILE=requirements.txt

REM Create a virtual environment
%PYTHON_EXECUTABLE% -m venv %VENV_DIR%

REM Activate the virtual environment
call %VENV_DIR%\Scripts\activate

REM Install requirements
pip install -r %REQUIREMENTS_FILE%

echo Virtual environment created and activated. Requirements installed.

