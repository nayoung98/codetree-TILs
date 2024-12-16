# 개발자 6명 -> 2명/2명/2명
# 팀원들의 능력 총합이 가장 큰 팀과 가장 작은 팀의 차이를 최소화
# 이 차이를 출력

power_list = list(map(int, input().split()))

def diff(i, j, k, l):
    sum1 = power_list[i] + power_list[j]
    sum2 = power_list[k] + power_list[l]
    sum3 = sum(power_list) - sum1 - sum2

    ret = abs(sum1 - sum2)
    ret = max(ret, abs(sum2 - sum3))
    ret = max(ret, abs(sum3 - sum1))

    return ret

min_sum = 1000000
# 첫 번째 팀원 
for i in range(len(power_list)):
    for j in range(i + 1, len(power_list)):

        # 두 번째 팀원 
        for k in range(len(power_list)):
            for l in range(k + 1, len(power_list)):
                
                if k == i or k == j or l == i or l == j:
                    continue

                min_sum = min(min_sum, diff(i, j, k, l))

print(min_sum)