#!/usr/bin/python3

if __name__ = "__main__":
    import calculator_1

    a = 10
    b = 5

    addition = add(a, b)
    difference = sub(a, b)
    product = mul(a, b)
    quotient = div(a ,b)

    print(f"a + b = {addition}")
    print(f"a - b = {difference}")
    print(f"a * b = {product}")
    print(f"a / b = {quotient}")
