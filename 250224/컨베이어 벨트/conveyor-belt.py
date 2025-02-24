# # 시계 방향으로 한 칸씩 회전하는 컨베이어 벨트
# # 1초에 한 칸씩 움직임

# 입력
n, t = map(int, input().split())
belt_up = list(map(int, input().split()))
belt_down = list(map(int, input().split()))

for _ in range(t):
    # 사라지는 원소들
    tmp_up = belt_up[n - 1]
    tmp_down = belt_down[n - 1]

    # 한 칸씩 이동
    for i in range(n - 1, 0, -1):
        belt_up[i] = belt_up[i - 1]
        belt_down[i] = belt_down[i - 1]
    
    # 옮겨담기
    belt_up[0] = tmp_down
    belt_down[0] = tmp_up

print(*belt_up)
print(*belt_down)