"""ca"""
import math
numbers = int(input())

line = math.ceil(math.sqrt(numbers))

if line % 2 != 0 and numbers % 2 == 0:
    answer = ((line * 2) - 2) - 1
elif line %2 == 0 and numbers % 2 != 0:
    answer = ((line * 2) - 2) - 1
else:
    answer = ((line * 2) - 2)

print(answer)
