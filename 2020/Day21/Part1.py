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


print(allergensMap)

for allergen in allergensMap:
    for ingredient in allergensMap[allergen]:
        ingredientsMap.pop(ingredient, None)


total = 0
for ingredient in ingredientsMap:
    total+= ingredientsMap[ingredient]

print(total)
    