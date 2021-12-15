#%%
import numpy as np
import os
from skimage.graph import route_through_array
os.chdir(os.path.dirname(__file__))

with open("example.txt", "r") as f:    
    matrix = np.array([list(line.strip()) for line in f.readlines()], dtype=int)

print(matrix)
path, cost = route_through_array((matrix), (0,0), (-1,-1), fully_connected=False, geometric = False)
print(cost-matrix[0,0])

# %%
