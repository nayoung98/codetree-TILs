# n개의 숫자
# 특정 구간 내 원소들의 평균값이 그 구간의 원소 중 하나가 되는 가짓수 구하기
n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n): # 구간의 시작점
    for j in range(i, n): # 구간의 끝점
        # 구간 [i, j] 내 원소의 합
        tmp_sum = 0
        for k in range(i, j + 1):
            tmp_sum += arr[k]
        tmp_sum /= (j - i + 1)
        
        chk = False
        for k in range(i, j + 1):
            if tmp_sum == arr[k]:
                chk = True
            
        if chk:
            cnt += 1

print(cnt)  