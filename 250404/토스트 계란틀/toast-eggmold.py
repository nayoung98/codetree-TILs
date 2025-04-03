# n * n 격자, 1 * 1 계란틀
# 각각의 계란틀에 담긴 계란의 양이 주어짐, 계란틀은 정사각형 형태, 계란틀을 이루는 4개의 선은 분리 가능
# 규칙 4
## 1. 하나의 선을 맞대고 있는 두 계란틀의 계란의 양의 차이가 L이상 R이하라면 계란틀의 해당 선을 분리함
## 2. 모든 계란 틀에 대하 검사를 실시하고 위의 규칙에 해당하는 모든 계란틀의 선을 분리
## 3. 선의 분리를 통해 합쳐진 계란틀의 계란은 하나로 합치고 이후에 다시 분리
## 4. 합쳤다가 다시 분리한 이후의 각 계란의 양 = 합쳐진 계란의 총 합/ 합쳐진 계란틀의 총 개수 (소수점 버림)
# 출력: 계란의 이동이 일어나는 횟수
from collections import deque
# 입력
n, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, nx, ny):
    return in_range(nx, ny) and \
            not visited[nx][ny] and \
            L <= abs(grid[nx][ny] - grid[x][y]) <= R

def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    result = []

    while q:
        x, y = q.popleft()
        result.append((x, y))
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(x, y, nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                result.append((nx, ny))
    
    return list(set(result))

# grid 돌면서 상하좌우 인접한 곳의 차 계산
cnt = 0
for _ in range(2000):
    flag = False
    for i in range(n):
        for j in range(n):
            q.append((i, j))
            visited[i][j] = True
            
            eggs = bfs()
            if len(eggs) >= 2:
                flag = True
                egg_sum = 0
                for x, y in eggs:
                    egg_sum += grid[x][y]
                for x, y in eggs:
                    grid[x][y] = int(egg_sum / len(eggs))
    if flag:
        cnt += 1
        
print(cnt)