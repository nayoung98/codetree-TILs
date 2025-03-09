# n * n 격자
# k개의 시작점으로부터 상하좌우 인접한 곳 이동(0: 이동 o, 1: 이동 x)
# 출력: 도달 가능한 칸의 수

# 입력 
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 각 시작점의 위치 (r, c)
info = [tuple(map(int, input().split())) for _ in range(k)]

# 격자 내부
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

# 방문 가능 여부
def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y] and \
            grid[x][y] == 0

# 방문 체크, 큐에 넣기
def push(x, y):
    visited[x][y] = True
    q.append((x, y))

# 이동
def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny)

# 실행
from collections import deque
q = deque()

for r, c in info:
    r -= 1
    c -= 1

    push(r, c)
    bfs()

# 출력
result = 0 
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            result += 1
print(result)