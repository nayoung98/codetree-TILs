# n * m 크기의 격자 
# 서로 겹치지 않는 두 직사각형
# 두 직사각형 안에 적힌 숫자들의 총 합이 최대가 되도록 함
import sys

# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
INT_MIN = - sys.maxsize

def rect_sum(x1, y1, x2, y2):
    sum_of_nums = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum_of_nums += grid[i][j]
    return sum_of_nums

def clear_grid():
    for i in range(n):
        for j in range(m):
            chk[i][j] = 0

def check_grid():
    for i in range(n):
        for j in range(m):
            if chk[i][j] >= 2:
                return True
    return False

def draw(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            chk[i][j] += 1

def is_overlapped(x1, y1, x2, y2, i, j, k, l):
    clear_grid()
    draw(x1, y1, x2, y2)
    draw(i, j, k, l)
    return check_grid()

def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not is_overlapped(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, rect_sum(x1, y1, x2, y2) + rect_sum(i, j, k, l))
    return max_sum

max_sum = INT_MIN
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                max_sum = max(max_sum, find_max_sum_with_rect(i, j, k, l))
# print(max_sum)