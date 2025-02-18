a, b, c = map(int, input().split())
nums = a * b * c
nums = str(nums)
result = 0

for i in range(len(nums)):
    result += int(nums[i])

print(result)