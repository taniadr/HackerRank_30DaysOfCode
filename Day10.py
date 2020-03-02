#!/bin/python3

import math
import os
import random
import re
import sys


def decToBin(n):
    binRep = []
    #First step is the conversion dec->bin with storage in an array for further checking
    while (n/2 > 1) :
        n = n//2;
        binRep.append(n%2)

    binRep.append(n%2)
    binRep.reverse()
    #print(binRep)
    bitewiseCheck(binRep)

def bitewiseCheck (arr) :
    counter = 0

    for i in range(0, len(arr)-1) :
        if (arr[i] == 1 and arr[i] == arr[i+1]) :
            counter = counter + 1

    print(counter*2)

if __name__ == '__main__':
    n = int(input())
    decToBin(n)

