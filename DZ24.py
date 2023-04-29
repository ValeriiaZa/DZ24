def difference(*some_digit):
    if len(some_digit) == 0:
        count = 0
    else:
        count = round(max(*some_digit) - (min(*some_digit)), 2)
    return count

digits = (1, 2, 3)
difference(digits)
