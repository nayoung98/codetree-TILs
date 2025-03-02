# 6개 면으로 이루어진 주사위 -> 마주보는 면끼리 적힌 숫자의 합 = 7
## n * n 격자의 특정 위치에 올려둠
## m번에 걸쳐 상하좌우 한 방향으로 한 칸을 이동하도록 굴리는 것을 반복
## 격자 밖으로 벗어나면, 굴리지 않고 그다음 과정 수행
# 격자판에는 해당 위치 주사위의 아랫면에 적혀있던 숫자가 적힘 (이미 해당 위치에 숫자가 있더라도, 새로 숫자가 적힘)
# 출력: 격자판에 적혀있는 숫자의 총합

# 입력 (격자의 크기, 주사위를 굴릴 횟수, 초기 주사위의 위치)
n, m, r, c = map(int, input().split())
r -= 1
c -= 1
info = list(input().split()) # L, R, U, D
grid = [[0] * n for _ in range(n)]

d_mapper = {'L': 0, 'D': 1, 'R': 2, 'U': 3}
drs, dcs = [0, 1, 0, -1], [-1, 0, 1, 0]

# 초기 위치
up, head, right = 1, 2, 3
dice = 6
grid[r][c] = dice # 초기 위치

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dice_mapper(d):
    global up, head, right
    
    if d == 0: # L
        tmp = up
        up = right
        right = 7 - tmp
    elif d == 1: # D
        tmp = head
        head = up
        up = 7 - tmp
    elif d == 2: # R 
        tmp = right 
        right = up
        up = 7- tmp
    elif d == 3: # U
        tmp = up
        up = head
        head = 7 - tmp
       
for i in info:
    d = d_mapper[i]
    nr, nc = r + drs[d], c + dcs[d]

    if not in_range(nr, nc):
        continue

    dice_mapper(d)

    dice = 7 - up
    grid[nr][nc] = dice
    r, c = nr, nc

result = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            result += grid[i][j]
print(result)