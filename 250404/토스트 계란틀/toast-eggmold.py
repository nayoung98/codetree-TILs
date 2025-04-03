from collections import deque

# 입력
n, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()

tmp_grid = [[0] * n for _ in range(n)]
for i in range(n):
        for j in range(n):
            tmp_grid[i][j] = grid[i][j]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, nx, ny):
    return in_range(nx, ny) and \
            not visited[nx][ny] and \
            L <= abs(grid[nx][ny] - grid[x][y]) <= R

def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    result = []
    while q:
        x, y = q.popleft()
        result.append((x, y))
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(x, y, nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                result.append((nx, ny))
    return list(set(result))

def update_grid():
    global grid    
    for i in range(n):
        for j in range(n):
            grid[i][j] = tmp_grid[i][j]

# grid 돌면서 상하좌우 인접한 곳의 차 계산
cnt = 0
for _ in range(2000):
    flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            q.append((i, j))
            visited[i][j] = True
            eggs = bfs()
            if len(eggs) >= 2:
                flag = True
                egg_sum = 0
                for x, y in eggs:
                    egg_sum += grid[x][y]
                for x, y in eggs:
                    tmp_grid[x][y] = int(egg_sum / len(eggs))
    update_grid()
    if flag:
        cnt += 1
    else:
        break
print(cnt)