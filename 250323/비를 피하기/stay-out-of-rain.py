# n * n 격자 (0: 이동 o, 1: 벽 o & 이동 x, 2: 사람 o, 3: 비를 피할 수 있는 곳)
# 사람 H명이 겹치치 않게 서있음 (상하좌우 인접한 곳 이동, 한 칸 움직이는 데 1초 소요)
# 비를 피할 수 있는 위치 m개 주어짐
# 출력: 사람이 있던 칸 = 각 사람마다 비를 피할 수 있는 공간까지 가는데 걸리는 최소시간 or -1, 사람이 없던 칸 = 0
from collections import deque

# 입력
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
time = [[-1] * n for _ in range(n)]
q = deque()

# 비를 피할 수 있는 곳에서 bfs
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            q.append((i, j))
            visited[i][j] = True
            time[i][j] = 0

# 격자 내 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 격자 내 & 방문 x & 벽 x
def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y] and \
            grid[x][y] != 1 and \
            time[x][y] == -1 # 최단 시간만 기록

# bfs 돌면서 최단 시간 기록
def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                
                visited[nx][ny] = True
                q.append((nx, ny))
                time[nx][ny] = time[x][y] + 1
bfs()
for i in range(n):
    for j in range(n):
        # 사람 있는 곳
        if grid[i][j] == 2:
            print(time[i][j], end=' ')
        else:
            print(0, end=' ')
    print()