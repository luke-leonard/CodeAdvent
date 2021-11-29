file = open("Day9-1.txt", "r")
f = file.read()
lines = f.split('\n')
nums = []
for line in lines:
    nums.append(int(line))


preambleLength = 25

for i in range(preambleLength, len(nums)):
    preamble = nums[i-preambleLength:i]
    preamble.sort()
    li = 0
    hi = preambleLength - 1
    valid = False
    while li != hi:
        if nums[i] > preamble[li] + preamble[hi]:
            li+=1
            continue
        if nums[i] < preamble[li] + preamble[hi]:
            hi-=1
            continue
        if nums[i] == preamble[li] + preamble[hi]:
            valid = True
            break
    if not valid:
        print("----------")
        print(preamble)
        print(nums[i])