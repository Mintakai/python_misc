import re
import string

iterate = string.ascii_lowercase
expressions = ["^[0-9][0-9][0-9][0-9][0-9]$", "^\d{5}$", "^[0-9]{5}$", "^\d\d\d\d\d$", "^00000-99999$"]

word_1 = "12345"
word_2 = "00200"


def result(p,s):
    try:
        return re.match(p,s)
    except re.error:
        return "Error"

for i in range(0, 5):
    print(f"\n---Results for {expressions[i]} ({iterate[i]})---")
    print(result(expressions[i], word_1))
    print(result(expressions[i], word_2))