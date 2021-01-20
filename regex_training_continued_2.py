import re

user_input = input("Please enter \"Yes\" or \"No\": ")

print(re.fullmatch(r"yes|no", user_input, re.IGNORECASE))