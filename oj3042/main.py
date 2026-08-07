number = int(input())
answer = [str(i * 10) for i in range((number//10),-1,-1)]
print(" ".join(answer))
