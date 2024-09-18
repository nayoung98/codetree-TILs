import sys

input = sys.stdin.readline
n = int(input())

tmp = 65
cnt = 0
# A = 65, Z = 90

for i in range(n):
    for j in range(cnt):
        print(' ', end =' ')
    for k in range(n-cnt):
        print(chr(tmp), end= ' ')
        tmp += 1
        if tmp > 90:
            tmp = 65
    cnt += 1
    print()