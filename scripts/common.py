import os
from datetime import datetime

# Generate To Filename 
def f_name(name,user_hash):
    last_4_digits = user_hash[-4:]
    return f"{name}_{last_4_digits}"

# Wrtie To File
def write_to_file(filename, data):
    base_directory = os.getcwd()
    report_directory = os.path.join(base_directory, 'reports')
    os.makedirs(report_directory, exist_ok=True)

    # Generate a filename based on the current date and time
    file_name = f"{filename}.txt"
        
    # Create the full path to the file
    file_path = os.path.join(report_directory, file_name)

    # Write data to the file
    with open(file_path, 'a') as file:
        file.write(data)