import streamlit as st
from calculator import add, exponent, modulus, percentage, subtract, multiply, divide


st.title("🧮 Simple Calculator")

# Take input from user
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# Select operation
operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Exponent", "Percentage"]
)

# Calculate button
if st.button("Calculate"):

    if operation == "Addition":
        result = add(num1, num2)

    elif operation == "Subtraction":
        result = subtract(num1, num2)

    elif operation == "Multiplication":
        result = multiply(num1, num2)

    elif operation == "Division":
        result = divide(num1, num2)
        
    elif operation == "Modulus":
        result = modulus(num1, num2)

    elif operation == "Exponent":
        result = exponent(num1, num2)

    elif operation == "Percentage":
        result = percentage(num1, num2)

    st.success(f"Result: {result}")