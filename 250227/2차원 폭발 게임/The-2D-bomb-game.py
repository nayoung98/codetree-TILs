# n * n 크기의 격자
# 열마다 연속으로 m개 이상의 같은 숫자가 적혀있는 폭탄들은 전부 다 터짐 -> 중력 작용
# 터지고 회전하는 과정: 한번 터짐 -> 중력 작용 -> 시계 방향으로 90도 회전 -> 중력 작용
# 출력: k번 반복 후 상자에 남아있는 폭탄의 수
# k번 반복 이후 터질 폭탄이 남아있다면, 폭탄을 모두 터트리고 출력

# 입력
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 중력 작용
def gravity(n):
    global grid
    tmp = [[0] * n for _ in range(n)]

    for i in range(n):
        row = n - 1
        for j in range(n - 1, -1, -1):
            if grid[j][i] != 0:
                tmp[row][i] = grid[j][i]
                row -= 1

    grid = tmp

def explode_bomb(n):
    global grid
    chk = [[False] * n for _ in range(n)]

    # 각 열마다 연속되는 m개 이상의 숫자가 있는지 검사
    for i in range(n):
        cnt = 1 
        for j in range(n - 1):
            if grid[j][i] == grid[j + 1][i]:
                cnt += 1
                chk[j][i], chk[j + 1][i] = True, True
        # 있으면 폭탄 터짐 -> 0이 됨
        for j in range(n):    
            if chk[j][i] == True:
                if cnt >= m:
                    grid[j][i] = 0

    # 중력 작용
    gravity(n)

# 시계 방향 90도 회전  (행 -> 열)
def rotate_grid(n):
    global grid
    col = 0
    tmp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(n):
            tmp[j][col] = grid[i][j]
        col += 1
    grid = tmp

    # 중력 작용
    gravity(n)

# 각 열마다 연속되는 m개 이상의 숫자가 있는지 검사
def inspection_grid(n):
    global grid

    for i in range(n):
        cnt = 1 
        for j in range(n - 1):
            if grid[j][i] != 0 and (grid[j][i] == grid[j + 1][i]):
                cnt += 1
        if cnt == m:
            return True
    return False

if n == 1 and m == 1:
    result = 0
else:
    # k번 반복 
    for _ in range(k):
        explode_bomb(n)
        rotate_grid(n)

    # 반복 이후 조건에 맞는 폭탄 있는지 확인
    while True:
        if not inspection_grid(n):
            break
        else:
            explode_bomb(n)

    # 출력
    result = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                result += 1

print(result)

