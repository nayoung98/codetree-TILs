# n * n 격자 (1 ~ n * n)
# m번에 걸쳐 숫자들을 이동, 선택된 숫자의 인접한 여덟방향에 아무 숫자도 없다면 이동 종료
## 각 위치에서 여덟방향으로 인접한 칸들 중 가장 큰 값이 적혀있는 숫자가 있는 곳으로 이동
# 출력: m번의 움직임 이후의 상태 출력

# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
nums_info = list(map(int, input().split()))

tmp_grid = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        tmp_grid[i][j].append(grid[i][j])

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_num(x, y, idx):
    global tmp_grid
    dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    mx, my, max_num = -1, -1, -1
    flag = False

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and len(tmp_grid[nx][ny]) != 0:
            flag = True
            if max_num < max(tmp_grid[nx][ny]):
                mx, my, max_num = nx, ny, max(tmp_grid[nx][ny])
    if not flag: # 근처가 모두 빈 곳이면 종료
        return 
    else:
        tmp_grid[mx][my].extend(tmp_grid[x][y][idx:])
        tmp_grid[x][y] = tmp_grid[x][y][:idx]

# 격자 돌면서 num_info에 해당하는 숫자 찾기
for num in nums_info:
    flag = False
    for i in range(n):
        for j in range(n):
            if num in tmp_grid[i][j]:
                idx = tmp_grid[i][j].index(num)
                flag = True
                move_num(i, j, idx)
                break
        if flag:
            break
                
# 출력
for i in range(n):
    for j in range(n):
        if not len(tmp_grid[i][j]):
            print('None', end=' ')
        else:
            print(*reversed(tmp_grid[i][j]), end=' ')
        print()