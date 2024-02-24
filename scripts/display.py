import time,os,platform

banner = """
                                   _                             _
                                  / \\   ___ ___ ___  _   _ _ __ | |_
                                 / _ \\ / __/ __/ _ \\| | | | '_ \\| __|
                                / ___ \\ (_| (_| (_) | |_| | | | | |_
                               /_/   \\_\\___\\___\\___/ \\__,_|_| |_|\\__|

                                         _____     _
                                        |_   _|_ _| | _____
                                          | |/ _` | |/ / _ \\
                                          | | (_| |   <  __/
                                          |_|\\__,_|_|\\_\\___|

                                         ___
                                        / _ \\__   _____ _ __
                                       | | | \\ \\ / / _ \\ '__|
                                       | |_| |\\ V /  __/ |
                                        \\___/  \\_/ \\___|_|

         Departement Cyber Security                                     Account Take Over tool For CRMS                               
"""

# Split the banner into lines
lines = banner.split('\n')

# Clean Screen
def clear_screen():
    system_platform = platform.system()

    if system_platform == "Windows":
        os.system("cls")
    elif system_platform == "Linux":
        os.system("clear")
    else:
        pass


# Print each line with a delay
def banner_display():
    clear_screen()
    for line in lines:
        print(line)
        time.sleep(0.1)  # Adjust the delay time as needed
