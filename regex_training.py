import re
import string

iterate = string.ascii_lowercase
expressions = ["[J-P]\w{3}", "[PJ]\w+", "\w{4,}", "[p-j]\w{3,}", "\w{5,}"]

Python = "Python"
JavaScript = "JavaScript"
Java = "Java"

C = "C#"
Swift = "Swift"
Ruby = "Ruby"

def result(p,s):
    try:
        return re.match(p,s)
    except re.error:
        return "Error"

for i in range(0, 5):
    print(f"\n---Results for {expressions[i]} ({iterate[i]})---")
    print(result(expressions[i], Python))
    print(result(expressions[i], JavaScript))
    print(result(expressions[i], Java))
    print(result(expressions[i], C))
    print(result(expressions[i], Swift))
    print(result(expressions[i], Ruby))