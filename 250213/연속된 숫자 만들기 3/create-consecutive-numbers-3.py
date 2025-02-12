# 세 사람의 위치, 
# 양 끝쪽에 있는 사람 중 한 사람을 선택해 남은 두 사람 사이로 이동시켜 연속된 숫자가 되도록
# 최대 이동 횟수

arr = list(map(int, input().split()))
arr.sort()

# 두 사람 간의 차이 중 '최댓값 - 1' 만큼 움직이게 될 떄 최대임
max_diff = max(arr[1] - arr[0], arr[2] - arr[1])
print(max_diff - 1)