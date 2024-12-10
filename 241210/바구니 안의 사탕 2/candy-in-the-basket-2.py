# 1차원 직선
# 총 N개의 바구니
# 중심점 c, [c-K, c+K] 구간에 있는 사탕의 수가 최대가 되도록
n, k = map(int, input().split())

# 사탕의 개수, 바구니의 위치
info_list = [list(map(int, input().split())) for _ in range(n)]
candy_list = [0] * 101 # 0-idx

# 같은 위치에 여러 바구니 가능
for num, idx in info_list:
    candy_list[idx] += num

max_candy = 0
for c in range(200):
    candy_num = 0
    for i in range(c-k , c+k+1):
        if i >= 0 and i <= 100:
            candy_num += candy_list[i]
        else:
            continue    
    max_candy = max(max_candy, candy_num)

print(max_candy)