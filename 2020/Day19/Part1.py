import re
file = open("Input.txt", "r")
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
        ret = {"valid":True, "remainder":""}
        if str == "":
            return ret
        if self.type == "val":
            ret["valid"] = str[0] == self.pattern
            ret["remainder"] = str[1:]
        if self.type == "list":
            inputString = str
            for ins in self.instructions:
                valRet = Instruction.mapper[ins].validate(inputString,show,nest + " ")
                if not valRet["valid"]:
                    ret["valid"] = False
                    if show:
                        print(nest,"ret:",ret)
                    return ret
                else:
                    inputString = valRet["remainder"]
            ret["remainder"] = inputString
        if self.type == "opt":
            self.type = "list"
            self.instructions = self.left
            valRet = self.validate(str,show,nest + "L")
            if valRet["valid"]:
                self.type = "opt"
                if show:
                    print(nest,"ret:",valRet)
                return valRet
            self.instructions = self.right
            ret = self.validate(str,show,nest + "R")
            self.type = "opt"
        if show:
            print(nest,"ret:",ret)
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

# print (Instruction.mapper['0'].validate(vals[0]))
total = 0
for val in vals:
    process = Instruction.mapper['0'].validate(val)
    if process["valid"] == True and process["remainder"] == "":
        total+=1
print(total)
