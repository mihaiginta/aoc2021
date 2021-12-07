#%%
import numpy as np
def task1(filename, days):
    with open(filename, "r") as f:
        a = np.loadtxt(f, delimiter=',')
        for i in range(days):
            count_zero=np.count_nonzero(a==0)
            a-=1            
            a[np.argwhere(a==-1)]=6
            a=np.append(a, 8*np.ones(count_zero))
        sum = len(a)
    return sum
days = 256
sum = task1("day6/input.txt", days)
print(sum)

# %%
