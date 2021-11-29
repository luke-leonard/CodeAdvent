def mult2020(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]

f = open("Day1-1.txt", "r")
nums = [];
for x in f:
    nums.append(int(x));

print(mult2020(nums))