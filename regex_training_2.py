import re
import string

iterate = string.ascii_lowercase
expressions = ["^\w+$", "^[^\s]*$", "^[^ ]+$", "^[^ ]*$", "^ +$"]

word_1 = "fine123"
word_2 = "Example"
word_3 = ".?!"

word_4 = " Leading"
word_5 = "Two\tParts"
word_6 = "trailing "


def result(p,s):
    try:
        return re.match(p,s)
    except re.error:
        return "Error"

for i in range(0, 5):
    print(f"\n---Results for {expressions[i]} ({iterate[i]})---")
    print(result(expressions[i], word_1))
    print(result(expressions[i], word_2))
    print(result(expressions[i], word_3))
    print(result(expressions[i], word_4))
    print(result(expressions[i], word_5))
    print(result(expressions[i], word_6))