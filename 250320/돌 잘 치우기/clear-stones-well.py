# n * n 격자 (0, 1 = 돌)
# 주어진 돌 중 m개의 돌만 적절히 치우고, k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동
# 출력: 도달 가능한 최대 칸의 수
from collections import deque

# 입력
n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starts_info = [tuple(map(int, input().split())) for _ in range(k)]
q = deque()
visited = [[False] * n for _ in range(n)]

# 격자 내
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 격자 내 & 방문 x & 돌 x
def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y] and \
            not tmp_grid[x][y]

def bfs():
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

def initialize_grid():
    global visited, tmp_grid

    tmp_grid = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            tmp_grid[i][j] = grid[i][j]

def move_stones(selected_stones):
    global visited, tmp_grid
    initialize_grid()

    # 선택한 돌 바꾸기
    for i, j in selected_stones:
        tmp_grid[i][j] = 0

    # 시작점에 따른 bfs
    for r, c in starts_info:
        r -= 1
        c -= 1
        q.append((r, c))
        visited[r][c] = True
        bfs()

    # 도달 가능 칸 수 계산
    tmp_cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                tmp_cnt += 1

    # 초기화
    initialize_grid()

    return tmp_cnt
   
max_cnt = 0
selected_stones = []
def simulate(curr_num, cnt):
    global max_cnt

    # k개 돌 중 m개 선택하기
    # 종료 조건
    if curr_num == k: # 총 돌의 개수
        if cnt == m: # 선택된 돌의 개수
            # 선택된 돌 바꾸고 칸 수 확인
            max_cnt = max(max_cnt, move_stones(selected_stones))
        return

    # 재귀 호출
    selected_stones.append(stones[curr_num])
    simulate(curr_num + 1, cnt + 1)
    selected_stones.pop()
    simulate(curr_num + 1, cnt)

# 설계
# 돌이 있는 위치 저장
stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stones.append((i, j))

# 실행
simulate(0, 0)

# 출력
print(max_cnt)