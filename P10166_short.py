a,b=map(int,input().split())
c=[]
for i in range(a,b+1): 
 for j in range(i+1):c.append(j/i)
print(len(list(set(c)))-1)