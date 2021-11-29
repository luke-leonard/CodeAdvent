import re
file = open("Input.txt", "r")
f = file.read()
lines = f.split("\n")


mapper = {}

for line in lines:
    x = 0
    y = 0
    matches = re.findall("(?:e)|(?:se)|(?:sw)|(?:w)|(?:nw)|(?:ne)",line)
    for match in matches:
        if match == "e":
            x+=2
        if match == "se":
            x+=1
            y-=1
        if match == "sw":
            x-=1
            y-=1
        if match == "w":
            x-=2
        if match == "nw":
            x-=1
            y+=1
        if match == "ne":
            x+=1
            y+=1
    key = str(x) +":"+str(y)
    if key not in mapper:
        mapper[key] = False
    mapper[key] = not mapper[key]

total = 0
for key in mapper:
    if mapper[key]:
        total+=1

print(total)
