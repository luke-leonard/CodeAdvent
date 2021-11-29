file = open("Day10-1.txt", "r")
f = file.read()
lines = f.split('\n')
nums = []
for line in lines:
    nums.append(int(line))

nums.sort()
diffs = {1:0,2:0,3:1}
index = 1
prevNum = nums[0]
diffs[nums[0]]+=1

while index < len(nums):
    diffs[nums[index] - prevNum]+=1
    prevNum = nums[index]
    index+=1

print(diffs[1] * diffs[3])

