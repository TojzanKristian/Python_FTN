import math

a = input("Please enter a number : ")
b = input("Please enter a number : ")
c = input("Please enter one of the following symbols (+, -, *, /, **, sqrt):")


def sum():
    return int(a)+int(b)


def difference():
    return int(a)-int(b)


def product():
    return int(a)*int(b)


def quotient():
    return int(a)/int(b)


def power():
    return int(a)**int(b)


def sqrt():
    print(math.sqrt(int(a)))
    print(math.sqrt(int(b)))


if c == "+":
    print(sum())
elif c == "-":
    print((difference()))
elif c == "*":
    print(product())
elif c == "/":
    print(quotient())
elif c == "**":
    print(power())
elif c == "sqrt":
    sqrt()
else:
    print("You entered the wrong symbol !!")