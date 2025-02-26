# n * n 격자
# 특정 위치를 중심으로 십자 모양 폭탄 터짐 -> 터진 이후 중력에 의해 숫자들이 아래로 떨어짐
# 십자 모양의 크기 = 선택된 위치에 적혀있는 숫자
# 출력: 폭탄이 터진 뒤 중력이 작용하고 나서의 결과

# 입력: 초기 격자판의 상태, 폭탄이 터질 곳의 중심 위치
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]

# 1-idx
r, c = map(int, input().split())
# 0-idx
r -= 1
c -= 1

# 폭탄의 크기 정하기
bomb = grid[r][c]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def expode_bomb(r, c):
    global grid

    # 폭탄 터트리기
    # 해당 위치
    grid[r][c] = 0
    # 주위
    for dr, dc in zip(drs, dcs):
        for i in range(1, bomb):
            nr, nc = r + i * dr, c + i * dc
            if not in_range(nr, nc):
                continue
            grid[nr][nc] = 0

    # 중력 작용하기
    tmp = [[0] * n for _ in range(n)]
    for i in range(n): # 첫번째 열 -> 마지막 열
        row = n - 1
        for j in range(n - 1, -1, -1):
            if grid[j][i] != 0:
                tmp[row][i] = grid[j][i]
                row -= 1
    grid = tmp

# 실행 
expode_bomb(r, c)

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()