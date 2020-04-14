N, M = map(int, input().split())
image = []
image2x = []
temp = ''
result = 1

for _ in range(N):
    image.append(input())

for i in range(N):
    for s in image[i]:
        temp += s * 2
    image2x.append(temp)
    temp = ''

for l in image2x:
    if input() == l:
        result *= 1
    else:
        result *= 0

if result == 1:
    print('Eyfa')
else:
    print('Not Eyfa')
