# 개발자 두명
# 가위바위보: 1, 2, 3 (어떤 숫자가 무엇을 나타내는지 정해지지 않음)
# 첫 번째 개발자가 이기는 횟수가 최대가 되도록

# 입력
# 가위바위보를 한 횟수, 서로 어떤 것을 냈는지
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]

# 첫번째 개발자가 이기는 쌍 (가위 = S, 보 = P, 바위 = R)
win_first = [('S', 'P'), ('P', 'R'), ('R', 'S')]

# 가위바위보와 숫자 매칭시키기
# Case 1. 가위, 바위, 보
def case1(a, b):
    if a == 1:
        a = 'S'
    elif a == 2:
        a = 'R'
    else:
        a = 'P'

    if b == 1:
        b = 'S'
    elif b == 2:
        b = 'R'
    else:
        b = 'P'
    return a, b

# Case 2. 가위, 보, 바위
def case2(a, b):
    if a == 1:
        a = 'S'
    elif a == 2:
        a = 'P'
    else:
        a = 'R'

    if b == 1:
        b = 'S'
    elif b == 2:
        b = 'P'
    else:
        b = 'R'
    return a, b

# Case 3. 바위, 가위, 보
def case3(a, b):
    if a == 1:
        a = 'R'
    elif a == 2:
        a = 'S'
    else:
        a = 'P'

    if b == 1:
        b = 'R'
    elif b == 2:
        b = 'S'
    else:
        b = 'P'
    return a, b

# Case 4. 바위, 보, 가위
def case4(a, b):
    if a == 1:
        a = 'R'
    elif a == 2:
        a = 'P'
    else:
        a = 'S'

    if b == 1:
        b = 'R'
    elif b == 2:
        b = 'P'
    else:
        b = 'S'
    return a, b

# Case 5. 보, 가위, 바위
def case5(a, b):
    if a == 1:
        a = 'P'
    elif a == 2:
        a = 'S'
    else:
        a = 'R'

    if b == 1:
        b = 'P'
    elif b == 2:
        b = 'S'
    else:
        b = 'R'
    return a, b

# Case 6. 보, 바위, 가위
def case6(a, b):
    if a == 1:
        a = 'P'
    elif a == 2:
        a = 'R'
    else:
        a = 'S'

    if b == 1:
        b = 'P'
    elif b == 2:
        b = 'R'
    else:
        b = 'S'
    return a, b

result, cnt = 0, 0
for a, b in info:
    a, b = case1(a, b)
    for chk_a, chk_b in win_first:
        if chk_a == a and chk_b == b:
            cnt += 1
result = max(result, cnt)

cnt = 0
for a, b in info:
    a, b = case2(a, b)
    for chk_a, chk_b in win_first:
        if chk_a == a and chk_b == b:
            cnt += 1
result = max(result, cnt)

cnt = 0
for a, b in info:
    a, b = case3(a, b)
    for chk_a, chk_b in win_first:
        if chk_a == a and chk_b == b:
            cnt += 1
result = max(result, cnt)

cnt = 0
for a, b in info:
    a, b = case4(a, b)
    for chk_a, chk_b in win_first:
        if chk_a == a and chk_b == b:
            cnt += 1
result = max(result, cnt)

cnt = 0
for a, b in info:
    a, b = case5(a, b)
    for chk_a, chk_b in win_first:
        if chk_a == a and chk_b == b:
            cnt += 1
result = max(result, cnt)

cnt = 0
for a, b in info:
    a, b = case6(a, b)
    for chk_a, chk_b in win_first:
        if chk_a == a and chk_b == b:
            cnt += 1
result = max(result, cnt)

print(result)
