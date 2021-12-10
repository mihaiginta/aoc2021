#%%
import numpy as np
import os
os.chdir(os.path.dirname(__file__))

illegalValue = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
errorSum = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        lineList = []
        for char in line:
            if char in illegalValue:
                if pairs[char] == lineList[-1]: #found closing pair
                    lineList.pop()
                else:
                    errorSum += illegalValue[char]
                    print("error")
                    break
            else:
                lineList.append(char)
print(errorSum)
# %%
