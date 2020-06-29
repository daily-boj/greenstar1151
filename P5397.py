import collections
import sys


Tcount = int(input())
keylog_in = sys.stdin.read().rstrip()
keylog = tuple(keylog_in.split('\n'))


cursor_L = collections.deque()
cursor_R = collections.deque()

for T in keylog:
    for K in T:
        if K == '<':
            try:
                cursor_R.appendleft(cursor_L.pop())
            except:
                pass
        elif K == '>':
            try:
                cursor_L.append(cursor_R.popleft())
            except:
                pass
        elif K == '-':
            try:
                cursor_L.pop()
            except:
                pass
        else:
            cursor_L.append(K)
    else:
        print(''.join(cursor_L) + ''.join(cursor_R))
        cursor_L.clear()
        cursor_R.clear()
