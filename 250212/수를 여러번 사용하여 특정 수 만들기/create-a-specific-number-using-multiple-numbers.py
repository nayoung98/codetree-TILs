# 서로 다른 세 정수: a, b, c
# a와 b를 더해서 만들 수 있는 c 이하의 수 중 가장 큰 값

# 입력
a, b, c = map(int, input().split())
max_result = 0

for i in range(1000):
    for j in range(1000):
        result = a * i + b * j

        if result <= c:
            max_result = max(max_result, result)
        else:
            break

print(max_result)