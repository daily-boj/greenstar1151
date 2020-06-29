N, M = map(int, input().split())


count = 0
count += N
while True:
    bundle = N//M
    if bundle < M:
        count += bundle
        break
    else:
        count += bundle
        N = bundle
print(count)