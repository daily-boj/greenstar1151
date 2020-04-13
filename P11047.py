N, K = map(int, input().split())
coin = []
for _ in range(N): coin.append(int(input()))
coincount = 0

coin.sort(reverse=True)
for i in coin:
    if i > K:
        continue
    while i <= K:
        coincount += K // i
        K = K % i

print(coincount)
