# n * n 격자 (1 ~ 100)
# 조건을 만족하는 숫자의 위치를 찾아 상하좌우로 이동 -> k번 반복
## k번 반복하지 못했지만, 더이상 새로 이동할 위치가 없으면 이동 종료 -> bfs 
## 조건: 1. 시작 위치에서 출발해 인접한 칸들(격자 내) 중 적혀있는 숫자가 작은 곳
### 1-1. 시작 위치의 상하좌우가 시작 숫자 보다 크면 이동 불가
## 2. 1번 조건을 만족하며 도달할 수 있는 칸들에 적혀있는 숫자 중 최댓값
## 3. 2번 조건을 만족하는 숫자가 여러개인 경우, 행 번호가 가장 작은 곳으로 이동
## 4. 2번 조건을 만족하고, 행 번호도 같은 숫자가 여러개인 경우, 열 번호가 가장 작은 곳으로 이동
# 출력: k번 반복한 후의 위치

from collections import deque

# 입력
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)] 
q = deque()
visited = [[False] * n for _ in range(n)]
move_list = []

# 초기 시작 위치
r, c = map(int, input().split()) 
r -= 1
c -= 1
num = grid[r][c]
visited[r][c] = True
q.append((r, c))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, num):
    return in_range(x, y) and \
            not visited[x][y] and \
            num > grid[x][y]

def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    global move_list, num

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, num):
                move_list.append((nx, ny, grid[nx][ny]))
                visited[nx][ny] = True
                q.append((nx, ny))
# 실행
for _ in range(k):
    bfs()
    if len(move_list) != 0:
        # 조건에 따라 정렬 (큰 숫자, 작은 행, 작은 열)
        move_list.sort(key=lambda x:(-x[2], x[0], x[1]))
        r, c, num = move_list[0][:]

        # 초기화 
        move_list = []
        visited = [[False] * n for _ in range(n)]
        visited[r][c] = True
        q.append((r, c))
    # 이동 불가능하면 멈춤
    else:
        break

# 출력 (1-idx)
print(r + 1, c + 1)