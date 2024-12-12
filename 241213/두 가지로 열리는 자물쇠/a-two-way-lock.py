# 1 ~ N 숫자 (원형으로 된 자물쇠) -> 총 3자리
# 모든 자리에 대해 첫 번째 조합과 거리가 2 이내 or 
# 모든 자리에 대해 두 번째 조합과 거리가 2 이내

n = int(input())
# 첫 번째 조합
comb_1 = list(map(int, input().split()))
# 두 번째 조합
comb_2 = list(map(int, input().split()))

def chk_dist(i, j, k, comb):
    if (abs(i - comb[0]) <= 2 or abs(i - comb[0]) == (n - 1) or abs(i - comb[0]) == (n - 2)) and \
        (abs(j - comb[1]) <= 2 or abs(j - comb[1]) == (n - 1) or abs(j - comb[1]) == (n - 2)) and \
        (abs(k - comb[2]) <= 2 or abs(k - comb[2]) == (n - 1) or abs(k - comb[2]) == (n - 2)):
        return True
    else:
        return False

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if chk_dist(i, j, k, comb_1) or chk_dist(i, j, k, comb_2):
                cnt += 1
print(cnt)