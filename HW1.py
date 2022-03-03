def my_func(x1, x2, x3):
    if x1 + x2 + x3 == 0:
        print('Not a number - denominator equals zero')
        exit(1)
    if type(x1) != float or type(x2) != float or type(x3) != float:
        print('Error: parameters should be float')
        exit(1)
    return ((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3)


def convert(hours, minutes):
    if hours < 0 or minutes < 0:
        print('Input error!')
        exit(1)
    x = hours*3600+minutes*60
    return print(x)

