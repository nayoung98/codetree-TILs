import sys

input = sys.stdin.readline
n = int(input())
tmp = n

for i in range(n):
    for j in range(tmp):
        if (j+1) == tmp:
            print(f'{i+1} * {j+1} = {(i+1)*(j+1)}', end='')
        else:
            print(f'{i+1} * {j+1} = {(i+1)*(j+1)}', end=' / ')
    tmp -= 1
    print()