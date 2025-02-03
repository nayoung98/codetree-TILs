# 입력 
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 삼각형 넓이 구하기
def get_area(i, j, k):

    x1, y1 = points[i]
    x2, y2 = points[j]
    x3, y3 = points[k]
    
    return 1/2 * abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))


# 축에 평행한지 확인하기
def is_parallel(i, j, k):
    x_chk, y_chk = False, False

    x1, y1 = points[i]
    x2, y2 = points[j]
    x3, y3 = points[k]

    if (x1 - x2 == 0) or (x2 - x3 == 0) or (x3 - x1 == 0):
        x_chk = True
    
    if (y1 - y2 == 0) or (y2 - y3 == 0) or (y3 - y1 == 0):
        y_chk = True
    
    if x_chk and y_chk:
        return True
    else:
        return False

# 완전 탐색: 3개 고르기
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 축에 평행한지 확인하고 넓이 구하기
            if is_parallel(i, j, k):
                area = get_area(i, j, k)
                ans = max(ans, area)
            
print(int(ans * 2))