import sys

input = sys.stdin.readline
A = input().rstrip()
B = input().rstrip()

cnt = 0
while True:
    A = A[-1] + A[:-1]
    # print(A)
    cnt += 1

    if cnt == len(A):
        cnt = -1
        break
    
    if A == B:
        break

print(cnt)