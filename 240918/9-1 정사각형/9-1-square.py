import sys

input = sys.stdin.readline
n = int(input())
tmp = 9

for i in range(n):
    for j in range(n):
        print(tmp, end='')
        tmp -= 1
        if tmp == 0:
            tmp = 9
    print()