# %%
import numpy as np

filename = "example1"

arr = np.fromfile(filename, sep='\n')

darr=np.diff(arr)

sum = np.sum(np.array(darr) >= 0, axis=0)
