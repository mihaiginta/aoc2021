filename = "example1"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

print(lines)