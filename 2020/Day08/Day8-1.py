file = open("Day8-1.txt", "r")
f = file.read()
lines = f.split('\n')

instructions = []
hitInstructions = {}

for line in lines:
    a = line.split(" ")
    b = {}
    b['in'] = a[0]
    b['val'] = int(a[1])
    instructions.append(b)

index = 0
total = 0

while index not in hitInstructions:
    hitInstructions[index] = total
    cur = instructions[index]
    if cur['in'] == "acc":
        total += cur['val']
    if cur['in'] == "jmp":
        index += cur['val'] - 1
    index += 1
print(hitInstructions)
print( total)

