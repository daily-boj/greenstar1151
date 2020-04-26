N_str = input()


Nsum = sum(tuple(map(int, list(N_str))))
Nlist = list(N_str)


if Nsum % 3 == 0:
    if '0' in Nlist:
        Nlist.sort(reverse=True)
        print(''.join(Nlist))
    else:
        print(-1)
else:
    print(-1)
