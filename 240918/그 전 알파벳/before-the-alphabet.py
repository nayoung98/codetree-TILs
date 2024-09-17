import sys

input = sys.stdin.readline
text = input().rstrip()
text = ord(text)
# print(text)
if text == 97:
    result = 122
else:
    result = text-1
print(chr(result))