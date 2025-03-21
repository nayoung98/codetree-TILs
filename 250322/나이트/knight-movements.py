# n * n 격자
# 노란색 위치를 기준으로 검은색 8곳으로 움직임
# 출력: 나이트가 시작점에서 도착점까지 가는 데 걸리는 최소 이동 횟수, 불가능하면 -1
from collections import deque

# 입력
n = int(input())
r1, c1, r2, c2 = map(int, input().split()) # 시작, 도착
r1 -= 1
c1 -= 1 
r2 -= 1
c2 -= 1

grid = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y]

def bfs():
    dxs, dys = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                grid[nx][ny] = grid[x][y] + 1

# 실행
q.append((r1, c1))
visited[r1][c1] = True
bfs()

# 출력
if visited[r2][c2]:
    print(grid[r2][c2])
else:
    print(-1)