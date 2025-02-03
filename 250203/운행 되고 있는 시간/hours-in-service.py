# n명의 개발자 중 1명 제외할 때, '운행 되고 있는 시간'이 최대가 되도록 선택
# '운행 되고 있는 시간': 적어도 한 명이상 일하는 경우

# 입력
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)] # 일하는 시간 (A, B)

# 운행 되고 있는 시간 체크
def chk_time(cnt):
    time = 0
    for i in range(len(cnt)):
        if cnt[i] >= 1:
            time += 1
    return time

# 완전 탐색
ans = 0
for i in range(n):
    cnt = [0] * 1001
    for j in range(n):
        if j == i:
            continue

        a, b = info[j]
        for k in range(a, b):
            cnt[k] += 1

    time = chk_time(cnt)
    ans = max(ans, time) 

print(ans)