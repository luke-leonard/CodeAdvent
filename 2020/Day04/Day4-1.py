file = open("Day4-1.txt", "r")
lines = file.read()
f = lines.split('\n')
users = []
user = {}
for line in f:
    if line == "":
        users.append(user)
        user = {}
        continue
    fields = line.split(" ")
    for field in fields:
        keyVal = field.split(":")
        user[keyVal[0]] = keyVal[1]
total = 0
for u in users:
    if "byr" in u and "iyr" in u and "eyr" in u and "hgt" in u and "hcl" in u and "ecl" in u and "pid"in u:
        total+=1
print(total)
