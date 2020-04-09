def a2i(a: str):
    return ord(a) - 65

N = int(input())
RPN = input()
numlist = []
for i in range(N): numlist.append(int(input()))

stack = []
for c in RPN:
    if c == '+': 
        t2 = stack.pop()
        t1 = stack.pop()
        stack.append(t1 + t2)
    elif c == '-':
        t2 = stack.pop()
        t1 = stack.pop()
        stack.append(t1 - t2)
    elif c == '*':
        t2 = stack.pop()
        t1 = stack.pop()
        stack.append(t1 * t2)
    elif c == '/':
        t2 = stack.pop()
        t1 = stack.pop()
        stack.append(t1 / t2)
    else: stack.append(numlist[a2i(c)])

print('%.2f' % stack[0])
