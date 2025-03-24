# 정수 n, 4가지 연산의 횟수를 최소화하여 1 만들기 (-1, +1, //2, //3)
# 출력: 1을 만들기 위해 필요한 최소 연산 횟수
from collections import deque

# 입력
n = int(input())
q = deque()
time = [0] * (n + 1)
visited = [False] * (n + 1)

def bfs():
    while q:
        x = q.popleft()
        if x == 1:
            return
        if x % 2 == 0 and not visited[x//2]:
            q.append(x//2)
            visited[x//2] = True
            time[x//2] = time[x] + 1
        if x % 3 == 0 and not visited[x//3]:
            q.append(x//3)
            visited[x//3] = True
            time[x//3] = time[x] + 1
        if not visited[x - 1]:
            q.append(x - 1)
            visited[x - 1] = True
            time[x - 1] = time[x] + 1
        if x != n and not visited[x + 1]:
            q.append(x + 1)
            visited[x + 1] = True
            time[x + 1] = time[x] + 1

# 실행
q.append(n)
visited[n] = True
bfs()
print(time[1])