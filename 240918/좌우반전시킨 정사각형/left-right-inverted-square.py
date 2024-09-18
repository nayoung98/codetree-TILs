import sys

input = sys.stdin.readline
n = int(input())
tmp = n

for i in range(n):
    for j in range(n):
        print((i+1) * tmp, end=' ')
        tmp -= 1
    tmp = n
    print()