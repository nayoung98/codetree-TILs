# 2차원 격자 위에서 여러 객체를 이동
# m개의 구슬을 동시에 인접한 4개의 칸 중 가장 큰 값이 적혀있는 곳으로 이동 -> t번 반복
## 우선순위: 상하좌우
## 이동할 수 있는 위치가 없는 경우 움직이지 않음
# 이동 후, 2개 이상의 구슬이 같은 칸에 오면 충돌이 생겨 해당 칸의 구슬은 모두 사라짐
# 출력: t번 구슬들을 동시에 움직인 후 남아있는 구슬의 수

# 입력 (격자의 크기, 구슬의 개수, 시간)
n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
info = [tuple(map(int, input().split())) for _ in range(m)] # 1-idx
cnt = [[0] * n for _ in range(n)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1,  1]

# 구슬의 위치 기록
for x, y in info:
    x -= 1
    y -= 1
    cnt[x][y] += 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# m개의 구슬이 서로 다른 곳에서 상하좌우로 동시에 움직임
def move_marbles():
    global cnt
    # next_cnt 초기화
    next_cnt = [[0] * n for _ in range(n)]

    # 격자 내 구슬이 있으면, next_cnt 내 해당 구슬의 다음 위치에 1 증가
    for i in range(n):
        for j in range(n):
            if cnt[i][j] == 1:
                max_num, x, y = 0, i, j
                
                # 4군데 살피면서 가장 값이 클 때를 저장
                for idx in range(4):
                    nx, ny = x + dxs[idx], y + dys[idx]
                    if not in_range(nx, ny):
                        continue

                    # 큰 숫자일 때 이동하고, 그때의 방향벡터 인덱스 저장
                    num = grid[nx][ny]

                    if max_num < num:
                        max_num = num
                        max_idx = idx
                
                # 가장 큰 곳으로 이동
                x, y = x + dxs[max_idx], y + dys[max_idx]
                next_cnt[x][y] += 1
    
    # 움직인 후, 충돌이 일어난 구슬 지우기
    cnt = next_cnt
    for i in range(n):
        for j in range(n):
            if cnt[i][j] >= 2:
                cnt[i][j] = 0

# 실행
for _ in range(t):
    move_marbles()

# 출력
result = 0
for i in range(n):
    for j in range(n):
        if cnt[i][j] == 1:
            result +=1
print(result)

