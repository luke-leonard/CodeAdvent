file = open("Day8-1.txt", "r")
f = file.read()
lines = f.split('\n')

instructions1 = []


for line in lines:
    a = line.split(" ")
    b = {}
    b['in'] = a[0]
    b['val'] = int(a[1])
    instructions1.append(b)

def test(instructions):
    index = 0
    total = 0
    hitInstructions = {}
    while index not in hitInstructions:
        if index == len(instructions):
            return {'s':True,"v":total}
        hitInstructions[index] = total
        cur = instructions[index]
        if cur['in'] == "acc":
            total += cur['val']
        if cur['in'] == "jmp":
            index += cur['val'] - 1
        index += 1
    return {'s':False,"v":total}

for i in range(len(instructions1)):
    if instructions1[i]['in'] == 'nop':
        instructions1[i]['in'] = "jmp"
        if test(instructions1)['s']:
            print(test(instructions1)['v'])
            print(i)
        instructions1[i]['in'] = "nop"
    if instructions1[i]['in'] == 'jmp':
        instructions1[i]['in'] = "nop"
        if test(instructions1)['s']:
            print(test(instructions1)['v'])
            print(i)
        instructions1[i]['in'] = "jmp"

