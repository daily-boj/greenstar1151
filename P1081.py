L, U = map(int, input().split())

def numseqsum(n):
    if n == -1:
        return 0
    num = []
    for s in str(n):
	    num.append(int(s))
    numsum = 0
    for i, j in enumerate(num):
        if i == (len(num) - 1):
            numsum += sum(num[:i])*(j+1) + j*(j+1)//2
        else:
            p = len(num) - i - 1
            numsum += j * p*10**(p-1) * 45 # 0~9 합   
            if i == 0: # 앞부분 합
            	numsum += j*(j-1)//2 * 10**p
            else:
                numsum += j*10**p * sum(num[:i]) + 10**p * j*(j-1)//2
    else:
        return numsum


print(numseqsum(U) - numseqsum(L-1))
