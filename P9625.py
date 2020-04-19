K = int(input())
AB = [1, 0]

for _ in range(K):
    A = AB[1]
    B = AB[0] + AB[1]
    AB[0], AB[1] = A, B

print(AB[0], AB[1])
