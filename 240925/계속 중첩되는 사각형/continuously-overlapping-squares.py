import sys

input = sys.stdin.readline
n = int(input())

rec_list = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

OFFSET = 100
MAX_R = 200

chk_list = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for idx, (x1, y1, x2, y2) in enumerate(rec_list):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    if idx % 2 == 0: # red = 1
        for row in range(x1, x2):
            for col in range(y1, y2):
                chk_list[row][col] = 1
    else: # blue
        for row in range(x1, x2):
            for col in range(y1, y2):
                chk_list[row][col] = 2

area = 0
for row in range(0, MAX_R + 1):
    for col in range(0, MAX_R + 1):
        if chk_list[row][col] == 2:
            area +=1

print(area)