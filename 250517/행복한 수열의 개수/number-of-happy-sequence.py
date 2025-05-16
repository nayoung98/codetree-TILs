# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 경우
answer = 0

# 각 행마다 수열 체크 (한 줄씩 돌면서 같은 원소인지 확인하기)
for i in range(n):
    cnt = 1
    for j in range(n - 1):
        if grid[i][j] == grid[i][j + 1]:
            cnt += 1
    if cnt >= m:
        answer += 1

# 각 열마다 수열 체크
for j in range(n):
    cnt = 1
    for i in range(n - 1):
        if grid[i][j] == grid[i + 1][j]:
            cnt += 1

    if cnt >= m:
        answer += 1

print(answer)