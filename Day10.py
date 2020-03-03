import math
import os
import random
import re
import sys


def decToBin(n):
    maxi = 0
    total = 0

    while (n > 0) :
        if (n%2 == 1) :
            total += 1
            if (total > maxi) :
                maxi = total
        else :
            total = 0
        n = n/2
    
    print(maxi)

if __name__ == '__main__':
    n = int(input())
    decToBin(n)