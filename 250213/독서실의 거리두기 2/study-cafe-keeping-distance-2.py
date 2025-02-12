# 새로운 한 명을 배치한 후, 최대한의 거리두기를 실행한 간격 출력
import math
# 입력
n = int(input())
strings = list(input())
length = len(strings)

# 양 끝이 모두 1인 경우
# 연속된 0의 개수 확인
cnt = 0
result = []
for i in range(length - 1):
    if strings[i] == '0' and strings[i] == strings[i + 1]:
        cnt += 1
    else:
        if cnt != 0:
            result.append((i + 1, cnt + 1))
        cnt = 0

answer = []

for b, num in result:
    # 1시작점(a), 1끝점(b)
    a = b - (num + 1)
    if strings[a] == '1' and strings[b] == '1':
        answer.append(int(math.ceil(num / 2)))

# 둘 중 한 끝이 1인 경우 
cnt = 0
result2 = []
if strings[0] == '0' and strings[length - 1] == '1':
    for i in range(length - 1):
        if strings[i] == strings[i + 1]:
            cnt += 1
        else:
            if cnt != 0:
                answer.append(cnt + 1)
            cnt = 0
            break
if strings[0] == '1' and strings[length - 1] == '0':
    for i in range(length - 1, -1, -1):
        if strings[i - 1] == strings[i]:
            cnt += 1
        else:
            if cnt != 0:
                answer.append(cnt + 1)
            cnt = 0
            break
print(max(answer))