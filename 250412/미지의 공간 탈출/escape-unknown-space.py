# 시작 공간에서 bfs로 어떻게 내려갈지를 결정하기 (평면 간 이동을 처리!)
# 시간 값을 미리 적어두고, 해당 칸에그 시간 보다 작으면 지나갈 수 있음
from pydoc import visiblename

N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr3 = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
wall = [list(map(int, input().split())) for _ in range(F)]

def find_3d_start():
    for i in range(M):
        for j in range(M):
            if arr3[4][i][j] == 2:
                return 4, i, j

def find_2d_end():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 4:
                arr[i][j] = 0
                return i, j

def find_3d_base():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                return i, j

def find_3d_end_2d_start():
    # 3차원 시작 좌표 찾기
    bi, bj = find_3d_base()

    # 3차원에서 2차원 연결 좌표 찾기
    for i in range(bi, bi + M):
        for j in range(bj, bj + M):

            if arr[i][j] != 3: # 3차원 위치가 아니면 넘어감
                continue

            if arr[i][j + 1] == 0: # 우측
                si, sj = i, j + 1
                ek_3d, ei_3d, ej_3d = 0, M - 1, (M - 1) - (i - bi)
                return ek_3d, ei_3d, ej_3d, si, sj
            elif arr[i][j - 1] == 0: # 좌측
                si, sj = i, j - 1
                ek_3d, ei_3d, ej_3d = 1, M - 1, i - bi
                return ek_3d, ei_3d, ej_3d, si, sj
            elif arr[i + 1][j] == 0: # 남측
                si, sj = i + 1, j
                ek_3d, ei_3d, ej_3d = 2, M - 1, j - bj
                return ek_3d, ei_3d, ej_3d, si, sj
            elif arr[i - 1][j] == 0: # 북
                si, sj = i - 1, j
                ek_3d, ei_3d, ej_3d = 3, M - 1, (M - 1) - (j - bj)
                return ek_3d, ei_3d, ej_3d, si, sj

    return -1  # 나갈 곳이 없음

# 1. 3d, 2d의 시작/종료 좌표 탐색 (3차원 시작, 3차원 끝, 2차원 시작, 2차원 끝 좌표 탐색)
sk_3d, si_3d, sj_3d = find_3d_start()
ei, ej = find_2d_end()
ek_3d, ei_3d, ej_3d, si, sj = find_3d_end_2d_start()
left_nxt = {0: 2, 2: 1, 1: 3, 3: 0}
right_nxt = {0: 3, 1: 2, 2: 0, 3: 1}

# # 3차원 격자 출력
# def my_print_3d(arr3):
#     for arr in arr3:
#         for lst in arr:
#             print(*lst)
#         print()
#     print()

from collections import deque
def bfs_3d(sk_3d, si_3d, sj_3d, ek_3d, ei_3d, ej_3d):
    q = deque()
    visited = [[[0] * M for _ in range(M)] for _ in range(5)]

    q.append((sk_3d, si_3d, sj_3d))
    visited[sk_3d][si_3d][sj_3d] = 1

    while q:
        ck, ci, cj = q.popleft()

        # 종료 조건
        if (ck, ci, cj) ==  (ek_3d, ei_3d, ej_3d):
            # print(arr3)
            return visited[ck][ci][cj]

        # 범위 내라면 이동, 범위 밖이면 다른 평면으로 이동 처리
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            # 범위 밖
            ## 위로 벗어난 경우
            if ni < 0:
                if ck == 0:
                    nk, ni, nj = 4, (M - 1) - cj, M - 1
                elif ck == 1:
                    nk, ni, nj = 4, cj, 0
                elif ck == 2:
                    nk, ni, nj = 4, M - 1, cj
                elif ck == 3:
                    nk, ni, nj = 4, 0, (M - 1) - cj
                else: # 4
                    nk, ni, nj = 3, 0, (M - 1) - cj
            elif ni >= M:
                if ck == 4:
                    nk, ni, nj = 2, 0, cj
                else:
                    continue # 막혀있어서 갈 수가 없어
            elif nj < 0: # 왼쪽으로 이탈
                if ck == 4:
                    nk, ni, nj = 1, 0, ci
                else:
                    nk, ni, nj = left_nxt[ck], ci, M - 1
            elif nj >= M: # 오른쪽으로 이탈
                if ck == 4:
                    nk, ni, nj = 0, 0, (M - 1) - ci
                else:
                    nk, ni, nj = right_nxt[ck], ci, 0
            else: # 범위 내
                nk = ck

            # 갈 수 있는지 확인
            if visited[nk][ni][nj] == 0 and arr3[nk][ni][nj] == 0:
                q.append((nk, ni, nj))
                visited[nk][ni][nj] = visited[ck][ci][cj] + 1 # 방문 기록과 거리를 동시에 저장
    return -1 # 경로 x

dis, djs = [0, 0, 1, -1], [1, -1, 0, 0] # 동, 서, 남, 북
def bfs_2d(visited, dist, si, sj, ei, ej): # dist: 초기 거리
    q = deque()
    q.append((si, sj))
    visited[si][sj] = dist # 3차원에서 탈출할 때 걸린 시간

    while q:
        ci, cj = q.popleft()

        # 종료 조건
        if (ci, cj) == (ei, ej):
            return visited[ci][cj]

        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            # 범위 내, 방문 안함, 시간 이상 현상 없음 (배수의 값이 아니어야 함)
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and visited[ci][cj] + 1 < visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1

    return -1 # 도착 못하는 경우

# 2. bfs_3d (경로가 없다면 -1 출력하고 종료), 평면 간 이동
dist = bfs_3d(sk_3d, si_3d, sj_3d, ek_3d, ei_3d, ej_3d) # 시작점부터 목표점까지

if dist != -1:
    # 시간 이상 현상 처리 (v에 시간 표시)
    visited = [[401] * N for _ in range(N)]
    for wi, wj, wd, wv in wall: # wv 단위로 wd 방향으로 확산 (출구가 아닌 경우만)
        visited[wi][wj] = 1
        for mul in range(1, N + 1):
            wi, wj = wi + dis[wd], wj + djs[wd]
            if 0 <= wi < N and 0 <= wj < N and arr[wi][wj] == 0 and (wi, wj) != (ei, ej): # 목적지가 아닌 경우만!
                visited[wi][wj] = wv * mul
            else:
                break
    # 3. bfs_2d (단, 이동 가능한 곳(확산 안된 곳)에서만 진행 가능)
    dist = bfs_2d(visited, dist, si, sj, ei, ej)

print(dist)