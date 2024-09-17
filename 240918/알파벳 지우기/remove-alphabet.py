import sys

input = sys.stdin.readline
a = input().rstrip()
a = list(a)
b = input().rstrip()
b = list(b)

result_a = ''
result_b = ''

for text in a:
    if text.isdigit():
        result_a += text
result_a = int(result_a)

for text in b:
    if text.isdigit():
        result_b += text
result_b = int(result_b)

print(result_a + result_b)