#!/usr/bin/env python
#
"""Some simple searching algorithms for practice"""

from random import randrange

def find_maximum(lst):
    "Finds the maximumimum number in a list."
    maximum = 0
    for val in lst:
        if val >= maximum:
            maximum = val
        else:
            continue
    return maximum

def find_minimum(lst):
    "Finds the minimumimum number in a list."
    minimum = float('inf')
    for val in lst:
        if val <= minimum:
            minimum = val
        else:
            continue
    return minimum


def main():
    """Tests the algorithms above."""
    # Some lists of random numbers for testing purposes.
    rnd_list_a = [randrange(0, 100) for i in range(10)]
    rnd_list_b = [randrange(0, 10000) for i in range(10)]

    print("\n", rnd_list_a, "\n", rnd_list_b)
    print(find_maximum(rnd_list_a), "\t| ", find_minimum(rnd_list_a))

    #print(find_maximum(rnd_list_a) == maximum(rnd_list_a))
    print(find_maximum(rnd_list_b), "\t| ", find_minimum(rnd_list_b))


if __name__ == "__main__":
    main()
