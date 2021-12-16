# %%
import numpy as np
import os
from collections import Counter

os.chdir(os.path.dirname(__file__))


def read_matrix(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    matrix = np.empty([len(lines), len(lines[1])])
    for num_line, line in enumerate(lines):
        for num_digit, digit in enumerate(line):
            matrix[num_line, num_digit] = int(digit)
    return matrix, lines


def vec2binary(vec):
    bin = 0
    for index, i in enumerate(reversed(vec)):
        bin += i * 2 ** index
    return bin


def task1(filename):
    matrix, lines = read_matrix(filename)
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
    gamma_rate = vec2binary(gamma_vec)
    epsilon_rate = vec2binary(epsilon_vec)
    powerConsumption = gamma_rate * epsilon_rate
    return powerConsumption


def task2(filename):
    matrix, lines = read_matrix(filename)
    ox_rating = np.copy(matrix)
    for i in range(ox_rating.shape[1]):
        most_common_bit = Counter(
            sorted(ox_rating[:, i], reverse=True)).most_common()[0][0]
        ox_rating = ox_rating[ox_rating[:, i] == most_common_bit]
    ox_value = vec2binary(np.ndarray.flatten(ox_rating))
    print(ox_value)

    co_rating = np.copy(matrix)
    for i in range(co_rating.shape[1]):
        if co_rating.shape[0] == 1:
            break
        least_common_bit = Counter(
            sorted(co_rating[:, i], reverse=True)).most_common()[1][0]
        co_rating = co_rating[co_rating[:, i] == least_common_bit]
    co_value = vec2binary(np.ndarray.flatten(co_rating))
    print(co_rating)
    life_support_rating = ox_value * co_value
    return life_support_rating


powerConsumption = task1("input.txt")
print(powerConsumption)
rating = task2("input.txt")
print(rating)

# %%
