"""prime"""
first, last = map(int, input().split())

prime = []
for i in range(first, last + 1):
    if i <= 1:
        continue
    if i == 2:
        prime.append(str(i))
        continue
    if i % 2 == 0:
        continue
    is_prime = True
    limit = int(i ** 0.5) + 1
    for j in range(3, limit, 2):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        prime.append(str(i))

if len(prime):
    print(" ".join(prime))
print(f"Total primes: {len(prime)}")
