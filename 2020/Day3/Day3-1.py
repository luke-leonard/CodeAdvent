f = open("Day3-1.txt", "r")
total = 0
on = 0
for x in f:
    on %= len(x) - 1
    if x[on] == "#":
        total+=1
    on+=3
print(total)