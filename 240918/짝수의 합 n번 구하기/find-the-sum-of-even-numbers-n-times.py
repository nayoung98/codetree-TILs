import sys

input = sys.stdin.readline
n = int(input())
result = 0

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if i % 2 == 0:
            result += i
    print(result)
    result = 0