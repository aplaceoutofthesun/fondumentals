#!/usr/bin/env python
#
# simple_searching.py - Some simple searching algorithms for practice
###

import os
import sys

from random import randrange

def find_max(lst):
    "Finds the maximum number in a list."
    max = 0
    for val in lst:
        if val >= max:
            max = val
        else:
            continue
    return max
    
def find_min(lst):
    "Finds the minimum number in a list."
    min = float('inf')
    for val in lst:
        if val <= min:
            min = val
        else:
            continue
    return min
    

def main():
    #pass
    rnd_list_a = [randrange(0, 100) for i in range(10)]
    rnd_list_b = [randrange(0, 10000) for i in range(10)]
    print("\n", rnd_list_a, "\n", rnd_list_b)
    print(find_max(rnd_list_a), "\t| ", find_min(rnd_list_a))
    #print(find_max(rnd_list_a) == max(rnd_list_a))
    print(find_max(rnd_list_b), "\t| ", find_min(rnd_list_b))
    
    

if __name__ == "__main__":
    main()