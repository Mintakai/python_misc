import random

def main():
    data = []
    for x in range(100):
        data.append(str(random.randint(0,100)))

    print(data)
    for y in data:
        print(y)


if __name__ == "__main__":
    main()