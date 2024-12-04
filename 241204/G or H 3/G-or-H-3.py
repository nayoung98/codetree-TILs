# n명의 사람들 -> G or H
# 사진의 크기 : k (양쪽 끝에 있는 x끼리의 차)
# G : += 1, H : += 2
# 사진을 찍어 얻을 수 있는 최대 점수 

n, k = map(int, input().split())
info_list = [list(input().split()) for _ in range(n)]
arr = [0] * (10001) # 1-idx

for x, elem in info_list:
    x = int(x)

    if elem == 'G':
        arr[x] = 1
    else:
        arr[x] = 2

max_score = 0
for i in range(1, 10001 - k):
    tmp_score = 0

    for j in range(i, i + k + 1):
        tmp_score += arr[j]

    max_score = max(max_score, tmp_score) 

print(max_score)