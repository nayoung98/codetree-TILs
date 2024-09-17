import sys

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
chk = [[0] * n for _ in range(n)]

for row in range(n):
    for col in range(1):
        row_idx = grid[row][col] - 1
        col_idx = grid[row][col+1] - 1
        chk[row_idx][col_idx] = (row_idx + 1) * (col_idx + 1)

for row in range(n):
    for col in range(n):
        print(chk[row][col], end=' ')
    print()