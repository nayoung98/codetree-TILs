# n * n 격자 (0, 1: 벽)
# k개의 벽을 적절하게 없애기
# 시작점으로부터 상하좌우 인접한 곳으로만 계속 이동
# 출력: 도착점까지 도달하는 데 걸리는 시간의 최솟값 or -1
from collections import deque
import sys

# 입력
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split()) # 시작점
r2, c2 = map(int, input().split()) # 도착점
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# bfs 돌면서 시간 계산하기
q = deque()
time = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
tmp_grid = [[0] * n for _ in range(n)]

# 초기화
def initialize():
    global tmp_grid, time, visited

    time = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            tmp_grid[i][j] = grid[i][j]
    
    q.append((r1, c1))
    visited[r1][c1] = True
    
# 격자 내 검사
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 격자 내 & 방문 x & 벽 x
def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y] and \
            not tmp_grid[x][y] # 0
# bfs
def bfs():
    global visited, time
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                time[nx][ny] = time[x][y] + 1

# 벽 찾기
wall = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            wall.append((i, j))

# 벽 k개 고르기
selected_wall = []
min_time = sys.maxsize
flag = False

def simulate(curr_num, cnt):
    global min_time, flag, visited
    if curr_num == len(wall):
        if cnt == k:
            # 초기화
            initialize()

            # 벽 없애기
            for i, j in selected_wall:
                tmp_grid[i][j] = 0

            # bfs 돌면서 시간 계산
            bfs()

            if visited[r2][c2]:
                tmp_time = time[r2][c2]
                min_time = min(tmp_time, min_time)
                flag = True

        return

    selected_wall.append(wall[curr_num])
    simulate(curr_num + 1, cnt + 1)
    selected_wall.pop()

    simulate(curr_num + 1, cnt)

# 실행
simulate(0, 0)

# 출력
if flag:
    print(min_time)
else:
    print(-1)