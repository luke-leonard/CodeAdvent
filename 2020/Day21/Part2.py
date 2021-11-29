import re
file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')

allergensMap = {}
ingredientsMap = {}

for line in lines:
    match = re.search(r"^([a-z\s]+) \(contains ([a-z,\s]+)\)$",line)
    ingredients = match.group(1).split(" ")
    allergens = match.group(2).split(", ")

    for ingredient in ingredients:
        if ingredient not in ingredientsMap:
            ingredientsMap[ingredient] = 0
        ingredientsMap[ingredient]+=1

    for allergen in allergens:
        if allergen not in allergensMap:
            allergensMap[allergen] = ingredients.copy()
        else:
            removables = []
            for ingredient in allergensMap[allergen]:
                if ingredient not in ingredients:
                    removables.append(ingredient)
            for ingredient in removables:
                allergensMap[allergen].remove(ingredient)


#print(allergensMap)

for allergen in allergensMap:
    for ingredient in allergensMap[allergen]:
        ingredientsMap.pop(ingredient, None)


total = 0
for ingredient in ingredientsMap:
    total+= ingredientsMap[ingredient]

allergensMapSolved = {}

while len(allergensMap) > 0:
    ingredient = ""
    for allergen in allergensMap:
        if len(allergensMap[allergen]) == 1:
            allergensMapSolved[allergen] = allergensMap[allergen][0]
            ingredient = allergensMap[allergen][0]
            allergensMap.pop(allergen)
            break
    for allergen in allergensMap:
        if ingredient in allergensMap[allergen]:
            allergensMap[allergen].remove(ingredient)
    
print(allergensMapSolved)

amsList = []

for allergen in allergensMapSolved:
    amsList.append(allergen)

amsList.sort()

print(amsList)

outString = ""

for allergen in amsList:
    outString += allergensMapSolved[allergen] + ","

outString = outString[:-1]
print(outString)