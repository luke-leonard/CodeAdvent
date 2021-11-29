import math
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
wayX = 10
wayY = 1
direction = 0
funMap = {}

def goNorth(val):
    global wayX,wayY,x, y, direction
    wayY+=val
funMap['N'] = goNorth
def goWest(val):
    global wayX,wayY,x, y, direction
    wayX-=val
funMap['W'] = goWest
def goEast(val):
    global wayX,wayY,x, y, direction
    wayX+=val
funMap['E'] = goEast
def goSouth(val):
    global wayX,wayY,x, y, direction
    wayY-=val
funMap['S'] = goSouth
def goForward(val):
    global wayX,wayY,x, y, direction
    x += (wayX) * val
    y += (wayY) * val
funMap['F'] = goForward
def turnLeft(val):
    global wayX,wayY,x, y
    deltaX = wayX
    deltaY = wayY
    rad = math.atan2(deltaY, deltaX)
    rad = rad + math.radians(val)
    dis = math.sqrt((deltaX **2) + (deltaY **2))
    wayY = round(math.sin(rad) * dis)
    wayX = round(math.cos(rad) * dis)
funMap['L'] = turnLeft
def turnRight( val):
    global wayX,wayY,x, y, direction
    deltaX = wayX
    deltaY = wayY
    rad = math.atan2(deltaY, deltaX)
    rad = rad - math.radians(val)
    dis = math.sqrt((deltaX **2) + (deltaY **2))
    wayY = round(math.sin(rad) * dis)
    wayX = round(math.cos(rad) * dis)
funMap['R'] = turnRight

for line in lines:
    funMap[line[0]](int(line[1:]))
    print(x,y,wayX,wayY)
print(abs(x) + abs(y))