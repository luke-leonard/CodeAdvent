import re
file = open("Input.txt", "r")
f = file.read()
lines = f.split("\n")

class HexNode:
    id = 0
    def __init__(self):
        self.graph = {
            "e":None,
            "se":None,
            "sw":None,
            "w":None,
            "nw":None,
            "ne":None
        }
        self.IsWhite = True
        self.id = HexNode.id
        HexNode.id+=1

    def getPrVal(self,on):
        if self.graph[on] == None:
            return "*"
        else:
            return str(self.graph[on].id)


    def printNode(self):
        print("  "+self.getPrVal("nw")+"   "+self.getPrVal("ne"))
        print("   \\ /")
        print(self.getPrVal("w")+" - "+str(self.id)+" - "+self.getPrVal("e"))
        print("   / \\")
        print("  "+self.getPrVal("sw")+"   "+self.getPrVal("se"))


    
    def connectNew(self,on):
        connectOrder = ["e","se","sw","w","nw","ne"]
        myDir = (connectOrder.index(on) + 3) % 6
        newNode = HexNode()
        currentIndex = myDir
        currentNode = self

        currentOn = on
        currentNode.graph[on] = newNode
        newNode.graph[connectOrder[currentIndex]] = currentNode

        while currentNode.graph[connectOrder[(currentIndex + 1) % 6]] != None:
            currentIndex = ((currentIndex - 1) + 6) % 6
            currentOn = (currentOn + 1) % 6
            currentNode = currentNode.graph[currentOn]
            currentNode.graph[on] = newNode
            newNode.graph[connectOrder[currentIndex]] = currentNode




center = HexNode()
center.printNode()

center.connectNew("ne")
center.printNode()
center.graph["ne"].printNode()













class HexMap:
    def __init__(self,size):
        self.center = HexNode()
        for i in range(size):
            print()

    def addLayer(self,size,start):
        innerNode = start
        firstNode = HexNode()
        firstNode.graph["w"] = innerNode
        innerNode.graph["e"] = firstNode
        nextNode = firstNode
        for i in range(size):
            innerNode = innerNode.graph["sw"].graph["se"]











# for line in lines:
#     matches = re.findall("(?:e)|(?:se)|(?:sw)|(?:w)|(?:nw)|(?:ne)",line)
#     for match in matches:
#         print(match, end=" ")
#     print()
