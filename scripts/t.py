import requests
import os
from datetime import datetime
def change_password(url,new_pass):

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
        "Aa222@22.\r\n"
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

    response = requests.post(url, headers=headers, data=data)

    print(response.text)



def write_to_file(filename, data):
    base_directory = os.getcwd()
    report_directory = os.path.join(base_directory, 'reports')
    os.makedirs(report_directory, exist_ok=True)

    # Generate a filename based on the current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"{filename}_{timestamp}.txt"
        
    # Create the full path to the file
    file_path = os.path.join(report_directory, file_name)

    # Write data to the file
    with open(file_path, 'w') as file:
        file.write(data)

write_to_file("aa","Description For tgest")