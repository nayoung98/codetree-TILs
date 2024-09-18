import sys

input = sys.stdin.readline
n = int(input())
left_cnt = 1
right_cnt = 1

for i in range(n):
    if i == 0 or i == (n-1):
        for j in range(n):
            print('*', end=' ')
    else:
        for j in range(left_cnt):
            print('*', end=' ')
        for k in range(n - left_cnt - right_cnt):
            print(' ', end=' ')
        for l in range(right_cnt):
            print('*', end=' ')   
        left_cnt += 1
    print()