#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    vallye_count = 0
    sea_level_count = 0
    list_of_path =list(s)

    for each in list_of_path:
        if each == "U":
            sea_level_count += 1
            if sea_level_count == 0:
                vallye_count += 1
        if each == "D":
            sea_level_count -= 1


    return vallye_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
