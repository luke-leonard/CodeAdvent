file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')
buses = lines[1].split(',')
dif = 0
mostRecent = int(buses[0])
runningMult = mostRecent
buses = buses[1:]
for val in buses:
    dif +=1
    if val != 'x':
        castVal = int(val)
        accum = mostRecent
        print(accum, castVal,dif)
        while((accum + dif ) % castVal != 0):
            accum+=runningMult
        mostRecent = accum + dif
        runningMult = runningMult * castVal
        dif=0
print(mostRecent - len(buses))