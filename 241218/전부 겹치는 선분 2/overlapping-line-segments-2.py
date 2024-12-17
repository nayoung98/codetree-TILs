# n개의 선분
# 하나를 제거하여 나머지 n - 1개의 선분이 전부 겹치는 지점이 있는지 확인

n = int(input())
info_list = [list(map(int, input().split())) for _ in range(n)]

chk = False
max_x1, max_x2 = 0, 100
for i in range(n):
    for j in range(n):
        # 하나 제거
        if i != j:
            x1, x2 = info_list[j]
            max_x1 = max(max_x1, x1)
            max_x2 = max(max_x2, x2)
    if max_x1 <= max_x2:
        chk = True

if chk:
    print('Yes')
else:
    print('No')