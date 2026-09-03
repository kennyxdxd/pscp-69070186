"""3157"""
number = int(input())
count = 0
for i in range(number):
    mark = input()
    if mark =="+":
        count += 10
    elif mark == '-':
        count -= 5
print(count)
