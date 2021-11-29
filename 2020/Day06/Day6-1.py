file = open("Day6-1.txt", "r")
lines = file.read()
f = lines.split('\n')
total = 0;
group = {}
for line in f:
    if line == "":
        total += len(group)
        group = {}
        continue
    for char in line:
        group[char] = 1
total+=len(group)
print(total)