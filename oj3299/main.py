"""3299"""
l,n = map(int,input().split())
idx = l
sums = 0
count = 0
while sums < n:
    left = (idx * (idx+1)) // 2
    right = ((idx - l) * (idx - l + 1)) // 2
    sums += left - right
    idx += l
    count += 1
print(count)
