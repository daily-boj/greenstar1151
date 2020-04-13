n, q = map(int, input().split())
seq = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        handleL = query[1] - 1
        handleR = query[2]
        print(sum(seq[handleL:handleR]))
        seq[handleL], seq[handleR - 1] = seq[handleR - 1], seq[handleL]
    elif query[0] == 2:
        a, b, c, d = query[1] - 1, query[2], query[3] - 1, query[4]
        print(sum(seq[a:b]) - sum(seq[c:d]))
