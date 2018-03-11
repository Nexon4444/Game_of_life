import random
import sys
import os
import time
from view.graphics import *
size = 6

simulateTime = 12
def main():
    createWindow()
    return 0
    # printAll()
    # tab = [[0] * size for i in range(size)]
    #
    #
    # setXY(0, 0, 1, tab)
    # setXY(1, 0, 1, tab)
    # setXY(0, 1, 1, tab)
    # setXY(5, 0, 1, tab)
    #
    # setXY(3, 3, 1, tab)
    # setXY(2, 3, 1, tab)
    # setXY(4, 3, 1, tab)
    #
    #
    #
    # simulate(tab)


def printAll(tab):
    for p in tab:
        for el in p:
            print (el, end="")
        print ("\n")

    print("===========")

def setXY (x, y, var, tab):
    tab[y][x] = var

def neighbours(x, y, tab):
    counter = 0
    #print("x: ", x, "y: ", y)

    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            #print(counter, "i: ", i, "j: ", j, "tab: ", tab[i][j])
            if (i==y and j==x) or (i<0 or i>=size) or (j<0 or j>=size):
                continue
            if tab[i][j] == 1:
                counter = counter + 1
    return counter


def checkRules(x, y, tab):
    test = neighbours(x, y, tab)
    if test < 2:
        return -1
    elif test == 2:
        return 0
    elif test == 3:
        return 1
    else:
        return -1

def scanAndModify(tab):
    tab2 = [[0] * size for i in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            checked = checkRules(j, i, tab)

            #print(counter, "i: ", i, "j: ", j, "tab: ", tab[i][j])
            if checked == -1:
                setXY(j, i, 0, tab2)
            elif checked ==1:
                setXY(j, i, 1, tab2)
            else:
                setXY(j, i, tab[i][j], tab2)

    tab[:] = list(tab2)

def simulate(tab):
    printAll(tab)
    for i in range(0, simulateTime):
        scanAndModify(tab)
        time.sleep(0.5)
        printAll(tab)


if __name__ == "__main__":
    main()