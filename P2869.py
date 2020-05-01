import math


A, B, V = map(int, input().split())


top = math.ceil((V - A) / (A - B)) + 1


print(top)
