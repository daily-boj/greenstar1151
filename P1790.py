import math

def numlen_prev(x: int):
    expX = math.floor(math.log10(x))
    numlen_prev_x = 0
    for i in range(expX):
        if expX == 0:
            return 0
        else:
            numlen_prev_x += 10**i * 9 * (i+1)
    else:
        return numlen_prev_x


N, k = map(int, input().split())


expN = math.floor(math.log10(N))
expk = math.floor(math.log10(k))
numlen_N_prev = numlen_prev(N)
base10_k_prev = 0
numlen_k_prev = 0


for i in range(9):
    numlen_k_prev += 10**i * 9 * (i+1)
    base10_k_prev += 1
    if numlen_k_prev >= k:
        numlen_k_prev -= 10**i * 9 * (i+1)
        base10_k_prev -= 1
        break
    else:
        continue
    
# 1234567891011121314151617181920
number = str(10**base10_k_prev + ((k - numlen_k_prev)//expk))
#number = str((10**expk) + (math.floor((k - numlen_knum - 1) / (expk + 1))))
numlen = numlen_N_prev + (N - 10**expN + 1)*(expN + 1)

# debug
print('base10_k_prev : {}, numlen : {}, numlen_k_prev : {}, number : {}' .format(base10_k_prev, numlen, numlen_k_prev, number))
print('{} % {} = {}' .format((k - numlen_k_prev - 1), ((math.floor(math.log10(int(number)))) + 1), ((k - numlen_k_prev - 1) % ((math.floor(math.log10(int(number)))) + 1))))

if k > numlen:
    print(-1)
else:
    print(number[((k - numlen_k_prev - 1) % ((math.floor(math.log10(int(number)))) + 1))])
