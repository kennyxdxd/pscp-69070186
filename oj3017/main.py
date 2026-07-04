"""Bill"""
price = input()

TOTAL_PRICE = float(price)
service_charge = 10 / 100 * TOTAL_PRICE

if service_charge < 50:
    service_charge = 50
elif service_charge > 1000:
    service_charge = 1000

TOTAL_PRICE += service_charge
vat = 7 / 100 * TOTAL_PRICE
TOTAL_PRICE += vat

print(f"{TOTAL_PRICE:.2f}")
