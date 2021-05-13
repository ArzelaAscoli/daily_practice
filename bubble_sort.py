#!/bin/python3
# import sys


class BubbleSort:

    def __init__(self, nn, aa):
        self.n = nn
        self.a = aa
        self.numberOfSwaps = None

    def bubble_sort(self):
        self.numberOfSwaps = 0
        for i in range(0, n):
            # Track number of elements swapped during a single array traversal

            for j in range(0, n-1):
                # Swap adjacent elements if they are in decreasing order
                if self.a[j] > self.a[j+1]:
                    self.a[j], self.a[j+1] = self.a[j+1], self.a[j]
                    self.numberOfSwaps = self.numberOfSwaps+1
            # If no elements were swapped during a traversal, array is sorted
            print(self.numberOfSwaps, a)
            if self.numberOfSwaps == 0:
                break
        return self.numberOfSwaps, self.a


if __name__ == '__main__':
    print("Input array length:")
    n = int(input().strip())
    print("Input array:")
    a = list(map(int, input().strip().split(' ')))
    # print(n, a)
    BB = BubbleSort(n, a)
    m, b = BB.bubble_sort()
    print("Array is sorted in " + str(m) + " swaps")
    print("First Element: ", b[0])
    print("Last Element: ", b[-1])
# Write Your Code Here
