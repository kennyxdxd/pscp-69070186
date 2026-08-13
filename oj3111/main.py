"""school"""
sub = input()
product = int(input())
count = 0
for i in range(product):
    i +=1
    count += float(input())
if sub == "Y":
    count -= ((5/100)*count)
elif sub == "N" and count >= 500:
    count -= ((3/100)*count)

ans = round(count + 1e-9, 2)
print(f"{ans:.02f}")
