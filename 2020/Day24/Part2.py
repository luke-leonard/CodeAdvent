import re
file = open("Input.txt", "r")
f = file.read()
lines = f.split("\n")

def printVisK(size,lis):
    arr = []
    for i in range(size):
        ar = []
        for j in range(size):
            ar.append(" ")
        arr.append(ar)
    for key in lis:
        tRaw = key.split(":")
        x = int(tRaw[0]) + (size//2)
        y = int(tRaw[1]) + (size//2)
        if lis[key]["IsBlack"]:
            arr[x][y] = lis[key]["count"]
    print("012345678901234567890123456789012345678901234567890")
    for i in range(len(arr)):
        ar = arr[i]
        print(i%10,end="")
        for a in ar:
            print(a,end="")
        print()

def printVis(size,lis):
    arr = []
    for i in range(size):
        ar = []
        for j in range(size):
            ar.append(" ")
        arr.append(ar)
    for key in lis:
        tRaw = key.split(":")
        x = int(tRaw[0]) + (size//2)
        y = int(tRaw[1]) + (size//2)
        if lis[key]:
            arr[x][y] = "b"
        else:
            arr[x][y] = "."
    print("012345678901234567890123456789012345678901234567890")
    for i in range(len(arr)):
        ar = arr[i]
        print(i%10,end="")
        for a in ar:
            print(a,end="")
        print()

def printVislis(size,lislis):
    arr = []
    for i in range(size):
        ar = []
        for j in range(size):
            ar.append(" ")
        arr.append(ar)
    for i in range(len(lislis)):
        lis = lislis[i]
        for key in lis:
            tRaw = key.split(":")
            x = int(tRaw[0]) + (size//2)
            y = int(tRaw[1]) + (size//2)
            if lis[key]:
                arr[x][y] = str((1<<i )+ (0 if arr[x][y] == " " else int(arr[x][y])))
    for i in range(len(arr)):
        ar = arr[i]
        print(i%10,end=" ")
        for a in ar:
            print(a,end=" ")
        print()





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
ts = "| "
for key in mapper:
    if mapper[key]:
        total+=1
        ts += key + " "
print(total)
# printVis(20,mapper)
# print("-------------------------")

days = 100



mapmaps = []
mapmaps.append(mapper)

for i in range(days):
    mapNums = {}
    stats = {"blf":0,"whf":0,"wh":0,"bl":0}
    for tile in mapper:
        if tile not in mapNums:
            mapNums[tile] = {"IsBlack":mapper[tile],"count":0}
        else:
            mapNums[tile]["IsBlack"] = mapper[tile]
        tRaw = tile.split(":")
        x = int(tRaw[0])
        y = int(tRaw[1])
        keys = [None] * 6
        keys[0] = str(x+2) +":"+str(y)
        keys[1] = str(x+1) +":"+str(y-1)
        keys[2] = str(x-1) +":"+str(y-1)
        keys[3] = str(x-2) +":"+str(y)
        keys[4] = str(x-1) +":"+str(y+1)
        keys[5] = str(x+1) +":"+str(y+1)

        if mapper[tile]:
            for key in keys:
                if key not in mapNums:
                    mapNums[key] = {"IsBlack":False,"count":0}
                mapNums[key]["count"]+=1

    for tile in mapNums:
        if mapNums[tile]["IsBlack"]:
            stats["bl"] +=1
            if mapNums[tile]["count"] == 0 or mapNums[tile]["count"] > 2:
                mapper[tile] = False
                stats["blf"] +=1
        else:
            stats["wh"] +=1
            if mapNums[tile]["count"] == 2:
                mapper[tile] = True
                stats["whf"] +=1
    
    mapmaps.append(mapper.copy())

    total = 0
    ts = "| "
    for key in mapper:
        if mapper[key]:
            total+=1
            ts += key + " "


    # print("-----------------------------------")
    print(total)
    # print(stats)
    # printVisK(20,mapNums)
    # print("-----------------------------------")

#printVislis(30,mapmaps)
