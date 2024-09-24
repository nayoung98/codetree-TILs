import sys

input = sys.stdin.readline
Y, M, D = map(int, input().split())

def is_leaf_year(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            return False
        return True
    return False

def is_valid_date(Y, M, D):
    if M < 1 or M > 12:
        return False

    month_days = [0, 31, 29 if is_leaf_year(Y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return 1 <= D <= month_days[M]

def get_sesson(M):
    if 3 <= M <= 5:
        return "Spring"
    elif 6 <= M <= 8:
        return "Summer"
    elif 9 <= M <= 11:
        return "Fall"
    else:
        return "Winter"

if is_valid_date(Y, M, D):
    print(get_sesson(M))
else:
    print(-1)