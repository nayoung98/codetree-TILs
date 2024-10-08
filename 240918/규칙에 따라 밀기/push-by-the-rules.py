import sys

input = sys.stdin.readline
A = input().rstrip()
rules = input().rstrip()
rule_cnt = 0

for rule in rules:
    if rule == 'L':
        rule_cnt -= 1
    else:
        rule_cnt += 1

rule_cnt %= len(A) # 문자열 보다 큰 경우 나머지 연산으로 길이 줄임
if rule_cnt < 0:
    rule_cnt = abs(rule_cnt)
    print(A[rule_cnt:] + A[:rule_cnt])
elif rule_cnt > 0:
    print(A[-rule_cnt:] + A[:-rule_cnt])
else:
    print(A)