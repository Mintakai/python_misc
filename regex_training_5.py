import re
import string

iterate = string.ascii_lowercase

expressions = ["\w{8,20}", "^\w{8,20}$", "^[a-za-Z0-9]{8,20}$", "^[a-za-Z0-9]{8, 20}$", "^[a-za-Z0-9]{8, 20}"]

pw = input("Enter password: ")

def result(p,s):
    try:
        return re.match(p,s)
    except re.error:
        return "Error"

for i in range(0, 5):
    if result(expressions[i], pw) == "Error" or result(expressions[i], pw) == None:
        print(f"Doesn't work with {expressions[i]} ({iterate[i]})")
    else:
        print(result(expressions[i], pw))
