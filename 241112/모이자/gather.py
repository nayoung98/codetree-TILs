# n개의 집
n = int(input())
# 각 지점에 살고 있는 사람 수
nums = list(map(int, input().split()))

min_sum = 1000000
for i, num in enumerate(nums):
    pivot = i
    sum_diff = 0

    for j in range(n):
        sum_diff += abs(pivot - j) * nums[j]

    min_sum = min(min_sum, sum_diff)

print(min_sum)