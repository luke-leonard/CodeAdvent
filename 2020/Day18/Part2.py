import re
file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')


def evaluatePM(left, right, op):
    if op == "+":
        return left + right
    if op == "*":
        return left * right

def evaluateMString(line):
    line = line.strip()
    val = re.search("[0-9]+",line)
    value = int(val.group())
    index = len(val.group())
    op = "*"
    while index < len(line):
        if line[index] == " ":
            index += 1
            continue
        if line[index] == "*":
            op = line[index]
        else:
            val = re.search("[0-9]+",line[index:])
            value = evaluatePM(value,int(val.group()),op)
            index+= len(val.group())
        index+=1
    return value

def evaluatePString(line):
    line = line.strip()
    val = re.search("[0-9]+",line)
    value = int(val.group())
    index = len(val.group())
    op = "+"
    retStr = ""
    while index < len(line):
        if line[index] == " ":
            index += 1
            continue
        if line[index] == "+":
            op = line[index]
        elif line[index] == "*":
            retStr += str(value) + " * "
            value = 0
        else:
            val = re.search("[0-9]+",line[index:])
            value = evaluatePM(value,int(val.group()),op)
            index+= len(val.group())
        index+=1
    return retStr + str(value)


def evaluatePMString(line):
    return evaluateMString(evaluatePString(line))

def parse(line):
    line = line.strip()
    stack = []
    stringStack = [""]
    for char in line:
        if char == "(":
            stack.append("(")
            stringStack.append("")
        elif char == ")":
            stack.pop()
            val = evaluatePMString(stringStack[-1])
            stringStack.pop()
            stringStack[-1] += str(val)
        else:
            stringStack[-1] += char
    return evaluatePMString(stringStack[-1])

total = 0
for line in lines:
    total += parse(line)

print(total)
