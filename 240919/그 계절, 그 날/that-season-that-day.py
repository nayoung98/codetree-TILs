import sys

input = sys.stdin.readline
Y, M, D = map(int, input().split())

def weather(Y, M, D):
    if Y % 4 == 0:
        Y = 0 # 윤년
    elif (Y % 4 == 0) and (Y % 100 == 0):
        Y = 1 # 윤년 x
    elif (Y % 4 == 0) and (Y % 100 == 0) and (Y % 400 ==0):
        Y = 0 # 윤년
    else:
        Y = 1 # 윤년 x

    if (M == 1) or (M == 3) or (M == 5) or (M == 7) or (M == 8) or (M == 10) or (M == 12):
        if D >= 1 and D <= 31:
            if M >= 3 and M <= 5:
                result = 'Spring'
            elif M >= 6 and M <= 8:
                result = 'Summer'
            elif M >= 9 and M <= 11:
                result = 'Fall'
            elif M == 12 or M == 1 or M == 2:
                result = 'Winter'
        else:
            result = -1
    else:
        if (M == 2) and (Y == 0):
            if D >= 1 and D <= 29:
                result = 'Winter'
            else:
                result = -1
        elif (M == 2) and (Y == 1):
            if D >= 1 and D <= 28:
                result = 'Winter'
            else:
                result = -1
        elif D >= 1 and D <= 30:
            if M >= 3 and M <= 5:
                result = 'Spring'
            elif M >= 6 and M <= 8:
                result = 'Summer'
            elif M >= 9 and M <= 11:
                result = 'Fall'
            elif M == 12 or M == 1 or M == 2:
                result = 'Winter'
        else:
            result = -1

    return result

print(weather(Y, M, D))