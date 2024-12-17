# n개의 선분
# 하나를 제거하여 나머지 n - 1개의 선분이 전부 겹치는 지점이 있는지 확인

n = int(input())
info_list = [list(map(int, input().split())) for _ in range(n)]

chk = False
for i in range(n):
    segments = [0] * 101
    for j in range(n):
        # 하나 제거
        if i != j:
            x1, x2 = info_list[j]
            for k in range(x1, x2 + 1):
                segments[k] += 1
    
    for seg in segments:
        if seg == (n - 1):
            chk = True
            
if chk:
    print('Yes')
else:
    print('No')
