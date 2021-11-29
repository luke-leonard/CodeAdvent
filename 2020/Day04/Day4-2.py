file = open("Day4-1.txt", "r")
lines = file.read()
f = lines.split('\n')
users = []
eyeColors = {"amb","blu","brn", "gry","grn","hzl","oth"}
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
    try:
        if  (
            "byr" in u and
            int(u["byr"]) >= 1920 and
            int(u["byr"]) <= 2002 and
            "iyr" in u and
            int(u["iyr"]) >= 2010 and
            int(u["iyr"]) <= 2020 and
            "eyr" in u and
            int(u["eyr"]) >= 2020 and
            int(u["eyr"]) <= 2030 and
            "hgt" in u and
            (u["hgt"][-2:] == "cm" or u["hgt"][-2:] == "in") and
            "hcl" in u and
            u["hcl"][0] == "#" and
            len(u["hcl"]) == 7 and 
            int("0x"+u["hcl"][-6:],16) and
            "ecl" in u and 
            u["ecl"] in eyeColors and
            "pid"in u and 
            len(u["pid"]) == 9 and 
            int(u["pid"]) != 0
            ): 
            if(
                u["hgt"][-2:] == "cm" and 
                int(u["hgt"][:-2]) >= 150 and 
                int(u["hgt"][:-2]) <= 193
                ):
                total+=1
            if(
                u["hgt"][-2:] == "in" and 
                int(u["hgt"][:-2]) >= 59 and 
                int(u["hgt"][:-2]) <= 76
                ):
                total+=1
    except:
        print(u)
print(total)
