import streamlit as st
from calculator.calculator import Calculator

# Custom CSS for beautiful UI
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
    }
    .stApp {
        background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
    }
    .stTitle {
        color: #333;
        font-family: 'Segoe UI', sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stNumberInput > label, .stSelectbox > label {
        color: #333;
        font-weight: 600;
        font-size: 1.1rem;
    }
    .stButton > button {
        background: #ff6e7f;
        color: white;
        border-radius: 8px;
        font-size: 1.1rem;
        padding: 0.5rem 2rem;
        border: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: background 0.3s;
    }
    .stButton > button:hover {
        background: #bfe9ff;
        color: #333;
    }
    .stSuccess {
        background: #fffbe6;
        color: #333;
        border-radius: 8px;
        font-size: 1.2rem;
        padding: 1rem;
        margin-top: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="stTitle">Simple Calculator</h1>', unsafe_allow_html=True)

num1 = st.number_input("Enter first number", value=0, key="num1", step=1, format="%d")
num2 = st.number_input("Enter second number", value=1, key="num2", step=1, format="%d")
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"], key="op")

if st.button("Calculate"):
    calc = Calculator()
    result: int | str | None = None
    if operation == "Add":
        result = calc.add(num1, num2)
    elif operation == "Subtract":
        result = calc.subtract(num1, num2)
    elif operation == "Multiply":
        result = calc.multiply(num1, num2)
    elif operation == "Divide":
        try:
            result = calc.divide(num1, num2)
        except ZeroDivisionError:
            result = "Error: Division by zero"
    if result is not None:
        st.markdown(f'<div class="stSuccess">Result: {result}</div>', unsafe_allow_html=True)
