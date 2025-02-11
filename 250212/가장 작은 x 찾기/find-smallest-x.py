# x에 2를 곱하는 것을 n번 반복
# 2를 곱할 때 마다 현재 숫자의 범위에 대한 단서가 주어짐 [ai, bi]
# 이러한 조건을 만족하는 x중 최솟값 구하기
import sys

# 입력
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
min_x = sys.maxsize

for i in range(1, 5001):
    x = i
    for a, b in info:
        i *= 2
        if not (a <= i and i <= b):
            chk = False
            break
        else:
            chk = True

    if chk:
        min_x = min(min_x, x)

print(min_x)    
