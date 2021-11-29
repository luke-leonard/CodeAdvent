file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')

validRange = {}
names = {}
myTicket = []
otherTicketsRows = []

invalidVals = []

state = 0

for line in lines:
    if line == "":
        state+=1
        continue
    if state == 0:
        val = line.split(":")
        ranges = val[1].strip().split("or")
        leftRange = ranges[0].strip()
        rightRange = ranges[1].strip()
        leftNums = leftRange.split("-")
        leftLower = int(leftNums[0])
        leftUpper = int(leftNums[1])
        rightNums = rightRange.split("-")
        rightLower = int(rightNums[0])
        rightUpper = int(rightNums[1])
        numRange = {}
        for i in range(leftLower,leftUpper + 1):
            validRange[i] = i
            numRange[i] = i
        for i in range(rightLower,rightUpper + 1):
            validRange[i] = i
            numRange[i] = i
        names[val[0]] = numRange
        continue
    if line == "your ticket:" or line == "nearby tickets:":
        continue
    if state == 1:
        nums = line.split(",")
        valid = True
        numRange = []
        for num in nums:
            castNum = int(num)
            numRange.append(castNum)
            if castNum not in validRange:
                print(castNum)
                valid = False
                invalidVals.append(castNum)
            if valid:
                myTicket = numRange
    if state == 2:
        nums = line.split(",")
        valid = True
        numRange = []
        for num in nums:
            castNum = int(num)
            numRange.append(castNum)
            if castNum not in validRange:
                print(castNum)
                valid = False
                invalidVals.append(castNum)
            if valid:
                otherTickets.append(numRange)

total = 0
for val in invalidVals:
    total+= val
print(total)
