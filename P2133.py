#(예능)ALTAWAY

def sp(i):
    if i == 2:
        return 3
    else:
        return 2

def threeNtiles(n):
    if n % 2 == 1:
        return 0
    elif n == 2:
        return 3
    k = 0
    for i in range(2, n, 2):
        k += threeNtiles(n - i) * sp(i)
    return k + 2

tiles = [-1]

for n in range(1, 31):
    tiles.append(threeNtiles(n))

#tiles = [-1, 0, 3, 0, 11, 0, 41, 0, 153, 0, 571, 0, 2131, 0, 7953, 0, 29681, 0, 110771, 0, 413403, 0, 1542841, 0, 5757961, 0, 21489003, 0, 80198051, 0, 299303201]


N = int(input())


print(tiles[N])
