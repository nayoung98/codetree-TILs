# L * L 크기 체스판 (왼쪽 상단: (1, 1), 1-idx, 빈칸, 함정, 벽)
# 왕실의 기사들 초기 위치: (r,c) -> 방패: (r, c)를 좌측 상단으로 한 h * w 크기의 직사각형 형태, 각 기사의 체력: k
## 1. 기사 이동
### 상하좌우 중 하나로 한 칸 이동
### 이동하려면 위치에 다른 기사가 있다면 그 기사도 함께 연쇄적으로 한 칸 밀려남, ...
### 기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동 불가능
### 체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없음
## 2. 대결 대미지
### 명령을 받은 기사가 다른 기사를 밀치게 되면, 밀려난 기사들은 피해를 입음 
### 해당 기사가 이동한 곳에서 w * h 직사각형 내에 놓여있는 함정의 수만큼 체력이 깎임, 현재 체력 이상의 데미지를 받으면 사라짐
### 명령을 받은 기사는 피해 x, 기사들이 모두 밀린 이후에 대미지
### 밀쳐진 위치에 함정이 전혀 없다면 피해를 전혀 받지 않음

# 출력: Q번의 대결이 모두 끝난 후 생존한 기사들이 총 받은 대미지의 합

# 입력
l, n, q = map(int, input().split()) # 체스판 크기, 기사들 수, 왕의 명령 수
grid = [list(map(int, input().split())) for _ in range(l)] # 0: 빈칸, 1: 함정, 2: 벽
knight_info = [list(map(int, input().split())) for _ in range(n)] # (r, c): 시작 위치, 1-idx, h: 세로 길이, w: 가로 길이, k: 초기 체력
command = [tuple(map(int, input().split())) for _ in range(q)] # i: 기사의 번호 (이미 사라진 기사일수도 있음), d: 방향 (0=위, 1=오, 2=아, 3=왼)
knight_life = [0] * n

# 처음 시작시 0-idx로 바꾸기
for idx, (r, c, h, w, k) in enumerate(knight_info):
    r, c = r - 1, c - 1
    knight_info[idx][:2] = r, c
    knight_info[idx].append(False)
    knight_life[idx] = k # 초기 체력 저장

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

# 왕의 명령에 따라 움직이기
drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]
for i, d in command:
    i -= 1
    flag = True
    chk_grid = [[-1] * l for _ in range(l)]

    for idx, (r, c, h, w, k, chk) in enumerate(knight_info):
        nr, nc = r + drs[d], c + dcs[d]
        knight_info[idx][-1] = False

        # 기사의 현재 위치 저장
        for x in range(r, r + h):
            for y in range(c, c + w):
                chk_grid[x][y] = idx

        if not can_go(nr, nc, h, w):
            flag = False
        
        # 하나라도 이동 불가능하면 멈춤
        if not flag:
            break

    # 이동 시키기
    if flag:

        # 미는 기사(i)의 이동 반경 내 있는지 확인
        chk_list = []
        r, c, h, w = knight_info[i][:4]
        nr, nc = r + drs[d], c + dcs[d]

        for x in range(nr, nr + h):
            for y in range(nc, nc + w):
                if chk_grid[x][y] != -1:
                    chk_list.append(chk_grid[x][y])
        
        chk_list.append(i) # 본인 추가
        chk_list = list(set(chk_list))

        for idx in chk_list:
            r, c, h, w, k, chk = knight_info[idx][:]
            nr, nc = r + drs[d], c + dcs[d]

            knight_info[idx][:2] = nr, nc
            chk = True
            knight_info[idx][-1] = chk

            # 이동한 기사의 체력 계산
            if i != idx and chk: # 미는 기사는 영향 x
                for x in range(nr, nr + h):
                    for y in range(nc, nc + w):
                        k -= grid[x][y]
                knight_info[idx][4] = k

    # print(knight_info)

# 생존한 기사들만 대미지 계산
result = 0
for i, (_, _, _, _, k, _) in enumerate(knight_info):
    if k == 0:
        continue
    result += (knight_life[i] - k)
    # print

print(result)
