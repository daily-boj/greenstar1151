N = int(input())
words = []

for _ in range(N):
    words.append(input())

for s in words:
    try:
        i = words.index(s[::-1])
        t = words[i]
        print(len(t), t[len(t)//2])
        break
    except:
        continue
