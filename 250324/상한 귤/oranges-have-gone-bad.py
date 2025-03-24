# n * n 격자 (0, 1: 귤, 2: 상한 귤)
# k개의 상한귤 -> 인접한 곳에 있는 귤이 동시에 전부 상함
# 출력: 각 귤마다 최초로 상하게 되는 시간
from collections import deque

# 입력
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
q = deque()
visited = [[False] * n for _ in range(n)]
time = [[-1] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y] and \
            grid[x][y] == 1 and \
            time[x][y] == -1

def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                time[nx][ny] = time[x][y] + 1

# 상한 귤로부터 동시 bfs
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            q.append((i, j))
            visited[i][j] = True
            time[i][j] = 0

# 실행
bfs()

# 출력
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            print(-2, end=' ')
        else:
            print(time[i][j], end=' ')
    print()