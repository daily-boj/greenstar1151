def fourNtiles(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 5
    k = 4 * fourNtiles(n-2) + fourNtiles(n-1)
    for i in range(3, n+1):
        if i % 2 == 1:
            k += 2 * fourNtiles(n - i)
        else:
            k += 3 * fourNtiles(n - i)
    return k

tiles = [-1]

loop = 1
while True:
    fn = fourNtiles(loop)
    if fn > 2147483647:
        break
    else:
        pass
    tiles.append(fn)
    loop += 1

#tiles = [-1, 1, 5, 11, 36, 95, 281, 781, 2245, 6336, 18061, 51205, 145601, 413351, 1174500, 3335651, 9475901, 26915305, 76455961, 217172736, 5901, 26915305, 76455961, 217172736, 616891945, 1752296281]


T = int(input())

    
for _ in range(T):
    print(tiles[int(input())])
