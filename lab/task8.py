value = 0
while value < 10:
    if value == 0:
        value += 1
    elif value // 5 > 2:
        value += 5
    else:
        value += 2
    print(value)