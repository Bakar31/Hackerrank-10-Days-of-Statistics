import numpy as np
from scipy import stats

N = int(input())
numbers = list(map(int, input().split()))

mean = np.mean(numbers)
median = np.median(numbers) 
mode = int(stats.mode(numbers)[0])
print(mean)
print(median)
print(mode)
