# 폭탄 n개, 특정 거리 k, 폭탄을 나열한 순서
# 같은 번호가 부여된 폭탄끼리 거리가 k안에 있으면 폭발함
# 폭발할 폭탄 중에 부여된 번호가 가장 큰 번호를 출력, 없으면 -1

# 입력
n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

# 두 개씩 비교해서 같은 번호 찾는 완전 탐색
ans = []
chk = False
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] == nums[j] and abs(i - j) <= k:
            chk = True
            ans.append(nums[i])

if chk:
    print(max(ans))
else:
    print(-1)