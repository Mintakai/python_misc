import re
import string

iterate = string.ascii_lowercase
expressions = ["^0?[1-31]$", "^0?[1-9]|[10-31]$", "^(3[01]|[12]\d|0?[1-9])$", "^1-31|01-31$", "^[0-31]$"]

weekdays = []

for i in range(1, 32):
    if i <= 9:
        weekdays.append(str(f"0{str(i)}"))
    else:
        weekdays.append(str(i))

def result(p,s):
    try:
        return re.match(p,s)
    except re.error:
        return "Error"

for i in range(0, 31):
    print(f"\n---Results for weekday: {weekdays[i]}---")
    print(f"a: {result(expressions[0], weekdays[i])}")
    print(f"b: {result(expressions[1], weekdays[i])}")
    print(f"c: {result(expressions[2], weekdays[i])}")
    print(f"d: {result(expressions[3], weekdays[i])}")
    print(f"e: {result(expressions[4], weekdays[i])}")

# for i in range(1,32):
    # print(f"\n---Results for {expressions[i]} ({iterate[i]})---")
    # print(result(expressions[i], word_1))
    # print(result(expressions[i], word_2))