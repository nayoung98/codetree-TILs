import sys

input = sys.stdin.readline
a, b = map(int, input().split())
origin_n = input().rstrip()

# a진수 -> 10진수
num = 0
for i in range(len(origin_n)):
   num += int(origin_n[i]) * (a ** (len(origin_n) -1 - i))

# 10진수 -> b진수
ans_list = []
if num == 0:
    print(0)
else:
    while num > 0:
        ans_list.append(num % b)
        num //= b

ans_list = reversed(ans_list)
for num in ans_list:
    print(num, end='')