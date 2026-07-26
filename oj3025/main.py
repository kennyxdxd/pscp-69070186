"""Season"""
month = int(input())
day = int(input())
list_month = [1,2,3,4,5,6,7,8,9,10,11,12]

if month in list_month[:3]:
    season = "winter"
elif month in list_month[3:6]:
    season = "spring"
elif month in list_month[6:9]:
    season = "summer"
else:
    season = "fall"

if not month % 3 and day >= 21:
    if season == "winter":
        season = "spring"
    elif season == "spring":
        season = "summer"
    elif season == "summer":
        season = "fall"
    elif season == "fall":
        season = "winter"

print(season)
