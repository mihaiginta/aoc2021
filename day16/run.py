# %%
import numpy as np
import re
import os

os.chdir(os.path.dirname(__file__))

with open("input.txt", 'r') as file:
    xmin, xmax, ymin, ymax = map(int, re.findall(r"[-\d]+", file.read()))
# %% part 1
ymax_0 = abs(ymin)*abs(ymin+1)/2
print(ymax_0)

# %%
