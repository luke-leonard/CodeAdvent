f = open("Day2-1.txt", "r")
total = 0
for x in f:
    count = 0
    var = x.split(" ")
    ran = var[0].split("-")
    char = var[1][0]
    for letter in var[2]:
        if letter ==char:
            count+=1
    if count >= int(ran[0]) and count <= int(ran[1]):
        total+=1

print(total)