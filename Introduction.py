import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Welcome to Finance Matrix", layout="centered")

#def card_button(label, description, key, bg_color, text_color):
    

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
        background: #E2F1FC;
        color: #E2F1FC;
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
        background-color: #E2F1FC;
        color: #E2F1FC;
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

    .info-container {
        background-color: #F4F8FC;          /* White background */
        border-radius: 15px;              /* Rounded corners */
        padding: 1.5rem 2rem;             /* Padding inside */
        width: 700px;                    /* Fixed width similar to cards */
        box-shadow: 0 2px 8px rgba(0,0,0,0.1); /* Subtle shadow */
        color: #333;                     /* Text color */
        text-align: left;                /* Left aligned text */
        margin: 2rem auto;               /* Vertical margin and center horizontally */
        font-size: 1rem;                 /* Comfortable font size */
        line-height: 1.5;                /* Better readability */
    }

    .info-container-101 {
        background-color: #FCFAE4;          /* White background */
        border-radius: 15px;              /* Rounded corners */
        padding: 1.5rem 2rem;             /* Padding inside */
        width: 700px;                    /* Fixed width similar to cards */
        box-shadow: 0 2px 8px rgba(0,0,0,0.1); /* Subtle shadow */
        color: #333;                     /* Text color */
        text-align: left;                /* Left aligned text */
        margin: 2rem auto;               /* Vertical margin and center horizontally */
        font-size: 1rem;                 /* Comfortable font size */
        line-height: 1.5;                /* Better readability */
    }

    .info-container-red {
        background-color: #FAE3E3;          /* White background */
        border-radius: 15px;              /* Rounded corners */
        padding: 1.5rem 2rem;             /* Padding inside */
        width: 700px;                    /* Fixed width similar to cards */
        box-shadow: 0 2px 8px rgba(0,0,0,0.1); /* Subtle shadow */
        color: #333;                     /* Text color */
        text-align: left;                /* Left aligned text */
        margin: 2rem auto;               /* Vertical margin and center horizontally */
        font-size: 1rem;                 /* Comfortable font size */
        line-height: 1.0;                /* Better readability */
    }

    .go-back-container {
        position: fixed;
        top: 20px;   /* Distance from top */
        left: 20px;  /* Distance from left */
        z-index: 9999; /* Make sure it stays on top */
    }

    .next-container {
        background-color: #F0ECF7;          /* White background */
        border-radius: 15px;              /* Rounded corners */
        padding: 1.5rem 2rem;             /* Padding inside */
        width: 700px;                    /* Fixed width similar to cards */
        box-shadow: 0 2px 8px rgba(0,0,0,0.1); /* Subtle shadow */
        color: #333;                     /* Text color */
        text-align: left;                /* Left aligned text */
        margin: 2rem auto;               /* Vertical margin and center horizontally */
        font-size: 1rem;                 /* Comfortable font size */
        line-height: 1.0;
    }
    .next-button-container {
        display: flex;
        justify-content: flex-end;
        max-width: 900px;
        margin: 0 auto 3rem auto;
    }

    .next-button-container {
        display: flex;
        justify-content: flex-end;
        max-width: 900px;
        margin: 0 auto 3rem auto;
    }
    div.stButton > button:first-child {
        white-space: normal;
        word-wrap: break-word;
        border-radius: 15px;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
        min-width: 220px;
        max-width: 100%;
        text-align: center;
    }

    .goB-button-container {
        display: flex;
        justify-content: flex-end;
        max-width: 900px;
        margin: 0 auto 3rem auto;
    }
    div.stButton > button:first-child {
        white-space: normal;
        word-wrap: break-word;
        border-radius: 15px;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
        min-width: 220px;
        max-width: 100%;
        text-align: center;
    }

    .cards-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 2rem;
        margin-bottom: 3rem;
    }

    .card {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        border-radius: 15px;
        padding: 2rem 2.5rem;
        width: 280px;
        color: white;
        box-shadow: 0 8px 20px rgba(37, 117, 252, 0.3);
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }

    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(37, 117, 252, 0.6);
    }

    .card-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .card-description {
        font-size: 1rem;
        line-height: 1.4;
    }

    /* Different background for second card */
    .card.financial-analysis {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        box-shadow: 0 8px 20px rgba(255, 75, 43, 0.3);
    }

    .card.financial-analysis:hover {
        box-shadow: 0 12px 30px rgba(255, 75, 43, 0.6);
    }
    div.stButton > button#{key} {{
            background: {bg_color};
            color: {text_color};
            border-radius: 15px;
            padding: 2rem 2.5rem;
            width: 320px;
            min-height: 150px;
            font-size: 1.35rem;
            font-weight: 700;
            border: none;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0,0,0,0.07);
            transition: transform 0.18s cubic-bezier(.4,2,.6,1), box-shadow 0.18s cubic-bezier(.4,2,.6,1);
            text-align: center;
            white-space: normal;
            word-wrap: break-word;
        }}
    div.stButton > button#{key}:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        }}

    </style>
    """, unsafe_allow_html=True)

    
if "page" not in st.session_state:
    st.session_state.page = ""


# --- Landing Page ---

def landing_page():
    
    st.markdown("""
    <div style = 'text-align: center;'>
        <h1 class="title-text">Welcome to Finance Matrix</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style = 'text-align: center; color: #ABABAD;'>
        <p> Welcome to the Finance Matrix, where I try to convert $1.000 of sales of digital products, within the 90 days challenege. Where I document everything.</p>
        <p> In the meanwhile explore the free resources on financial freedom and corporate finance. Feel free to subscribe to my newsletter to stay updated!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div style = 'text-align: center; color: #0B0B0B; font-size: 2rem;'>
        <p style = font-weight: bold;'>Finance Matrix Newsletter</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div style = 'text-align: center; color: #ABABAD;'>
        <p> Ready to master your finances? Join our newsletter for expert tips and practical strategies delivered straight to your inbox. Subscribe today and start making smarter money decisions!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 10px;"></div>', unsafe_allow_html=True)
     

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
        <b>FREE RESOURCES</b>
    </div>

    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)

    # Cards as buttons

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "Financial Freedom\n\nFree resources on financial freedom, budgeting and investment strategies.",
            key="btn_fin_freedom"
        ):
            st.session_state.page = "financial_freedom"
            st.rerun()

    with col2:
        if st.button(
            "Financial Analysis 101\n\nInsights into corporate finance, investments, and business growth.",
            key="btn_fin_analysis"
        ):
            st.session_state.page = "financial_analysis_101"
            st.rerun()


    st.markdown("---")


# --- Financial Freedom Page ---

def financial_freedom_page():
    st.header("Financial Freedom Calculator")
    st.markdown("""
        <div class="info-container">
        <div style= 'text-align: center; color: #A4A4A4;'>
            <p>🧮 Calculate how your funds will grow until retirement and how much you need to retire comfortably. The green box represents funds needed to retire comfortably, whereas the blue box represent the future value of your investment portfolio.</p>
        </div>
    """, unsafe_allow_html=True)
    

    # --- User Inputs ---
    current_funds = st.number_input("Current funds (USD):", min_value=0.0, value=0.0, format="%.2f")
    monthly_contribution = st.number_input("Monthly contribution (USD):", min_value=0.0, value=0.0, format="%.2f")
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
        <div style="background-color:#E0EFE1; border-radius:16px; padding:1.2em 1em; margin:1.5em 0; border:1.5px solid #b2e2c6;">
            <span style="color:#217a41; font-size:1.15rem; font-weight:600;">
                💡 Funds needed to retire comfortably: <span style="color:#167a2f">${funds_needed:,.2f}</span>
            </span>
        </div>
        """, unsafe_allow_html=True
    )

    # --- W Rate ---
    st.markdown(
        f"""
       <p><i>Withdrawal rate of 4% should suffice for 30 years of life in the retirement.</i></p>
        """, unsafe_allow_html=True
    )

    # --- Compounding growth calculation ---
    years = np.arange(0, years_until_retirement + 1)
    rate = expected_return / 100
    portfolio_values = []
    balance = current_funds
    for year in years:
        if year == 0:
            portfolio_values.append(balance)
        else:
            # Add contributions for the year
            balance = balance * (1 + rate) + monthly_contribution * 12
            portfolio_values.append(balance)

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
        <div style="background-color:#C7E4FB; border-radius:16px; padding:1.2em 1em; margin:1.5em 0; border:1.5px solid #98C9F2;">
            <span style="color:#1867C0; font-size:1.1rem; font-weight:600;">
                📈 End amount of funds when compounded: ${portfolio_values[-1]:,.2f}.</span>
            </span>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("""
    <div class="info-container">
        <p> ✅ Below you can acess the excel template for finacial budgeting and investing.</p>
        <p> The template will make it easier for you to calculate your monthly expenses and funds disposable for investing. </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)

    with open("template.xlsx", "rb") as f:
        excel_bytes = f.read()

        st.download_button(
        label="📥 Download Excel Template",
        data=excel_bytes,
        file_name="Budgeting_template.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    
    st.markdown('<div style="margin-top: 10px;"></div>', unsafe_allow_html=True)
    st.markdown("---")


    if st.button("Go Back"):
        st.session_state.page = ""
        st.rerun()

    

# --- Financial Analysis 101 Page ---
def financial_analysis_101_page():
    st.markdown("""
    <h1 style= 'text-align: center; margin-top: 2rem; margin-bottom: 2rem;'>
        📘 Financial Analysis 101 </h1>
    """,unsafe_allow_html=True)

    st.markdown("""
        <div style = 'text-align: center;'>
           <p>Detailed financial analysis is the foundation of company valuation and investing.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-container-101">
    <div style= 'text-align: center; color: #952F2F;'>
        <p>💬</p>
        <p><i> Whether you're an aspiring financial analyst, a business owner looking to understand your company's financials, or an investor seeking to make informed decisions, this course provides you with the essential tools and knowledge to dissect and interpret financial statements.
</i></p>
        <p><i>In this module, we will walk through key financial statements like balance sheets, income statements, and cash flow statements, and show how you can leverage them to evaluate financial health.
 </i></p>
        <p><i> Take your time to go through every matter, and make sure you understand it.</i></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 1px;"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p> 🧑‍💻 The balance sheet is a snapshot of a company's assets, liabilities, and equity at a specific point in time (e.g., December 31, 2023).  
            It illustrates the company's financial position, showing what it owns (assets), what it owes (liabilities), and the owners' stake in the company (equity).</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🏭 **ASSETS**", expanded=True):
        st.markdown("""

    <i>Assets are a company's possessions, reflecting its resources and capabilities. Key assets include cash, accounts receivable, inventory, PPE (Property, Plant, and Equipment), and intangible assets. Differentiating them involves assessing their nature (physical vs. non-physical) and liquidity (ease of conversion to cash).</i>

    <i>An asset is anything of value owned or controlled by a company that is expected to provide future economic benefit. This benefit can come from generating revenue, reducing expenses, or increasing purchasing power. Assets are a fundamental part of a company’s net worth and are critical for assessing its financial health and operational capacity.</i>

    Assets are classified in several ways, but the most common distinctions are:

    - **By Convertibility (Liquidity) 💰**
      - *Current Assets*: Expected to be converted into cash, sold, or consumed within one year or operating cycle. Examples: Cash, accounts receivable, inventory.
      - *Non-Current (Long-Term) Assets*: Provide value beyond one year. Examples: Property, plant, equipment, intangible assets.

    - **By Physical Existence 🏠**
      - *Tangible Assets*: Physical items like buildings, machinery.
      - *Intangible Assets*: Non-physical assets like patents, trademarks.

    - **By Usage ⚙️**
      - *Operating Assets*: Used in daily business operations.
      - *Non-Operating Assets*: Not essential to core operations.

    Assets are listed on the balance sheet in order of <b>liquidity, from most liquid to least</b>.

    """,unsafe_allow_html=True)


    st.markdown("""
    <div class="info-container-red">
    <div style= 'text-align: left; color: #C52A2A;'>
        <p>💡Important notice:</p>
        <p> This equiation shall hold true <b>at all times:</b> ASSETS  = LIABILITIES + EQUITY</p>
    </div>
    """, unsafe_allow_html=True)

    
    st.image("assets_example.png", caption = "Example of a Balance Sheet - Assets",
    use_container_width=True)

    st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p> 📊 Example balance sheet shows the state of the company's assets for the period 31.12.2020 - 31.12.2023. As stated, the financial statements are unaudited, meaning that there still could be changes made after revision. </p>
    </div>
    """, unsafe_allow_html=True)


    with st.expander("🏗️ **LONG TERM ASSETS**", expanded=False):
        st.markdown("""

    <i>Long-term assets, also known as non-current assets, are resources a company owns that provide value for more than one year. These assets are essential for supporting a company’s operations and growth over the long term.</i>

    Types of Long-Term Assets
    
    1. **Property, Plant, and Equipment (PP&E)**: Tangible assets like buildings, machinery, and land used in production or operations.
    2. **Intangible Assets**: Non-physical assets such as patents, trademarks, copyrights, and goodwill.
    3. **Long-Term Investments**: Investments in stocks, bonds, or other companies held for an extended period.
    4. **Other Assets**: Includes items like deferred tax assets or long-term receivables.

       
    
    **Importance**
    
    Long-term assets are critical for a company’s capacity to generate revenue and sustain competitive advantage. They are recorded at historical cost and typically depreciated or amortized over their useful lives to reflect wear and obsolescence.


    """, unsafe_allow_html=True)

    with st.expander("💰 **SHORT TERM ASSETS**", expanded=False):
        st.markdown("""

    <i>Short-term assets, also known as current assets, are resources that a company expects to convert into cash or use up within one year or one operating cycle, whichever is longer. These assets are crucial for maintaining liquidity, supporting daily operations, and meeting short-term financial obligations such as paying suppliers, employees, and other operating expenses.</i>

    KEY CATEGORIES:

    1. **Cash and Cash Equivalents**: The most liquid assets, including physical cash and bank deposits, used for immediate payments.
    2. **Accounts Receivable**: Amounts owed by customers for goods or services delivered but not yet paid for. This is a critical asset affecting cash flow.
    3. **Inventory**: Goods held for sale or production, which will be converted into cash once sold.
    4. **Short-Term Investments**: Highly liquid financial instruments like Treasury bills or certificates of deposit, intended to be converted into cash within a year. Or some Short-term given loans to the related parties.
    5. **Prepaid Expenses**: Payments made in advance for services or goods to be received later.



            """,unsafe_allow_html=True)

    st.markdown("""
    <div class="info-container-red">
    <div style= 'text-align: left; color: #C52A2A;'>
        <p> ⚠️ <b>Pay attention</b> to the assets that might be leased. Those assets are <b>NOT</b> in company's direct ownership, but they affect the balance sheet as well as the P&L statement. </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top: 1px;"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="next-container">
    <div style= 'text-align: left; color: #000000;'>
       <p><b>Next: Equity and Liabilities</b></p>
            <p>Now that you understand the assets side of the Balance Sheet, it is time to tackle also the Liabilities side. In the next chapter you will learn to:</p>
            <ul>
            <li>︎Identify how the company is financing itself (through debt or equity)</li>
            <li>︎Decide whether the company has any liquidity issues</li>
            <li>︎Calculate the gearing ratio of the company</li>
            </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

   # if st.button("Go Back"):
        #st.session_state.page = ""
        #st.rerun()
            
          # Next up button aligned right
   # with st.container():
    #    col1, col2 = st.columns([4,1])
     #   with col2:
      #      if st.button("Next up: Equity & Liabilities"):
                # Replace with your actual next page name or session state logic
       #         st.switch_page("pages/Equity & Liabilities.py")
        #        st.rerun()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(
            "<div style='display: flex; justify-content: flex-start;'>",
            unsafe_allow_html=True)
        if st.button("Go Back"):
            st.session_state.page = ""  # or your landing page
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        # Align the button to the right in the column
        st.markdown(
            "<div style='display: flex; justify-content: flex-end;'>",
            unsafe_allow_html=True
        )
        if st.button("Next up: Equity & Liabilities"):
            st.switch_page("pages/Equity & Liabilities.py")
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
      

# --- Main app navigation ---
page = st.query_params.get("page", "")

if st.session_state.page == "financial_freedom":
    financial_freedom_page()
elif st.session_state.page == "financial_analysis_101":
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
