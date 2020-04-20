import math
def sol2max(a,b,c):
    return max((-b + math.sqrt(b**2 - 4*a*c)) / 2*a, (-b - math.sqrt(b**2 - 4*a*c)) / 2*a)


A = int(input())
T = int(input())
pupa = int(input())


nth = int(sol2max(1, 7, -2*T+2) + 1)
prev = (nth-1)**2 + 7*(nth-1)
nth_in = T - prev//2

if nth_in <= 2:
    if pupa == 0:
        peoplecount = prev + 2*nth_in-1
    elif pupa == 1:
        peoplecount = prev + 2*nth_in
else:
    if pupa == 0:
        peoplecount = nth_in-2 + 4 + prev
    elif pupa == 1:
        peoplecount = nth_in-2 + 4 + nth+1 + prev

print((peoplecount-1) % A)
