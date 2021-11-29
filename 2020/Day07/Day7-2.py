import re

file = open("Day7-1.txt", "r")
lines = file.read()
mapper = {}
matches = re.findall("(.*) bags contain ([0-9]) ([^,]+?) bags?(?:, ([0-9]) ([^,]+?) bags?)?(?:, ([0-9]) ([^,]+?) bags?)?(?:, ([0-9]) ([^,]+?) bags?)?\.", lines)
for match in matches:
    mapper[match[0]] = []
    if match[2] != "":
        mat = {}
        mat['number'] = int(match[1])
        mat['color'] = match[2]
        mapper[match[0]].append(mat)
    if match[4] != "":
        mat = {}
        mat['number'] = int(match[3])
        mat['color'] = match[4]
        mapper[match[0]].append(mat)
    if match[6] != "":
        mat = {}
        mat['number'] = int(match[5])
        mat['color'] = match[6]
        mapper[match[0]].append(mat)
    if match[8] != "":
        mat = {}
        mat['number'] = int(match[7])
        mat['color'] = match[8]
        mapper[match[0]].append(mat)


def getNum(bags):
    val = 0
    for bag in bags:
        if bag['color'] in mapper:
            val += getNum(mapper[bag['color']]) * bag['number']
        val += bag['number']
    return val


print(getNum(mapper["shiny gold"]))




