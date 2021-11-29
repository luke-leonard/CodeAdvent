file = open("Day6-1.txt", "r")
lines = file.read()
f = lines.split('\n')
total = 0
people = 0
group = {}
for line in f:
    if line == "":
        for answers in group:
            if group[answers] == people:
                total+=1
        group = {}
        people = 0
        continue
    people+=1
    for char in line:
        group[char] = group[char] + 1 if char in group else 1
for answers in group:
    if group[answers] == people:
        total+=1
print(total)