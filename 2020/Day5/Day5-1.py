file = open("Day5-1.txt", "r")
lines = file.read()
f = lines.split('\n')
seats = []
a=[]
for line in f:
    ud = line[:-3]
    rl = line[-3:]
    udIndex = 0
    udIndex += 0 if ud[0] == "F" else 64
    udIndex += 0 if ud[1] == "F" else 32
    udIndex += 0 if ud[2] == "F" else 16
    udIndex += 0 if ud[3] == "F" else 8
    udIndex += 0 if ud[4] == "F" else 4
    udIndex += 0 if ud[5] == "F" else 2
    udIndex += 0 if ud[6] == "F" else 1
    rlIndex = 0
    rlIndex += 0 if rl[0] == "L" else 4
    rlIndex += 0 if rl[1] == "L" else 2
    rlIndex += 0 if rl[2] == "L" else 1
    seat = udIndex * 8 + rlIndex
    seats.append(seat)
print(max(seats))

