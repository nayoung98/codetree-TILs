# 구간을 잘 골라 -> 모든 구간 정해야됨
# 해당 구간 내 숫자 합이 최대가 되도록

arr = [4, -5, 8, -1, -6, 9]
max_sum = 0
for i in range(n):
    for j in range(i, n): # 구간 잡기
        sum_val = 0

        for k in range(i, j + 1):
            sum_val += arr[k]

        max_sum = max(max_sum, sum_val)

# n개의 숫자
# 특정 구간 내 원소들의 평균값이 그 구간의 원소 중 하나가 되는 가짓수 구하기
n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        tmp_sum = 0
        for k in range(i, j + 1):
            tmp_sum += arr[k]
        tmp_sum //= abs(i - j + 1)
        
        for k in range(i, j + 1):
            if tmp_sum == arr[k]:
                cnt += 1

print(cnt)