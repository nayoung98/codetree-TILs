import sys

input = sys.stdin.readline
a, b = map(int, input().split())

def calculator(a, b):
    if a < b:
        a += 10
        b *= 2
    elif a > b:
        a *= 2
        b += 10

    print(a, b)

calculator(a, b)