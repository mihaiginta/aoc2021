#%%
import numpy as np
import os
from skimage.graph import route_through_array
os.chdir(os.path.dirname(__file__))

with open("input.txt", "r") as f:    
    matrix = np.array([list(line.strip()) for line in f.readlines()], dtype=int)

print(matrix)
path, cost = route_through_array((matrix), (0,0), (-1,-1), fully_connected=False, geometric = False)
print(cost-matrix[0,0])

# %%

pattern_matrix = np.zeros((5,5))
pattern_matrix[0,0] = 1
matrix_element = matrix
extended_matrix = np.kron(pattern_matrix, matrix_element)
element_no = [2,3,4,5,4,3,2,1]
for count, value in enumerate(element_no):
    matrix_element = matrix_element%9+1
    pattern_matrix = np.flipud(np.diag(np.ones(value), -3+count))
    extended_matrix = extended_matrix+np.kron(pattern_matrix, matrix_element)

path, cost = route_through_array((extended_matrix), (0,0), (-1,-1), fully_connected=False, geometric = False)
print(cost-extended_matrix[0,0])

# %%
