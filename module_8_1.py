def add_everything_up(a,b):
    try:
        return round(a + b, 3)
    except TypeError:
        if (isinstance(a, str) or isinstance(a, int)
                or isinstance(a, float) and isinstance(b, int)
                or isinstance(b, str) or isinstance(b, float)):
            return str(a)+ str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))