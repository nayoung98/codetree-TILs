# 4 * 4 격자 (2의 거듭제곱꼴로 나타나는 숫자들(2~2048)로 구성)
# 상하좌우 중 한 방향을 정하면, 해당 방향으로 모든 숫자들이 밀림
# 같은 숫자끼리 만나면 두 숫자가 합쳐짐 (단, 이미 합쳐진 숫자가 연쇄적으로 합쳐지진 않음)
## 세 개 이상의 같은 숫자가 있는경우, 벽에서 가까운 숫자부터 두 개씩만 합쳐짐
# 출력: d 방향으로 움직인 이후의 결과 (숫자가 적혀있지 않은 경우 0)

# 입력
n = 4
grid = [list(map(int, input().split())) for _ in range(n)]
d = input()

################ 이동하는 함수 ################
def move_right(n):
    global grid
    tmp = [[] for _ in range(n)]
    # 0이 없는 숫자만 tmp에 저장
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                tmp[i].append(grid[i][j])
    for i in range(n):
        for j in range(n - len(tmp[i])):
            tmp[i].insert(0, 0)
    # 오른쪽으로 이동 완료
    grid = tmp 

def move_left(n):
    global grid
    tmp = [[] for _ in range(n)]
    # 0이 없는 숫자만 tmp에 저장
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                tmp[i].append(grid[i][j])
    for i in range(n):
        for j in range(n - len(tmp[i])):
            tmp[i].append(0)
    # 왼쪽으로 이동 완료
    grid = tmp 

################ 합치는 함수 ################
def sum_right(n):
    global grid
    # 같은 숫자가 있는지 확인 후 합치기
    for i in range(n):
        for j in range(n - 1, 0, -1):
            if grid[i][j] == grid[i][j - 1]:
                grid[i][j] += grid[i][j - 1]
                grid[i][j - 1] = 0

def sum_left(n):
    global grid
    # 같은 숫자가 있는지 확인 후 합치기
    for i in range(n):
        for j in range(n - 1):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j] += grid[i][j + 1]
                grid[i][j + 1] = 0

################ 회전하는 함수 (열 -> 행) ################
def rotate(n):
    global grid
    # 한 열씩 아래 행으로 쌓기 -> 그리고 나서 왼쪽 이동
    tmp = []
    for i in range(n - 1, -1, -1):
        tmp_col = []
        for j in range(n):
            tmp_col.append(grid[j][i])
        tmp.append(tmp_col)
    grid = tmp

################ 실행 ################
if d == 'R':
    move_right(n)
    sum_right(n)
    move_right(n)

    # 출력
    for i in range(n):
        print(*grid[i], sep=' ')

elif d == 'L':
    move_left(n)
    sum_left(n)
    move_left(n)

    # 출력
    for i in range(n):
        print(*grid[i], sep=' ')

elif d == 'U':
    # 방향 회전 -> 행 방향으로 바꾸기
    rotate(n)

    # L방향으로 움직이기
    move_left(n)
    sum_left(n)
    move_left(n)
    
    # 출력
    for i in range(n):
        for j in range(n - 1, -1, -1):
            print(grid[j][i], end=' ')
        print()

elif d == 'D':
    # 방향 회전 -> 행 방향으로 바꾸기
    rotate(n)

    # R방향으로 움직이기
    move_right(n)
    sum_right(n)
    move_right(n)

    # 출력
    for i in range(n):
        for j in range(n - 1, -1, -1):
            print(grid[j][i], end=' ')
        print()
