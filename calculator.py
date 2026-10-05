def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Cannot perform modulus by zero"
    return a % b

def exponent(a, b):
    return a ** b

def percentage(a, b):
    if b == 0:
        return "Cannot calculate percentage with zero"
    return (a / b) * 100