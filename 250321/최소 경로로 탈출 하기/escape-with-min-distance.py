# n * m 격자
# 좌상단 -> 우하단 이동 (상하좌우 인접한 칸, 뱀이 있는 칸(0)으로는 이동 불가능)
# 출력: 탈출 가능한 경로의 최단 거리, 불가능한 경우 -1 출력
from collections import deque

# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y] and \
            grid[x][y]

def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                grid[nx][ny] = grid[x][y] + 1

# 수행
q.append((0, 0))
visited[0][0] = True
bfs()

# 출력
if visited[n - 1][m - 1]:
    print(grid[n - 1][m - 1] - 1)
else:
    print(-1)