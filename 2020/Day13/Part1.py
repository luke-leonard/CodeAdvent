file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')
timeStamp = int(lines[0])
mm = timeStamp
mn = 0
buses = lines[1].split(',')
for val in buses:
    if val != 'x':
        num = int(val)
        m = num - (timeStamp % num)
        if m < mm:
            mm = m
            mn = num

print(mn,mm,mm*mn)