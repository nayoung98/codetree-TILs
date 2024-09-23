import sys

input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))

median_list = []
for idx, num in enumerate(num_list):
    median_list.append(num)
    median_list = sorted(median_list)
    if (idx + 1) % 2 != 0:
        print(median_list[int(len(median_list)/2)], end = ' ')