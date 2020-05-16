N = int(input())
loc = tuple(map(int, input().split()))


compressed = {}
loc_unique = list(set(loc[:]))
loc_unique.sort()

for i, j in enumerate(loc_unique):
    compressed[j] = i

for k in loc:
    print(compressed[k], end=' ')
