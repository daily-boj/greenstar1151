P_n = [1, 1, 1, 2, 2]

for i in range(6, 101):
    P_n.append(P_n[i - 6] + P_n[i - 2])

N = int(input())

for _ in range(N):
    print(P_n[int(input()) - 1])

