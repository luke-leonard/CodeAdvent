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

xydir = [
    {'x':-1,'y':-1},
    {'x':-1,'y':0},
    {'x':-1,'y':1},
    {'x':0,'y':-1},
    {'x':0,'y':1},
    {'x':1,'y':-1},
    {'x':1,'y':0},
    {'x':1,'y':1}
    ]

def getAdjCount(y,x):
    count = 0
    for dirs in xydir:
        i = x + dirs['x']
        j = y + dirs['y']
        while (i >= 0 and i < len(lines) and j >= 0 and j < len(lines[0])):
            if lines[i][j] == '#':
                count+=1
                break
            if lines[i][j] == 'L':
                break
            i = i + dirs['x']
            j = j + dirs['y']
    return count

switches = 1
while switches > 0:
    switches = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            count = getAdjCount(j,i)
            # print(count, end='')
            if(count >=5 and lines[i][j] == '#'):
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
        #     print(lines2[i][j], end='')
        # print()
    print(switches)
    lines = lines2
    lines2 = copy.deepcopy(lines)

count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if(lines[i][j] == '#'):
            count+=1
print(count)