# n * n 격자, 1이상 100 이하의 숫자
# 기울어진 직사각형: 대각선으로 움직이며 반시계 순회, 1 -> 2 -> 3 -> 4, 각 방향으로 최소 1번은 움직여야 함, 이동 도중 격자 밖으로 넘어가면 안됨
# 출력: 기울어진 직사각형들 중 숫자들의 합이 최대인 값

# 입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]

# 범위 내 인지 확인 
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 직사각형 만들기 ((x, y): 시작 위치, width = 긴 변, height = 짧은 변) 
def make_rect(x, y, w, h):
    sum_of_nums = 0
    for i in range(4):
        if i % 2 == 0:
            for _ in range(w):
                nx, ny = x + dxs[i], y + dys[i]
                if in_range(nx, ny):
                    sum_of_nums += grid[nx][ny]
                    x, y = nx, ny
                else:
                    return 0
        else:
            for _ in range(h):
                nx, ny = x + dxs[i], y + dys[i]
                if in_range(nx, ny):
                    sum_of_nums += grid[nx][ny]
                    x, y = nx, ny
                else:
                    return 0
    return sum_of_nums

# 출력
max_nums = 0
for i in range(n):
    for j in range(n):
        for w in range(1, n):
            for h in range(1, n):
                sum_of_nums = make_rect(i, j, w, h)
                max_nums = max(max_nums, sum_of_nums)
print(max_nums)