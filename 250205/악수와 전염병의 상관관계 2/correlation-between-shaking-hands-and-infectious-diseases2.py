# n명의 개발자들
# T번에 걸쳐 t초에 x와 y가 악수를 나눈다
# 1명의 개발자가 K번의 악수 동안 전염병을 옮김 -> 그 이후부터는 걸려있지만 옮기지 않음
# 최종적으로 누가 전염병에 걸리는지 출력 # 0: 음성, 1: 양성

# 입력 
n, k, p, T = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(T)] # (t, x, y)

# 시간 순 정렬
info.sort(key=lambda x:x[0])

# 결과
result = [0] * n # 0-idx

# 시간 순 악수
for (t, x, y) in info:
    if k > 0:
        if x == p or y == p or result[x - 1] == 1 or result[y - 1] == 1:
            k -= 1
            result[x - 1] = 1
            result[y - 1] = 1
            
print(*result, sep='')