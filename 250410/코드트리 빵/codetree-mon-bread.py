from collections import deque

# 입력
n, m = map(int, input().split()) # 격자의 크기, 사람 수
grid = [list(map(int, input().split())) for _ in range(n)] # 0: 빈 곳 , 1: 베캠
targets = [list(map(int, input().split())) for _ in range(m)] # 가고자 하는 m개의 편의점
tmp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        tmp[i][j] = grid[i][j]

people = [(-1, -1) for _ in range(m)] # 사람이 있는 곳 위치
move = [False] * m

q = deque()
distance = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
route = [[None] * n for _ in range(n)]
t = 0

# 0-idx로 바꾸기
for idx, (x, y) in enumerate(targets):
    x, y = x - 1, y - 1
    targets[idx][:] = x, y


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, idx): # 격자 내 & 방문 x & 갈 수 있는 곳
    return 0 <= x < n and 0 <= y < n and \
            not visited[x][y] and \
            (abs(grid[x][y]) == (idx + 1) or grid[x][y] >= 0) # 본인은 갈 수 있음 or 비어있는 곳

def bfs(idx):
    global route, visited, distance
    # q = deque()
    # q.append((sx, sy))
    # distance = [[0] * n for _ in range(n)]
    # visited = [[False] * n for _ in range(n)]
    # route = [[None] * n for _ in range(n)]

    # visited[sx][sy] = True

    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0] # 우선 순위
    while q:
        x, y = q. popleft()
        for i in range(4):
            nx, ny = x + dxs[i], y + dys[i]
            if can_go(nx, ny, idx):
                q.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                route[nx][ny] = (x, y)

def init():
    global route, visited, distance
    distance = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    route = [[None] * n for _ in range(n)]

# 도착지에서부터 bfs 돌면서 경로 역추적
def move_store(idx, x, y):
    global route, visited, distance

    # # 초기화
    init()

    # bfs 돌면서 최단 거리 계산
    q.append((x, y))
    visited[x][y] = True
    bfs(idx)
    # bfs(x, y, idx)

    px, py = people[idx]  # t번 사람의 현재 위치
    # print(px, py)
    # print(route[px][py])
    if route[px][py] != None:
        # 해당 경로로 한칸 이동
        nx, ny = route[px][py]
        # print(nx, ny)
        # 사람의 위치 업뎃
        people[idx] = nx, ny

def move_basecamp(t):
    basecamp = []
    idx = t
    tx, ty = targets[idx]  # 자신이 가고 싶은 편의점 (0-idx)

    # # 초기화
    init()
    # 편의점 기준 bfs
    q.append((tx, ty))
    visited[tx][ty] = True
    # bfs(tx, ty, idx)
    bfs(idx)
    # print(idx)
    # print(distance)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1: # 베캠이라면
                # # 초기화
                # init()
                # # 자신이 가고 싶은 편의점과 가장 가까운 베캠 구하기
                # q.append((i, j))
                # visited[i][j] = True
                # bfs(idx)
                basecamp.append((distance[i][j], i, j))
    # print(basecamp)
    basecamp.sort(key=lambda x: (x[0], x[1], x[2]))

    # 해당 베이스캠프로 옮기기
    _, nx, ny = basecamp[0]
    tmp[nx][ny] = -(idx + 1)  # 사람이 들어갔으니까 더이상 여기는 못가
    people[idx] = nx, ny  # 그 사람의 현재 위치 업뎃

cnt = 0
def simulate():
    global t, move, cnt
    # 1. 격자 안에 있는 사람들이 가고 싶은 편의점에 대한 최단 거리 구하기 -> 우선 순위에 따라 한 칸 이동
    # 우선 순위: 최단 거리 -> 위 -> 좌 -> 우 -> 아래
    for idx, (x, y) in enumerate(targets):
        if people[idx] == (-1, -1):  # 사람이 격자 위에 없으면 안함
            continue
        move_store(idx, x, y)
    # print(people)

    # 사람들 전부 이동했으면 편의점 도착 여부 확인
    for idx in range(m):
        tx, ty = targets[idx]  # t번 사람의 편의점의 위치
        if not move[idx] and people[idx] == (tx, ty):
            tmp[tx][ty] = -(idx + 1)  # 도착했다면 거기로 못감
            move[idx] = True
            cnt += 1

    # 다 이동한 후에 못가게 됨
    for i in range(n):
        for j in range(n):
            grid[i][j] = tmp[i][j]

    # print(grid)

    # t번 사람의 편의점에 대해 가장 가까운 베캠 구하기: bfs로 최단 거리 -> 작은 행 -> 작은 열
    if t < m:
        # idx = t
        move_basecamp(t)

    # print(people)
    # 다 이동한 후에 못가게 됨
    for i in range(n):
        for j in range(n):
            grid[i][j] = tmp[i][j]
    # print(grid)
    t += 1

# #
while True:
# for _ in range(9):
    # cnt = simulate()
    # print(f'Turn: {_}')
    simulate()

    # print(move)
    if cnt == m:
        break
print(t)