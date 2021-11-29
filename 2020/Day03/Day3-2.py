file = open("Day3-1.txt", "r")
lines = file.read()
f = lines.split('\n')
def fun(f,d,r):
    total = 0
    on = 0
    i = d-1
    for x in f:
        i+=1
        i%=d
        if i != 0:
            continue
        on %= len(x) 
        if x[on] == "#":
            total+=1
        on+=r
    return total

print (fun(f,1,1) * fun(f,1,3) * fun(f,1,5) * fun(f,1,7) * fun(f,2,1))