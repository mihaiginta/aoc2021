# %%
import numpy as np

def sum_positive_changes (arr):
    darr=np.diff(arr)
    sum = np.sum(np.array(darr) > 0, axis=0)
    return sum

filename = "input1"

arr = np.fromfile(filename, sep='\n')

print(sum_positive_changes (arr))

marr = np.convolve(arr, np.ones(3), 'valid')

print(sum_positive_changes (marr))
# %%
