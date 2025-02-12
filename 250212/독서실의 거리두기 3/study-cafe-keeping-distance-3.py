# 좌석 간의 거리
# 새로 한 명 -> 좌석 간 거리 최대가 되도록 위치
# 양쪽 끝자리는 항상 사람이 앉아있음

# 입력
n = int(input())
strings = input()

# 사람이 앉은 좌석 위치 구하기
chk = []
for i, item in enumerate(strings):
    if item == '1':
        chk.append(i + 1)

# 가장 먼 간격 구하기
max_distance = 0
for i in range(len(chk) - 1):
    tmp_distance = abs(chk[i] - chk[i + 1])
    max_distance = max(max_distance, tmp_distance)

chk_max = []
for i in range(len(chk) - 1):
    tmp_distance = abs(chk[i] - chk[i + 1])

    if tmp_distance == max_distance:
        chk_max.append((chk[i], chk[i + 1]))

# 가장 먼 간격의 가운데 위치 시키기
a, b = chk_max[0]

idx = int((a + b)/2)
strings = list(strings)
strings[idx - 1] = '1'
strings = ''.join(strings)

# 가장 가까운 거리 구하기
chk = []
for i, item in enumerate(strings):
    if item == '1':
        chk.append(i + 1)

min_distance = 1000
for i in range(len(chk) - 1):
    tmp_distance = abs(chk[i] - chk[i + 1])
    min_distance = min(min_distance, tmp_distance)
print(min_distance)
