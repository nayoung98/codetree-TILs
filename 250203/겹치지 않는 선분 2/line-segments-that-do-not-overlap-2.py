# n개의 선분, (x1, 0) ~ (x2, 1)
# 다른 선분과 전혀 겹치지 않는 선분의 수 출력

# 입력
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 겹치는지 확인
def is_overlapped(i, j):
    global cnt
    cnt = 0

    _, x = points[i]  
    _, y = points[j]

    if x > y:
        cnt += 1

# 완전 탐색 -> 2개씩 겹치는지 조사
for i in range(n):
    for j in range(i + 1, n):
        is_overlapped(i, j)
        
print(n - 2 * cnt)