N, K = map(int, input().split())
Nnumber = input()


Kcount = K
numbers_erased = []

for i in Nnumber:
    number = int(i)
    if len(numbers_erased) == 0:
        numbers_erased.append(number)
        continue
        
    while not(len(numbers_erased) == 0) and numbers_erased[-1] < number and Kcount > 0:
        numbers_erased.pop()
        Kcount -= 1
    else:
        numbers_erased.append(number)
        continue

    if numbers_erased[-1] >= number:
        numbers_erased.append(number)


for i in numbers_erased[:N-K]:
    print(i, end='')
