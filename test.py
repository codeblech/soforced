import string
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

for i in combinations():
    print(i)