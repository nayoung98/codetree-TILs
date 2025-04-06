# 입력
from collections import deque
from wsgiref.util import request_uri

R, C, K = map(int, input().split()) # 행, 열, 정령의 수
golems = [list(map(int, input().split())) for _ in range(K)] # 골렘이 출발하는 열 (ci), 골렘의 출구 방향 정보 (di)

grid = [[0] * C for _ in range(R)]
q = deque()
visited = [[False] * C for _ in range(R)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < R and 0 <= y < C

def can_move(x, y):
    if not in_range(x, y):
        if x < R and 0 <= y < C:
            return True # 이동 가능
    else:
        if grid[x][y] == 0:
            return True
    return False

def move_golem(x, y, d):
    # 현재 정령의 좌표: x, y
    while True:
        # 남쪽으로 이동 가능한지 확인 (격자 내 & 다른 골렘 x)
        if can_move(x + 2, y) and can_move(x + 1, y - 1) and can_move(x + 1, y + 1):
            x += 1  # 남쪽으로 이동
        elif can_move(x - 1, y - 1) and can_move(x, y - 2) and can_move(x + 1, y - 1) and can_move(x + 1, y - 2) and can_move(x + 2, y - 1):
            x += 1
            y -= 1 # 서쪽으로 이동 및 하강
            d = (d - 1) % 4
        elif can_move(x - 1, y + 1) and can_move(x, y + 2) and can_move(x + 1, y + 1) and can_move(x + 1, y + 2) and can_move(x + 2, y + 1):
            x += 1
            y += 1 # 동쪽으로 이동 및 하강
            d = (d + 1) % 4
        else:
            return x, y, d # 정령의 위치, 출구 방향

def update_grid(idx, x, y, d):
    global grid

    # 골렘 이동
    ## 가로 방향
    for j in range(y - 1, y + 2):
        grid[x][j] = idx + 1
    ## 세로 방향
    for i in range(x - 1, x + 2):
        grid[i][y] = idx + 1

    # 출구 표시
    ex, ey = x + dxs[d], y + dys[d]
    grid[ex][ey] = -(idx + 1)

def can_go(x, y):
    return 0 <= x < R and 0 <= y < C and \
            not visited[x][y] and \
            grid[x][y] != 0

def bfs():
    global visited
    visited = [[False] * C for _ in range(R)]
    positions = []

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not can_go(nx, ny):
                continue
            # 골렘 내에서만 이동 or 탈출구를 통해 다른 골렘으로 이동
            if abs(grid[nx][ny]) == abs(grid[x][y]) or (grid[x][y] < 0 and abs(grid[nx][ny]) != abs(grid[x][y])):
                q.append((nx, ny))
                visited[nx][ny] = True
                positions.append((nx, ny))
    return positions

def isnot_golem(x, y):
    if grid[x][y] == 0 and \
        in_range(x, y) and in_range(x, y - 1) and in_range(x, y + 1) and in_range(x - 1, y) and in_range(x + 1, y):
        return True
    return False

# 실행
result = 0
for idx, (ci, di) in enumerate(golems):
    ci -= 1  # 0-idx

    # 골렘의 이동
    x, y, d = move_golem(-2, ci, di) # 정령의 좌표, 출구 방향

    # 격자에 골렘 표시하기
    if isnot_golem(x, y):
        update_grid(idx, x, y, d)
        # 정령의 이동
        q.append((x, y))
        visited[x][y] = True
        positions = bfs()
        positions.sort(key=lambda x: -x[0])
        mx = positions[0][0] + 1

    else: # 불가능 하면 (이미 해당 위치에 골렘이 있음 or 격자 밖) 숲 초기화
        grid = [[0] * C for _ in range(R)]
        mx = 0
    result += mx
print(result)