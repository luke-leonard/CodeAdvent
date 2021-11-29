
def getMask(addrs,mask,val):
    if mask == 0:
        addrs.append(val)
    else:
        bit = getLowestBit(mask)
        val1 = (val | bit) ^ bit
        val2 = val | bit
        mask1 = (mask | bit) ^ bit
        getMask(addrs,mask1,val1)
        getMask(addrs,mask1,val2)

def getLowestBit(val):
    if val == 0:
        return 0
    i = 1
    while val | i != val:
        i <<= 1
    return i

file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')
xmasks = 0
onemask = 0
mapper = {}
for line in lines:
    splitVal = line.split(" ")
    if splitVal[0] == "mask":
        mask = splitVal[2]
        xmask = 0
        onemask = 0
        for i in range(len(mask)):
            if mask[len(mask)-1-i] == 'X':
                xmask += (1 << i)
            if mask[len(mask)-1-i] == '1':
                onemask += (1 << i)
        #print("{0:b}".format(zeromask), zeromask)
        #print("{0:b}".format(onemask),onemask)
    else:
        addrRaw = splitVal[0][4:-1]
        castAddr = int(addrRaw)
        val = int(splitVal[2])
        castAddr |= onemask
        addrs = []
        getMask(addrs,xmask,castAddr)
        for addr in addrs:
            mapper[addr] = val

total = 0
for key in mapper:
    total += mapper[key]
print(total)
