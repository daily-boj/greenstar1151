def Rev(x):
    x_sting = str(x)
    return int(x_sting[::-1])


X, Y = map(int, input().split())


print(Rev(Rev(X) + Rev(Y)))
