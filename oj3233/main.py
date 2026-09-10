"""3233"""
win_char, win_num = input().split()
my_char, my_num = input().split()

if my_char == win_char and my_num == win_num:
    print(1000000)
elif my_num == win_num:
    print(100000)
elif my_char == win_char and my_num[-3:] == win_num[-3:]:
    print(2000)
elif my_char == win_char and my_num[-2:] == win_num[-2:]:
    print(1000)
elif my_num[-3:] == win_num[-3:]:
    print(200)
elif my_num[-2:] == win_num[-2:]:
    print(100)
elif my_char == win_char:
    print(20)           
else:
    print(0)
