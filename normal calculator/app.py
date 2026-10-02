import streamlit as st
from calculator import add, subtract, multiply, divide


st.title("🧮 Simple Calculator")

# Take input from user
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# Select operation
operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
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

    st.success(f"Result: {result}")