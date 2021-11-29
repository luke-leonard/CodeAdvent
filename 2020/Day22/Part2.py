from queue import Queue
import copy

file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n\n')
player1 = lines[0]
player2 = lines[1]
player1Cards = player1.split("\n")[1:]
player2Cards = player2.split("\n")[1:]

player1Cards = [int(numeric_string) for numeric_string in player1Cards]
player2Cards = [int(numeric_string) for numeric_string in player2Cards]

totalnum = len(player1Cards) + len(player2Cards)

roundWins = {}
game=0
gameWins = {}
def playGame(player1Cards,player2Cards,nest = ""):
    global gameWins
    rounds = {}
    roundNum = 0
    roundKeys = []
    while player1Cards and player2Cards:
        thisRound = "p1" + " ".join(str(x) for x in player1Cards) + "p2"+" ".join(str(x) for x in player2Cards)
        if thisRound in rounds:
            #print(nest,"dup")
            return player1Cards + player2Cards , []
        rounds[thisRound] = True
        roundNum +=1
        roundKeys.append(thisRound)
        if thisRound in gameWins:
            return gameWins[thisRound]["a"],gameWins[thisRound]["b"]

        left = player1Cards[0]
        right = player2Cards[0]
        player1Cards = player1Cards[1:]
        player2Cards = player2Cards[1:]

        if(left > len(player1Cards) or right >len(player2Cards)):
            if left > right:
                #print(nest,"p1 wins round",roundNum,":",left,right)
                player1Cards.append(left)
                player1Cards.append(right)
            else:
                #print(nest,"p2 wins round",roundNum,":",left,right)
                player2Cards.append(right)
                player2Cards.append(left)
        else:
            p1,p2 = playGame(player1Cards[:left],player2Cards[:right],nest+" ")
            if p1:
                player1Cards.append(left)
                player1Cards.append(right)
            if p2:
                player2Cards.append(right)
                player2Cards.append(left)
    for r in roundKeys:
        gameWins[r] = {"a":player1Cards,"b":player2Cards}

    return player1Cards,player2Cards











player1Cards, player2Cards =playGame(player1Cards,player2Cards)


winnersHand = player1Cards if player1Cards else player2Cards


total = 0

for i in range(len(winnersHand)) :
    total += (totalnum - i) * winnersHand[i]


print(total)
    
