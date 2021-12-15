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

with open("example.txt", "r") as f:
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
reversed_pairs = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">"
}
missingValue = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}
errorSum = 0

with open("input.txt", "r") as f:
    missingSum = []
    for line_no, line in enumerate(f.read().splitlines()):
        lineList = []
        is_error = False
        for char in line:
            if char in illegalValue:
                if pairs[char] == lineList[-1]: #found closing pair
                    lineList.pop()
                else:
                    is_error = True
                    break
            else:
                lineList.append(char)
#task2
        if not(is_error):
            missingSum.append(0)
            for char in lineList:
                if char in illegalValue:
                    if pairs[char] == lineList[-1]: #found closing pair
                        lineList.pop()
            for char in reversed(lineList):
                missingSum[-1] = missingSum[-1]*5
                missingSum[-1] += missingValue[char]
missingSum.sort()
print(missingSum[len(missingSum)//2])
# %%
