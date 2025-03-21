# n * m 격자 (0: 물, 1: 빙하)
# 빙하는 1초에 한 번씩 물에 닿아있는 부분들(상하좌우 인접)이 동시에 녹음
## 빙하로 둘러싸인 물은 붙어있는 빙하를 녹이지 못함
# 출력: 빙하가 전부 녹는데 걸리는 시간, 마지막으로 녹은 빙하의 크기
from collections import deque

# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ice_list = [(0, 0)]
q = deque()
t = 0

# 격자 내 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 격자 내 & 방문 x
def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y]

# bfs 돌면서 빙하인지 확인
def bfs():
    global visited, ice_list, t
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]

    # 설계
    r, c = ice_list[0]
    q.append((r, c))
    visited[r][c] = True

    ice_list = []
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                if not grid[nx][ny]: # 빙하 x
                    q.append((nx, ny))
                    visited[nx][ny] = True
                else: # 빙하 o
                    ice_list.append((nx, ny))

    # 탐색 완료               
    t += 1

# 빙하를 물(0)로 변경
def remove_ice():
    global grid

    for r, c in ice_list:
        grid[r][c] = 0

# 반복 종료 체크
def is_end():
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                return False
    return True

# # 설계
# q.append((0, 0))
# visited[0][0] = True

# 실행 
# for _ in range(2):
while True:

    bfs()
    ice_list = sorted(list(set(ice_list)))
    remove_ice()

    # print(ice_list)
    # print(grid)
    # print(is_end())
    if is_end():
        print(t, len(ice_list))

        # 마지막 개수 
        # print(ice_list)
        # print()
        
        break 