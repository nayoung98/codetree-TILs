import sys

n = int(input())
tmp = n

for _ in range(n):
    for _ in range(n):
        print(tmp, end=' ')
        tmp -= 1
    print()
    tmp = n