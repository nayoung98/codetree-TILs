import sys

input = sys.stdin.readline
m1, d1, m2, d2 = map(int, input().split())
A = input().rstrip()

if A == 'Mon':
    ans = 1
elif A == 'Tue':
    ans = 2
elif A == 'Wed':
    ans = 3
elif A == 'Thu':
    ans = 4
elif A == 'Fri':
    ans = 5
elif A == 'Sat':
    ans = 6
elif A == 'Sun':
    ans = 7

chk = 1
cnt = 0 

def chk_month(m1):
    if m1 == 2:
        return 29
    elif m1 == 1 or m1 == 3 or m1 == 5 or m1 == 7 or m1 == 8 or m1 == 10 or m1 == 12:
        return 31
    else:
        return 30

while True:
    d1 += 1
    chk += 1

    if d1 == chk_month(m1):
        m1 += 1
        d1 = 1

    if m1 == m2 and d1 == d2:
        break

print(chk//ans)