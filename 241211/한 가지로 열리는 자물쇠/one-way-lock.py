# 1~n 까지 숫자를 중복해서 뽑아 3자리수 만들기
# 한 자리라도 주어지는 조합과 거리가 2 이내면 열림 
# n, 조합
n = int(input())
a, b, c = map(int, input().split())

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if abs(a - i) <= 2 or abs(b - j) <= 2 or abs(c - k) <= 2:
                cnt += 1

# 자물쇠가 열리는 서로 다른 조합의 수
print(cnt)