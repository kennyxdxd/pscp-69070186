"""oj3031"""
import math
s , num = map(int,input().split())

for i in range(num):
    i+= 1
    x, y = map(int,input().split())
    area = 3.1416 * (x**2 + y**2)
    t = area/s
    print(math.ceil(t))
