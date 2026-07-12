"""SurprisingVote"""
total = float(input())
most = float(input())

a = total - most
if a > 10 and a - 10 > most:
    least = a - 10
elif a < 10 and a < most:
    least = a // 2
else:
    least = a - most

if most - least > 2:
    print("Surprising")
else:
    print("Not surprising")
