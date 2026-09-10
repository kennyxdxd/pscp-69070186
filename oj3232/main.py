"""3232"""
jump, target = map(int,input().split())
jumps = 0
while jump > 0 and target > 0:
    target -= jump
    jump -= 2
    jumps+=1
print(jumps if target <=0 else -1)
