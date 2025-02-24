# n * m, 0~9 숫자
# 총 Q번의 바람 -> 특정 행의 모든 원소들을 왼쪽 or 오른쪽으로 전부 한 칸씩 shift -> 밀리기 시작한 행을 기준으로 위 아래 방향으로 순차적으로 전파
## 전파 조건
### 현재 행과 나아가려는 행을 비교했을 때, 단 하나라도 같은 열에 같은 숫자가 있어야 함
### 현재 행이 밀렸던 방향과 반대 방향으로 작용
### 같은 숫자가 하나도 존재하지 않거나, 끝에 다다랐다면 전파를 종료
# 한 바람이 분 이후, 모든 전파가 완료되었을 때 그 다음 바람이 불어옴
# 출력: 총 Q개의 바람을 거친 이후 건물(grid)의 상태 출력

# 입력
n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 바람의 정보 (행 번호 0-idx, 방향 'L' or 'R')
wind_info = [tuple(input().split()) for _ in range(q)]

# 바람 불기 
def make_wind(r, m, d):
    # r: 행(0-idx), m, d: 바람 방향
    if d == 'L': # 왼쪽에서 불어오는 바람
        tmp = grid[r][m - 1] # 맨 오른쪽 원소
        for i in range(m - 1, 0, -1):
            grid[r][i] = grid[r][i - 1]
        grid[r][0] = tmp

    else: # 오른쪽에서 불어오는 바람
        tmp = grid[r][0] # 맨 왼쪽 원소
        for i in range(0, m - 1):
            grid[r][i] = grid[r][i + 1]
        grid[r][m - 1] = tmp

# 위 행 전파 
def wind_up(r, m, d): 
    tmp_up = d # 시작할 때의 바람 방향
    for i in range(r, 0, -1):
        cnt = 0
        for j in range(m):
            if grid[i][j] == grid[i - 1][j]:
                cnt += 1
        
        if cnt >= 1:
            if tmp_up == 'R':
                make_wind(i - 1, m, 'L')
                tmp_up = 'L'
            else:
                make_wind(i - 1, m, 'R')
                tmp_up = 'R'

# 아래 행 전파
def wind_down(r, m, d):
    tmp_down = d # 시작할 때의 바람 방향
    for i in range(r, n - 1):
        cnt = 0
        for j in range(m):
            if grid[i][j] == grid[i + 1][j]:
                cnt += 1
        
        if cnt >= 1:
            if tmp_down == 'R':
                make_wind(i + 1, m, 'L')
                tmp_down = 'L'
            else:
                make_wind(i + 1, m, 'R')
                tmp_down = 'R'

for (r, d) in wind_info:
    r = int(r) - 1

    # 바람 불기
    make_wind(r, m, d)
    # 위 행 전파 
    wind_up(r, m, d)
    # 아래 행 전파
    wind_down(r, m, d)

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
