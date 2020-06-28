X, Y, W, S = map(int, input().split())


b = (X + Y) * W
d = min(X, Y) * S + abs(X - Y) * W
if (X + Y) % 2 == 0:
    a = max(X, Y) * S
    print(min(a, b, d))
else:
    c = (max(X, Y) - 1) * S + W
    print(min(b, c, d))
