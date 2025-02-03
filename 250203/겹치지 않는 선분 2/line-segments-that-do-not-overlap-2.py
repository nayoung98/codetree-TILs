# n개의 선분, (x1, 0) ~ (x2, 1)
# 다른 선분과 전혀 겹치지 않는 선분의 수 출력

# 입력
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# # 겹치는지 확인
# def is_overlapped(i, j):
#     global cnt
    

    

# 완전 탐색 -> 2개씩 겹치는지 조사
cnt = 0
for i in range(n):
    for j in range(i + 1, n):

        x1, x2 = points[i]  
        x3, x4 = points[j]

        if x1 > x3 and x2 < x4:
            cnt += 1
        elif x1 < x3 and x2 > x4:
            cnt += 1

ans = n - 2 * cnt
if ans < 0:
    print(0)
else:
    print(ans)

# print(n - 2 * cnt)