# n * n 격자
# 우측 방향을 바라보고 시작해서 오른쪽 벽을 짚고 쭉 이동하며 미로 탈출
# 바라보고 있는 방향으로 이동 불가능 할 때 -> 반 시계 방향으로 90도 회전하여 이동
# 바라보고 있는 방향으로 이동 가능 할 때 -> 격자 밖이라면 탈출
# 바라보고 있는 방향으로 이동 가능 할 때 -> 오른쪽으로 짚을 벽이 있다면 -> 그 방향으로 한칸 이동
# 바라보고 있는 방향으로 이동 가능 할 때 -> 오른쪽으로 짚을 벽이 없다면 -> 시계방향으로 90도 회전, 전진
# 출력: 미로를 탈출하는 데 걸리는 시간 (방향 회전에는 시간 x), 탈출이 불가능한 경우 -1 출력

# 입력 (벽: #)
n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1
grid = [list(input().strip()) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
d = 0 # 현재 방향
t = 0 # 소요 시간

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 한 번 이동
def simulate():
    global flag, x, y, d, t
    flag = False

    # 한번 이동
    nx, ny = x + dxs[d], y + dys[d]
    if in_range(nx, ny) and grid[nx][ny] == '#':
        d = (d - 1) % 4
    elif grid[nx][ny] != '#':
        if not in_range(nx, ny):
            t += 1 # 탈출
            flag = True
        else:
            t += 1
            x, y = nx, ny
            if d == 0:
                if not (in_range(nx + 1, ny) and grid[nx + 1][ny] == '#'):
                    d = (d + 1) % 4
                    x, y = x + dxs[d], y + dys[d]
                    t += 1
            elif d == 1:
                if not (in_range(nx, ny - 1) and grid[nx][ny - 1] == '#'):
                    d = (d + 1) % 4
                    x, y = x + dxs[d], y + dys[d]
                    t += 1
            elif d == 2:
                if not (in_range(nx - 1, ny) and grid[nx - 1][ny] == '#'):
                    d = (d + 1) % 4
                    x, y = x + dxs[d], y + dys[d]
                    t += 1
            elif d == 3:
                if not (in_range(nx, ny + 1) and grid[nx][ny + 1] == '#'):
                    d = (d + 1) % 4
                    x, y = x + dxs[d], y + dys[d]
                    t += 1

    
for _ in range(n * n):
    # flag = False
    simulate()
    # # 한번 이동
    # nx, ny = x + dxs[d], y + dys[d]
    # if in_range(nx, ny) and grid[nx][ny] == '#':
    #     d = (d - 1) % 4
    # elif grid[nx][ny] != '#':
    #     if not in_range(nx, ny):
    #         t += 1 # 탈출
    #         flag = True
    #     else:
    #         t += 1
    #         x, y = nx, ny
    #         if d == 0:
    #             if not (in_range(nx + 1, ny) and grid[nx + 1][ny] == '#'):
    #                 d = (d + 1) % 4
    #                 x, y = x + dxs[d], y + dys[d]
    #                 t += 1
    #         elif d == 1:
    #             if not (in_range(nx, ny - 1) and grid[nx][ny - 1] == '#'):
    #                 d = (d + 1) % 4
    #                 x, y = x + dxs[d], y + dys[d]
    #                 t += 1
    #         elif d == 2:
    #             if not (in_range(nx - 1, ny) and grid[nx - 1][ny] == '#'):
    #                 d = (d + 1) % 4
    #                 x, y = x + dxs[d], y + dys[d]
    #                 t += 1
    #         elif d == 3:
    #             if not (in_range(nx, ny + 1) and grid[nx][ny + 1] == '#'):
    #                 d = (d + 1) % 4
    #                 x, y = x + dxs[d], y + dys[d]
    #                 t += 1

    if flag:
        break

if flag:
    print(t)
else:
    print(-1)