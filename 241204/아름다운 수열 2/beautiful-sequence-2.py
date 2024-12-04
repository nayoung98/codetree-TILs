# n개의 숫자로 이루어진 수열 A
# m개의 숫자로 이루어진 수열 B 
# 아름다움 수열: 수열 B의 각 원소들의 순서를 바꿔 나오는 수열
# 수열 A에서 길이가 M인 연속 부분 수열 중 아름다운 수열의 개수

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# 가능한 모든 구간의 시작점을 정하여 완전탐색
cnt = 0 
for i in range(0, n - m + 1):
    if sorted(arr1[i:i+m]) == sorted(arr2):
        cnt += 1
    
print(cnt)