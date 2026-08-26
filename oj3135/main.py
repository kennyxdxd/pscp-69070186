"""ของขวัญและขโมย"""
n , k ,t = map(int,input().split())

run = False
count = 0
ex = 1
if t == 1:
    run = True
    count = 1
while run == False:
    if ex + k <= n:
        ex += k
    else:
        ex = (ex + k) - n
    if ex == 1 :
        run = True
    elif ex == t:
        run = True
        count += 1
    count += 1

print(count)

