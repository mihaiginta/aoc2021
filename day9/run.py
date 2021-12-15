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
                    break
            else:
                lineList.append(char)
print(errorSum)
# %%
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
missingValue = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
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
                    break
            else:
                lineList.append(char)
#task2
        missingSum = 0
        for char in lineList:
            if char in illegalValue:
                if pairs[char] == lineList[-1]: #found closing pair
                    lineList.pop()
        for char in reversed(lineList):
            missingSum *= 5
            missingSum += missingValue[char]
print(errorSum)