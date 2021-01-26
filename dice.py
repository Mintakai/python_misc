from random import randint

def die(n = 1, sides = 6):
    sum = 0
    for x in range(n):
        sum += randint(1, 6)

    return sum

def d6(n = 1):
    return die(n)