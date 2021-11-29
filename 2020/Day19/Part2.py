import re
file = open("Input2.txt", "r")
f = file.read()
lines = f.split('\n')

class Instruction:
    mapper = {}

    def __init__(self, line):
        spl = line.split(":")
        self.name = spl[0]

        match = re.search("([a-zA-z])",spl[1])
        if match:
            self.pattern = match.group(1)
            self.type = "val"
            #print(self.pattern)
        
        match = re.search("\s+([\d\s]+)\s+\|\s+([\d\s]+)$",spl[1])
        if match:
            self.left = match.group(1).split(" ")
            self.right = match.group(2).split(" ")
            self.type = "opt"
            #print(self.left,":",self.right)

        match = re.search("^\s+([\d\s]+)$",spl[1])
        if match:
            self.type = "list"
            self.instructions = match.group(1).split(" ")
            #print(self.instructions)
        
        Instruction.mapper[self.name] = self

    def validate(self,str,show = False,nest = ""):
        if show:
            print(nest,self.name,":",str)
        ret = {"valid":False, "remainder":[]}
        if str == "":
            return ret
        if self.type == "val":
            ret["valid"] = str[0] == self.pattern
            ret["remainder"].append(str[1:])
        if self.type == "list":
            ret = self.validateList(str,show,nest,self.instructions)
        if self.type == "opt":
            ret = self.validateOpt(str,show,nest)
        if show:
            print(nest,"ret:",ret)
        return ret

    def validateList(self,str,show = False,nest = "", inst = []):
        ret = {"valid":True, "remainder":[]}
        inputStrings = [str]
        for ins in inst:
            valid = False
            retInStrs = []
            for inputString in inputStrings:
                valRet = Instruction.mapper[ins].validate(inputString,show,nest + ins+" ")
                if not valRet["valid"]:
                    continue
                valid = True
                retInStrs += valRet["remainder"]
            if not valid:
                return ret
            inputStrings = retInStrs
        ret["remainder"] = inputStrings
        return ret

    def validateOpt(self,str,show = False,nest = ""):
        ret = {"valid":True, "remainder":[]}
        leftRet = self.validateList(str,show,nest + "L",self.left)
        rightRet = self.validateList(str,show,nest + "R",self.right)
        if leftRet["valid"]:
            ret["remainder"]+=leftRet["remainder"]
        if rightRet["valid"]:
            ret["remainder"]+=rightRet["remainder"]
        return ret

inst = True
vals = []

for line in lines:
    if line == "":
        inst = False
        continue
    if inst:
        Instruction(line)
    else:
        vals.append(line)

#print (Instruction.mapper['0'].validate(vals[2],True))
total = 0
for val in vals:
    process = Instruction.mapper['0'].validate(val)
    if process["valid"] == True and "" in process["remainder"]:
        #print(val)
        total+=1
print(total)
