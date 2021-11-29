import math
intake = "538914762"
cups = list(intake)
cups = [int(numeric_string) for numeric_string in cups]
print(cups)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

    def __repr__(self):
        return str(self.data)

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,node : Node):
        if self.head == None:
            self.head = node
            self.tail = node
            self.tail.next = node
            self.tail.back = node
        else:
            self.tail.next = node
            node.back = self.tail
            self.tail = node
            self.tail.next = self.head
            self.head.back = self.tail

    

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))

    def __repr__(self):
        nodes = []
        for node in self.traverse(None):
            if node == self.head:
                nodes.append("("+str(node)+")")
            else:
                nodes.append(str(node))
        return(" -> ".join(nodes))

    def startLooking(self,index = 0):
        self.gap = index
        a = self.head
        self.lookStart = [a]
        self.lastInd = 0

    def getCurrent(self):
        return self.head

    def cut3(self):
        start = self.head.next
        n1 = start.next
        n2 = n1.next
        n3 = n2.next
        self.head.next = n3
        n3.back = self.head
        return start

    def paste3(self,value,cs):
        
        lefts = []
        rights = []
        for node in self.lookStart:
            lefts.append(node)
            rights.append(node)
        temp = self.lookStart
        ind = 0
        out = "f"
        checking = True
        index = 0
        while checking:
            ind+=1
            for i in range(len(lefts)):
                node = lefts[i]
                if node.data == value:
                    temp = node
                    out = "l"
                    checking = False
                    index = i
                    break
                lefts[i] = node.back
                node = rights[i]
                if node.data == value:
                    temp = node
                    out = "r"
                    checking = False
                    index = i
                    break
                rights[i] = node.next
        tempHold = temp
        print(self.lastInd,ind,out)
        after = temp.next 
        temp.next = cs
        cs.back = temp
        c1 = cs.next
        c2 = c1.next
        c2.next = after
        after.back = c2
        self.head = self.head.next


        if abs(ind) < 2000:
            for i in range(abs(ind)):
                if (out == 'l'):
                    self.lookStart[index] = self.lookStart[index].back
                else:
                    self.lookStart[index] = self.lookStart[index].next
        else:
            self.lookStart.append(tempHold)
            for i in range(abs(ind)):
                if (out == 'l'):
                    self.lookStart[-1] = self.lookStart[-1].back
                else:
                    self.lookStart[-1] = self.lookStart[-1].next
            print(tempHold,self.lookStart)
        self.lastInd = ind





for i in range (max(cups) + 1,1000000+1):
    cups.append(i)
    #print(i)

linkedCups = CircularLinkedList()
for cup in cups:
    linkedCups.append(Node(cup))

numRounds = 10000000
size = len(cups)
linkedCups.startLooking()
for i in range(numRounds):
    #print(linkedCups)
    current = linkedCups.getCurrent().data
    c3 = linkedCups.cut3()
    current = current-1
    if current == 0:
        current = size
    if (c3.data == current or c3.next.data == current or c3.next.next.data == current):
        current = current-1
        if current == 0:
            current = size
    if (c3.data == current or c3.next.data == current or c3.next.next.data == current):
        current = current-1
        if current == 0:
            current = size
    if (c3.data == current or c3.next.data == current or c3.next.next.data == current):
        current = current-1
        if current == 0:
            current = size
    linkedCups.paste3(current,c3)
    if i % 10000 == 0:
        print(i//10000)






# for i in range(numRounds):
#     currentCup = cups[:1]
#     trailingCups = cups[1:4]
#     cups = cups[4:]
#     targetCup = currentCup[0] - 1
#     while targetCup not in cups:
#         targetCup = ((targetCup - 1) + 10) % 10
#     ind = cups.index(targetCup) + 1
#     cups = cups[:ind] + trailingCups + cups[ind:] + currentCup
#     print(i)



# ind = cups.index(1)
# sol = cups[ind+1:] + cups[:ind]
# sol = [str(x) for x in sol]
# print ("".join(sol))

head = linkedCups.head

while head.data != 1:
    head = head.next

print(head.data, head.next.data,head.next.next.data)