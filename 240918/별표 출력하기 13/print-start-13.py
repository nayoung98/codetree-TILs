import sys

input = sys.stdin.readline
n = int(input())
cnt = n
tnc = 1

for i in range(2 * n):
    if i % 2 == 0:
        for j in range(cnt):
            print('*', end = ' ')
        cnt -= 1
    else:
        for j in range(tnc):
            print('*', end = ' ')
        tnc += 1
    print()