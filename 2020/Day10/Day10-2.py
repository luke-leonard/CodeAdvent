file = open("Day10-1.txt", "r")
f = file.read()
lines = f.split('\n')
nums = []
for line in lines:
    nums.append(int(line))

nums.sort()
ways = {0:1}

for i in range(len(nums)):
    num = nums[i]
    way1 = 0
    if num-1 in ways:
        way1 = ways[num-1]
    way2 = 0
    if num-2 in ways:
        way2 = ways[num-2]
    way3 = 0
    if num-3 in ways:
        way3 = ways[num-3]
    ways[num] = way1 + way2 + way3

print(ways[nums[-1]])
