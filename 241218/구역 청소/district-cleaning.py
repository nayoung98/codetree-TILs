# A: x = a ~ x = b
# B: x = c ~ x = d
# 총 몇 구역이나 청소 됐는지 출력

# A의 청소 구역
a, b = map(int, input().split())
# B의 청소 구역
c, d = map(int, input().split())

cleaning = [0] * 101

for i in range(a, b + 1):
    cleaning[i] = 1

for i in range(c, d + 1):
    cleaning[i] = 1

ans = 0
# 안겹치는 경우
if b < c or d < a:
    for area in cleaning:
        if area != 0:
            ans += 1
# 겹치는 경우
else:
    for area in cleaning:
        if area != 0:
            ans += 1
    ans -= 1

print(ans)