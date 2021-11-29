from queue import Queue

file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n\n')
player1 = lines[0]
player2 = lines[1]
player1Cards = player1.split("\n")[1:]
player2Cards = player2.split("\n")[1:]

maxSize = len(player1Cards) + len(player2Cards)

player1Hand = Queue(maxsize = maxSize)
player2Hand = Queue(maxsize = maxSize)

for card in player1Cards:
    player1Hand.put(int(card))

for card in player2Cards:
    player2Hand.put(int(card))

roundNum = 0
while (not player1Hand.empty()) and (not player2Hand.empty()):
    roundNum +=1
    left = player1Hand.get()
    right = player2Hand.get()
    if left > right:
        print("p1 wins round",roundNum,":",left,right)
        player1Hand.put(left)
        player1Hand.put(right)
    else:
        print("p2 wins round",roundNum,":",left,right)
        player2Hand.put(right)
        player2Hand.put(left)

winnersHand = player1Hand if not player1Hand.empty() else player2Hand

total = 0
index = maxSize
while not winnersHand.empty():
    total += index * winnersHand.get()
    index-=1

print(total)
    
