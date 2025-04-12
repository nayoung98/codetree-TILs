from collections import deque

r, c, k = map(int, input().split())
golems = [list(map(int, input().split())) for _ in range(k)]

grid = [[0] * c for _ in range(r)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

for i, (ci, di) in enumerate(golems):
    ci -= 1 # 0-idx
    golems[i][0] = ci # 0-idx로 바꾸기

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def can_move(x, y):
    if not in_range(x, y):
        if x < r and 0 <= y < c:
            return True
    else:
        if grid[x][y] == 0:
            return True
    return False

# 골렘의 최종 이동 위치 확인
def get_dst(x, y, d):
    while True:
        # 남쪽 이동
        if can_move(x + 1, y - 1) and can_move(x + 2, y) and can_move(x + 1, y + 1):
            x += 1
        # 서쪽 회전, 이동
        elif can_move(x - 1, y - 1) and can_move(x, y - 2) and can_move(x + 1, y - 2) and can_move(x + 1, y - 1) and can_move(x + 2, y - 1):
            y -= 1
            d = (d - 1) % 4
        # 동쪽 회전, 이동
        elif can_move(x - 1, y + 1) and can_move(x, y + 2) and can_move(x + 1, y + 1) and can_move(x + 1, y + 2) and can_move(x + 2, y + 1):
            y += 1
            d = (d + 1) % 4
        else:
            break
    return x, y, d

def golem2grid(i, x, y, d):
    # 골렘 표시
    grid[x - 1][y], grid[x][y], grid[x + 1][y] = (i + 1), (i + 1), (i + 1)
    grid[x][y - 1], grid[x][y + 1] = (i + 1), (i + 1)

    # 출구 표시
    ex, ey = x + dxs[d], y + dys[d]
    grid[ex][ey] = -(i + 1)

visited = [[False] * c for _ in range(r)]
q = deque()

def can_go(x, y, golem): # 격자 내 & not 방문 & 골렘 안에서만 움직이기 & 같은 idx 내 or  탈출구라면 다른 숫자로만 이동
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 0 and \
            ((abs(grid[x][y]) == abs(golem)) or (golem < 0 and abs(grid[x][y]) != abs(golem)))

def bfs():
    global max_row
    max_row = 0
    while q:
        x, y = q.popleft()
        golem = grid[x][y]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, golem):
                q.append((nx, ny))
                visited[nx][ny] = True
                max_row = max(max_row, nx)

# 정령의 최종 위치 (가장 큰 행) 출력
def get_location():
    for i in range(r - 1, -1, -1):
        for j in range(c):
            if visited[i][j]:
                return i

# 실행
result = 0
for i, (ci, di) in enumerate(golems):
    # 1. 골렘의 최종 위치 구하기
    x, y, d = get_dst(0, ci, di)

    # 아무데도 못가면 숲 초기화함 (골렘 다 빠져나가고 다시 시작)
    if x == 0 and y == ci and d == di:
        grid = [[0] * c for _ in range(r)]
        continue

    # 2. 골렘 최남단에 도착 -> 정령의 이동
    golem2grid(i, x, y, d)
    q.append((x, y))
    visited[x][y] = True
    bfs()

    # 정령의 최종 위치 구하기
    result += (max_row + 1)

    # 초기화
    visited = [[False] * c for _ in range(r)]
print(result)