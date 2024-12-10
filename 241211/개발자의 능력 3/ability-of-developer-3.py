# 개발자 6명의 알고리즘 능력을 수치화 
# 6명 -> 3명/ 3명
# 팀원들의 능력 총합간의 차이를 최소화

power_list = list(map(int, input().split()))

def get_diff(i, j, k):
    sum1 = power_list[i] + power_list[j] + power_list[k]
    sum2 = sum(power_list) - sum1

    diff = abs(sum1 - sum2)

    return diff

min_power = 1000000 * 6
for i in range(len(power_list)):
    for j in range(i + 1, len(power_list)):
        for k in range(j + 1, len(power_list)):

            min_power = min(min_power, get_diff(i, j, k))

print(min_power)