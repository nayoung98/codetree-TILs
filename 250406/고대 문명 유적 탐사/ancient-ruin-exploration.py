############ 변수 정리 ############



from collections import deque

k, m = map(int, input().split()) # 탐사의 반복 횟수, 벽면에 적힌 유물 조각의 개수
grid = [list(map(int, input().split())) for _ in range(5)]
nums = list(map(int, input().split())) # 유물 조각들의 값

# grid값 따로 저장 해두기
init_grid = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        init_grid[i][j] = grid[i][j]

# bfs 관련 
q = deque()
visited = [[False] * 5 for _ in range(5)]

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def can_go(x, y):
    return in_range(x, y) and \
            not visited[x][y]

def bfs(num):
    # cnt: bfs의 depth (모이는 유물 조각의 개수)
    global grid

    # new_grid = [[0] * 5 for _ in range(5)]
    # for i in range(5):
    #     for j in range(5):
    #         new_grid[i][j] = grid[i][j]
    new_grid = [row[:] for row in grid]
    cnt = 0
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    positions = []

    while q:
        x, y = q.popleft()
        positions.append((x, y))
        cnt += 1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny) and grid[nx][ny] == num:
                # positions.append((nx, ny))
                # new_grid[x][y], new_grid[nx][ny] = 0, 0 # 유물 사라짐 (grid에 바로 저장하면 값이 바뀌니까 new_grid에 저장 해놓고 다시 옮기기)
                q.append((nx, ny))
                visited[nx][ny] = True
                # cnt += 1

    if cnt >= 3:
        for i, j in positions:
            grid[i][j] = 0
        # # new_grid의 값 저장
        new_grid = [row[:] for row in grid]
        # for i in range(5):
        #     for j in range(5):
        #         grid[i][j] = new_grid[i][j]
        return cnt # 해당 위치에서 (i, j) 유물의 개수
    else:
        return 0

# 같은 숫자 3개 있으면 연결 (유물 개수 cnt)
def count_nums(visited):
    result = 0
    for i in range(5):
        for j in range(5):
            # bfs 시작
            q.append((i, j))
            visited[i][j] = True
            num = grid[i][j] # 현재 숫자
            result += bfs(num)
    return result

def update_grid(init_grid):
    global grid, visited
    
    # 초기 배열(init grid)에 다시 옮겨 담기, 다시 bfs 수행을 위해 방문 배열 초기화
    for x in range(5):
        for y in range(5):
            grid[x][y] = init_grid[x][y]
    visited = [[False] * 5 for _ in range(5)]

# 3 * 3 격자 만들기
def make_tmpgrid(i, j):

    tmp_nums = [] # 3 * 3 격자에 들어갈 숫자
    tmp_grid = [[0] * 3 for _ in range(3)] # 3 * 3 격자 초기

    # 3 * 3 격자에 들어갈 숫자 뽑기
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            tmp_nums.append(grid[x][y])

    # 3 * 3 격자 만들기
    cnt = 0
    for x in range(3):
        for y in range(3):
            tmp_grid[x][y] = tmp_nums[cnt]
            cnt += 1

    return tmp_grid

# 3 * 3 격자 회전
def rotate_90(tmp_grid):
    rotated_grid = [[0] * 3 for _ in range(3)]
    # 90도 회전
    row = 0
    for y in range(3):
        col = 0
        for x in range(2, -1, -1):
            rotated_grid[row][col] = tmp_grid[x][y]
            col += 1
        row += 1
    return rotated_grid

def make_newgrid(i, j, rotated_grid):
    global grid

    # 격자에 다시 배치 시킴
    row = 0
    for x in range(i - 1, i + 2):
        col = 0
        for y in range(j - 1, j + 2):
            grid[x][y] = rotated_grid[row][col]
            col += 1
        row += 1

# 총 k번 반복
new_cnt = 0
answer = []
for _ in range(k):
    # print(f'phase: {_}')
    total_cnt = 0
    # print(grid)
    # 1. 탐사 진행
    results = []
    # 중심 좌표 선택
    for i in range(1, 4): # 1, 4
        for j in range(1, 4):
            tmp_grid = make_tmpgrid(i, j)
            ######### 3가지 각도로 회전 -> 각각의 회전에 따른 유물 개수 계산 #########
            ## 90도 회전
            rotated_grid = rotate_90(tmp_grid)
            make_newgrid(i, j, rotated_grid)
            # bfs 돌면서 유물 개수 저장
            visited = [[False] * 5 for _ in range(5)]

            results.append((count_nums(visited), 90, i, j))
            # 격자 초기화
            update_grid(init_grid)
            # update_grid()

            ## 180도 회전 -> 90도 회전 * 2
            rotated_grid = rotate_90(rotated_grid)
            make_newgrid(i, j, rotated_grid)
            visited = [[False] * 5 for _ in range(5)]

            results.append((count_nums(visited), 180, i, j))
            update_grid(init_grid)
            # update_grid()

            ## 270도 회전 -> 90도 회전 * 3
            rotated_grid = rotate_90(rotated_grid)
            make_newgrid(i, j, rotated_grid)
            visited = [[False] * 5 for _ in range(5)]

            results.append((count_nums(visited), 270, i, j))
            update_grid(init_grid)
            # update_grid()
            
    # 회전 목표에 맞게 정렬
    results.sort(lambda x: (-x[0], x[1], x[3], x[2]))
    # print(results)
    # 2. 유물 획득
    # 회전 결과 출력
    max_num, rotate, mx, my = results[0]
    # print(f'max_num, rotate, mx, my: {results[0]}')
    # 회전 했을 때 유물의 최대 개수가 0이면 더이상 진행 불가능하니까 멈춤
    if max_num == 0:
        answer.append(0)
        break
        
    # 회전 (격자 최종 업데이트)
    if rotate == 90:
        tmp_grid = make_tmpgrid(mx, my)
        rotated_grid = rotate_90(tmp_grid)
        make_newgrid(mx, my, rotated_grid)
    elif rotate == 180:
        tmp_grid = make_tmpgrid(mx, my)
        rotated_grid = rotate_90(rotate_90(tmp_grid))
        make_newgrid(mx, my, rotated_grid)
    else: # 270
        tmp_grid = make_tmpgrid(mx, my)
        rotated_grid = rotate_90(tmp_grid)
        rotated_grid = rotate_90(rotate_90(rotate_90(tmp_grid)))
        make_newgrid(mx, my, rotated_grid)

    # 유물 1차 획득
    visited = [[False] * 5 for _ in range(5)]
    tmp_num = count_nums(visited)  # 유물 사라짐
    total_cnt += tmp_num
    # print(f'tmp_num: {tmp_num}')
    # print(grid)
    # 새로운 조각 생기기
    for j in range(5):
        for i in range(4, -1, -1):
            if grid[i][j] == 0:
                grid[i][j] = nums[new_cnt]
                new_cnt += 1
  
    # 유물 연쇄 획득
    while True:
        # 원래 배열 저장해두고
        new_grid = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                new_grid[i][j] = grid[i][j]

        # 새로운 조각이 생긴 grid 검사
        visited = [[False] * 5 for _ in range(5)]
        tmp_num = count_nums(visited)
        total_cnt += tmp_num
        # print(f'tmp_num: {tmp_num}')
        # print(grid)
        if tmp_num == 0: # 유물 연쇄 획득 중단
            # 비워진 부분 다시 채워야됨 (유물의 조각으로 채우는게 아니고, 원래 값이 다시 들어가야됨)
            for i in range(5):
                for j in range(5):
                    grid[i][j] = new_grid[i][j]
            # 배열 업뎃
            for i in range(5):
                for j in range(5):
                    init_grid[i][j] = grid[i][j]
            answer.append(total_cnt)
            total_cnt = 0 
            # print(grid)
            break
        else:
            # 새로운 조각 생기기
            for j in range(5):
                for i in range(4, -1, -1):
                    if grid[i][j] == 0:
                        grid[i][j] = nums[new_cnt]
                        new_cnt += 1
            # print(grid)
# print(answer)
for ans in answer:
    if ans != 0:
        print(ans, end = ' ')
