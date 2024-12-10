# n, k = map(int, input().split())
# nums = list(map(int, input().split()))

# max_sum = 0
# for i in range(n - k + 1):
#     inter_sum = 0
#     for j in range(i, i + k):
#         inter_sum += nums[j]

#     max_sum = max(max_sum, inter_sum)

# print(max_sum)

# 1차원 직선
# 총 N개의 바구니
# 중심점 c, [c-K, c+K] 구간에 있는 사탕의 수가 최대가 되도록
n, k = map(int, input().split())

# 사탕의 개수, 바구니의 위치
info_list = [list(map(int, input().split())) for _ in range(n)]
candy_list = [0] * 101 # 1-idx

for num, idx in info_list:
    candy_list[idx] = num


max_candy = 0
for c in range(200):
    candy_num = 0
    for i in range(c-k , c+k+1):
        # candy_num += candy_list[i]
        if i >= 0 and i <= 100:
            candy_num += candy_list[i]
        else:
            # print(i)
            continue    
    max_candy = max(max_candy, candy_num)

print(max_candy)