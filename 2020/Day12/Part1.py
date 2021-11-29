file = open("Input.txt", "r")
f = file.read()
lines = f.split('\n')

#    N ^ (90)
# W    |   (0)
# <----+---->      
#(-x)  |    E
#  (-y)v S


x = 0
y = 0
direction = 0
funMap = {}

def goNorth(val):
    global x, y, direction
    y+=val
funMap['N'] = goNorth
def goWest(val):
    global x, y, direction
    x-=val
funMap['W'] = goWest
def goEast(val):
    global x, y, direction
    x+=val
funMap['E'] = goEast
def goSouth(val):
    global x, y, direction
    y-=val
funMap['S'] = goSouth
def goForward(val):
    global x, y, direction
    if(direction == 0):
        goEast(val)
    if(direction == 90):
        goNorth(val)
    if(direction == 180):
        goWest(val)
    if(direction == 270):
        goSouth(val)
funMap['F'] = goForward
def turnLeft(val):
    global x, y, direction
    direction = (direction + val + 360) % 360
funMap['L'] = turnLeft
def turnRight( val):
    global x, y, direction
    direction = (direction - val + 360) % 360
funMap['R'] = turnRight

for line in lines:
    funMap[line[0]](int(line[1:]))
    print(x,y)
print(abs(x) + abs(y))