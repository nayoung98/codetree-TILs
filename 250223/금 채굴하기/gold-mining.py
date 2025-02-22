# n * n 크기 격자
# 최대한 많은 금 채굴
# 채굴 -> 마름모 모양 (특정 중심점을 기준으로 k번 이내로 상하좌우의 인접한 곳으로 이동하는 걸 반복), k=0: 한곳에서만 채굴!
# 채굴에 드는 비용 -> k^2 + (k + 1)^2
# 금 한 개의 가격 -> m
# 출력: 손해를 보지 않으면서 채굴할 수 있는 가장 많은 금의 개수 -> 채굴에 드는 비용 < 금의 총 가격

# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

# 범위 확인
def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def find_gold(x, y, k):
    gold = grid[x][y]
    tmp_x = x
    tmp_k = k

    # 가운데줄
    for dx, dy in zip(dxs, dys):
        for i in range(1, k + 1):
            nx, ny = x + i * dx, y + i * dy
            if in_range(nx, ny):
                # grid[nx][ny] = 1
                gold += grid[nx][ny]

    # 윗줄
    while True:
        x -= 1
        k -= 1

        if k < 0:
            break

        for idx in range(2):
        # for dx, dy in zip(dxs, dys):
            for i in range(1, k + 1):
                nx, ny = x + i * dxs[idx], y + i * dys[idx]
                if in_range(nx, ny):
                    # grid[nx][ny] = 1
                    gold += grid[nx][ny]
         
    # 아랫줄
    x = tmp_x 
    k = tmp_k 
    while True:
        x += 1
        k -= 1

        if k < 0:
            break

        for idx in range(2):
        # for dx, dy in zip(dxs, dys):
            for i in range(1, k + 1):
                nx, ny = x + i * dxs[idx], y + i * dys[idx]
                if in_range(nx, ny):
                    # grid[nx][ny] = 1
                    gold += grid[nx][ny]
    
    return gold

# 비용 계산
def find_cost(k):
    return k**2 + (k + 1)**2

# 격자 안에서 시뮬레이션 
# k를 바꿔가며 완전탐색
max_gold = 0 
for k in range(n + 1):
    for i in range(n):
        for j in range(n):
            gold = find_gold(i, j, k)
            # 손해보는지 확인
            if find_cost(k) <= gold * m: 
                max_gold = max(max_gold, gold)

print(max_gold)