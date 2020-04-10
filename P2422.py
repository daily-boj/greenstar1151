space = [[0 for j in range(201)] for i in range(201)]

N, M = map(int, input().split())
for a in range(M):
    x, y = map(int, input().split())
    space[x][y] = 1
    space[y][x] = 1

combination = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        if space[i][j] == 1:
            continue
        for k in range(j+1, N+1):
            if (space[j][k] or space[i][k]) == 1:
                continue
            combination += 1
print(combination)
