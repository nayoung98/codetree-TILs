from collections import deque

## 1. 입력 받기
n, t = map(int, input().split())
# 신봉 음식 (T: 민트, C: 초코, M: 우유)
F = [list(input().strip()) for _ in range(n)]
# 초기 신앙심
B = [list(map(int, input().split())) for _ in range(n)]

## 2. 아침: 신앙심 += 1
def morning_routine():
    for i in range(n):
        for j in range(n):
            B[i][j] += 1

## 3. 점심: 신봉 음식이 같은 인접 학생들 그룹핑 -> 대표자 선정 -> 신앙심 계산
### 신봉 음식이 같은 인접 학생들 찾아서 그룹핑
q = deque()
visited = [[False] * n for _ in range(n)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def same_food(x, y, nx, ny):
    return F[x][y] == F[nx][ny]

def can_go(nx, ny): # 격자 내 & 방문 x & 신봉 음식 같음
    return in_range(nx, ny) and not visited[nx][ny]

def bfs():
    students = []
    while q:
        x, y = q.popleft()
        students.append((B[x][y], x, y))
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny) and same_food(x, y, nx, ny):
                # 그룹핑
                q.append((nx, ny))
                visited[nx][ny] = True
                students.append((B[nx][ny], nx, ny))
    # 중복 제거
    students = list(set(students))
    return students

presidents = []
def afternoon_routine(i, j):
    global presidents
    # 신봉 음식이 같은 인접 학생들 찾아서 그룹핑
    q.append((i, j))
    visited[i][j] = True
    students = bfs()

    # 대표자 선정하기
    students = sorted(students, key=lambda x: (-x[0], x[1], x[2]))
    _, pr, pc = students[0]  # 대표자의 신앙심, 대표자의 행 번호, 대표자의 열 번호

    # 신앙심 계산
    B[pr][pc] += (len(students) - 1)
    for idx, (_, r, c) in enumerate(students):
        if idx == 0:
            continue
        B[r][c] -= 1
    presidents.append([-1, B[pr][pc], pr, pc, False]) # 전파 우선순위, 신앙심, 행, 열, 전파 받았는지 체크용

## 4. 저녁: 신앙 전파 순서 정하기 (그룹 내 -> 그룹 외) -> 전파 순서 대로 전파자 결정 (전파자의 간절함, 전파 방향 결정) -> 전파 방향으로 한 칸씩 이동하며 전파 시도 (격자 밖이거나, 간절함이 0이면 전파 종료, 신봉음식이 다르면 전파 안함) -> 강한 전파(음식 단일화, 간절함 감소(이때 간절함이 0이 되면 전파 종료), 신앙심 증가) or 약한 전파(음식 합치기, 간절함 0, 신앙심 증가)
### 신앙 전파 순서 정하기 (그룹 내 -> 그룹 외)
# 각 대표자들의 우선 순위 정하기 (단일 음식 -> 이중 조합 -> 삼중 조합)
def get_rank(pr, pc):
    if F[pr][pc] == 'T' or F[pr][pc] == 'C' or F[pr][pc] == 'M':
        return 1
    elif F[pr][pc] == 'CM' or F[pr][pc] == 'TM' or F[pr][pc] == 'TC':
        return 2
    else: # TCM
        return 3

### 전파자 결정: 간절함, 전파 방향
def get_xd(pr, pc):
    # 간절함 = 신앙심 - 1
    x = B[pr][pc] - 1
    # 전파 방향
    d = B[pr][pc] % 4
    # # 신앙심 = 1
    # B[pr][pc] = 1

    return x, d

# 음식 합치기 (민트: T, 초코: C, 우유: M, 초코우유: CM, 민트우유: TM, 민트초코: TC, 민트초코우유: TCM)
def get_food(tmp_food):
    priority = {'T': 0, 'C': 1, 'M': 2}
    return ''.join(sorted(set(''.join(tmp_food)), key=lambda x: priority[x]))

### 전파할 방향으로 한 칸씩 이동하면서 전파 시도 (종료 조건: 격자 밖 or 간절함 == 0)
def night_routine():
    phase = 1
    for i, (_, _, pr, pc, pchk) in enumerate(presidents):
        # print(f'phase: {phase}, ({pr}, {pc}, {pchk})')
        x, d = get_xd(pr, pc)
        # print(d)
        origin_food = F[pr][pc] # 전파자의 원래 음식
        # 전파를 당한 대표자는 방어상태가 되어 당일에는 전파 불가능
        if pchk:
            continue
        # 신앙심 = 1
        B[pr][pc] = 1
        while True:
            nr, nc = pr + dxs[d], pc + dys[d]

            # 격자 밖이면 전파 종료
            if not in_range(nr, nc):
                break

            # 간절함 == 0이면 전파 종료
            if x == 0:
                break

            # 전파 여부 확인 (전파 대상이 전파자와 신봉 음식이 같으면 pass, 다르면 전파 진행)
            if origin_food == F[nr][nc]:
                pr, pc = nr, nc # 한 칸 이동
                # flag = False
                continue

            # 전파 진행되는 경우, 강한 전파 or 약한 전파 확인
            y = B[nr][nc]

            if x > y: # 강한 전파: 전파자와 동일한 음식, x -= (y + 1), 전파자의 신앙심 += 1
                F[nr][nc] = origin_food
                x -= (y + 1)
                B[nr][nc] += 1
            else: # 약한 전파: 음식 합치기, x = 0, 신앙심 += x
                tmp_food = [F[nr][nc], origin_food]
                F[nr][nc] = get_food(tmp_food)
                B[nr][nc] += x
                x = 0

            for idx, (_, _, ir, ic, _) in enumerate(presidents):
                if i == idx: # 같은 대표자는 패스
                    continue
                if nr == ir and nc == ic: # 전파를 당한 대표자는 방어상태
                    presidents[idx][-1] = True

            # 한 칸 이동
            pr, pc = nr, nc

        # print(B)
        # print(F)
        phase += 1

def print_food():
    TCM, TC, TM, CM, M, C, T = 0, 0, 0, 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if F[i][j] == 'TCM':
                TCM += B[i][j]
            elif F[i][j] == 'TC':
                TC += B[i][j]
            elif F[i][j] == 'TM':
                TM += B[i][j]
            elif F[i][j] == 'CM':
                CM += B[i][j]
            elif F[i][j] == 'M':
                M += B[i][j]
            elif F[i][j] == 'C':
                C += B[i][j]
            elif F[i][j] == 'T':
                T += B[i][j]
    print(TCM, TC, TM, CM, M, C, T)

## 5. 2~4를 t만큼 반복
for _ in range(t):
    # print(f'Day: {_ + 1}')
    # 아침 실행
    morning_routine()

    # 대표자 초기화
    presidents = []
    visited = [[False] * n for _ in range(n)]
    # 점심 실행
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                afternoon_routine(i, j)
    # 저녁 실행
    # 그룹 외: 음식에 따른 우선순위 저장
    for idx, (_, _, pr, pc, _) in enumerate(presidents):
        presidents[idx][0] = get_rank(pr, pc)

    # 그룹 내: 신앙심 높 > 행 작 > 열 작
    presidents.sort(key=lambda x: (x[0], -x[1], x[2], x[3]))

    # 저녁 실행
    night_routine()

    # pchk 하루 지나면 다시 False로 초기화
    for i in range(len(presidents)):
        presidents[i][-1] = False

    # 출력
    print_food()

