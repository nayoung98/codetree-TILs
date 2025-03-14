# m개의 구슬, n * n 격자
# 구슬은 상하좌우 중 한 방향으로 이동, 1초에 한 칸씩 움직임 (방향을 바꾸는데도 1초 소요)
# 충돌 발생 시, 해당 위치의 구슬들은 전부 합쳐짐 
## 구슬의 무게 = 해당 위치에 모인 모든 구슬의 합, 뱡향 = 가장 큰 번호가 매겨져 있는 구슬의 방향
# 출력: t초 후 격자 안에 남아있는 구슬의 개수, 가장 무거운 구슬의 무게

# 입력
n, m, t = map(int, input().split())
marbles_info = [list(input().split()) for _ in range(m)] # r, c, d, w
grid = [[0] * n for _ in range(n)]
d_mapper = {'U': 0, 'R': 1, 'D': 2, 'L': 3}

# 구슬의 정보 업데이트, 초기 구슬 배치
def start():
    for i, (r, c, d, w) in enumerate(marbles_info):
        # r, c -> 0-idx
        r, c = int(r) - 1, int(c) - 1
        # d -> int
        d = d_mapper[d]
        # w -> int
        w = int(w)
        # 구슬의 정보 업데이트
        marbles_info[i][:] = r, c, d, w
        # 초기 구슬 배치
        grid[r][c] += 1

# 격자 내 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
    
# 방향에 따라 구슬 움직이기
def move_marbles():
    global tmp_grid, marbles_info
    tmp_grid = [[0] * n for _ in range(n)]
    drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i, (r, c, d, w) in enumerate(marbles_info):
        # 소멸된 구슬은 이동 x
        if d == -1:
            continue
        nr, nc = r + drs[d], c + dcs[d]
        if in_range(nr, nc):
            tmp_grid[nr][nc] += 1
            marbles_info[i][:2] = nr, nc # 새로운 위치 업데이트
        else:
            tmp_grid[r][c] += 1 # 현재 위치 그대로
            d = (d + 2) % 4
            marbles_info[i][2] = d # 새로운 방향 업데이트

# 충돌 검사
def chk_marbles():
    global tmp_grid, marbles_info
    chk = []

    for i in range(n):
        for j in range(n):
            if tmp_grid[i][j] >= 2:
                # 구슬 한개로 합치기
                tmp_grid[i][j] = 1
                for idx, (r, c, d, w) in enumerate(marbles_info):
                    if r == i and c == j:
                        # 같은 위치의 구슬들 저장
                        chk.append((idx, w))
                
                # 조건에 맞게 구슬 합치기 (무게 = 총합, 번호 = 최댓값, 방향 = 최대 번호의 방향)
                sum_w = sum(x[1] for x in chk)
                sum_i = max(chk, key=lambda x:x[0])[0]
                sum_d = marbles_info[sum_i][2]
                
                # 구슬의 정보 업데이트
                for idx, _ in chk:
                    if idx == sum_i:
                        marbles_info[idx][2:] = sum_d, sum_w
                    else: # 소멸
                        marbles_info[idx][2] = -1
            # 초기화
            chk = []

    # 원래 배열에 옮겨담기
    for i in range(n):
        for j in range(n):
            grid[i][j] = tmp_grid[i][j]

# 설계
start()

# t초 동안 실행
for _ in range(t):
    move_marbles()
    chk_marbles()

# 출력
num_marbles, max_weight = 0, 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            num_marbles += 1
            for r, c, d, w in marbles_info:
                if r == i and c == j:
                    max_weight = max(max_weight, w)
print(num_marbles, max_weight)