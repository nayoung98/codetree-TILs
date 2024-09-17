import sys

input = sys.stdin.readline
n = int(input())

result = 0
for _ in range(n):
    result += int(input())

result = str(result) 
print(result[1:] + result[0])