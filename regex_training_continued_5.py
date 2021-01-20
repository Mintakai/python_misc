import random, re

def r(m):
    return m.group(0)+random.choice(("Script", "++"))

s = input("?")

print(re.sub(r"Shell|Power", r, s))