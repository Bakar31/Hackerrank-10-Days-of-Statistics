import math
import os
import random
import re
import sys
from statistics import median

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    val_freq = []
    for i in range(n):
        val_freq += [values[i]] * freqs[i]
        
    val_freq_sorted = sorted(val_freq)
    if len(val_freq_sorted) %2 == 0:
        lower_half = val_freq_sorted[: (len(val_freq_sorted)//2)]       
        upper_half = val_freq_sorted[(len(val_freq_sorted)//2):]
    else:
        lower_half = val_freq_sorted[: (len(val_freq_sorted)//2)]
        upper_half = val_freq_sorted[((len(val_freq_sorted)//2)+1):]
        
    Q1 = median(lower_half)
    Q3 = median(upper_half)
    
    print(round(float(Q3 - Q1), 1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
