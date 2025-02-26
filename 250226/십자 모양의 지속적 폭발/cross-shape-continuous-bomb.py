# n * n 격자
# 특정 열 선택 -> 해당 열에 숫자가 적혀있는 위치 중 가장 위의 칸을 중심으로 십자 모양으로 폭탄이 터짐
# 폭탄의 크기 = 선택된 칸에 적혀있는 숫자
# 터진 이후 중력이 작용함
# 출력: 반복된 폭탄이 터진 이후의 결과

# 입력 (초기 격자판의 상태, 폭탄이 터질 열의 위치)
n, m = map(int, input().split()) # 폭탄이 터지는 횟수: m번
grid = [list(map(int, input().split())) for _ in range(n)]
info = [int(input()) for _ in range(m)] # 1-idx
drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 해당 열에서 숫자가 적힌 칸 중 가장 위의 칸 찾기 -> 폭탄 지정
def find_bomb(n):
    bombs = []
    for i in range(n):
        if grid[i][c] != 0:
            bombs.append((i, grid[i][c]))

    if len(bombs) != 0:
        r = bombs[0][0] # 폭탄의 위치 (행) 지정
        bomb = bombs[0][1] # 폭탄의 크기 결정
    else:
        r = -1
        bomb = 0
    
    return r, bomb

# 폭탄 터짐 
def explode_bomb(r, c, bomb):
    global grid

    # 0으로 만들기
    # 해당 위치
    grid[r][c] = 0
    # 주위
    for dr, dc in zip(drs, dcs):
        for i in range(1, bomb):
            nr, nc = r + i * dr, c + i * dc
            if not in_range(nr, nc):
                continue
            grid[nr][nc] = 0

    # 중력 작용 (아래로 이동)
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        row = n - 1
        for j in range(n - 1, -1, -1): # 맨 아래 행부터
            if grid[j][i] != 0:
                tmp[row][i] = grid[j][i]
                row -= 1
    grid = tmp

# 실행 
for c in info:
    c -= 1 # 0-idx
    r, bomb = find_bomb(n)

    if bomb == 0:
        break

    explode_bomb(r, c, bomb)

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()