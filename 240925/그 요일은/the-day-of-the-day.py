import sys

input = sys.stdin.readline
m1, d1, m2, d2 = map(int, input().split())
A = input().rstrip()

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
target_day_idx = days.index(A)

current_day_idx = 0 
current_month = m1
current_day = d1
cnt = 0

def chk_month(m1):
    if m1 == 2:
        return 29
    elif m1 == 1 or m1 == 3 or m1 == 5 or m1 == 7 or m1 == 8 or m1 == 10 or m1 == 12:
        return 31
    else:
        return 30

while not (current_month == m2 and current_day == d2 + 1):

    if current_day_idx == target_day_idx:
        cnt += 1

    current_day += 1
    current_day_idx = (current_day_idx + 1) % 7  

    if current_day > chk_month(m1):
        current_day = 1
        current_month += 1

print(cnt)