#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_dict = dict(Counter(ar))
    division_result = 0
    for each in count_dict:
        temp = count_dict[each]
        division_result = division_result + temp // 2

    return division_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
