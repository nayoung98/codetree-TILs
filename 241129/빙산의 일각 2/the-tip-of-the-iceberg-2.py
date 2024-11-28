# 해수면의 높이에 따라 물에 잠기는 빙산
# 빙산의 개수 : N, 높이 : H(i)
# 빙산들이 물에 잠기지 않은 채로 붙어있는 경우 = 한 덩어리
# 해수면의 높이를 적절하게 설정했을 때 가능한 빙산 덩어리의 최대 개수

n = int(input())
heights = list(int(input()) for _ in range(n))

max_cnt = 0
for i in range(1001): # 해수면의 높이
    cnt = 0
    chk = [0] * n

    for j in range(n):
        heights[j] -= i 

    for j in range(n):
        if heights[j] > 0:
            chk[j] = 1

    for j in range(1, n):
        if chk[j - 1] != chk[j]:
            cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
