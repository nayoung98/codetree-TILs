# 1이하 n이하의 숫자 중 m개의 숫자를 골라 만들 수 있는 모든 조합
# 출력: 한 조합 내 숫자들을 오름차순으로 정렬해 출력

# 입력
n, m = map(int, input().split())
selected_nums = []

# curr_num 위치에 숫자 뽑기
def choose(curr_num, cnt):
    # 종료 조건
    if curr_num == n + 1:
        if cnt == m: # 자리수
            print(*selected_nums)
        return
    
    # 재귀 호출
    selected_nums.append(curr_num)
    choose(curr_num + 1, cnt + 1)
    selected_nums.pop()
    choose(curr_num + 1, cnt)

# 실행
choose(1, 0)
