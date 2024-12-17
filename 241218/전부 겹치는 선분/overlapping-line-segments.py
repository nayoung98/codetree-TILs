# n개의 선분
# 모든 선분이 겹치는 지점이 있는지를 판단

n = int(input())
info_list = [list(map(int, input().split())) for _ in range(n)]

segments = [0] * 101 # 1-idx
for (x1, x2) in info_list:
    for i in range(x1, x2 + 1):
        segments[i] += 1

chk = False
for seg in segments:
    if seg == n:
        chk = True

if chk:
    print('Yes')
else:
    print('No')