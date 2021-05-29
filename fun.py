def funkkari(nopeus1, nopeus2, aika):
    return (nopeus2 - nopeus1) / aika

def main():
    for x in range(40, 50):
        print(funkkari(x, 80, 60))

if __name__ == '__main__':
    main()