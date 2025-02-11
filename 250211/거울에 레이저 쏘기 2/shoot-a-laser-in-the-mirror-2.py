# n * n 격자, 거울 \ / 
# 격자 밖 4n개의 위치 중 특정 위치에서 레이저를 쏘았을 때, 거울에 튕기는 횟수 구하기

# 입력
n = int(input())
grid = [list(input().strip()) for _ in range(n)]
k = int(input()) - 1# 레이저를 쏘는 위치

# 시작 위치 결정 -> 레이저 쏘는 위치에 따른 격자의 위치
def get_starting(k, n):
    if k // n == 0:
        r = 0
        c = k % n
    elif k // n == 1:
        r = k % n
        c = n - 1
    elif k // n == 2:
        r = n - 1
        c = (n - 1) - (k % n)
    else:
        r = (n - 1) - (k % n)
        c = 0

    return r, c

# 범위 확인 
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 거울에 따라 방향 전환
# 시작 위치 
r, c = get_starting(k, n)
curr_dir = 1
cnt = 0

# 방향 벡터 -> 몫(k // n), 거울의 방향에 따라 결정
down_mirror = [[(1, 0), (0, 1)], [(0, -1), (-1 ,0)], [(-1, 0), (0, -1)], [(0, 1), (1, 0)]]
up_mirror = [[(1, 0), (0, -1)], [(0, -1), (-1 ,0)], [(-1, 0), (0, 1)], [(0, 1), (-1, 0)]]

def get_directs(r, c, curr_dir):
    if grid[r][c] == '\\':
        dr, dc = down_mirror[k // n][curr_dir]
    else:
        dr, dc = up_mirror[k // n][curr_dir]
    return dr, dc

# 시뮬레이션
while True:

    dr, dc = get_directs(r, c, curr_dir)
    nr, nc = r + dr, c + dc

    if in_range(nr, nc):
        cnt += 1
        r, c = nr, nc
        curr_dir = (curr_dir + 1) % 2
    else: 
        break

print(cnt + 1) # 나가는거 포함