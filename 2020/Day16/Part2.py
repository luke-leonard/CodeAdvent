file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')

validRange = {}
names = {}
myTicket = []
otherTickets = []

invalidVals = []

result = {}

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
                valid = False
                invalidVals.append(castNum)
        if valid:
            myTicket = numRange
            otherTickets.append(numRange)
    if state == 2:
        nums = line.split(",")
        valid = True
        numRange = []
        for num in nums:
            castNum = int(num)
            numRange.append(castNum)
            if castNum not in validRange:
                valid = False
                invalidVals.append(castNum)
        if valid:
            otherTickets.append(numRange)

otherTickesRows = []
for i in range(len(myTicket)):
    row = []
    otherTickesRows.append(row)

for ticket in otherTickets:
    for i in range(len(ticket)):
        otherTickesRows[i].append(ticket[i])

validNameTicketRows = {}
rowOptions = []
index = 0
for row in otherTickesRows:
    rowOp = []
    for name in names:
        valid = True
        for val in row:
            if val not in names[name]:
                valid = False
                break
        if valid:
            if name not in validNameTicketRows:
                validNameTicketRows[name] = {"q":0,"l":[]}
            validNameTicketRows[name]["q"] += 1
            validNameTicketRows[name]["l"].append(index)
            rowOp.append(name)
            continue
    rowOptions.append(rowOp)
    index+=1

numRes = index
while numRes > 0:
    for thing in validNameTicketRows:
        if validNameTicketRows[thing]["q"] == 1:
            numRes-=1
            ind = validNameTicketRows[thing]['l'][0]
            result[ind] = thing
            validNameTicketRows[thing]['l'] = []
            validNameTicketRows[thing]['q'] = 0
            toUpdate = rowOptions[ind]
            toUpdate.remove(thing)
            for cosa in toUpdate:
                validNameTicketRows[cosa]['q'] -=1
                validNameTicketRows[cosa]['l'].remove(ind)
            break

total = 1
for i in range(index):
    if result[i].startswith("departure"):
        print(result[i], myTicket[i])
        total*=myTicket[i]

print(total)

