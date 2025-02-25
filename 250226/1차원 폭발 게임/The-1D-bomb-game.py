# n개의 폭탄 
# m개 이상 연속으로 같은 숫자가 적혀있는 폭탄들은 전부다 폭발 -> 중력에 의해 위에 있던 폭탄들은 밑으로 떨어짐
# m개 이상 연속한 숫자를 갖는 폭탄들이 존재하지 않을 때까지 반복

# 입력
n, m = map(int, input().split())
bombs = list(int(input()) for _ in range(n))
memory = [1 for _ in range(101)]

def remove_bomb(): 
    location = []

    # m개 이상의 폭탄이 있는지 검사
    for i in range(n - 1):
        if bombs[i] == bombs[i + 1]:
            memory[bombs[i]] += 1
            location.append((i, bombs[i]))
            location.append((i + 1, bombs[i]))

    # 폭탄 터짐 (0으로 해당 자리 채우기)
    bomb_list = []
    for i in range(101):
        if memory[i] >= m:
            bomb_list.append(i)

    for num in bomb_list:
        for (i, bomb) in location:
            if bomb == num:
                bombs[i] = 0

    # 아래로 떨어짐
    tmp = []
    for i in range(n):
        if bombs[i] != 0:
            tmp.append(bombs[i])

    # 원래 배열로 옮기기
    for _ in range(n - len(tmp)):
        tmp.append(0)

    for i in range(n):
        bombs[i] = tmp[i]


# 실행      
result = []
for _ in range(100):
    if m == 1:
        flag = False
    else:
        remove_bomb()
        flag = True
        
for i in range(n):
    if bombs[i] != 0 and flag:
        result.append(bombs[i])

# 출력
if len(result) != 0:
    print(len(result))
    print(*result, sep='\n')
else:
    print(0)