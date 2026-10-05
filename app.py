import streamlit as st
import math

from calculator import (
add,
subtract,
multiply,
divide,
percentage,
power,
square_root,
sine,
cosine,
tangent,
log10,
ln,
factorial
)

# Page settings

st.set_page_config(
page_title="Scientific Calculator",
page_icon="🧮"
)

# Title

st.title("🧮 Scientific Calculator")

st.write("Simple Scientific Calculator using Python and Streamlit")

# Input numbers

number1 = st.number_input(
"Enter first number",
value=0.0
)

number2 = st.number_input(
"Enter second number",
value=0.0
)

# Select operation

operation = st.selectbox(
"Select Operation",
[
"Addition",
"Subtraction",
"Multiplication",
"Division",
"Percentage",
"Power",
"Square Root",
"Sine",
"Cosine",
"Tangent",
"Log10",
"Natural Log",
"Factorial"
]
)

# Calculate button

if st.button("Calculate"):

    try:

        if operation == "Addition":
            result = add(number1, number2)

        elif operation == "Subtraction":
            result = subtract(number1, number2)

        elif operation == "Multiplication":
            result = multiply(number1, number2)

        elif operation == "Division":
            result = divide(number1, number2)

        elif operation == "Percentage":
            result = percentage(number1)

        elif operation == "Power":
            result = power(number1, number2)

        elif operation == "Square Root":
            result = square_root(number1)

        elif operation == "Sine":
            result = sine(number1)

        elif operation == "Cosine":
            result = cosine(number1)

        elif operation == "Tangent":
            result = tangent(number1)

        elif operation == "Log10":
            result = log10(number1)

        elif operation == "Natural Log":
            result = ln(number1)

        elif operation == "Factorial":
            result = factorial(number1)


        # Display result
        st.success(f"Result: {result}")


    except ValueError as error:

        st.error(str(error))

