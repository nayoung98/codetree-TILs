# 1이상 k이하의 숫자 하나 고르는 행위를 n번 반복하여 나올 수 있는 순서쌍 구하기
# 연속하여 같은 숫자가 3번 이상 나오는 경우는 제외

# 입력
k, n = map(int, input().split())
seleted_nums = []

# 연속된 3개의 숫자인지 확인
def check_nums(seleted_nums):
    for i in range(len(seleted_nums) - 2):
        if seleted_nums[i] == seleted_nums[i + 1] and \
            seleted_nums[i + 1] == seleted_nums[i + 2]:
            return True
    return False

# 1이상 k이하의 숫자 하나 고르는 행위를 n번 반복
def choose(cnt):
    # 종료 조건
    if cnt == n + 1:
        if not check_nums(seleted_nums):
            print(*seleted_nums)
        return

    # 재귀 호출 (같은 숫자 3번 연속 나오지 않아야 함)
    for num in range(1, k + 1):
        seleted_nums.append(num)
        choose(cnt + 1)
        seleted_nums.pop()

# 실행
choose(1)