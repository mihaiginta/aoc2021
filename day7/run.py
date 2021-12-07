#%%
import numpy as np
import os
os.chdir(os.path.dirname(__file__))
with open("example.txt", "r") as f:
    a = np.loadtxt(f, delimiter=',')
    average = round(np.median(a))
    individual_fuels = a-average
    fuel = sum(abs(individual_fuels))
print(a)
print(fuel)
# %%
