from collections import deque

# 입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
q = deque()

def can_go(x, y, level):
    return 0<= x < n and 0 <= y < n and \
            not visited[x][y] and \
            grid[x][y] <= level

def bfs(level):
    global time
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, level): # 격자 내 & 레벨이 높은 몬스터 있는 곳은 못감
                time[nx][ny] = time[x][y] + 1
                q.append((nx, ny))
                visited[nx][ny] = True

# 실행
total_time, cnt = 0, 0
level = 2 # 현재 전투 로봇의 레벨

while True:
    visited = [[False] * n for _ in range(n)]
    time = [[0] * n for _ in range(n)]
    monsters = []

    # 1. 전투 로봇의 위치 찾기
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 9:
                q.append((i, j))
                visited[i][j] = True
                bfs(level)
                grid[i][j] = 0 # 이동할거니까 자리 비우기

    for i in range(n):
        for j in range(n):
            # 없앨 몬스터 기록
            if grid[i][j] != 0 and time[i][j] != 0 and grid[i][j] < level:
                monsters.append((time[i][j], i, j)) # 걸리는 시간, 행, 열

    # 없앨 몬스터 이동 규칙에 맞게 정렬
    monsters.sort(key=lambda x: (x[0], x[1], x[2]))

    # 더 이상 없앨 몬스터가 없으면 종료
    if len(monsters) == 0:
        break
    else: # 2. 몬스터가 있는 곳으로 이동해서 없애기 -> 없애고 전투 로봇의 레벨업 체크
        tmp_time, x, y = monsters[0] # 전투 로봇이 이동한 최종 위치
        grid[x][y] = 9 # 헤당 위치의 전투 로봇은 없어짐, 대신 전투 로봇이 위치
        total_time += tmp_time # 몬스터 없애러 가는데 걸리는 시간 추가
        cnt += 1

        # 레벨업 체크용 변수
        if cnt == level:
            level += 1
            cnt = 0

# 출력
print(total_time)