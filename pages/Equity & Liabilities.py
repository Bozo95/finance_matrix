import streamlit as st

# Page config
st.set_page_config(
    page_title="Chapter 2: Equity and Liabilities",
    page_icon="📊",
    layout="centered",
)

# Custom CSS for consistent styling
st.markdown("""
<style>
.card-container {
    background-color: #ede9fe;  /* Light lavender */
    border-radius: 15px;
    padding: 1.5rem 2rem;
    max-width: 700px;
    margin: 2rem auto;
    font-size: 1rem;
    line-height: 1.5;
    color: #333;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    white-space: pre-wrap; /* preserve line breaks */
    word-wrap: break-word;
}
.card-title {
    font-weight: 700;
    font-size: 1.3rem;
    margin-bottom: 1rem;
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
div.stButton > button:first-child:hover {
    transform: scale(1.03);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
img.screenshot {
    display: block;
    margin: 1rem auto;
    max-width: 90%;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
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
.info-container-red {
    background-color: #FFD7D7;          /* White background */
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
.info-container-green {
    background-color: #CAFFBF;          /* White background */
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
.hover-row {
    position: relative;
    display: inline-block;
    cursor: pointer;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    background: #f5f5fa;
    margin-bottom: 1rem;
    font-size: 1rem;
    transition: background 0.2s;
}
.hover-row:hover {
    background: #FAE3E3;
}
.hover-explanation {
    display: none;
    position: absolute;
    left: 0;
    top: 110%;
    min-width: 450px;
    background: #FAE3E3;
    color: #333;
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 0.8rem 1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12);
    z-index: 10;
    font-size: 0.95rem;
}
.hover-row:hover .hover-explanation {
    display: block;
}

.next-container {
    background-color: #F3E4F5;          /* White background */
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
</style>
""", unsafe_allow_html=True)

# Title centered
st.markdown("<h1 style='text-align:center; margin-top: 2rem;'>📊 Chapter 2: Equity and Liabilities</h1>", unsafe_allow_html=True)

# Content sections

st.markdown("""
<div style = 'text-align: center;'>
           <p>Liabilities side of the Balance Sheet indirectly dictate how effective can company use its assets to produce cash flow.</p>
        </div>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p>💬 Equity and liabilities are the two fundamental components that finance a company’s assets and operations.</p>
        <p>While <b>equity</b> represents the owners’ stake and retained earnings invested in the business, <b>liabilities</b> are the obligations the company owes to external parties.</p>
        <p>Together, they form the right side of the balance sheet and provide insight into how a company funds its activities-whether through ownership capital or borrowed funds.</p>
        <p>Understanding the balance between equity and liabilities is essential for assessing a company’s financial health, stability, and risk.</p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("📘 **EQUITY**", expanded=True):
    st.markdown("""


    <i>Equity represents the owners’ residual interest in the company after all liabilities are deducted from assets. It includes shareholder contributions (paid-in capital), retained earnings, and reserves.</i>
    <p><i>By the type of the company, weather is it a private or a public company, equity composition varies. In private companies equity is held by a limited number of private investors or founders, often not publicly traded. Ownership changes are less liquid and more controlled.</i></p>
    <p><i>On the other hand in the public companies or also commonly reffered to as <b>Traded companies</b> equity is divided into shares traded on stock exchanges, accessible to the general public, with greater regulatory oversight and transparency.</i></p>

    **EQUITY RATIO**
    
    The equity ratio measures the proportion of a company’s assets financed by equity.
    A higher equity ratio indicates financial strength and lower reliance on debt.

    **Why Healthy Equity Matters**
    
    1. Strong equity provides a cushion against losses, supports borrowing capacity, and signals financial stability.
    2. Companies with weak equity are more vulnerable to financial distress.
    3. Leaving the companies more prone to the occurance of events like <b>Insolvency</b> or in sever case even <b>Banktrupcy</b>.
    
    A company becomes insolvent when it cannot meet its debt obligations or when liabilities exceed assets. Insolvency often leads to bankruptcy, where the company may be liquidated or restructured.

    <i>For a list of a specific requirements needed for a company to qualify as insolvent, look at your country's specific law that tackles that matter. In the USA, U.S. Code: Title 11 gives a complete overview on bankruptcy procedure.</i>.


""",unsafe_allow_html=True)

st.markdown("""
    <div class="info-container-red">
    <div style= 'text-align: left; color: #C52A2A;'>
        <p>💡<b> Equity ratio formula:</b></p>
        <p> EQUITY RATIO = (EQUITY / TOTAL ASSETS) x 100% </p>
        <p><i> It is a commonly used metrics within the banks, when deciding on the company's financial health and repayment capacity.</i>
    </div>
""", unsafe_allow_html=True)

    

with st.expander("🏙️ **LONG TERM LIABILITIES**", expanded=False):
    st.markdown("""

    <i>Long-term liabilities are financial obligations or debts that a company must pay off over a period longer than one year. Unlike short-term liabilities, which are due within 12 months, long-term liabilities extend beyond this timeframe and are crucial for financing a company’s long-term investments and growth.</i>

    
    <b>Think</b> of long-term liabilities as loans or debts that a company takes on to fund major purchases or projects, such as buying land, buildings, machinery, or expanding operations. Because these debts are paid back slowly over several years, they allow companies to invest in their future without immediately draining their cash reserves.

    **Common Examples of Long-Term Liabilities**
    
    1. **Long-Term Loans:** These are loans from banks or other lenders that must be repaid over multiple years. For example, a mortgage loan on a company’s office building might be repaid over 15 or 30 years.
    2. **Bonds Payable:** Companies may issue bonds to investors to raise capital. These bonds are promises to pay back the borrowed money with interest over a set period, often many years.
    3. **Pension Liabilities:** These represent the company’s obligations to pay retirement benefits to employees in the future.
    4. **Post-Retirement Healthcare Liabilities:** Some companies provide healthcare benefits to retired employees, creating long-term obligations.
    5. **Deferred Revenues:** Money received in advance for goods or services to be delivered in the future, beyond one year.
    6. **Provisions or Reservations:** These include estimated liabilities for employee benefits, warranties, or potential legal penalties that may arise over the long term.

    **Importance of Long-Term Liabilities**

    Long-term liabilities are essential because they help companies finance big investments without needing to pay everything upfront. By spreading payments over many years, companies can maintain liquidity and invest in growth. However, having too much long-term debt can increase financial risk, especially if the company struggles to generate enough cash flow to meet interest and principal payments.

    How Long-Term Liabilities Appear on the Balance Sheet

    On the balance sheet, liabilities are split into current (short-term) and long-term sections. Long-term liabilities are listed after current liabilities, ordered by their due dates. For example, a debt due in 18 months is listed before one due in 24 months.

    If any portion of a long-term liability is due within the next year, that portion is reclassified as a current liability to show the upcoming payment.

    **Key points for memorization**

    - Long-term liabilities are debts payable after one year.
    - They fund major investments and help companies grow without immediate cash outflows.
    - Examples include loans, bonds, pensions, and deferred revenues.
    - Proper management of long-term liabilities balances growth opportunities with financial risk.
    - Understanding these liabilities helps you assess a company’s long-term financial health and stability.

""",unsafe_allow_html=True)

st.markdown("""
    <div class="info-container-green">
    <div style= 'text-align: left; color: #398D3D;'>
        <p>💬<b> My view on Long Term Liabilities:</b></p>
        <p> Long term liabilities are not necessary "bad". For company expansion and investments, debt is needed. By economic theory the most efficient company is the on with 99% of debt in it's capital structure.</p>
        <p> Things get complicated if company ecounters different market conditions that affect the cash flow generation ability of the company. In that case, L-T obligations/debt needs to be restructured ASAP, as company could face lack of short term liquidity.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hover-row">
        🚧 <b>IBR</b> - Independant Business Review <b>(hover to read)</b>
        <div class="hover-explanation">
            <b>IBR</b> is a independant review of the current situation of the company. Banks ordert their clients (commpanies) to supply them with an IBR. Latter is performed by and individual finance consultancy agency. Purpose of the IBR is to give a bank or creditor, a clear vision of the
            current situation within the company, in regards to cash flow generation ability and debt servicing ability.
        </div>
    </div>
""", unsafe_allow_html=True)


with st.expander("💸 **SHORT TERM LIABILITIES**", expanded=False):
    st.markdown("""

    <i>Short-term liabilities, also known as current liabilities, are financial obligations that a company must settle within one year or within its normal operating cycle, whichever is longer. These liabilities represent the company’s immediate debts and obligations that require prompt payment, often using current assets like cash or accounts receivable.</i>
    <i>Because these liabilities are due quickly, managing them effectively is crucial for maintaining liquidity and avoiding cash flow problems.</i>

    **Common Examples of Short-Term Liabilities**
    
    1. **Accounts Payable:** Money owed to suppliers for goods or services already received but not yet paid for. This is one of the most common short-term liabilities.
    2. **Accrued Expenses:** Expenses that have been incurred but not yet paid, such as wages, utilities, and interest.
    3. **Short-Term Loans:** Loans or credit lines that must be repaid within a year, often used to cover temporary cash shortages.
    4. **Current Portion of Long-Term Debt:** The part of long-term loans that must be paid within the next 12 months.
    5. **Taxes Payable:** Taxes due to government authorities within the year, including income taxes, sales taxes, or payroll taxes.
    6. **Unearned Revenue:** Payments received in advance from customers for goods or services that will be delivered within the year.
    7. **Dividends Payable:** Dividends declared by the company’s board but not yet paid to shareholders.

    **Importance of Short-Term Liabilities**
    
    Short-term liabilities are critical because they reflect the company’s immediate financial obligations. Proper management ensures the company can meet these obligations without disrupting operations or damaging relationships with suppliers and employees. Failure to manage short-term liabilities can lead to liquidity crises, forcing a company to take costly emergency measures or even risk insolvency.
    
    Short-term liabilities are listed under the current liabilities section of the balance sheet. They are typically ordered by due date, with the most urgent obligations listed first. This helps investors and creditors assess the company’s short-term financial health and liquidity.


     **Key points for memorization**
    
    - Short-term liabilities are debts due within one year.
    - They include accounts payable, accrued expenses, short-term loans, taxes, and unearned revenue.
    - Managing these liabilities effectively is essential to maintain liquidity and operational stability.
    - They appear as current liabilities on the balance sheet and are closely monitored through liquidity ratios.
    - Understanding short-term liabilities helps you evaluate a company’s ability to meet its immediate financial commitments.

""",unsafe_allow_html=True)


st.image("equity_example.png", caption = "Example of a Balance Sheet - Equity & Liabilities",
    use_container_width=True)

st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p>⚠️<b> Key Financial Ratios Related to Short-Term Liabilities:</b></p>
        <p><b>Current Ratio:</b> Measures the company’s ability to cover short-term liabilities with short-term assets. A ratio above 1 indicates sufficient liquidity.</p>
        <p><b>Working Capital:</b> The difference between current assets and current liabilities, showing the net resources available to fund daily operations.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="next-container">
    <div style= 'text-align: left; color: #45298B;'>
       <p><b>Next: Balance Sheet Ratios</b></p>
            <p>Now that you understand the composition of the Balance Sheet, it is time to tackle also importance of the Balance Sheet ratios. In the next chapter you will learn to:</p>
            <ul>
            <li>︎Understand the company's operations through the working capital</li>
            <li>︎Decide on the financial health and structure of the company</li>
            <li>︎Calculate the gearing ratio of the company</li>
            </ul>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

#with col1:
 #   st.markdown(
  #      "<div style='display: flex; justify-content: flex-start;'>",
   #     unsafe_allow_html=True)
   # if st.button("Go Back"):
    #    st.session_state.page = ""  # or your landing page
     #   st.rerun()
    #st.markdown("</div>", unsafe_allow_html=True)

with col2:
        # Align the button to the right in the column
    st.markdown(
        "<div style='display: flex; justify-content: flex-end;'>",
        unsafe_allow_html=True)
    if st.button("Next up: Balance Sheet Ratios"):
        st.switch_page("pages/Balance Sheet Ratios.py")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# Next up button aligned right
#with st.container():
 #   col1, col2 = st.columns([4,1])
  #  with col2:
   #     if st.button("Next up: Balance Sheet Ratios"):
            # Replace with your actual next page name or session state logic
    #        st.switch_page("pages/Balance Sheet Ratios.py")
     #       st.rerun()
