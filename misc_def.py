def f1(x):
    y = x*7
    return y
def f2(x):
    global y
    y = x*2
    return y
def f3(x):
    return y*3

f1(1)
f2(2)
f3(3)

print(y)