"""Arcade of Time: Store Check"""
store ,a = map(int,input().split())
openlist = []
for _ in range(store):
    opens, close = map(int,input().split())
    openlist.append([opens,close])
check = list(map(int,input().split()))

answer = []
for i in check:
    count = 0
    for sopen,close in openlist:
        if sopen <= i < close:
            count += 1
    answer.append(str(count))

print(" ".join(answer))
