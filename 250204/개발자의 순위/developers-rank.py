# k번의 경기, n명의 개발자의 순위
# 항상 a번 개발자가 b번 개발자보다 더 높은 순위였던 서로 다른 (a, b)의 쌍 구하기

# 입력 
k, n = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(k)]

# 모든 (a, b) 쌍에 대해 완전 탐색
cnt = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            continue

        chk = [False] * k
        for idx, tmp in enumerate(info):
            # 인덱스 기준 검색
            if tmp.index(a) < tmp.index(b):
                chk[idx] = True

        if False in chk:
            continue
        else:
            cnt += 1

print(cnt)