import sys


T = int(input())
coincase_in = sys.stdin.read().rstrip()
coincase = tuple(coincase_in.split('\n'))


for C in coincase:
    coin_list = [0,0,0,0,0,0,0,0]
    for i in range(38):
        coin_index = (ord(C[i])%11*-1+7)*4 + (ord(C[i+1])%11*-1+7)*2 + ord(C[i+2])%11*-1+7
        coin_list[coin_index] += 1
    else:
        print(' '.join([str(x) for x in coin_list]))
