'''
# O(n)
N = int(input())


csum = 0
for i in range(1, N):
    csum += N * i + i
else:
    print(csum)

# O(1)
print((lambda N:(N*(N-1)//2)*(N+1))(int(input())))
print((lambda N:((N**3-N)//2))(int(input())))
'''

# O(1) short
N=int(input());print((N**3-N)//2)
