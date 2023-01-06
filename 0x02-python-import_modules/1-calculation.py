#!/usr/bin/python3

if __name__ = "__main__":
    import calculator_1

    a = 10
    b = 5

    addition = add(a, b)
    difference = sub(a, b)
    product = mul(a, b)
    quotient = div(a ,b)

    print('{:d} + {:d} = {:d}'.format(a, b, addition)))
    print('{:d} - {:d} = {:d}'.format(a, b, difference)))
    print('{:d} * {:d} = {:d}'.format(a, b, product)))
    print('{:d} / {:d} = {:d}'.format(a, b, quotient)))
