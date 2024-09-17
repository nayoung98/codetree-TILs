import sys

input = sys.stdin.readline
texts = input().rstrip()

for text in texts:
    if text.isupper():
        text = text.lower()
    else:
        text = text.upper()
    print(text,end='')

# print(texts)