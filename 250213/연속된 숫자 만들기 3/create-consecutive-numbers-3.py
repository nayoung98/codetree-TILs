# 세 사람의 위치, 
# 양 끝쪽에 있는 사람 중 한 사람을 선택해 남은 두 사람 사이로 이동시켜 연속된 숫자가 되도록
# 최대 이동 횟수

arr = list(map(int, input().split()))
arr.sort()

if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
    print(0)
elif arr[1] - arr[0] == 1 or arr[2] - arr[1] == 1:
    print(3)
else:
    print(2)