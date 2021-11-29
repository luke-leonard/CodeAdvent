file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')
zeromask = 0
onemask = 0
mapper = {}
for line in lines:
    splitVal = line.split(" ")
    if splitVal[0] == "mask":
        mask = splitVal[2]
        zeromask = 0
        onemask = 0
        for i in range(len(mask)):
            if mask[len(mask)-1-i] != '0':
                zeromask += (1 << i)
            if mask[len(mask)-1-i] == '1':
                onemask += (1 << i)
        #print("{0:b}".format(zeromask), zeromask)
        #print("{0:b}".format(onemask),onemask)
    else:
        addr = splitVal[0][4:-1]
        val = int(splitVal[2])
        val &= zeromask
        val |= onemask
        mapper[addr] = val

total = 0
for key in mapper:
    total += mapper[key]
print(total)

