import sys
text = sys.stdin.read()

while 'BUG' in text:
    text = text.replace('BUG', '')

print(text)
