# 수학 내다버린 풀이

D_1, D_2 = map(int, input().split())
list_temp = []

for i in range(D_1, D_2 + 1):
    for j in range(i+1):
        list_temp.append(j / i)

print(len(list(set(list_temp))) - 1)
