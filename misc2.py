from random import shuffle

def main():
    namelist = []
    while True:
        name = input("Please enter a name or press \"Enter\" to exit: ")
        if name == "":
            break
        
        namelist.append(name)
    
    print_names_random(namelist)
    print_names_sorted(namelist)

def print_names_random(namelist):
    print("Random order:")
    shuffle(namelist)
    for name in namelist:
        print(name)

def print_names_sorted(namelist):
    print("Sorted order:")
    for name in sorted(namelist):
        print(name)

if __name__ == '__main__':
    print('Namelist')
    main()