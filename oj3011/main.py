"""color"""
color1 = input().capitalize()
color2 = input().capitalize()
if color1 in color2:
    if color1 in "Yellow" and color2 in "Yellow":
        print("Yellow")
    elif color1 in "Red" and color2 in "Red":
        print("Red")
    elif color1 in "Blue" and color2 in "Blue":
        print("Blue")
    else:
        print("Error")
else:
    if (color1 in "Red" or color1 in "Yellow") and (color2 in "Yellow" or color2 in "Red"):
        print("Orange")
    elif (color1 in "Red" or color1 in "Blue") and (color2 in "Blue" or color2 in "Red"):
        print("Violet")
    elif (color1 in "Yellow" or color1 in "Blue") and (color2 in "Blue" or color2 in "Yellow"):
        print("Green")
    else:
        print("Error")
