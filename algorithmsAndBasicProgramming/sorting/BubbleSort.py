#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


exchangeCounter = 0
# t=n - 1
for i in range(0,n):

    print("i=",i)

    for j in range(0,n-i-1):
        print("===========================",j)
        if a[j] > a[j+1] :
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            print("==",a)
            exchangeCounter+=1



print("Array is sorted in"+" "+str(exchangeCounter)+" "+"swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])
print(a)


# 7
# 7 6 5 4 3 2 1
# Array is sorted in 21 swaps.
# First Element: 1
# Last Element: 7

# Complexity
# Case 1) O(n) (Best case) This time complexity can occur if the array is already sorted, and that means that no swap occurred and only 1 iteration of n elements
#
# Case 2) O(n^2) (Worst case) The worst case is if the array is already sorted but in descending order. This means that in the first iteration it would have to look at n elements, then after that it would look n - 1 elements (since the biggest integer is at the end) and so on and so forth till 1 comparison occurs. Big-O = n + n - 1 + n - 2 ... + 1 = (n*(n + 1))/2 = O(n^2)