import math


N = int(input())


sidelength = math.floor(math.sqrt(N))
d = N - sidelength**2
if d == 0:
    if N == 1:
        print(4)
    else:
        print(4*(sidelength - 1))
elif d <= sidelength:
    if N == 2:
        print(4)
    else:
        print(4*sidelength - 2)
else:
    print(4*sidelength)
