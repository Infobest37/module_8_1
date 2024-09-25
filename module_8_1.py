def add_everything_up(a,b):
    try:

        str(b),float(a)
    except (TypeError, ValueError):
        return str(b)+a
    try:
        str(a), int(b)
    except (TypeError, ValueError):
        return str(a)+b

    return a+b





print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))