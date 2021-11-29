start = [2,0,6,12,1,3]

mapper = {}
turn = 1
for val in start:
    obj = {"last":turn,"first":turn}
    mapper[val] = obj
    #print(turn,val,mapper[val])
    turn+=1
lastNumber = start[-1]

while turn <= 2020:
    #print(turn,lastNumber,mapper[lastNumber])
    if mapper[lastNumber]["first"] == turn-1:
        lastNumber = 0
    else:
        lastNumber = mapper[lastNumber]["last"] - mapper[lastNumber]["first"]
        
    if lastNumber in mapper:
        mapper[lastNumber]["first"] = mapper[lastNumber]["last"]
        mapper[lastNumber]["last"] = turn 
    else:
        mapper[lastNumber] = {"last":turn,"first":turn}
        print(turn)
    turn+=1
print(lastNumber)


