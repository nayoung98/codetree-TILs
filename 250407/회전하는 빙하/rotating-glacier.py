# 입력
from collections import deque
n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**n)] # 건드리면 안됨, 초기 상태의 격자
levels = list(map(int, input().split()))

q = deque()
visited = [[False] * (2**n) for _ in range(2**n)]

def divide_grid(rs, re, cs, ce, grid):
    # 4등분
    new_grid = []
    for i in range(rs, re):
        for j in range(cs, ce):
            new_grid.append(grid[i][j])
    return new_grid

def rotate_grid(rs, re, cs, ce, grid, new_grid):
    cnt = 0
    for i in range(rs, re):
        for j in range(cs, ce):
            new_grid[i][j] = grid[cnt]
            cnt += 1
    return new_grid

def rotate_minigrid(length, rs, re, cs, ce):
    tmp_grid = []
    # 격자 1조각 선택
    for i in range(rs, re):
        tmp_grid.append(grid[i][cs:ce])

    # 4등분
    tmp_grid1 = divide_grid(0, int(length/2), 0, int(length/2), tmp_grid)
    tmp_grid2 = divide_grid(0, int(length / 2), int(length / 2), length, tmp_grid)
    tmp_grid3 = divide_grid(int(length / 2), length, int(length / 2), length, tmp_grid)
    tmp_grid4 = divide_grid(int(length / 2), length, 0, int(length / 2), tmp_grid)

    # 회전
    new_grid = [[0] * length for _ in range(length)]
    new_grid = rotate_grid(0, int(length / 2), int(length / 2), length, tmp_grid1, new_grid)
    new_grid = rotate_grid(int(length / 2), length, int(length / 2), length, tmp_grid2, new_grid)
    new_grid = rotate_grid(int(length / 2), length, 0, int(length / 2), tmp_grid3, new_grid)
    new_grid = rotate_grid(0, int(length / 2), 0, int(length / 2), tmp_grid4, new_grid)

    return new_grid

def in_range(x, y):
    return 0 <= x < 2 ** n and 0 <= y < 2 ** n

def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y] and \
            grid[x][y] != 0

def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    positions = []
    while q:
        x, y = q.popleft()
        positions.append((x, y))
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                positions.append((nx, ny))
    positions = list(set(positions))
    return positions

def check_ice(x, y):
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and rotated_grid[nx][ny] != 0:
            cnt += 1
    return cnt

# 실행
rotated_grid = [[0] * (2**n) for _ in range(2**n)]
for level in levels: 
    # 1. 회전 레벨에 맞게 1번 회전시키기
    if level == 0: # 레벨 0이면 변화 없음
        rotated_grid = grid
    else: 
        total, length = 2**n, 2**level
        num = int(total/length)
        
        for l in range(num):
            rs, re = length * l, length * (l + 1)
            for k in range(num):
                cs, ce = length * k, length * (k + 1)
                # 선택한 각각의 격자를 4등분해서 회전하기
                new_grid = rotate_minigrid(length, rs, re, cs, ce)      

                # 원래 격자에 집어넣기
                row = 0
                for i in range(rs, re):
                    col = 0
                    for j in range(cs, ce):
                        rotated_grid[i][j] = new_grid[row][col]
                        col += 1
                    row += 1

    tmp_grid = [[0] * (2 ** n) for _ in range(2 ** n)]
    # 격자 복사
    for i in range(2 ** n):
        for j in range(2 ** n):
            tmp_grid[i][j] = rotated_grid[i][j]

    # 2. 1회 회전 후 얼음 녹이기 (회전된 격자 내에서 4방향으로 얼음이 있는지 확인하기, 3개 이상 있으면 그대로, 아니면 녹이기)
    for i in range(2**n):
        for j in range(2**n):
            if rotated_grid[i][j] == 0:
                continue
            cnt = check_ice(i, j)
            if cnt < 3:
                tmp_grid[i][j] -= 1

    # 원래 배열 업뎃
    for i in range(2**n):
        for j in range(2**n):
            grid[i][j] = tmp_grid[i][j]

# 출력 (bfs로 얼음 있는 곳 연결해서 cnt, 얼음 있는 곳의 rotated_grid 값 더하기)
result, max_ice = 0, 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if grid[i][j] != 0:
            result += grid[i][j]
            q.append((i, j))
            visited[i][j] = True
            positions = bfs()
            max_ice = max(max_ice, len(positions))
print(result)
if max_ice == 0:
    print(0)
else:
    print(max_ice)

