# n * n 격자, m개의 구슬
# 각 구슬은 1초에 한 칸씩 동일한 속도, 정해진 방향으로 움직임
# 구슬이 벽에 부딪히면 움직이는 방향만 바뀜
# 구슬이 충돌 (이동 후 같은 위치에 있는 경우)하면 부딪힌 구슬 모두 사라짐
# 출력: 아주 오랜시간이 흐른 뒤 남아있는 구슬의 개수

# 구슬의 방향 인덱스 리턴
def get_idx(d):
    if d == 'U':
        return 0
    elif d == 'R':
        return 1
    elif d == 'D':
        return 2
    else: # L
        return 3

# 구슬의 방향 인덱스 반환, 구슬 배치
def start():
    global marbles, grid

    for i, (x, y, d) in enumerate(marbles):
        idx = get_idx(d)
        marbles[i][2] = idx

        x, y = int(x) - 1, int(y) - 1
        marbles[i][0], marbles[i][1] = x, y
        grid[x][y] += 1

# 격자 내 검사
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 구슬 1번 이동
def move_marbles():
    global marbles, tmp_grid
    tmp_grid = [[[] for _ in range(n)] for _ in range(n)]
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 구슬 1번 이동
    for i, (x, y, d) in enumerate(marbles):
        
        # 없어진 구슬은 이동 안함
        if d == -1: 
            continue
        nx, ny = x + dxs[d], y + dys[d]

        if in_range(nx, ny):
            tmp_grid[nx][ny].append(i)
            x, y = nx, ny
        else: # 방향만 바꿈
            tmp_grid[x][y].append(i)  
            d = (d + 2) % 4
        
        # 1번 움직인 뒤 구슬의 정보 (위치, 방향) 저장
        marbles[i][0], marbles[i][1], marbles[i][2] \
            = x, y, d

# 충돌 제거
def remove_marbles():

    for i in range(n):
        idx = []
        for j in range(n):
            # 충돌한 구슬 제거
            if len(tmp_grid[i][j]) >= 2:
                idx = tmp_grid[i][j]
                for tmp_id in idx:
                    marbles[tmp_id][2] = -1

    # 구슬 저장
    new_grid = [[0] * n for _ in range(n)]
    for x, y, d in marbles:
        if d == -1:
            continue
        new_grid[x][y] += 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = new_grid[i][j]
        
# 입력
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    marbles = [list(input().split()) for _ in range(m)] # x, y, d
    grid = [[0] * n for _ in range(n)]

    # 실행
    start()
    for _ in range(2 * n):
        move_marbles()
        remove_marbles()

    
    # 결과 출력
    result = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                result += 1
    print(result)
