from collections import deque

# 입력
l, n, q = map(int, input().split()) # 체스판 크기, 기사들 수, 왕의 명령 수
grid = [list(map(int, input().split())) for _ in range(l)] # 0: 빈칸, 1: 함정, 2: 벽
knight_info = [list(map(int, input().split())) for _ in range(n)] # (r, c): 시작 위치, 1-idx, h: 세로 길이, w: 가로 길이, k: 초기 체력
command = [tuple(map(int, input().split())) for _ in range(q)] # i: 기사의 번호 (이미 사라진 기사일수도 있음), d: 방향 (0=위, 1=오, 2=아, 3=왼)

# 방향: 상, 우, 하, 좌
drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]

# 초기 체력
knight_life = [0] * n 

# 체스판 위 기사 정보
chk_grid = [[-1] * l for _ in range(l)]

# 초기 기사 정보 수정 (0-idx), 체력 저장
for idx, (r, c, h, w, k) in enumerate(knight_info):
    r, c = r - 1, c - 1
    knight_info[idx][:2] = r, c
    knight_info[idx].append(False) # 이동 여부 표시용
    knight_life[idx] = k 
    for x in range(r, r + h):
        for y in range(c, c + w):
            chk_grid[x][y] = idx

# 격자 내 검사
def in_range(nr, nc, h, w):
    return 0 <= nr < l and \
            0 <= nc < l and \
            0 <= nr + h - 1 < l and \
            0 <= nc + w - 1 < l

# 이동 여부 검사 (격자 내 & 벽 x)
def can_go(nr, nc, h, w):
    if not in_range(nr, nc, h, w):
        return False
    for x in range(nr, nr + h):
        for y in range(nc, nc + w):
            if grid[x][y] == 2:
                return False
    return True

# 연쇄 밀리는 기사 찾기
def find_knights(start_idx, d):
    q = deque()
    visited = set()
    q.append(start_idx)
    visited.add(start_idx)

    while q:
        idx = q.popleft()
        r, c, h, w = knight_info[idx][:4] # 밀리는 애들 정보
        nr, nc = r + drs[d], c + dcs[d]

        for x in range(nr, nr + h):
            for y in range(nc, nc + w):
                if not (0 <= x < l and 0 <= y < l):
                    continue
                other = chk_grid[x][y]
                if other != -1 and other not in visited:
                    visited.add(other)
                    q.append(other)
    
    return visited

# 명령 처리
for i, d in command:
    i -= 1

    # 사라진 기사라면 무시
    if knight_info[i][4] <= 0:
        continue
    
    move_targets = find_knights(i, d)

    # 이동 가능 여부 확인
    can_move_all = True
    for idx in move_targets:
        r, c, h, w, k, _ = knight_info[idx]
        nr, nc = r + drs[d], c + dcs[d]
        if not can_go(nr, nc, h, w):
            can_move_all = False
            break
    
    if not can_move_all:
        continue
    
    # 이동 및 피해 처리
    for idx in move_targets:
        r, c, h, w, k, _ = knight_info[idx]
        nr, nc = r + drs[d], c + dcs[d]
        knight_info[idx][:2] = nr, nc
        knight_info[idx][-1] = True # 이동 표시

        # 명령 받은 기사는 피해 x
        if idx != i:
            damage = 0
            for x in range(nr, nr + h):
                for y in range(nc, nc + w):
                    if grid[x][y] == 1:
                        damage += 1
            knight_info[idx][4] -= damage

    # 체스판 상태 갱신
    chk_grid = [[-1] * l for _ in range(l)]
    for idx, (r, c, h, w, k, chk) in enumerate(knight_info):
        if k <= 0:
            continue
        for x in range(r, r + h):
            for y in range(c, c + w):
                chk_grid[x][y] = idx

# 생존한 기사들의 총 데미지 출력
result = 0
for i in range(n):
    if knight_info[i][4] <= 0:
        continue
    result += (knight_life[i] - knight_info[i][4])
print(result)