import re
import string


def generate_combinations(pattern):
    def backtrack(combo, index):
        if index == len(pattern):
            if re.match(pattern, combo):
                combinations.append(combo)
            return

        if pattern[index] == "\\d":
            for digit in range(10):
                backtrack(combo + str(digit), index + 1)
        elif pattern[index] == "[A-Z]":
            for letter in string.ascii_uppercase:
                backtrack(combo + letter, index + 1)

    combinations = []
    backtrack("", 0)
    return combinations


# Define the regular expression pattern
pattern = r"\d\d\d\d\d\d[A-Z][A-Z]"

# Generate and print the combinations
combinations = generate_combinations(pattern)
for combo in combinations:
    print(combo)
