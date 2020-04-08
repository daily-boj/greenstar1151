a,b=map(int,input().split())
c=set()
for i in range(a,b+1): 
 for j in range(i+1):c.add(j/i)
print(len(c)-1)