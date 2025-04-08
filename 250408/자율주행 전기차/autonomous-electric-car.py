from collections import deque
from traceback import print_tb

# 입력
n, m, c = map(int, input().split()) # 격자의 크기: n, 승객의 수: m, 초기 배터리 충전량: c
grid = [list(map(int, input().split())) for _ in range(n)] # 0: 도로, 1: 벽
x, y = map(int, input().split()) # 1-idx
info = [list(map(int, input().split())) for _ in range(m)] # 1-idx

q = deque()
visited = [[False] * n for _ in range(n)]
distance = [[0] * n for _  in range(n)]

# 택시, 승객들 0-idx로 바꿔두기
x, y = x - 1, y - 1
for i, (xs, ys, xe, ye) in enumerate(info):
    xs, ys, xe, ye = xs - 1, ys - 1, xe - 1, ye - 1
    info[i][:] = xs, ys, xe, ye

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):  # 격자 내, 방문 x, 벽 x
    return in_range(x, y) and \
        not visited[x][y] and \
        grid[x][y] == 0

def bfs(visited, distance):
    # global visited, distance
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

def bfs_target(visited, distance, tx, ty):
    # global visited, distance
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    while q:
        x, y = q.popleft()
        if tx == x and ty == y: # 승객의 목적지에 도착하면 더이상 계산 안함
            break
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

# # 1. 택시의 현재 위치로부터 승객들의 최단거리 bfs로 구하기 -> 우선 순위에 맞게 승객 탑승
# # 택시의 현재 위치 (0-idx로 바꿈)
# x, y = x - 1, y - 1
# q.append((x, y))
# visited[x][y] = True
#
# # 실행
# bfs()
#
# # 승객들의 최단 거리 구하기
# target = []
# for xs, ys, xe, ye in info:
#     xs, ys, xe, ye = xs - 1, ys - 1, xe - 1, ye - 1
#     target.append((distance[xs][ys], xs, ys, xe, ye))
# target.sort(key=lambda x: (x[0], x[1], x[2]))
#
# # 우선 순위에 맞게 승객 탑승 -> 배터리 계산 (이때 0 이하가 되면 -1 출력 및 종료)
# d, xs, ys, xe, ye = target[0]
# x, y = xs, ys # 택시의 위치 업뎃 (승객이 탑승하는 곳으로)
# c -= d # 배터리 계산
# # if c <= 0:
# #     break
#
# # 2. 목적지로 택시 이동 -> 배터리 계산 -> 배터리 충전
# # 목적지까지로 이동하는 최단 거리 계산을 위해 bfs 수행
# # 초기화
# visited = [[False] * n for _ in range(n)]
# distance = [[0] * n for _  in range(n)]
#
# # bfs 수행
# q.append((x, y))
# visited[x][y] = True
# bfs_target(xe, ye)
#
# # 목적지 도착
# x, y = xe, ye # 택시 위치 업뎃
# # 배터리 계산
# d = distance[x][y]
# c = c - d + d * 2
def init_bfs():
    global visited, distance
    # for i in range(n):
    #     for j in range(n):
    #         visited[i][j] = False
    #         distance[i][j] = 0
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _  in range(n)]

# 3. 1~2 반복
move = True
for _ in range(m):
    # 1. 택시의 현재 위치로부터 승객들의 최단거리 bfs로 구하기 -> 우선 순위에 맞게 승객 탑승
    # 초기 시작
    # print(x, y, c) # 처음 택시의 위치, 배터리

    q.append((x, y))
    visited[x][y] = True
    bfs(visited, distance)
    # print(distance)

    # 승객들의 최단 거리 구하기
    target = []
    for idx, (xs, ys, xe, ye) in enumerate(info):
        if xs == -1 and ys == -1: # 이미 탑승한 승객은 안태움
            continue
        if distance[xs][ys] != 0:
            target.append((distance[xs][ys], xs, ys, xe, ye, idx))

    if len(target) == 0: # 갈 수 있는 곳이 없음
        move = False
        break

    target.sort(key=lambda x: (x[0], x[1], x[2]))

    # 모든 승객들의 거리가 0이라면 막혀서 갈 수 없다는 것을 의미하므로
    # print(target)
    # 우선 순위에 맞게 승객 탑승 -> 배터리 계산 (이때 0 이하가 되면 -1 출력 및 종료)
    d, xs, ys, xe, ye, idx = target[0] # 승객이 있는 곳 까지의 거리, 출발지, 목적지, 손님 번호
    # print(d, xs, ys, xe, ye, idx)
    x, y = xs, ys # 택시의 위치 업뎃 (승객이 탑승하는 곳으로)
    # 탑승한 승객은 지우기
    info[idx][:2] = -1, -1
    c -= d # 배터리 계산
    # print(c)
    if c <= 0:
        move = False
        break

    # 2. 목적지로 택시 이동 -> 배터리 계산 -> 배터리 충전
    # 목적지까지로 이동하는 최단 거리 계산을 위해 bfs 수행
    # 초기화
    init_bfs()

    # bfs 수행
    q.append((x, y))
    visited[x][y] = True
    bfs(visited, distance)
    # print(distance)
    # 목적지 도착
    x, y = xe, ye # 택시 위치 업뎃

    d = distance[x][y]
    # 이동 중 배터리 계싼
    c -= d
    # print(c)
    if c < 0:
        move = False
        break
    # 배터리 충전
    c += d * 2
    # print(c)
    # 다 끝나면 visitied, distance 초기화
    init_bfs()
    # print(info)

# 출력
if move:
    print(c)
else:
    print(-1)