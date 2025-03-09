# n * n 격자 (1 ~ n * n 수들이 한번씩만 등장)
# m번의 턴에 걸쳐 수들을 이동
## 한 번의 턴: 1이 적힌 위치에서부터 n * n이 적힌 위치까지 순서대로 하나씩 봄  
## 각 위치에서 여덟 방향으로 인접한 칸들 중 가장 큰 수와 가운데 칸의 수를 교환
# 출력: m번의 턴을 거친 후 격자의 상태

# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 격자 내인지 판단
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 8방향으로 이동하면서 숫자 비교 
def change_num(x, y):

    dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    mx, my, max_num = -1, -1, -1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny):
            curr_num = grid[nx][ny]

            # 최댓값 찾기
            if curr_num > max_num:
                max_num = curr_num
                mx, my = nx, ny

    # 최댓값과 변경
    grid[mx][my] = grid[x][y]
    grid[x][y] = max_num

# 1번의 턴
def simulate():
    target_num = 1

    while True:
        flag = False

        for i in range(n):
            for j in range(n):
                if grid[i][j] == target_num:
                    # 8방향 검사 및 숫자 교환 
                    change_num(i, j)
                    target_num += 1
                    flag = True
                    break
            if flag == True:
                break
        
        if target_num == n * n + 1:
            break

# m번 반복 실행
for _ in range(m):
    simulate()

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()