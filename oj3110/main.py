"""sada"""
src, dst = input().split()

weight = float(input())

route = {
    ("BKK", "CNX"): (10, 30),
    ("CNX", "UBP"): (15, 40),
    ("UBP", "BKK"): (20, 40),
    ("BKK", "PKT"): (25, 50),
    ("PKT", "CNX"): (30, 60),
    ("UBP", "PKT"): (40, 70)
}

if (src, dst) in route:
    fee, kg = route[(src, dst)]
    total = fee + (weight * kg)
    print(f"{total:.2f}")
else:
    print("Error")