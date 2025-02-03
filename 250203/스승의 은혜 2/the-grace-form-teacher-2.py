# n명의 학생, B만큼의 예산
# 학생 i가 원하는 선물의 가격: P(i)
# 선물 하나를 반값으로 할인 가능
# 선생님이 선물 가능한 학생의 최대 명수

# 입력
n, b = map(int, input().split())
prices = [int(input()) for _ in range(n)]
prices = sorted(prices)
ans = 0 

# 완전탐색 -> 선물 하나씩 반값으로 
for i in range(n):
    prices[i] /= 2
    budget, cnt = prices[i], 1

    # 예산에서 가능한 최대 학생 수
    for j in range(n):
        if j == i:
            continue

        budget += prices[j]
        cnt += 1
        
        if budget > b:
            budget -= prices[j]
            cnt -= 1
        
    prices[i] *= 2
    ans = max(ans, cnt)
            
print(ans)