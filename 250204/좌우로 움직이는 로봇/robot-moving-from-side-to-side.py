# 1초에 한칸씩 좌우로 움직이는 로봇 A, B
# A가 움직이는 횟수 n, B가 움직이는 횟수 m
# 로봇 A와 B가 바로 직전에 다른 위치에 있다가 그 다음 번에 같은 위치에 오게 되는 (마주치는) 경우의 수 구하기

# 입력
n, m = map(int, input().split())
a_info = [tuple(input().split()) for _ in range(n)] # (t, d), t: 움직이는 시간, d: 움직이는 거리
b_info = [tuple(input().split()) for _ in range(m)]

# 시간에 따른 로봇의 위치 기록
MAX_INT = 1000000

a_location, b_location = [0] * MAX_INT, [0] * MAX_INT
a_chk, b_chk = 0, 0

# 이동
def simulate(tmp, time, location, chk):
    chk += t
    if d == 'R':
        for _ in range(t):
            time += 1
            tmp += 1
            
            location[time] = tmp
    else: # 'L'
        for _ in range(t):
            time += 1
            tmp -= 1

            location[time] = tmp
    
    return tmp, time, location, chk

# A 시뮬레이션
a_tmp, a_time, a_final = 0, 0, 0
for (t, d) in a_info:
    t = int(t)

    a_tmp, a_time, a_location, a_chk = simulate(a_tmp, a_time, a_location, a_chk)

# B 시뮬레이션 
b_tmp, b_time, b_final = 0, 0, 0
for (t, d) in b_info:
    t = int(t)

    b_tmp, b_time, b_location, b_chk = simulate(b_tmp, b_time, b_location, b_chk)

# A, B의 최종 위치 기록
max_chk = max(a_chk, b_chk)

a_final = a_tmp
for i in range(a_chk + 1, max_chk + 1):
    a_location[i] = a_final

b_final = b_tmp
for i in range(b_chk + 1, max_chk + 1):
    b_location[i] = b_final

# 시간에 따른 위치 겹치는지 확인
cnt = 0
for i in range(1, max_chk):
    if (a_location[i - 1] != b_location[i - 1]) and (a_location[i] == b_location[i]):
        cnt += 1
        
print(cnt) 