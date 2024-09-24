m1, d1, m2, d2 = map(int, input().split())
day = input()
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_dict = {days:idx for idx, days in enumerate(days)}
idx = days_dict[day]

def calcDate(m, d):
    sum2 = 0
    for i in range(1, m):
        if i >= 8:
            if i % 2 == 0:
                sum2 += 31
            else:
                sum2 += 30
        else:
            if i % 2 == 0:
                if i == 2:
                    sum2 += 29
                else:
                    sum2 += 30
            else:
                sum2 += 31
    sum2 += d
    return sum2

sum1 = calcDate(m1, d1)
sum2 = calcDate(m2, d2)

sum0 = sum2-sum1

count = sum0//7
if sum0%7 >= idx:
    count += 1

print(count)