import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    res = {}
    for i in brr:
        if i not in res:
            res[i] = 1
        else :
            res[i] += 1
    for i in arr:
        if i in res:
            res[i] -= 1
    a = []
    for k,v in res:
        if v !=0:
            a.append(k)
    a.sort()
    return a





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
