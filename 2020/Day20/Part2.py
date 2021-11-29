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
    
    def rotate(self):
        arr = []
        self.rotation = (self.rotation + 1) % 4
        for i in range(len(self.tile)):
            colArr = []
            for j in range(len(self.tile)):
                colArr.append(self.tile[j][i])
            arr.append(colArr)
        self.tile = arr
        self.flipHorz()

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

    def nextOrientation(self):
        self.rotate()
        if self.rotation == 0:
            self.flipVert()
            if not self.flippedVert:
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
        self.totalCodesOccurencesIds = {}
        for tile in tiles:
            for code in tile.possibleCodes:
                if code not in self.totalCodesOccurences:
                    self.totalCodesOccurences[code] = 0
                    self.totalCodesOccurencesIds[code] = []
                self.totalCodesOccurences[code] +=1
                self.totalCodesOccurencesIds[code].append(tile.id)
        self.numRequiredMatches = (self.length * (self.length - 1)) * 2
        self.indexTiles()
        self.findFirstPiece()
        self.solvePuzzle()
        self.makeImage()
    
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

    def compileFullPuzzle(self):
        arr = []
        for i in range(self.length):
            strArr = ["","","","","","","","","",""]
            for j in range (self.length):
                for k in range(len(self.puzzleGrid[i][j].tile)):
                    for l in range(len(self.puzzleGrid[i][j].tile[k])):
                        strArr[k]+=self.puzzleGrid[i][j].tile[k][l]
                    strArr[k]+=" "
            for s in strArr:
                arr.append(s)
            arr.append("")
        self.assembled = arr

    def printFullPuzzle(self):
        self.compileFullPuzzle()
        for s in self.assembled:
            print(s)

    def findFirstPiece(self):
        for tile in self.tiles:
            matchCount = 0
            matches = {}
            for code in tile.possibleCodes:
                if self.totalCodesOccurences[code] >= 2:
                    matchCount +=1
                    matches[code] = True
            if matchCount == 4:
                while(tile.rightCode not in matches or tile.bottomCode not in matches):
                    tile.rotate()
                self.puzzleGrid[0][0] = tile
                break
    
    def indexTiles(self):
        self.tilesById = {}
        self.tilesByCode = {}
        for tile in self.tiles:
            self.tilesById[tile.id] = tile
            for code in tile.possibleCodes:
                if code not in self.tilesByCode:
                    self.tilesByCode[code] = []
                self.tilesByCode[code].append(tile)

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

    def solveRow(self,rowIndex):
        firstTile = self.puzzleGrid[rowIndex][0]
        for i in range(self.length - 1):
            rightCode = firstTile.rightCode
            twoTiles = self.tilesByCode[rightCode]
            secondTile = Puzzle.blankTile
            if twoTiles[0].id == firstTile.id:
                secondTile = twoTiles[1]
            else:
                secondTile = twoTiles[0]
            while secondTile.leftCode != rightCode:
                secondTile.nextOrientation()
            self.puzzleGrid[rowIndex][i+1] = secondTile
            firstTile = secondTile

    def solvePuzzle(self):
        firstTile = self.puzzleGrid[0][0]
        self.solveRow(0)
        for i in range(self.length - 1):
            bottomCode = firstTile.bottomCode
            twoTiles = self.tilesByCode[bottomCode]
            secondTile = Puzzle.blankTile
            if twoTiles[0].id == firstTile.id:
                secondTile = twoTiles[1]
            else:
                secondTile = twoTiles[0]
            while secondTile.topCode != bottomCode:
                secondTile.nextOrientation()
            self.puzzleGrid[i+1][0] = secondTile
            self.solveRow(i+1)
            firstTile = secondTile
    
    def makeImage(self):
        arr = []
        for i in range(self.length):
            strArr = ["","","","","","","",""]
            for j in range (self.length):
                for k in range(1,len(self.puzzleGrid[i][j].tile)-1):
                    for l in range(1,len(self.puzzleGrid[i][j].tile[k])-1):
                        strArr[k-1]+=self.puzzleGrid[i][j].tile[k][l]
            for s in strArr:
                arr.append(s)
        self.image = arr
    
    def printImage(self):
        self.makeImage()
        for s in self.image:
            print(s)


tiles = []
for tile in tilesRaw:
    lines = tile.split("\n")
    tileId = int(lines[0][4:-1])
    tile = Tile(tileId,lines[1:])
    tiles.append(tile)

puzzle = Puzzle(tiles)
tile = tiles[0]

#puzzle.findCornerPiecesProduct()


imageTile = Tile(1,puzzle.image)

#imageTile.printTile()
print()
pattern =[
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]
patternIndexes = []
for i in range(len(pattern)):
    patternIndexes.append([])
    for j in range(len(pattern[i])):
        if pattern[i][j] == "#":
            patternIndexes[i].append(j)

for itterations in range(16):

    for i in range (len(imageTile.tile) - len(pattern)):
        for j in range(len(imageTile.tile[0]) - len(pattern[0])):
            monster = True
            for x in range(len(patternIndexes)):
                for index in patternIndexes[x]:
                    if not (imageTile.tile[i+x][j+index] == "#" or imageTile.tile[i+x][j+index] == "0"):
                        monster = False
            if monster:
                for x in range(len(patternIndexes)):
                    for index in patternIndexes[x]:
                        imageTile.tile[i+x][j+index] = "0"

    imageTile.nextOrientation()

imageTile.printTile()

total = 0
for s in imageTile.tile:
    for c in s:
        if c == "#":
            total += 1
print(total)












# count = 0 
# for code in puzzle.totalCodesOccurences:
#     if puzzle.totalCodesOccurences[code] >= 2:
#         count +=1
#         #print(code)

# print(puzzle.length)
# print(puzzle.numRequiredMatches , count)