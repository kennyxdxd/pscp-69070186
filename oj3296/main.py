"""3296"""
import math as m
r1,g1,b1 = map(int,input().split())
r2,g2,b2 = map(int,input().split())
print(f"{m.floor((r1+r2)/2)} {m.floor((g1+g2)/2)} {m.floor((b1+b2)/2)}")
