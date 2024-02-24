@echo off

REM Set the path to your Python interpreter
set PYTHON_EXECUTABLE=python

REM Set the path where you want to create the virtual environment
set VENV_DIR=env

REM Set the path to your main.py file
set MAIN_SCRIPT=main.py

REM Activate the virtual environment
call %VENV_DIR%\Scripts\activate

REM Run main.py
python %MAIN_SCRIPT%
