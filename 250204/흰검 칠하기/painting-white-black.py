# 일직선으로 나열된 타일
# n번에 걸쳐 명령에 따라 움직임
# x L : 왼쪽 이동, 현재 위치 포함 총 x칸을 흰색으로 칠함
# x R : 오른쪽 이동, 현재 위치 포함 총 x칸을 검은색으로 칠함
# 각 명령이후에는 마지막으로 칠한 타일에 위치
# 타일 하나가 흰색, 검은색 각각 2번 이상 칠해지면 회색
# 흰색, 검은색, 회색 타일 수 출력

# 입력
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
black_tiles, white_tiles, tmp_tiles = [0] * 201, [0] * 201, [0] * 201 # 1-idx

# 초기 위치
tmp = 100 

# 움직이는 함수
def simulate(x, d):
    global tmp

    if d == 'R':
        for i in range(tmp, tmp + x):
            black_tiles[i] += 1
            tmp_tiles[i] = 'B'
        tmp += (x - 1)
    
    else: # 'L'
        for i in range(tmp, tmp - x, -1):
            white_tiles[i] += 1
            tmp_tiles[i] = 'W'
        tmp -= (x - 1)
    
# 시뮬레이션
for (x, d) in commands:
    x = int(x)
    simulate(x, d)

# 타일 개수 카운팅
white, black, gray = 0, 0, 0
for i in range(201):
    if black_tiles[i] >= 2 and white_tiles[i] >= 2:
        gray += 1
    elif not (black_tiles[i] >= 2 and white_tiles[i] >= 2) and tmp_tiles[i] == 'B':
        black += 1
    elif not (black_tiles[i] >= 2 and white_tiles[i] >= 2) and tmp_tiles[i] == 'W':
        white += 1

print(white, black, gray)
