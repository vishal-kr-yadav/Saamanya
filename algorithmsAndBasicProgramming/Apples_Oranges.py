# https://www.hackerrank.com/challenges/apple-and-orange/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))
    # apple_count=0
    # orange_count=0
    # final_apples = [a+each for each in apples]
    # final_oranges = [b+each for each in oranges]
    # # print(final_apples,final_oranges)
    # for i,j in zip(final_apples,final_oranges):
    #     if i >= s and i <= t:
    #         apple_count+=1
    #     if j >= s and j <= t :
    #         orange_count+=1
    # print(apple_count)
    # print(orange_count)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
