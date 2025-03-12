# n * n 격자, m개의 구슬
# 각 구슬은 일정 속도를 갖고 정해진 방향으로 움직임
# 벽에 부딪히면 움직이는 방향이 반대로 뒤집힘 (방향을 바꾸는데는 시간 소요 x)
# 움직이고 난 후 같은 위치에 구슬이 k개 이하라면 다음 과정을 진행, 
# k개가 넘는 구슬이 있다면 우선순위가 높은 k개만 살아남음
## 우선순위: 구슬의 속도가 빠를수록 높음, 구슬의 속도가 일치할 경우 구슬의 번호가 더 큰 구슬이 높음
# 출력: t초 후 격자 안에 남아있는 구슬의 개수

# 입력
n, m, t, k = map(int, input().split())
marbles_info = [list(input().split()) for _ in range(m)] # (r, c, d, v)
grid = [[0] * n for _ in range(n)]
mapper = {'U': 0, 'R': 1, 'D': 2, 'L': 3}

# 구슬의 초기 배치, 구슬 정보 업데이트
def start():
    global marbles_info, grid

    for i, (r, c, d, v) in enumerate(marbles_info):
        r, c, v = int(r) - 1, int(c) - 1, int(v)
        idx = mapper[d]

        # 구슬 정보 업데이트
        marbles_info[i][:] = r, c, idx, v 

        # 구슬의 초기 배치
        grid[r][c] += 1

# 격자 범위 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 1초 동안 구슬 움직임
def move_marbles():
    global tmp_grid, marbles_info
    tmp_grid = [[0] * n for _ in range(n)]

    for i, (x, y, d, v) in enumerate(marbles_info):
        # 없어진 구슬은 안움직임
        if v == -1:
            continue

        dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
        
        # 한 칸씩 움직일 때 마다 범위 내인지 확인
        for _ in range(v):
            nx, ny = x + dxs[d], y + dys[d]

            if in_range(nx, ny):
                x, y = nx, ny
            else:
                d = (d + 2) % 4
                nx, ny = x + dxs[d], y + dys[d]
                if in_range(nx, ny):
                    x, y = nx, ny   

        # 최종 위치에 구슬 기록, 저장
        tmp_grid[x][y] += 1
        marbles_info[i][:-1] = x, y, d

# 충돌 검사
def remove_marbles():
    global grid, tmp_grid, marbles_info
    chk_marbles = []
    tmp_marbles = [[-1] * 4 for _ in range(m)]

    # tmp_grid 돌면서 구슬의 개수 확인
    for i in range(n):
        for j in range(n):
            if tmp_grid[i][j] > k:
                # 우선 순위 높은 k개만 생존
                tmp_grid[i][j] = k

                # 같은 위치인 구슬만 남기기
                for idx,(r, c, d, v) in enumerate(marbles_info):
                    if in_range(r, c) and r == i and c == j:
                        chk_marbles.append((idx, r, c, d, v))
                
                # 남아있는 구슬의 개수 확인 후, 우선순위에 따라 정리
                if len(chk_marbles) > k:
                    chk_marbles.sort(key=lambda x: (-x[4], -x[0]))

                    for marble in range(k):
                        mi = chk_marbles[marble][0]
                        tmp_marbles[mi] = list(chk_marbles[marble][1:])

                # 구슬의 정보 업데이트
                for idx, r, c, d, v in chk_marbles:
                    if in_range(r, c):
                        marbles_info[idx] = tmp_marbles[idx]
                
                chk_marbles = []
                tmp_marbles = [[-1] * 4 for _ in range(m)]
            
    # 원래 grid에 저장
    for i in range(n):
        for j in range(n):
            grid[i][j] = tmp_grid[i][j]

# 설계
start()

# t초 동안 실행
for time in range(t):
    move_marbles()
    remove_marbles()

# 출력
result = 0
for i in range(n):
    for j in range(n):
        result += grid[i][j]
print(result)
