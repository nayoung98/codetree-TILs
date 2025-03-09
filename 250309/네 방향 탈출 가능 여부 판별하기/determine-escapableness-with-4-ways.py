# n * m 이차원 격자
# 좌측 상단 출발 -> 우측 하단 
# 상하좌우 인접한 칸으로만 이동, 뱀이 있으면(0) 이동 불가능
# 출력: 뱀에게 물리지 않고 탈출 가능한 경로가 있는지 여부를 판별
from collections import deque

# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()

# 방문 처리, queue에 append (방문 예정)
def push(x, y):
    visited[x][y] = True
    q.append((x, y))

# 격자 내인지
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 이동 여부 확인
def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y] and \
            grid[x][y] == 1

# 이동: queue가 비워질 때 까지 상하좌우 이동 반복
def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny)

    # queue가 비워졌을 때, 마지막 칸에 있다면 탈출 가능
    if visited[n - 1][m - 1] == True:
        print(1)
    else: 
        print(0)

# 실행
visited[0][0] = True
q.append((0, 0))
bfs()