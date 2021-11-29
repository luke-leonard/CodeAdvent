file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')


def generatePublicKey(subjectNumber,loopSize):
    value = 1
    for i in range(loopSize):
        value *= subjectNumber
        value = value % 20201227
    return value

cardPublicKey = int(lines[0])
doorPublicKey = int(lines[1])

index = 1
encryptionKey = 0
value = 1
while True:
    value = value * 7
    value = value % 20201227
    if value == cardPublicKey:
        encryptionKey = generatePublicKey(doorPublicKey,index)
        break
    if value == doorPublicKey:
        encryptionKey = generatePublicKey(cardPublicKey,index)
        break
    index+=1
print(encryptionKey)
