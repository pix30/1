# simple calculator using functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # dividing by zero is not allowed
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# test each function
print("10 + 5 =", add(10, 5))
print("10 - 5 =", subtract(10, 5))
print("10 * 5 =", multiply(10, 5))
print("10 / 5 =", divide(10, 5))
print("10 / 0 =", divide(10, 0))
