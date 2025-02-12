# 사람 한 명을 빈 자리에 앉히려고 할 때, 가장 멀리 있는 사람 간의 간격을 최소화
# 1. 가장 멀리 떨어진 1을 고르기
# 2. 새로운 1을 가운데에 두고 최대 간격을 최소화
# 3. 가장 먼 1 간의 간격을 시뮬레이션 

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
