#!/usr/bin/env python3
#
# insertsort.py - implementation of insertion sort algorithm

def insertion_sort(seq):
    """
        Maintains a sorted sublist in the lower positions in the list.
        Each new item is then inserted back into the prev sublist s.t.
        the sorted sublist is one item larger.
        
        Complexity: O(n**2)
        
        param: seq - list of integers.
    """
    
    length = len(seq)
    for i in range(1, length):
        key = seq[i]    # Current value
        j = i           # Position
        while j > 0 and seq[j - 1] > key:
            seq[j] = seq[j - 1]
            j = j - 1
        seq[j] = key
    return seq

def main():
    """
        Example of insertion sort.
    """
    seq = [48, 11, 45, 92, 32, 61, 65, 57, 29, 96]
    print(insertion_sort(seq))
    
    
if __name__ == "__main__":
    main()