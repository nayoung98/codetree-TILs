# 정수 n, 4가지 연산의 횟수를 최소화하여 1 만들기 (-1, +1, //2, //3)
# 출력: 1을 만들기 위해 필요한 최소 연산 횟수
from collections import deque

# 입력
n = int(input())
q = deque()
time = [0] * 4000004 # 10000001 * 4(연산 종류)
visited = [False] * 4000004

def push(nx, x):
    q.append(nx)
    visited[nx] = True
    time[nx] = time[x] + 1

def bfs():
    while q:
        x = q.popleft()

        if x == 1:
            return

        if x % 2 == 0 and not visited[x//2]:
            push(x//2, x)

        if x % 3 == 0 and not visited[x//3]:
            push(x//3, x)

        if not visited[x - 1]:
            push(x- 1, x)

        if not visited[x + 1]:
            push(x + 1, x)

# 실행
q.append(n)
visited[n] = True
bfs()
print(time[1])