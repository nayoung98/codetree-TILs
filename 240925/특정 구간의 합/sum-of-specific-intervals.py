import sys

input = sys.stdin.readline
n, m = map(int, input().split())

A = []


def sum_range(a1, a2):
    return sum(A[a1-1 : a2])

A = list(map(int, input().split()))

for _ in range(m):
    a1, a2 = map(int, input().split())
    result = sum_range(a1, a2)
    print(result)