# n개의 수 중 서로 다른 3개의 수를 골랐을 때, carry가 전혀 발생하지 않으면서 나올 수 있는 수의 합의 최댓값
# carry : 수와 수를 더했을 때, 10의 자리는 넘너가는 것, 각 자리수를 모두 더했을 때 10 이상이 되는 경우가 전혀 없어야 함

# 입력
n = int(input())
nums = [int(input()) for _ in range(n)]
cnt = 0

# carry인지 확인하기
def isnot_carry(a_info, b_info, c_info):
    # 각 자리수를 더하면서 carry인지 검사
    chk, result = False, []
    for i in range(5):
        result.append(a_info[i] + b_info[i] + c_info[i])

    for num in result:
        if num >= 10:
            chk = True
            break
    
    if not chk:
        return True # 캐리 발생 안함
    return False # 캐리 발생
    
# 서로 다른 3개의 수 고르기
result = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a_info, b_info, c_info= [], [], []
            a, b, c = nums[i], nums[j], nums[k]
            
            # 만, 천, 백, 십, 일
            a_info.extend((a//10000, a%10000//1000, a%1000//100, a%100//10, a%10))
            b_info.extend((b//10000, b%10000//1000, b%1000//100, b%100//10, b%10))
            c_info.extend((c//10000, c%10000//1000, c%1000//100, c%100//10, c%10))

            # 캐리 검사
            if isnot_carry(a_info, b_info, c_info):
                result.append(a + b + c)

if result:
    print(max(result))
else:
    print(-1)