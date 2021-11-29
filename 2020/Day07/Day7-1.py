import re
bags = {}
def getSub(head,mapper,tab):
    ret = 0
    print(head)
    for key in head:
        bags[key] = 1
        print(tab + key)
        ret += 1
        if key in mapper:
            ret+= getSub(mapper[key],mapper,tab + "\t")
    return ret

file = open("Day7-1.txt", "r")
lines = file.read()
mapper = {}
matches = re.findall("(.*) bags contain [0-9] ([^,]+?) bags?(?:, [0-9] ([^,]+?) bags?)?(?:, [0-9] ([^,]+?) bags?)?(?:, [0-9] ([^,]+?) bags?)?\.", lines)
for match in matches:
    if match[1] != "":
        if match[1] not in mapper:
            mapper[match[1]] = []
        mapper[match[1]].append(match[0])
    if match[2] != "":
        if match[2] not in mapper:
            mapper[match[2]] = []
        mapper[match[2]].append(match[0])
    if match[3] != "":
        if match[3] not in mapper:
            mapper[match[3]] = []
        mapper[match[3]].append(match[0])
    if match[4] != "":
        if match[4] not in mapper:
            mapper[match[4]] = []
        mapper[match[4]].append(match[0])
print(mapper)
total = 0
head = mapper["shiny gold"]
getSub(head,mapper,"\t")

print(len(bags))
print(bags)


