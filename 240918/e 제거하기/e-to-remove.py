import sys

input = sys.stdin.readline
a = input().rstrip()
a = list(a)

for idx, text in enumerate(a):
    if text == 'e':
        a.remove(a[idx])
        break

for i in range(len(a)):
    print(a[i], end='')