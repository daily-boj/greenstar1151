N = int(input())
q1 = 0
q2 = 0
q3 = 0

for _ in range(N):
    a, b = input().split('/')
    if a + b == '14':
        q1 += 1
    elif a + b == '12':
        q2 += 1
    elif a + b == '34':
        q3 += 1

if q3 >= q1:
    print(q3 + q2//2 + q2%2)
elif q2%2 == 0:
    print(q3 + q2//2 + (q1-q3)//4 + min((q1-q3)%4, 1))
elif q1%4 <= 2:
    print(q3 + q2//2 + (q1-q3)//4 + 1)
elif q1%4 > 2:
    print(q3 + q2//2 + (q1-q3)//4 + 2)
