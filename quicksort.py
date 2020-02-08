#!/usr/bin/env python3
#
"""Implementation of the quicksort algorithm."""

# TODO: Alternative implementations using different partition schemes (see wiki)

from random import randrange

def quicksort(seq):
    """Uses a 'divide-and-conquer' approach to sort a sequence. The member at
        the midpoint of the sequence is chosen to act as a pivot and the
        remaining members are partitioned into two subarrays depending on
        whether they less than or greater than the pivot, and the subarrays are
        then sorted recursively.

        Algorithm averages O(n log n) comparisons to sort 'n' items, with the
        worst case being O(n^2).

        Quicksort. (2020). Wikipedia. https://en.wikipedia.org/wiki/Quicksort

        https://cs231n.github.io/python-numpy-tutorial/
    """
    seq_len = len(seq)

    if seq_len <= 1:
        return seq

    pivot = seq[seq_len // 2]

    left = [n for n in seq if n < pivot]
    middle = [n for n in seq if n == pivot]
    right = [n for n in seq if n > pivot]

    return quicksort(left) + middle + quicksort(right)


def main():
    "Tests the implementation of the quicksort algorithm."
    test_list_one = [randrange(0, 100) for x in range(10)]
    test_list_two = [randrange(0, 1000) for x in range(10)]

    print(f'Unsorted: {test_list_one}')
    print(f'Sorted:   {quicksort(test_list_one)}\n')

    print(f'Unsorted: {test_list_two}')
    print(f'Sorted:   {quicksort(test_list_two)}\n')

if __name__ == "__main__":
    main()
