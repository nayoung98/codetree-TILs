# n * n 정사각형 
# '왼쪽 -> 위 -> 오른쪽 -> 아래'로 회전하며 숫자 적기
n = int(input())
grid = [[0] * n for _ in range(n)]
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]

# 현재 위치, 방향
x, y, dir_num = n - 1, n - 1, 0
grid[x][y] = n * n

# 범위 내인지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 시뮬레이션
def simulate(x, y, dir_num):
    num = n * n - 1

    while True:
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        if in_range(nx, ny) and grid[nx][ny] == 0:
            x, y = x + dxs[dir_num], y + dys[dir_num]
            grid[x][y] = num
            num -= 1
        else:
            dir_num = (dir_num + 1) % 4

        if num == 0:
            break


# 실행 
simulate(x, y, dir_num)

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()