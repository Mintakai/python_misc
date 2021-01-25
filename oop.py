class Person:
    def __init__(self, name, age=13):
        self.name = name
        self.age = age

class Testi:
    def __init__(self, test1, test2):
        self.test1 = test1
        self.test2 = test2

def testiii():
    henk = Person("anna", 18)
    return henk.age

def main():
    henkilo = Person("topi")
    print(henkilo.name)
    print(testiii())

    henkilo.name = "ville"
    print(henkilo.name)

if __name__ == '__main__':
    main()