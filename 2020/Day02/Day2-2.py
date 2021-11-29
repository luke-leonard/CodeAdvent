f = open("Day2-1.txt", "r")
total = 0
for x in f:
    var = x.split(" ")
    ran = var[0].split("-")
    char = var[1][0]
    pos1 = 1 if char == var[2][int(ran[0])-1] else 0
    pos2 = 1 if char == var[2][int(ran[1])-1] else 0
    if pos1 + pos2 == 1:
        total+=1

print(total)