import sys

input = sys.stdin.readline
a, b = map(int, input().split())
origin_n = input().rstrip()

# a진수 -> 10진수
num = 0
for i in range(len(origin_n)-1, -1, -1):
   num += a ** i

# 10진수 -> b진수
ans_list = []
while True:
    ans_list.append(num % b)
    num //= b

    if num == 1:
        ans_list.append(num)
        break

for num in ans_list:
    print(num, end='')