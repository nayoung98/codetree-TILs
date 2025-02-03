# n명의 학생, B만큼의 예산
# 학생 i가 원하는 선물의 가격: P(i)
# 선물 하나를 반값으로 할인 가능
# 선생님이 선물 가능한 학생의 최대 명수

# 입력
n, b = map(int, input().split())
prices = [int(input()) for _ in range(n)]
ans = 0 

# 완전탐색 -> 선물 하나씩 반값으로 
for i in range(n):
    prices[i] /= 2

    # 예산에서 가능한 최대 학생 수
    for j in range(n):
        budget, cnt = 0, 0
        for k in range(n):
            if k == j:
                continue

            budget += prices[k]
            cnt += 1
            
            if cnt > b:
                budget -= prices[k]
                cnt -= 1
    
    prices[i] *= 2
    ans = max(ans, cnt)
            
print(ans)