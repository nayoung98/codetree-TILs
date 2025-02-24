# n * m 행렬, q번의 바람
# 특정 직사각형 영역의 경계 내 숫자들을 시계 방향으로 한칸씩 shift, 해당 값들을 각각 자신의 위치를 기준으로 인접한 원소들과의 평균 값으로 바꿈
# 한 번 바람이 분 이후, 다음 바람이 불어옴
import math

# 입력
n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

# 바람에 대한 정보: (r1, c1) = 직사각형 좌측 상단, (r2, c2) = 직사각형 우측 하단
wind_info = [(tuple(map(int, input().split()))) for _ in range(q)]

# 직사각형 이동
def move_rect(r1, c1, r2, c2):
    # 윗변 
    tmp_up = grid[r1][c2]
    for i in range(c2, c1, -1):
        grid[r1][i] = grid[r1][i - 1]

    # 우변
    tmp_right = grid[r2][c2]
    for i in range(r2, r1, -1):
        grid[i][c2] = grid[i - 1][c2]
    
    # 아랫변
    tmp_down = grid[r2][c1]
    for i in range(c1, c2):
        grid[r2][i] = grid[r2][i + 1]
    
    # 좌변
    tmp_left = grid[r1][c1]
    for i in range(r1, r2):
        grid[i][c1] = grid[i + 1][c1]
    
    # 원소 채우기
    grid[r1 + 1][c2] = tmp_up
    grid[r2][c2 - 1] = tmp_right
    grid[r2 - 1][c1] = tmp_down
        
# 범위 내인지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 직사각형 내 원소 바꾸기
def change_rect(r1, c1, r2, c2):
    # 원소 계산하고 tmp 배열에 저장하기
    tmp_arr = [list(0 for _ in range(m)) for _ in range(n)]
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            nums, cnt = grid[i][j], 1
            for (dx, dy) in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if in_range(nx, ny):
                    nums += grid[nx][ny]
                    cnt += 1
            tmp_arr[i][j] = int(math.floor(nums/cnt))

    # tmp 배열 -> 원래 배열에 옮기기
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            grid[i][j] = tmp_arr[i][j]

# 실행 
for (r1, c1, r2, c2) in wind_info:
    # 0-idx
    r1 -= 1
    c1 -= 1 
    r2 -= 1
    c2 -= 1

    move_rect(r1, c1, r2, c2)
    change_rect(r1, c1, r2, c2)

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()