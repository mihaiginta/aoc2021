#%%
def task1(filename):
    with open(filename, "r") as f:
        vertivalValues = 0
        forwardValues = 0
        for line in f:
            print(line.rstrip())
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
