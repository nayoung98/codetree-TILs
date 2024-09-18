import sys

input = sys.stdin.readline
n = int(input())
cnt = 0

for i in range(n):
    for j in range(n-cnt, n+1):
        print(j, end=' ')
    cnt += 1
    print()