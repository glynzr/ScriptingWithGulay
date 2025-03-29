# the purpose of this script is to scan given IPs with Nextpose

import requests
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ip_list_file = "ips.txt"

#session_id = input("Enter your NexposeCCSessionID: ")
nextpose_host=input("Enter nextpose server IP:")
nextpose_port=input("Enter nextpose service port:")

#result files
alive_file = "alive_ips.txt"
down_file = "down_ips.txt"

# Required headers(extracted from Burp Suite)
headers = {
    "Host": "10.13.187.72:3780",
    "Cookie": "time-zone-offset=-240; nexposeCCSessionID=<your nextpose session id>; TIMEOUT=session-alive; i18next=en",
    "Sec-Ch-Ua-Platform": "\"Windows\"",# depending on the OS you use it should be changed
    "Nexposeccsessionid": "<your nextpose session id",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://10.13.187.72:3780",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://10.13.187.72:3780/admin/global/diag_console.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i",
    "Connection": "keep-alive"
}

url = "https://"+nextpose_host+nextpose_port+"/data/diagnostics/command"


with open(ip_list_file, "r") as file:
    ip_list = [line.strip() for line in file.readlines()]

for ip in ip_list:
    data = {"command": f"ping {ip}"} 
    #print(data)
    try:
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=10)
        if response.status_code == 200:
            if "ALIVE" in response.text:
                print(f"{ip} is ALIVE")
            else:
                print(f"{ip} is DOWN")
        else:
            print(f"{ip} - Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{ip} - ERROR: {e}")

