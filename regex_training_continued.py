import re

word = input("Enter a string: ")

print(re.sub(r"-?\d+", "XXX", word))