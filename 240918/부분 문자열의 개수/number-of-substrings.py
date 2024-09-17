import sys

input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()

cnt = 0

# print(a[0])
# print(a[1])
# print(a[0:2])

for i in range(0, len(a)-1):
    if a[i:i+2] == b:
        cnt += 1
print(cnt)