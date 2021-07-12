import math
import os
import random
import re
import sys
from statistics import median

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr_sorted = sorted(arr)
    if len(arr_sorted) %2 == 0:
        lower_half = arr_sorted[: (len(arr_sorted)//2)]       
        upper_half = arr_sorted[(len(arr_sorted)//2):]
    else:
        lower_half = arr_sorted[: (len(arr_sorted)//2)]
        upper_half = arr_sorted[((len(arr_sorted)//2)+1):]
        
    return round(median(lower_half)), round(median(arr_sorted)), round(median(upper_half))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
