#!/usr/bin/env python3
#
"""Implementation of selection sort algorithm."""

def selection_sort(seq):
    """Makes one exchange for every pass through the list. Looks for the
       largest value as it makes a pass, and after completing the pass,
       places it in the proper location. Like bubble sort, after the first
       pass the largest item is in the correct place.

       Complexity: O(n**2)

       param: seq - list of integers
    """
    length = len(seq)

    for i in range(length-1, 0, -1):

        max_pos = 0     # Position of max value

        for j in range(1, i+1):
            if seq[j] > seq[max_pos]:
                max_pos = j

        tmp = seq[i]
        seq[i] = seq[max_pos]
        seq[max_pos] = tmp

    return seq

def main():
    """Tests the implementation of Selection sort."""
    seq = [48, 11, 45, 92, 32, 61, 65, 57, 29, 96]
    print(selection_sort(seq))

if __name__ == "__main__":
    main()
