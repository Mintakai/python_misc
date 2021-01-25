def make_multiplier(x):
    def multiplier(y):
        return x*y
    return multiplier

mul10 = make_multiplier(10)
print(mul10(2))