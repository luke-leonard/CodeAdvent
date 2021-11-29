file = open("Day9-1.txt", "r")
f = file.read()
lines = f.split('\n')
nums = []
for line in lines:
    nums.append(int(line))

number = 15690279
ran = []
i = 0
while nums[i] < number:
    j = 0
    while sum(nums[i:j]) < number:
        j+=1
    if sum(nums[i:j]) == number:
        ran =nums[i:j]
    i+=1
print(max(ran) + min(ran))
