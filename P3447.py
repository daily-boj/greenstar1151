import sys
text_in = sys.stdin.readlines()



for s in text_in:
    print(s.replace('BUG', ''), end='')
