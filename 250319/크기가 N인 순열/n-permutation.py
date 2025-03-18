# 1부터 n까지의 수를 한번씩만 사용해 만들 수 있는 가능한 모든 수열
n = int(input())
visited = [False] * (n + 1)
answer = []

def choose(curr_num):
    if curr_num == n + 1:
        print(*answer)
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)
        choose(curr_num + 1)

        answer.pop()
        visited[i] = False

# 실행
choose(1)