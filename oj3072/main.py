"""A-E-I-O-U"""

text = input().lower
a = ["a","e","i","o","u"]
for i in a:
    if text.count(i):
        print(f"{i} : {text.count(i)}")
