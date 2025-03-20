# n * n 격자 (각 도시마다의 높이 정보)
# k개의 도시를 겹치지 않게 골라, 골라진 k개의 도시로부터 갈 수 있는 서로 다른 도시의 수 최대화
# 상하좌우 인접한 도시간의 이동만 가능
# 두 도시간의 높이 차가 u이상 d이하인 경우에만 가능
# 출력: 서로 다른 도시의수 최댓값 (시작 도시 포함)
from collections import deque

# 입력
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()

# 격자 내 검사
def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

# 격자 내 & 방문 x & 거리 조건 만족
def can_go(nx, ny, x, y):
    return in_range(nx, ny) and \
            not visited[nx][ny] and \
            u <= abs(grid[nx][ny] - grid[x][y]) <= d

# 상하좌우 인접한 칸 방문
def bfs():
    global visited
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, x, y):
                q.append((nx, ny))
                visited[nx][ny] = True

# k개의 도시 고르기 (0 ~ n * n - 1의 숫자 중 k개 선택)
nums = [i for i in range(0, n * n)]
selected_city = []

def get_cnt(selected_city):
    global visited
    tmp_cnt = 0
    visited = [[False] * n for _ in range(n)]

    # 고른 도시의 넘버 -> 좌표로 변경
    for i in range(len(selected_city)): # k
        num = selected_city[i]
        x, y = num // n, num % n

        q.append((x, y))
        visited[x][y] = True
        bfs()

    # 방문한 곳 cnt
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                tmp_cnt += 1

    return tmp_cnt

max_cnt = 0
def choose_city(curr_num, cnt):
    global max_cnt

    # 종료 조건
    if curr_num > len(nums) or cnt > k:
        return

    if curr_num == len(nums):
        if cnt == k:
            max_cnt = max(max_cnt, get_cnt(selected_city))
        return

    selected_city.append(nums[curr_num])
    choose_city(curr_num + 1, cnt + 1)
    selected_city.pop()
    choose_city(curr_num + 1, cnt)

# 실행
choose_city(0, 0)

# 출력
print(max_cnt)