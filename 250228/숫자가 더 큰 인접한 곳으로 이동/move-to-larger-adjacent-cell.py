# # 2차원 격자 
# # 인접한 4개의 칸 중 가장 큰 숫자로 이동 -> t번 반복
# ## 가장 큰 숫자가 여러 개인 경우 우선 순위: 상하좌우
# # 출력: 최종 위치

# def simulate():
#     max_num = 0
#     max_x, max_y = -1, -1
#     global curr_x, curr_y
#     dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

#     for dx, dy in zip(dxs, dys):
#         nx, ny = curr_x + dx, curr_y + dy
#         if in_range(nx, ny) and grid[nx][ny] > max_num:
#             max_num = grid[nx][ny]
#             max_x, max_y = nx, ny
    
#     curr_x, curr_y = nx, ny

# n * n 격자
# 특정 위치에서 시작하여 이동
# 상하좌우로 인접한 곳에 있는 숫자들 중 현재 위치에 있는 숫자보다 더 큰 위치로 이동
## 우선순위: 상하좌우 (숫자가 아님!)
# 격자를 벗어나면 안됨
# 더 이상 움직일 수 없을 때까지 반복
# 출력: 방문하게 되는 위치에 적힌 숫자들을 차례대로 출력

# 입력: 격자의 크기, 시작 위치
n, r, c = map(int, input().split())
grid = [list(map(int ,input().split())) for _ in range(n)]
r -= 1
c -= 1

result = [grid[r][c]] # 현재 위치
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def simulate():
    global r, c
    flag = False

    # 현재 위치에서 이동
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if in_range(nr, nc) and grid[nr][nc] > grid[r][c]:
            result.append(grid[nr][nc])
            r, c = nr, nc
            flag = True
            break

    return flag

while True:
    flag = simulate()

    if not flag:
        break

print(*result)