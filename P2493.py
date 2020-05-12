N = int(input())
towers = tuple(map(int, input().split()))


stack = []

for index, tower in enumerate(towers):
    while stack != []:
        if stack[-1][1] < tower:
            stack.pop()
        else:
            print(stack[-1][0], end=' ')
            stack.append((index + 1, tower))
            break
    else:
        print(0, end=' ')
        stack.append((index + 1, tower))
