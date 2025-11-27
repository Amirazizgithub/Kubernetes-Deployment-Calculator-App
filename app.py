import streamlit as st
from calculator.calculator import ScientificCalculator

# Custom CSS for beautiful UI
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: #ffffff;
    }
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    }
    .stTitle {
        color: #D21F3C;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0px 0px 20px rgba(255, 255, 255, 0.6);
    }
    .stSubheader1 {
        color: #fff!important;
        font-family: 'Segoe UI', sans-serif;
        font-size: 2rem;
        text-align: center;
        margin-bottom: 2rem;
        border-bottom: 2px solid #D21F3C;
        padding-bottom: 0.2rem;
    }
    .stSubheader2 {
        color: #fff!important;
        font-family: 'Segoe UI', sans-serif;
        font-size: 2rem;
        margin-top: 5rem;
        margin-bottom: 2rem;
    }
    .stNumberInput > label, .stSelectbox > label {
        color: #ffffff;
        font-weight: 500;
        font-size: 1.1rem;
    }
    .stButton > button {
        background: rgba(0, 0, 0, 0.2);
        color: white;
        border-radius: 25px;
        font-size: 1.8rem;
        padding: 0.6rem 2.5rem;
        border: 2px solid #D21F3C;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        background-color: rgba(210, 31, 60, 0.2); /* Red tint on hover */
        border-color: #ffffff;
    }
    .stSuccess {
        background: rgba(255, 82, 82, 0.2);
        backdrop-filter: blur(10px);
        color: #ffffff;
        border-radius: 15px;
        font-size: 2rem;
        padding: 1.5rem;
        margin-top: 2rem;
        text-align: center;
        border: 2px solid #ffffff;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .stError {
        background: rgba(255, 82, 82, 0.2);
        backdrop-filter: blur(10px);
        color: #ffffff;
        border-radius: 15px;
        font-size: 1.5rem;
        padding: 1rem;
        margin-top: 1rem;
        text-align: center;
        border: 2px solid #ffffff;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.2);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #D21F3C;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 1.8rem;
        # text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #D21F3C;
        padding-bottom: 0.5rem;
        display: inline-block;
    }
    
    /* Radio Button Styling */
    .stRadio > div[role="radiogroup"] > label {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid #D21F3C;
        padding: 6px 6px;
        border-radius: 8px;
        margin-bottom: 4px;
        transition: all 0.2s ease;
        cursor: pointer;
        color: white !important;
    }

    .stRadio > div[role="radiogroup"] > label p,
    .stRadio > div[role="radiogroup"] > label div,
    .stRadio > div[role="radiogroup"] > label span {
        color: white !important;
    }
    
    .stRadio > div[role="radiogroup"] > label:hover {
        background-color: rgba(210, 31, 60, 0.2); /* Red tint on hover */
        border-color: #ffffff;
        transform: translateX(5px);
    }
    
    /* Active Radio Button (approximate via checked state if accessible, otherwise relies on Streamlit's default highlighting which we can accent) */
    .stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] {
        /* This targets the container of the radio item */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="stTitle">Scientific Calculator</h1>', unsafe_allow_html=True)
st.markdown(
    '<h3 class="stSubheader1">Advanced Mathematical Operations</h3>',
    unsafe_allow_html=True,
)

calc = ScientificCalculator()

# Layout
# Sidebar for Operations
with st.sidebar:
    st.markdown("### Operations")
    operation = st.radio(
        "Choose Function",
        [
            "Add (+)",
            "Subtract (-)",
            "Multiply (x)",
            "Divide (÷)",
            "Power (x^y)",
            "Square Root (√x)",
            "Logarithm (log10)",
            "Natural Log (ln)",
            "Sin (Degrees)",
            "Cos (Degrees)",
            "Tan (Degrees)",
            "Factorial (x!)",
        ],
        label_visibility="collapsed",
    )

# Main Area for Inputs and Results
st.markdown('<h4 class="stSubheader2">Inputs</h4>', unsafe_allow_html=True)

# Determine if we need one or two inputs
requires_two_inputs = operation in [
    "Add (+)",
    "Subtract (-)",
    "Multiply (x)",
    "Divide (÷)",
    "Power (x^y)",
]

num1 = st.number_input("Enter first number (x)", value=0.0, step=1.0, format="%.4f")

num2 = 0.0
if requires_two_inputs:
    num2 = st.number_input(
        "Enter second number (y)", value=0.0, step=1.0, format="%.4f"
    )

st.markdown("###")  # Spacer
if st.button("Calculate Result"):
    result = None
    error = None

    try:
        if operation == "Add (+)":
            result = calc.add(num1, num2)
        elif operation == "Subtract (-)":
            result = calc.subtract(num1, num2)
        elif operation == "Multiply (x)":
            result = calc.multiply(num1, num2)
        elif operation == "Divide (÷)":
            result = calc.divide(num1, num2)
        elif operation == "Power (x^y)":
            result = calc.power(num1, num2)
        elif operation == "Square Root (√x)":
            result = calc.sqrt(num1)
        elif operation == "Logarithm (log10)":
            result = calc.log(num1)
        elif operation == "Natural Log (ln)":
            result = calc.ln(num1)
        elif operation == "Sin (Degrees)":
            result = calc.sin(num1)
        elif operation == "Cos (Degrees)":
            result = calc.cos(num1)
        elif operation == "Tan (Degrees)":
            result = calc.tan(num1)
        elif operation == "Factorial (x!)":
            result = calc.factorial(num1)
    except Exception as e:
        error = str(e)

    if error:
        st.markdown(
            f'<div class="stError">Error: {error}</div>', unsafe_allow_html=True
        )
    elif result is not None:
        st.markdown(
            f'<div class="stSuccess">{round(result, 4)}</div>', unsafe_allow_html=True
        )

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #aaa; font-size: 0.8rem;'>© 2025 Scientific Calculator App</div>",
    unsafe_allow_html=True,
)
