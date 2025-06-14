from collections import deque

# 1. 입력 받기
n, Q = map(int, input().split())
locations = [list(map(int, input().split())) for _ in range(Q)]

# 미생물 투입 격자
grid = [[-1] * n for _ in range(n)]

# 2. 미생물 투입: 변경된 좌표로 미생물 넣기 -> 다른 미생물이 그 위치에 있는지 확인 (있으면 잡아먹기) -> 배치 후 갈라진 미생물 있는지 확인 (있으면 삭제)
## 변경된 좌표로 미생물 넣기 -> 넣는 과정에서 다른 미생물이 있으면 그냥 덯어 씌우기
def put_germs(idx, r1, c1, r2, c2):
    for row in range(r1, r2):
        for col in range(c1, c2):
            grid[row][col] = idx

## 배치 후 갈라진 미생물 확인하기
q = deque()
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def can_go(nx, ny, idx):
    return in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == idx

def bfs(idx):
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, idx):
                q.append((nx, ny))
                visited[nx][ny] = True

def chk_germs(idx):
    component = 0
    for row in range(n):
        for col in range(n):
            if grid[row][col] == idx and not visited[row][col]:
                component += 1
                q.append((row, col))
                visited[row][col] = True
                bfs(idx)
    return component

# 실행: 미생물 투입
def put_routine(idx, r1, c1, r2, c2):
    chk_germs(idx)
    put_germs(idx, r1, c1, r2, c2)
    # print(f"미생물 투입 후: {grid}")
    #
    # ##############3 현재까지 투입된 모든 미생물에 대해 계산하도록 바꿔야됨
    # component = chk_germs(idx)
    # print(f"component: {component}")
    # # 미생물이 갈라졌다면 삭제하기
    # if component >= 2:
    #     for row in range(n):
    #         for col in range(n):
    #             if grid[row][col] == idx:
    #                 grid[row][col] = -1  # 삭제

# 3. 배양 용기 이동: 새로운 배양 용기 생성 -> 기존 배양 용기에서 미생물들의 넓이 계산 -> 우선 순위(넓이 큰거 > 가장 먼저 투입된 것)으로 배치 (최대한 x가 작은 곳 > y가 작은곳) -> 어떤 곳에도 둘 수 없으면 삭제
# 새로운 배양 용기
new_grid = [[-1] * n for _ in range(n)]

## 옮기는 미생물 정하기: 가장 차지한 넓이 넓은 것 -> 먼저 투입된 것
### 미생물 넓이 구하기
def get_area(idx): # idx에 해당하는 면적
    area = 0
    for row in range(n):
        for col in range(n):
            if grid[row][col] == idx:
                area += 1
    return area

## 미생물 옮기기: x 작은 것 -> y 작은 것 (옮기지 못하면 삭제)
def move_germs(idx):
    # 미생물이 있는 위치 찾기
    min_r, min_c, max_r, max_c = n, n, -1, -1
    for row in range(n):
        for col in range(n):
            if grid[row][col] == idx:
                min_r, max_r = min(min_r, row), max(max_r, row)
                min_c, max_c = min(min_c, col), max(max_c, col)
    height, width = max_r - min_r + 1, max_c - min_c + 1

    # 미생물 모양의 상대 좌표 저장 (방향 벡터처럼 저장함)
    shape = []
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if grid[r][c] == idx:
                shape.append((r - min_r, c - min_c))

    # 빈칸 찾아서 하나씩 옮기기 (못옮기면 삭제(그냥 냅두기))
    for sr in range(n - height + 1):
        for sc in range(n - width + 1):
            can_place = True
            for dr, dc in shape:
                nr, nc = sr + dr, sc + dc
                if new_grid[nr][nc] != -1:
                    can_place = False
                    break

            if can_place:
                for dr, dc in shape:
                    nr, nc = sr + dr, sc + dc
                    new_grid[nr][nc] = idx
                return

# 실행: 배양 용기 이동
def move_routine():
    priority = []
    for idx in range(Q):
        # 각 미생물의 넓이 구하기
        area = get_area(idx)
        priority.append((idx, area))

    ## 우선 순위 구하기: 가장 차지한 넓이 넓은 것 -> 먼저 투입된 것
    priority.sort(key=lambda x: (-x[1], x[0]))

    for idx, _ in priority:
        move_germs(idx)

# 4. 실험 결과 기록: 상하좌우 맞닿은 인접한 무리 확인 -> 각 무리 별 넓이 계산 후 다 곱하기 -> 출력
## new_grid -> grid로 옮기고 초기화
def init_grid():
    global new_grid
    # new_grid -> grid로 옮기기
    for row in range(n):
        for col in range(n):
            grid[row][col] = new_grid[row][col]

    # new_grid 초기화
    new_grid = [[-1] * n for _ in range(n)]

## 상하좌우 인접한 무리 찾기 -> 무리 별 넓이 계산 (무리가 1개인 경우에는 0) -> 다 더하기
def get_total_area():
    adj_list = []
    # 인접한 무리 찾기: 인접한거 찾아서 idx 저장
    for row in range(n):
        for col in range(n):
            if grid[row][col] == -1:
                continue

            for dr, dc in zip(dxs, dys):
                nr, nc = row + dr, col + dc
                if not in_range(nr, nc) or grid[nr][nc] == -1:
                    continue
                if grid[nr][nc] != grid[row][col]:
                    adj_list.append(sorted([grid[row][col], grid[nr][nc]]))
    adj_list = list(set(map(tuple, adj_list)))
    # print((adj_list))

    # 무리 별 넓이 계산하기: 저장된게 2개일때만 넓이 계산, 1개인 경우는 0
    total_area = 0
    for adj in adj_list:
        if len(adj) != 2:
            continue

        areaA, areaB = 0, 0
        A, B = adj
        for row in range(n):
            for col in range(n):
                if grid[row][col] == -1:
                    continue
                if grid[row][col] == A:
                    areaA += 1
                elif grid[row][col] == B:
                    areaB += 1
        # print(areaA, areaB)

        # 다 더해서 리턴
        total_area += (areaA * areaB)
    # print(total_area)
    return total_area

# def cal_routine():
#     init_grid()
#     get_total_area()

# 5. 2~4의 과정을 Q번 반복
for i in range(Q):
    put_routine(i, *locations[i])

    # 현재까지 투입된 모든 미생물에 대해 컴포넌트 계산 후 갈라져 있으면 삭제함
    for id in range(i + 1):
        visited = [[False] * n for _ in range(n)]

        component = chk_germs(id)
        # print(f"component: {component}")

        # 미생물이 갈라졌다면 삭제하기
        if component >= 2:
            for row in range(n):
                for col in range(n):
                    if grid[row][col] == id:
                        grid[row][col] = -1  # 삭제

    # 새로운 배양 용기
    new_grid = [[-1] * n for _ in range(n)]
    move_routine()

    init_grid()
    total_area = get_total_area()

    # total_area = cal_routine()
    print(total_area)
    # print(grid)