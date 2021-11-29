import math
import string
file = open("Input.txt", "r")
f = file.read()
tilesRaw = f.split('\n\n')

class Tile:
    def __init__(self, id, stringArr):
        self.id = id
        self.rotation = 0
        self.flippedVert = False
        self.flippedHor = False
        arr = []
        for string in stringArr:
            charArr = []
            for char in string:
                charArr.append(char)
            arr.append(charArr)
        self.tile = arr
        self.calcCodes()
        self.getPossibleCodes()

    def calcCodes(self):
        code = 0
        for i in range(len(self.tile)):
            if self.tile[0][i] == "#":
                code |= 1 << i
        self.topCode = code
        code = 0
        for i in range(len(self.tile)):
            if self.tile[i][0] == "#":
                code |= 1 << i
        self.leftCode = code
        code = 0
        for i in range(len(self.tile)):
            if self.tile[len(self.tile)-1][i] == "#":
                code |= 1 << i
        self.bottomCode = code
        code = 0
        for i in range(len(self.tile)):
            if self.tile[i][len(self.tile)-1] == "#":
                code |= 1 << i
        self.rightCode = code
        self.codes = []
        self.codes.append(self.topCode)
        self.codes.append(self.leftCode)
        self.codes.append(self.bottomCode)
        self.codes.append(self.rightCode)
    
    def printTile(self):
        for tStr in  self.tile:
            for c in tStr:
                print(c,end="")
            print()
    
    def flipVert(self):
        arr = []
        self.flippedVert = not self.flippedVert
        for row in self.tile[::-1]:
            arr.append(row)
        self.tile = arr
        self.calcCodes()

    def flipHorz(self):
        arr = []
        self.flippedHor = not self.flippedHor 
        for row in self.tile:
            rowArr = []
            for col in row[::-1]:
                rowArr.append(col)
            arr.append(rowArr)
        self.tile = arr
        self.calcCodes()

    def getPossibleCodes(self):
        self.possibleCodes = self.codes
        self.possibleCodesCombos = [self.codes]
        self.flipVert()
        self.possibleCodesCombos.append(self.codes)
        self.flipHorz()
        self.possibleCodes += self.codes
        self.possibleCodesCombos.append(self.codes)
        self.flipVert()
        self.possibleCodesCombos.append(self.codes)
        self.flipHorz()

class Puzzle:
    blankTile = Tile(0,["..........","..........","..........","..........","..........","..........","..........","..........","..........",".........."])
    symbols = string.printable[:-6]
    def __init__(self,tileList):
        self.tiles = tileList
        self.length = int(math.sqrt(len(tileList)))
        self.puzzleGrid = []
        for i in range(self.length):
            row = []
            for j in range(self.length):
                row.append(Puzzle.blankTile)
            self.puzzleGrid.append(row) 
        self.codePrintMap = {}
        self.totalCodesOccurences = {}
        for tile in tiles:
            for code in tile.possibleCodes:
                if code not in self.totalCodesOccurences:
                    self.totalCodesOccurences[code] = 0
                self.totalCodesOccurences[code] +=1
        self.numRequiredMatches = (self.length * (self.length - 1)) * 2
        self.findFirstPiece()
    
    def mapCodePrint(self,code:int):
        if code in self.codePrintMap:
            return self.codePrintMap[code]
        self.codePrintMap[code] = Puzzle.symbols[self.symbolsIndex]
        self.symbolsIndex+=1
        return self.codePrintMap[code]

    def printPuzzle(self):
        self.symbolsIndex = 0
        for i in range(self.length):
            str1 = ""
            str2 = ""
            str3 = ""
            for j in range (self.length):
                tile = self.puzzleGrid[i][j]
                str1 += " "                                   + str(self.mapCodePrint(tile.topCode))    + " "                                    + " "
                str2 += str(self.mapCodePrint(tile.leftCode)) + str(tile.id)                            + str(self.mapCodePrint(tile.rightCode)) + " "  
                str3 += " "                                   + str(self.mapCodePrint(tile.bottomCode)) + " "                                    + " "
            print(str1)
            print(str2)
            print(str3)
            print()

    def findFirstPiece(self):
        for tile in self.tiles:
            matchCount = 0
            for code in tile.possibleCodes:
                if self.totalCodesOccurences[code] >= 2:
                    matchCount +=1
            if matchCount == 4:
                self.puzzleGrid[0][0] = tile

    def findCornerPiecesProduct(self):
        total = 1
        for tile in self.tiles:
            matchCount = 0
            for code in tile.possibleCodes:
                if self.totalCodesOccurences[code] >= 2:
                    matchCount +=1
            if matchCount == 4:
                total *= tile.id
        print(total)

    #def solve(self):
        




tiles = []
for tile in tilesRaw:
    lines = tile.split("\n")
    tileId = int(lines[0][4:-1])
    tile = Tile(tileId,lines[1:])
    tiles.append(tile)

puzzle = Puzzle(tiles)
tile = tiles[0]


#puzzle.printPuzzle()
puzzle.findCornerPiecesProduct()


















# count = 0 
# for code in puzzle.totalCodesOccurences:
#     if puzzle.totalCodesOccurences[code] >= 2:
#         count +=1
#         #print(code)

# print(puzzle.length)
# print(puzzle.numRequiredMatches , count)