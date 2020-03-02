#PYTHON2

import math
import os
import random
import re
import sys


def decToBin(n):
    binRep = []
    #First step is the conversion dec->bin with storage in an array for further checking
    while (n/2 > 1) :
        n = n/2;
        binRep.append(n%2)

    binRep.append(n%2)
    binRep.reverse()
    #print(binRep)
    bitewiseCheck(binRep)

def bitewiseCheck (arr) :
    counter = 0
    #fronteira - arr ter so um 1 consecutivo. 
    #How to Check - counter == 0 e n != 0.
    for i in range(0, len(arr)-1) :
        #algorithm for finding consecutive numbers goes here :
            counter = counter + 1
        

    print(counter)

if __name__ == '__main__':
    n = int(input())
    if n <> 0: 
        decToBin(n)
    else : 
        print ('0')

