import streamlit as st

# Set page configuration
st.set_page_config(page_title="Income Tax Calculator", page_icon="💰")

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            font-size: 32px;
            font-weight: bold;
        }
        .cyan-text {
            color: cyan;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
        .stButton > button {
            background-color: #FFA500;
            color: white;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Title (with slightly smaller font for better contrast)
st.markdown('<p class="title">Income Tax Calculator for FY 2025-26</p>', unsafe_allow_html=True)
st.write("As per new tax regime (including marginal tax relief)")

# Input for annual income
income = st.number_input("Enter your Annual Income (₹)", min_value=0, step=1000, value=0)

# Standard deduction
std_deduction = 75000
taxable_income = max(0, income - std_deduction)

# Tax calculation logic
tax = 0
if taxable_income > 1200000:
    slabs = [(400000, 0.05), (400000, 0.10), (400000, 0.15), (400000, 0.20), 
             (400000, 0.25), (float('inf'), 0.30)]
    remaining_income = taxable_income - 1200000
    for slab, rate in slabs:
        if remaining_income > 0:
            taxable_slab = min(slab, remaining_income)
            tax += taxable_slab * rate
            remaining_income -= taxable_slab
        else:
            break

# Apply marginal relief if applicable
if 1200000 < taxable_income <= 1275000:
    tax = taxable_income - 1200000

# Apply 4% cess
cess = tax * 0.04
total_tax = tax + cess

# Display Tax Breakdown
if st.button("Calculate Tax"):
    st.subheader("💰 Tax Calculation Breakdown")
    st.write(f"**Standard Deduction:** ₹{std_deduction:,}")
    st.write(f"**Tax (Before Cess & Relief):** ₹{tax:,}")
    st.write(f"**Cess (4%):** ₹{cess:,}")
    st.write(f"### **Total Tax Payable: ₹{total_tax:,}**")

# Developer credit in cyan color
st.markdown('<p class="cyan-text">Developed by Paramjeet Gusain</p>', unsafe_allow_html=True)
