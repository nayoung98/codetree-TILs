# 두 직사각형이 겹치는지에 대한 여부
# 겹치지 않는 경우 -> 그 외를 제외하고 나머지

# 첫 번째 직사각형
x1, y1, x2, y2 = map(int, input().split())
# 두 번째 직사각형
a1, b1, a2, b2 = map(int, input().split())

if (x2 < a1) or (a2 < x1) or (b2 < y1) or (y2 < b1):
    print('nonoverlapping')
else:
    print('overlapping')