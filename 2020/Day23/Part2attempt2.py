
size = 1000000

start = 5
#linkedList = [0,2,5,8,6,4,7,10,9,1]
linkedList = [0,4,10,8,7,3,2,6,9,1]
for i in range(len(cups)+1,size):
    linkedList.append(i+1)
linkedList.append(start)

def printIt(ll,ind):
    global size
    str1 = ""
    for i in range(size):
        str1+= str(ll[ind]) + " -> "
        ind = ll[ind]
    print(str1)

numRounds = 10000000
current = start
#printIt(linkedList,size)
for i in range(numRounds):
    prev = current
    s = linkedList[current]
    i1 = linkedList[s]
    i2 = linkedList[i1]
    linkedList[current] = linkedList[i2]
    current = current-1
    if current == 0:
        current = size
    if (s == current or i1 == current or i2 == current):
        current = current-1
        if current == 0:
            current = size
    if (s == current or i1 == current or i2 == current):
        current = current-1
        if current == 0:
            current = size
    if (s == current or i1 == current or i2 == current):
        current = current-1
        if current == 0:
            current = size
    temp = linkedList[current]
    linkedList[current] = s
    linkedList[i2] = temp

    current = linkedList[prev]
    #printIt(linkedList,prev)
    


print(linkedList[linkedList[1]] *linkedList[1])

















