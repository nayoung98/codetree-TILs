# n개의 선분
# 서로 다른 3개의 선분 제거, 남은 n - 3개끼리 모두 겹치지 않도록 하는 가짓수 출력

# 입력
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 겹치는지 찾기
def is_overlapped(i, j, k):
    chks = [0] * 10 
    for l in range(n):
        if l in [i, j, k]:
            continue
        
        a, b = segments[l]
        for m in range(a, b + 1):
            chks[m] += 1
    
    flag = [False] * 10
    for idx, chk in enumerate(chks):
        if chk < 2:
            flag[idx] = True            
    
    if False in flag:
        return False
    else:
        return True

# 서로 다른 3개의 선분 제거하는 완전 탐색 
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if is_overlapped(i, j, k):
                cnt += 1
            
print(cnt)