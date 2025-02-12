# 가로, 세로, 대각선 방향으로 같은 색의 바둑알이 5알이면 그 색이 이김
# 누가 이겼는지, 혹은 아직 승부가 결정되지 않았는지 판단

# 입력 (1: 검, 2: 흰, 0: 공백)
grid = [list(map(int, input().split())) for _ in range(19)]
dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]

# 범위 확인
def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def simulate(x, y):
    target = grid[x][y]
    
    for dx, dy in zip(dxs, dys):
        cnt = 1
        flag = False
        nx, ny = x + dx, y + dy
        
        while True:
            cnt += 1
        
            if not in_range(nx, ny) or grid[nx][ny] != target:
                break
             
            if cnt == 5:
                if in_range(x - dx, y - dy) and grid[x - dx][y - dy] == target:
                    break
                if in_range(nx + dx, ny + dy) and grid[nx + dx][ny + dy] == target:
                    break
                print(target)
                print(x + 1 + dx * 2, y + 1 + dy * 2)
                exit(0)
            
            nx += dx
            ny += dy

for i in range(19):
    for j in range(19):
        if grid[i][j] != 0:
            simulate(i, j)