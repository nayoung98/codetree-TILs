# n명의 개발자들
# T번에 걸쳐 t초에 x와 y가 악수를 나눈다
# 1명의 개발자가 K번의 악수 동안 전염병을 옮김 -> 그 이후부터는 걸려있지만 옮기지 않음
# 최종적으로 누가 전염병에 걸리는지 출력 # 0: 음성, 1: 양성

# 입력 
n, k, p, T = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(T)] # (t, x, y)

# 시간 순 정렬
info.sort(key=lambda x:x[0])

# 감염 결과
result = [0] * n # 0-idx
result[p - 1] = 1 # 처음 걸린 사람

# 감염 횟수
cnt = [k] * n

# 시간 순 악수
for (t, x, y) in info:    

    # 감염자가 x인 경우
    if x == p or result[x - 1] == 1:
        if cnt[x - 1] > 0:
            result[y - 1] = 1
            cnt[x - 1] -= 1

    # 감염자가 y인 경우
    if y == p or result[y - 1] == 1:
        if cnt[y - 1] > 0:
            result[x - 1] = 1
            cnt[y - 1] -= 1
    
print(*result, sep='')