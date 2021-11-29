file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')

itters = 6

startHeight = len(lines)
startWidth = len(lines[0]) 

exHeight = startHeight + (itters * 2) + 2
exWidth = startWidth + (itters * 2) + 2
exDepth = (itters * 2) + 3
exDepth2 = (itters * 2) + 3


def getAdj(x,y,z,w,brd):
    val = 0 - brd[x][y][z][w]
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for l in range(-1,2):
                    val += brd[x+i][y+j][z+k][w+l]
    return val
    
def copyBoard(brd):
    board2 = []
    for i in range(len(brd)):
        w = []
        for j in range(len(brd[i])):
            d = []
            for k in range(len(brd[i][j])):
                d2 = []
                for l in range(len(brd[i][j][k])):
                    d2.append(brd[i][j][k][l])
                d.append(d2)
            w.append(d)
        board2.append(w)
    return board2


board = []
for i in range(exHeight):
    w = []
    for j in range(exWidth):
        d = []
        for k in range(exDepth):
            d2 = []
            for l in range(exDepth2):
                d2.append(0)
            d.append(d2)
        w.append(d)
    board.append(w)

xOffset = int((exHeight - len(lines)) / 2)
yOffest = int((exWidth - len(lines[0])) / 2)
zOffset = int(exDepth / 2)
wOffset = int(exDepth2 / 2)


for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            board[xOffset + i][yOffest + j][zOffset][wOffset] = 1

#printBoard(board)
#print("----------------------------")
for a in range(itters):
    boardCopy = copyBoard(board)
    for i in range(1,exHeight-1):
        for j in range(1,exWidth-1):
            for k in range(1,exDepth-1):
                for l in range(1,exDepth2-1):
                    adj = getAdj(i,j,k,l,board)
                    if adj == 3 and board[i][j][k][l] == 0:
                        boardCopy[i][j][k][l] = 1
                    elif (adj == 3 or adj == 2) and board[i][j][k][l] == 1:
                        boardCopy[i][j][k][l] = 1
                    else:
                        boardCopy[i][j][k][l] = 0
    board = boardCopy
    #printBoard(board)
    #print("----------------------------")

total = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        for k in range(len(board[0][0])):
            for l in range(len(board[0][0][0])):
                total += board[i][j][k][l]
print(total)