# 1이상 k이하의 숫자를 하나 고르는 행위를 n번 반복
# 나올 수 있는 모든 서로 다른 순서쌍 구하기

# 입력
k, n = map(int, input().split())
nums = [i for i in range(1, k + 1)]
selected_nums = []

def print_nums(selected_nums):
    for num in selected_nums:
        print(num, end=' ')
    print()

# 현재 위치에서 1 ~ k 숫자 하나 고르기
def choose(curr_num):
    if curr_num == n:
        print_nums(selected_nums)
        return

    for select in range(1, k + 1):
        selected_nums.append(select)
        choose(curr_num + 1)
        selected_nums.pop()

choose(0)