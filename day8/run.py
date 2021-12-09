# %%
import numpy as np
import os
os.chdir(os.path.dirname(__file__))
with open("input.txt", "r") as f:
    matrix = np.array([list(line.strip()) for line in f.readlines()], dtype=int)
paddedMatrix = np.pad(matrix, 1, 'constant', constant_values=9)
(nRows, nColumns) = paddedMatrix.shape
sumRiskLevel = 0
for iRow in range(1, nRows-1):
    for iColumn in range(1, nColumns-1):
        if (paddedMatrix[iRow][iColumn] < paddedMatrix[iRow-1][iColumn] and
            paddedMatrix[iRow][iColumn] < paddedMatrix[iRow+1][iColumn] and
            paddedMatrix[iRow][iColumn] < paddedMatrix[iRow][iColumn+1] and
                paddedMatrix[iRow][iColumn] < paddedMatrix[iRow][iColumn-1]):
            sumRiskLevel += paddedMatrix[iRow][iColumn]+1
print(sumRiskLevel)
# %%
