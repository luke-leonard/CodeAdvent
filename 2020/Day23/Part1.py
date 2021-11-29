intake = "538914762"
cups = list(intake)
cups = [int(numeric_string) for numeric_string in cups]
print(cups)

numRounds = 100
size = len(cups)
for i in range(numRounds):
    currentCup = cups[:1]
    trailingCups = cups[1:4]
    cups = cups[4:]
    targetCup = currentCup[0] - 1
    while targetCup not in cups:
        targetCup = ((targetCup - 1) + 10) % 10
    ind = cups.index(targetCup) + 1
    cups = cups[:ind] + trailingCups + cups[ind:] + currentCup
    print(currentCup, trailingCups, cups, targetCup)

ind = cups.index(1)
sol = cups[ind+1:] + cups[:ind]
sol = [str(x) for x in sol]
print ("".join(sol))