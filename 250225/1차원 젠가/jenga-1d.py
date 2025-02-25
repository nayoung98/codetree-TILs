# n개의 층으로 이루어진 1차원 젠가
# 2번에 걸쳐 특정 구간의 블럭들을 빼는 작업
# 출력: 블럭을 두 번 빼는 과정을 거친 이후의 결과 출력

# 입력
n = int(input())
blocks = list(int(input()) for _ in range(n))

# 제거할 블록의 정보 (1-idx)
info = [tuple(map(int, input().split())) for _ in range(2)]

def remove_blocks(s, e):
    tmp = []

    # info의 정보에 따라 블럭 빼기
    for i in range(s, e + 1):
        blocks[i] = 0

    # 0이 아닌 값들을 tmp에 저장하기
    for i in range(n):
        if blocks[i] != 0:
            tmp.append(blocks[i])
    for _ in range(len(blocks) - len(tmp)):
        tmp.append(0)
    
    # tmp 값을 다시 원래 배열에 저장학
    for i in range(n):
        blocks[i] = tmp[i]

# 실행 
for (s, e) in info:
    # info는 0-idx로 바꾸기
    s -= 1
    e -= 1

    # 블럭 빼기
    remove_blocks(s, e)

# 남아있는 블럭의 개수 세기
cnt = 0
result = []
for i in range(n):
    if blocks[i] != 0:
        cnt += 1
        result.append(blocks[i])

# # 출력
if cnt != 0:
    print(cnt)
    print(*result, sep='\n')
else: 
    print(cnt)