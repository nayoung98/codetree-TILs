# n, m, n * m 문자열
# 가로, 세로, 대각선 방향으로 도중에 방향으르 틀지 않고 인접하여 나오는 LEE의 개수 구하기

# 입력
n, m = map(int, input().split())
info = [list(input().strip()) for _ in range(n)]
cnt = 0
answer1 = 'LEE'
answer2 = 'EEL'

# 가로 확인 (행 방향)
for i in range(n):
    # 좌 -> 우
    for j in range(m - 2):
        chk = True
        for k in range(3):
            if info[i][j + k] != answer1[k]:
                chk = False   
        if chk:
            cnt += 1

    # 우 -> 좌
    for j in range(m - 3, -1, -1):
        chk = True
        for k in range(2, -1, -1):
            if info[i][j + k] != answer2[k]:
                chk = False 
        if chk:
            cnt += 1

# 세로 확인 (열 방향)
for i in range(m):
    # 위 -> 아래
    for j in range(n - 2):
        chk = True
        for k in range(3):
            if info[j + k][i] != answer1[k]:
                chk = False
        if chk:
            cnt += 1
    
    # 아래 -> 위
    for j in range(n - 3, -1, -1):
        chk = True
        for k in range(2, -1, -1):
            if info[j + k][i] != answer2[k]:
                chk = False
        if chk:
            cnt += 1

#  대각선 확인
# 정방향 (위 -> 아래)
for i in range(n - 2):
    # 좌상 -> 우하
    for j in range(m - 2):
        chk = True
        for k in range(3):
            if info[i + k][j + k] != answer1[k]:
                chk = False
        if chk:
            cnt += 1
    
    # 우상 -> 좌하
    for j in range(m - 3, -1, -1):
        chk = True
        for k in range(2, -1, -1):
            if info[i + k][j + k] != answer1[k]:
                chk = False
        if chk:
            cnt += 1

# 역방향 (아래 -> 위)
for i in range(n - 2):
    # 우하 -> 좌상
    for j in range(m - 2):
        chk = True
        for k in range(3):
            if info[i + k][j + k] != answer2[k]:
                chk = False
        if chk:
            cnt += 1
    
    # 좌하 -> 우상
    for j in range(m - 3, -1, -1):
        chk = True
        for k in range(2, -1, -1):
            if info[i + k][j + k] != answer2[k]:
                chk = False
        if chk:
            cnt += 1

print(cnt)
