import numpy as np
import matplotlib.pyplot as plt
import random

def createList():
    x = np.linspace(1,10,10)

    y = list(x); random.shuffle(y)
    z = list(x); random.shuffle(z)
    z = np.subtract(y, z).tolist()

    return z

def drawLists(num):
    thisList = []
    for x in range(num):
        thisList.append(createList())

    for x in range(len(thisList)):
        plt.plot(thisList[x], label = f"line {x+1}")

    plt.legend()
    plt.show()

if __name__ == "__main__":
    drawLists(int(input("Please enter the number of lines you wish to see: ")))