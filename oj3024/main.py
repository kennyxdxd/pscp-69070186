"""SurprisingVote"""
total = float(input())
most = float(input())

least = total - (2 * most)

if least < 0:
    least = 0

if most - least > 2:
    print("Surprising")
else:
    print("Not surprising")
