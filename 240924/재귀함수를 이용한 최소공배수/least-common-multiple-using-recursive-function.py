import sys

input = sys.stdin.readline
n = int(input())

num_list = input().split()
num_list = [int(num) for num in num_list]

def gcd(n, m):

    while m:
        n, m = m, n % m

    return n

def lcm(n, m):

    return (n * m) // gcd(n, m)

def lcm_recursive(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return lcm(num_list[0], lcm_recursive(num_list[1:]))

print(lcm_recursive(num_list))