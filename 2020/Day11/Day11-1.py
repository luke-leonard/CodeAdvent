import copy
file = open("Day11-1.txt", "r")

f = file.read()
flines = f.split('\n')
lines = []
for i in range(len(flines)):
    inarr = []
    for j in range(len(flines[i])):
        inarr.append(flines[i][j])
    lines.append(inarr)

lines2 = copy.deepcopy(lines)

def getAdjCount(x,y):
    count = 0
    smallX = x - 1 >= 0
    smallY = y - 1 >= 0
    bigX = x + 1 < len(lines[y])
    bigY = y + 1 < len(lines)
    if smallX and smallY:
        count += 1 if lines[y-1][x-1] == '#' else 0
    if smallX:
        count += 1 if lines[y][x-1] == '#' else 0
    if smallY:
        count += 1 if lines[y-1][x] == '#' else 0
    if smallX and bigY:
        count += 1 if lines[y+1][x-1] == '#' else 0
    if bigX and smallY:
        count += 1 if lines[y-1][x+1] == '#' else 0
    if bigX:
        count += 1 if lines[y][x+1] == '#' else 0
    if bigX and bigY:
        count += 1 if lines[y+1][x+1] == '#' else 0
    if bigY:
        count += 1 if lines[y+1][x] == '#' else 0
    return count

switches = 1
while switches > 0:
    switches = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            count = getAdjCount(j,i)
            # print(count, end='')
            if(count >=4 and lines[i][j] == '#'):
                lines2[i][j] = 'L'
                switches+=1
            if(count == 0 and lines[i][j] == 'L'):
                lines2[i][j] = '#'
                switches+=1

        # print(" ", end='')
        # for j in range(len(lines[i])):
        #     print(lines[i][j], end='')

        # print(" ", end='')
        # for j in range(len(lines[i])):
    #         print(lines2[i][j], end='')
    #     print()
    # print()
    lines = lines2
    lines2 = copy.deepcopy(lines)

count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if(lines[i][j] == '#'):
            count+=1
print(count)