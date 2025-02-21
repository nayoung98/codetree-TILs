# 완전탐섹 -> 시간 복잡도를 계산해보고, 시간초과가 나지 않을 것 같으면 항상 적용 
## for문 기반 구현, backtracking 기반 구현

# n * n 격자 -> 동전 있으면 1, 없으면 0
# 3 * 3 격자 -> 해당 범위 안에 들어있는 동전의 개수가 최대

# 입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 범위 확인 
def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def chk_coin(row_s, col_s, row_e, col_e):
    tmp_coin = 0
    
    for i in range(row_s, row_e + 1):
        for j in range(col_s, col_e + 1):
            if in_range(i, j):
                tmp_coin += grid[i][j]
    
    return tmp_coin
            
max_coin = 0
for i in range(n):
    for j in range(n):
        tmp_coin = chk_coin(i, j, i + 2, j + 2)
        max_coin = max(max_coin, tmp_coin)

print(max_coin)