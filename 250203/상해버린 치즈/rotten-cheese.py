# n명의 사람, m개의 치즈
# 하나의 치즈가 상함
# 특정 사람이 어떤 지즈를 언제 먹었는지 -> d
# 특정 사람이 언제 확실이 아팠는지 (다른 사람도 아플 수 있음) -> s
# 상한 치즈를 먹은 사람에게 약을 복용시킬 때, 필요한 약의 최대 개수

# 입력
n, m, d, s = map(int, input().split())
eat_info = [tuple(map(int, input().split())) for _ in range(d)]
sick_info = [tuple(map(int, input().split())) for _ in range(s)]

# sick_info로 상한 치즈 정보 추리기
cheese = [0] * (m + 1) # 1-idx
for (p, t) in sick_info:
    for i in range(d):
        if eat_info[i][0] == p and eat_info[i][2] <= (t - 1):
            idx = eat_info[i][1]
            cheese[idx] += 1

cheese_info = []
for idx, item in enumerate(cheese):
    if item >= 1:
        cheese_info.append(idx)

# eat_info로 상한 치즈 먹은 사람 추리기
ans = [0] * (m + 1)
for item in cheese_info:
    for (p, m, t) in eat_info:
        if m == item:
            ans[item] += 1

# 상한 치즈 먹은 사람의 최댓값
print(max(ans))
