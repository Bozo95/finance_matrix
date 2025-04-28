import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Welcome to Finance Matrix", layout="centered")

# --- CSS for cards and styling ---
st.markdown("""
<style>
.cards-container {
    display: flex;
    justify-content: center;
    gap: 2.5rem;
    margin-top: 3rem;
    margin-bottom: 3rem;
}
.card-btn {
    border-radius: 15px;
    padding: 2.2rem 2.5rem;
    width: 320px;
    min-height: 150px;
    font-size: 1.35rem;
    font-weight: 700;
    border: none;
    cursor: pointer;
    transition: transform 0.18s cubic-bezier(.4,2,.6,1), box-shadow 0.18s cubic-bezier(.4,2,.6,1);
    text-align: center;
    margin-bottom: 0;
    margin-top: 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    background: #a7d9ed;
    color: #174b6d;
}
.card-btn.yellow {
    background: #fff8d5 !important;
    color: #b17b00 !important;
}

}
.card-desc {
    font-size: 1rem;
    font-weight: 400;
    color: #444;
    margin-top: 0.7rem;
}

div.stButton > button.financial-freedom {
    background-color: #a7d9ed;
    color: #174b6d;
    border-radius: 16px;
    font-size: 1.15rem;
    font-weight: 600;
    padding: 1.7rem 1.2rem;
    width: 100%;
    margin-bottom: 1rem;
    border: none;
    box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    transition: 0.2s;
    text-align: center;
}

div.stButton > button.corporate-finance {
    background-color: #fff8d5;
    color: #b17b00;
    border-radius: 16px;
    font-size: 1.15rem;
    font-weight: 600;
    padding: 1.7rem 1.2rem;
    width: 100%;
    margin-bottom: 1rem;
    border: none;
    box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    transition: 0.2s;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# --- Landing Page ---

def landing_page():
    
    st.markdown("""
    <div style = 'text-align: center;'>
        <h1 class="title-text">Welcome to Finance Matrix</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style = 'text-align: center;'>
        <p> Welcome to the Finance Matrix, where I try to convert $1.000 of sales of digital products, within the 90 days challenege. Where I document everything.</p>
        <p> In the meanwhile explore the free resources on financial freedom and corporate finance. Feel free to subscribe to my newsletter to stay updated!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 100px;"></div>', unsafe_allow_html=True)

    # Newsletter form
    with st.form("newsletter_form", clear_on_submit=True):
        email = st.text_input("Enter your email address", placeholder="you@example.com")
        submitted = st.form_submit_button("Subscribe")
        if submitted:
            if email and "@" in email:
                st.success(f"Thank you for subscribing, {email}!")
            else:
                st.error("Please enter a valid email address.")

    st.markdown("---")

    st.markdown("""
    <div style = 'text-align: center;'>
        FREE RESOURCES
    </div>

    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 70px;"></div>', unsafe_allow_html=True)

    # Cards as buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Financial Freedom\n\n Free resources on financial freedom.",
                     key="financial_freedom_card",
                     help="Go to Financial Freedom"):
            st.query_params["page"] = "financial_freedom"
            st.rerun()
    with col2:
        if st.button("Financial Analysis 101\n\nInsights into corporate finance, investments, and business growth.",
                     key="financial_analysis_101_card",
                     help="Go to Financial Analysis 101"):
            st.query_params["page"] = "financial_analysis_101"
            st.rerun()

    st.markdown("---")

# --- Threads section ---

# --- Financial Freedom Page ---

def financial_freedom_page():
    st.header("Financial Freedom Calculator")
    st.write("Calculate how your funds will grow until retirement and how much you need to retire comfortably.")

    # --- User Inputs ---
    current_funds = st.number_input("Current funds (USD):", min_value=0.0, value=0.0, format="%.2f")
    years_until_retirement = st.number_input("Years until retirement:", min_value=1, max_value=100, value=30, step=1)
    expected_return = st.number_input("Expected annual return (%):", min_value=0.0, max_value=100.0, value=7.0, step=0.1)
    expected_expenses = st.number_input("Expected monthly expenses in retirement (USD):", min_value=0.0, value=2000.0, step=100.0)
    withdrawal_rate = st.number_input("Withdrawal rate (%):", min_value=1.0, max_value=10.0, value=4.0, step=0.1)

    # --- Calculate funds needed for retirement ---
    if withdrawal_rate > 0:
        annual_expenses = expected_expenses * 12
        funds_needed = annual_expenses / (withdrawal_rate / 100)
    else:
        funds_needed = 0

    # --- Show funds needed in a green rounded container ---
    st.markdown(
        f"""
        <div style="background-color:#e6f9ec; border-radius:16px; padding:1.2em 1em; margin:1.5em 0; border:1.5px solid #b2e2c6;">
            <span style="color:#217a41; font-size:1.15rem; font-weight:600;">
                💡 Funds needed to retire comfortably: <span style="color:#167a2f">${funds_needed:,.2f}</span>
            </span>
        </div>
        """, unsafe_allow_html=True
    )

    # --- Compounding growth calculation ---
    years = np.arange(0, years_until_retirement + 1)
    rate = expected_return / 100
    portfolio_values = current_funds * (1 + rate) ** years

    # --- Plotting ---
    fig, ax = plt.subplots()
    ax.plot(years, portfolio_values, color="#217a41", linewidth=2.5)
    ax.set_xlabel("Years until retirement")
    ax.set_ylabel("Portfolio Value (USD)")
    ax.set_title("Projected Portfolio Growth")
    ax.grid(alpha=0.2)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x):,}'))
    st.pyplot(fig)


    # --- Show funds compounded ---
    st.markdown(
        f"""
        <div style="background-color:#98C9F2; border-radius:16px; padding:1.2em 1em; margin:1.5em 0; border:1.5px solid #98C9F2;">
            <span style="color:#1867C0; font-size:1rem; font-weight:450;">
                📈 Amount of funds when compounded: ${portfolio_values[-1]:,.2f}.</span>
            </span>
        </div>
        """, unsafe_allow_html=True
    )

    if st.button("Go Back"):
        st.query_params["page"] = ""
        st.rerun()

# --- Financial Analysis 101 Page ---
def financial_analysis_101_page():
    st.header("Financial Analysis 101")
    st.write("""
    Welcome to Financial Analysis 101! Here is your course content:
    - Module 1: Understanding Financial Statements
    - Module 2: Ratio Analysis
    - Module 3: Valuation Basics
    - ... (add your actual content here)
    """)

    if st.button("Go Back"):
        st.query_params["page"] = ""
        st.rerun()

# --- Main app navigation ---
page = st.query_params.get("page", "")

if page == "financial_freedom":
    financial_freedom_page()
elif page == "financial_analysis_101":
    financial_analysis_101_page()
else:
    landing_page()

# --- Footer ---
st.markdown("""
<footer style="margin-top: 3rem; text-align: center;">
    <div>Connect with me:</div>
    <div style="margin-top: 0.5rem; display: flex; justify-content: center; gap: 2rem;">
        <a href="https://linkedin.com/in/yourprofile" target="_blank" title="LinkedIn" style="font-size: 1.8rem;">🔗</a>
        <a href="https://twitter.com/yourprofile" target="_blank" title="X (Twitter)" style="font-size: 1.8rem;">🐦</a>
        <a href="https://instagram.com/yourprofile" target="_blank" title="Instagram" style="font-size: 1.8rem;">📸</a>
    </div>
</footer>
""", unsafe_allow_html=True)
