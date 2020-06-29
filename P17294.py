import sys


k = int(input())


numst = str(k)
if len(numst) == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
    sys.exit(0)

d = int(numst[1]) - int(numst[0])

for i in range(len(numst) - 1):
    if int(numst[i+1]) - int(numst[i]) == d:
        continue
    else:
        break
else:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
    sys.exit(0)

print('흥칫뿡!! <(￣ ﹌ ￣)>')
