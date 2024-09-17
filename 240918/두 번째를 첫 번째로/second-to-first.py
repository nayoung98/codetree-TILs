import sys

input = sys.stdin.readline
a = input().rstrip()
b = a[1] # a
c = a[0] # b

a = list(a)

for i in range(len(a)):
    if a[i] == b:
        a[i] = c

for i in range(len(a)):
    print(a[i], end='')