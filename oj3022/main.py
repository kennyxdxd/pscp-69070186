"""asa"""
c = float(input())

tem1 = input()
tounit = input()

result = 0
if tem1 == "C":
    if tounit == "F":
        result = (c * 9/5) + 32
    elif tounit == "K":
        result = c + 273.15
    elif tounit == "R":
        result = c * 9/5 + 491.67
    elif tounit == "C":
        result = c
elif tem1 == "F":
    if tounit == "C":
        result = (c - 32) * 5/9
    elif tounit == "K":
        result = (c - 32) * 5/9 + 273.15
    elif tounit == "R":
        result = c + 459.67
    elif tounit == "F":
        result = c
elif tem1 == "R":
    if tounit == "C":
        result = (c - 491.67) * 5/9
    elif tounit == "K":
        result = c * 5/9
    elif tounit == "F":
        result = c  - 459.67
    elif tounit == "R":
        result = c
elif tem1 == "K":
    if tounit == "C":
        result = c - 273.15
    elif tounit == "R":
        result = c * 9/5
    elif tounit == "F":
        result = (c - 273.15) * 9/5 + 32
    elif tounit == "K":
        result = c
print(f"{result:.2f}")