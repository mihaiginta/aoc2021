#%%
import numpy as np
import os

os.chdir(os.path.dirname(__file__))


def task1(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    print(lines)
    matrix = np.empty([len(lines), len(lines[1])])
    for num_line, line in enumerate(lines):
        for num_digit, digit in enumerate(line):
            matrix[num_line, num_digit] = int(digit)

    print(matrix)
    average = np.mean(matrix, axis=0)
    print(average)

    gamma_vec = np.empty(len(lines[1]))
    epsilon_vec = np.empty(len(lines[1]))
    for index, i in enumerate(average):
        if i > 0.5:
            gamma_vec[index] = 1
            epsilon_vec[index] = 0
        else:
            gamma_vec[index] = 0
            epsilon_vec[index] = 1
    print(gamma_vec)
    print(epsilon_vec)
    gamma_rate = 0
    epsilon_rate = 0
    for index, i in enumerate(reversed(gamma_vec)):
        gamma_rate += i * 2 ** index
    for index, i in enumerate(reversed(epsilon_vec)):
        epsilon_rate += i * 2 ** index
    powerConsumption = gamma_rate * epsilon_rate
    return powerConsumption


powerConsumption = task1("input.txt")
print(powerConsumption)

# %%
