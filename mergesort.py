#!/usr/bin/env python3
#
# mergesort.py - implementation of the mergesort algorithm


def mergesort(seq):
    """ Implementation of the mergesort algorithm.

        Sourced from Hetland, M. L. (2014). 'Python Algorithms'. pp. 125-126     
    """
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)

    result = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            result.append(lft.pop())
        else:
            result.append(rgt.pop())
    result.reverse()
    return (lft or rgt) + result

def main():
    """Tests the implementation of the algorithm."""
    seq = [48, 11, 45, 92, 32, 61, 65, 57, 29, 96]
    print(mergesort(seq))

if __name__ == "__main__":
    main()
    