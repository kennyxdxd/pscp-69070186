a = int(input())
b = int(input())
goal = int(input())

if goal // 5 >= b:
    goal -= (b * 5)
else:
    goal %= 5
if goal > a:
    print(-1)
else:
    print(goal)