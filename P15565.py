import sys


N, K = map(int, input().split())
dolls = sys.stdin.readline().rstrip().split()


if dolls.count('1') < K:
    print(-1)
else:
    lion_index = [i for i, n in enumerate(dolls) if n == '1']
    lion_min = []
    for i in range(len(lion_index) - K + 1):
        lion_min.append(lion_index[i + K - 1] - lion_index[i] + 1)
    else:
        print(min(lion_min))
