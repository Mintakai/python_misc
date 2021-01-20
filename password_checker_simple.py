import re

check = "^\w{8,20}$"

pw = input("Enter password: ")

def result(p,s):
    try:
        return re.match(p,s)
    except re.error:
        return "Error"

access = str(result(check,pw))

if access == "Error" or access == None:
    print("Invalid password!")
else:
    print("Password accepted")