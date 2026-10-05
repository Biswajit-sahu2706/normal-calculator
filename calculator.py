import math

# Addition

def add(a, b):
    return a + b

# Subtraction

def subtract(a, b):
    return a - b

# Multiplication

def multiply(a, b):
    return a * b

# Division

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Percentage

def percentage(a):
    return a / 100

# Power

def power(a, b):
    return a ** b

# Square root

def square_root(a):
    if a < 0:
        raise ValueError("Cannot find square root of a negative number")
    return math.sqrt(a)

# Sine

def sine(a):
    return math.sin(math.radians(a))

# Cosine

def cosine(a):
    return math.cos(math.radians(a))

# Tangent

def tangent(a):
    return math.tan(math.radians(a))

# Logarithm base 10

def log10(a):
    if a <= 0:
        raise ValueError("Log is only defined for positive numbers")
    return math.log10(a)

# Natural logarithm

def ln(a):
    if a <= 0:
        raise ValueError("Natural log is only defined for positive numbers")
    return math.log(a)

# Factorial

def factorial(a):
    if a < 0 or not a.is_integer():
        raise ValueError("Factorial requires a non-negative integer")
    return math.factorial(int(a))
