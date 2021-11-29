file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')

itters = 6

startHeight = len(lines)
startWidth = len(lines[0]) 

exHeight = startHeight + (itters * 2) + 2
exWidth = startWidth + (itters * 2) + 2
exDepth = (itters * 2) + 3

def printBoard(brd):
    h = len(brd)
    w = len(brd[0])
    d = len(brd[0][0])
    for k in range(d):
        for i in range(h):
            for j in range(w):
                print(brd[i][j][k], end='')
            print()
        print()

def getAdj(x,y,z,brd):
    val = 0 - brd[x][y][z]
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                val += brd[x+i][y+j][z+k]
    return val
    
def copyBoard(brd):
    board2 = []
    for i in range(len(brd)):
        w = []
        for j in range(len(brd[i])):
            d = []
            for k in range(len(brd[i][j])):
                d.append(brd[i][j][k])
            w.append(d)
        board2.append(w)
    return board2


board = []
for i in range(exHeight):
    w = []
    for j in range(exWidth):
        d = []
        for k in range(exDepth):
            d.append(0)
        w.append(d)
    board.append(w)

xOffset = int((exHeight - len(lines)) / 2)
yOffest = int((exWidth - len(lines[0])) / 2)
zOffset = int(exDepth / 2)


for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            board[xOffset + i][yOffest + j][zOffset] = 1

#printBoard(board)
#print("----------------------------")
for a in range(itters):
    boardCopy = copyBoard(board)
    for i in range(1,exHeight-1):
        for j in range(1,exWidth-1):
            for k in range(1,exDepth-1):
                adj = getAdj(i,j,k,board)
                if adj == 3 and board[i][j][k] == 0:
                    boardCopy[i][j][k] = 1
                elif (adj == 3 or adj == 2) and board[i][j][k] == 1:
                    boardCopy[i][j][k] = 1
                else:
                    boardCopy[i][j][k] = 0
    board = boardCopy
    #printBoard(board)
    #print("----------------------------")

total = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        for k in range(len(board[0][0])):
            total += board[i][j][k]
print(total)