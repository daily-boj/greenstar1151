N = int(input())

tiles = [1, 2]
for i in range(2, 1000001):
    tiles.append((tiles[i-2] + tiles[i-1]) % 15746)

print(tiles[N-1])
