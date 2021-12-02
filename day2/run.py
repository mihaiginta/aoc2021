#%%
def task1(filename):
    with open(filename, "r") as f:
        vertivalValues = 0
        forwardValues = 0
        for line in f:
            #print(line.rstrip())
            if 'up' in line:
                vertivalValues -= int(line.split()[1])
            elif 'down' in line:
                vertivalValues += int(line.split()[1])
            elif 'forward' in line:
                forwardValues += int(line.split()[1])
    position = vertivalValues*forwardValues 
    return position

position = task1("input.txt")
print(position)



# %%
def task2(filename):
    with open(filename, "r") as f:
        depth = 0
        horizontalPosition = 0
        aim = 0
        for line in f:
            #print(line.rstrip())
            if 'up' in line:
                aim -= int(line.split()[1])
            elif 'down' in line:
                aim += int(line.split()[1])
            elif 'forward' in line:
                horizontalPosition += int(line.split()[1])
                depth += aim*int(line.split()[1])
    position = depth*horizontalPosition 
    return position

position = task2("input.txt")
print(position)