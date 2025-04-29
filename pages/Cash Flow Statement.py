import streamlit as st

# Page config
st.set_page_config(
    page_title="Chapter 5: Cash Flow Statement",
    page_icon="💰",
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
st.markdown("<h1 style='text-align:center; margin-top: 2rem;'>💰 Chapter 5: Cash Flow Statement</h1>", unsafe_allow_html=True)

# Content sections

st.markdown("""
<div style = 'text-align: center;'>
           <p>Cash Flow statement has no mercy. It is straight forward, weather your entitiy generates money or loses it. There is no inbetween.</p>
        </div>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p>💬 <b>The cash flow statement</b> is a vital financial report that details how cash moves into and out of a company over a specific period, such as a quarter or fiscal year.</p>
        <p> Unlike the income statement, which records revenues and expenses on an accrual basis, the cash flow statement focuses solely on actual cash transactions, providing a clear picture of liquidity and cash management.</p>
        <p> It breaks down cash flows into three main categories: <b>operating activities</b>, <b>investing activities</b> and <b>financing activities</b>.
        <p> By showing the sources and uses of cash, this statement helps investors, managers, and creditors assess a company’s ability to sustain operations, fund growth, meet obligations, and return value to shareholders.</p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("📈 **OPERATING CASH FLOW**", expanded=True):
    st.markdown("""


    <p><i>Operating cash flow (OCF) is a vital component of the cash flow statement that reflects the cash generated or consumed by a company’s core business operations during a specific period.</p>
    <p>It shows whether the company’s day-to-day activities are producing enough cash to sustain operations, invest in growth, and meet financial obligations without relying on external financing.</i></p>

    **What Is Operating Cash Flow?**

    Operating cash flow represents the actual cash inflows and outflows directly related to producing and delivering goods or services.
    Unlike net income, which includes non-cash items and accounting adjustments, OCF focuses strictly on cash transactions from operations.

    **How Is Operating Cash Flow Calculated?**

    There are two primary methods to calculate operating cash flow:

    1. **Indirect Method (Most Common)**
    This method starts with net income from the income statement and adjusts for:
    Non-cash expenses: Add back depreciation, amortization, and other non-cash charges.
    Changes in working capital: Adjust for increases or decreases in current assets and liabilities, such as accounts receivable, inventory, accounts payable, and accrued expenses.
    Other operating cash items: Adjust for gains or losses on sales of assets, deferred taxes, and other items affecting operating cash but not included in net income.
    2. **Direct Method**
    This method lists actual cash receipts and payments, including:
    Cash received from customers
    Cash paid to suppliers and employees
    Cash paid for operating expenses, interest, and taxes

    Although more transparent, the direct method is less commonly used due to the detailed data required.

    **Why Is Operating Cash Flow Important?**

    - **Liquidity Indicator:** OCF shows if the company generates sufficient cash from its core business to maintain operations and fund investments without external financing.
    - **Profit Quality:** Comparing net income to OCF helps assess the quality of earnings. If net income is high but OCF is low or negative, it may indicate issues like aggressive revenue recognition or poor cash collection.
    - **Financial Health:** Positive and growing OCF signals a healthy, sustainable business, while persistent negative OCF may warn of operational problems or cash flow constraints.
    - **Debt Servicing and Dividends:** Lenders and investors look at OCF to evaluate the company’s ability to repay debt and pay dividends.


""",unsafe_allow_html=True)

st.markdown("""
    <div class="info-container-green">
    <div style= 'text-align: left; color: #398D3D;'>
        <p>⚠️ <b>Key Considerations</b> to pay attention to:</p>
        <ul>
        <li><b>Working Capital Changes:</b> Large increases in accounts receivable or inventory consume cash, reducing OCF, while increases in accounts payable provide a temporary cash boost.</li>
        <li><b>Seasonality:</b> Some businesses have seasonal cash flow patterns; understanding these helps interpret OCF fluctuations.</li>
        <li><b>Non-Recurring Items:</b> One-time cash inflows or outflows related to operations (e.g., legal settlements, restructuring costs) should be identified and considered separately.</li>
        <li><b>Consistency Over Time:</b> Trends in OCF over multiple periods provide better insight than a single period snapshot.</li></p>
        </ul>
    </div>
    """, unsafe_allow_html=True)
  

with st.expander("⚙️ **CASH FLOW FROM INVESTMENTS**", expanded=False):
    st.markdown("""

    <i>Cash flow from investing activities <b>(CFI)</b> is a key section of the cash flow statement that reports the cash inflows and outflows related to a company’s long-term investments and capital expenditures.
    It reflects how much cash a company spends on acquiring or improving fixed assets like property, plant, and equipment (PP&E), as well as cash received from the sale of such assets or investments.
    This section provides insight into <b>how a company is investing</b> in its future growth and operational capacity.</i>

    **What Does Cash Flow from Investing Include?**

    **Cash Outflows:**

    1.Purchase of fixed assets such as buildings, machinery, and equipment (capital expenditures or CapEx).
    2.Acquisition of other businesses or subsidiaries.
    3.Purchase of investments in securities or equity stakes in other companies.
    4.Loans made to other entities.

    **Cash Inflows:**

    1. Proceeds from the sale of fixed assets or property.
    2. Cash received from divestitures or selling parts of the business.
    3. Sale or maturity of investment securities.
    4. Repayment of loans made to others.

    **Why Is Cash Flow from Investing Important?**

    - **Indicator of Growth and Strategy:** Negative cash flow from investing is often a positive sign, showing that a company is investing in its long-term growth through asset purchases or acquisitions.
    - **Cash Usage Insight:** It reveals how much cash is tied up in capital expenditures or investments, which may affect liquidity in the short term.
    - **Performance Assessment:** Investors use this section to evaluate whether a company is wisely allocating capital to sustain or expand operations.
    - **Cash Flow Sustainability:** A company consistently generating positive cash flow from investing (selling assets) without reinvesting may face future operational challenges

    <p>Cash flow from investing activities tracks the cash a company spends and receives from long-term investments and asset transactions.
    It provides crucial insight into how a company is investing in its future and managing its capital assets.
    While negative cash flow here often indicates growth investments, analyzing this section alongside operating and financing cash flows gives a comprehensive view of a company’s financial health and strategy.</p>


""",unsafe_allow_html=True)


with st.expander("📊 **CASH FLOW FROM FINANCING**", expanded=False):
    st.markdown("""

    <i>Cash flow from financing activities <b>(CFF)</b> represents the net cash a company raises or repays through transactions involving its capital structure during a specific period.
    This section of the cash flow statement shows <b>how a company funds its operations</b> and growth by raising money from or returning money to its investors and creditors.</i>

    What Does Cash Flow from Financing Include?

    **Cash Inflows:**

    1. Proceeds from issuing new equity shares (stock issuance).
    2. Proceeds from borrowing funds through loans or bond issuances.

    **Cash Outflows:**

    1. Repayment of debt principal (loan repayments, bond redemptions).
    2. Dividends paid to shareholders.
    3. Share repurchases (buybacks).

    **Why Is Cash Flow from Financing Important?**

    - **Funding Operations and Growth:** CFF reveals how a company finances its activities, whether through equity, debt, or returning capital to shareholders.
    - **Financial Strategy Insight:** Positive CFF indicates raising more funds than repaid, often signaling expansion or new investments. Negative CFF usually reflects debt repayment or returning capital, which might indicate financial prudence or liquidity constraints.
    - **Risk Assessment:** Persistent reliance on external financing (high positive CFF) can increase financial risk due to debt burdens, while steady repayments and dividends (negative CFF) can reflect stability and shareholder value focus.
    - **Liquidity and Capital Structure:** Understanding CFF helps stakeholders evaluate how financing decisions impact cash availability and long-term solvency.


    Neither a positive nor negative CFF is inherently good or bad; context matters.

    For example, raising capital through debt or equity can fuel growth but may increase risk.
    Consistent negative CFF due to dividends and debt repayments can signal strong cash flow and financial health but may also indicate limited growth opportunities.
    Large fluctuations in CFF should be analyzed alongside operating and investing cash flows to get a full picture of financial health.

    

""",unsafe_allow_html=True)


#---CASHFLOW PICTURE-----

st.image("cash_flow.png", caption = "Example of complete Cash Flow Statement",
    use_container_width=True)

st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p>🧠<b> CASH FLOW BRAIN FOOD</b></p>
        <p> When calculating the changes in cash flows categories, one has to be really focused as mistakes like to creep in on this one.</p>
        <p> <b>For Example:</b> If the company <b>Increased</b> the amount of inventories compared to the previous year, that means that it paid money to buy more stock. Latter shows as a cash <b>outflow.</b></p>
        <p> On the other hans if the company <b>Increased</b> the amount of Short-term liabilities compared to the previous year, that means that it received "new" money from the banks or other creditors. Latter shows as a cash <b>inflow.</b></p>
    </div>
""", unsafe_allow_html=True)


with st.expander("💵 **NET CASH FLOW**", expanded=False):
    st.markdown("""

    <i>Net cash flow is a fundamental financial metric that represents the difference between the total cash inflows and total cash outflows of a business over a specific period.
    It provides a clear measure of how much cash a company has generated or used, reflecting its liquidity and ability to fund operations, investments, and financing activities without relying excessively on external sources.</i>

    **Components of Net Cash Flow**

    Net cash flow is the sum of cash flows from three main activities, as reported in the cash flow statement:

    - **Operating Activities:** Cash generated or used by core business operations.
    - **Investing Activities:** Cash used for or generated from buying and selling long-term assets and investments.
    - **Financing Activities:** Cash raised from or paid to investors and creditors, including debt issuance, repayments, dividends, and equity transactions.

    **Importance of Net Cash Flow**

    - Liquidity and Financial Health: Positive net cash flow indicates that a company can cover its expenses and obligations, invest in growth, and return value to shareholders. Negative net cash flow over extended periods may signal financial distress.
    - Profit Quality: Net cash flow provides a reality check against accrual-based net income, which can include non-cash items and accounting adjustments. A company might report profits but still experience cash shortages.
    - Decision-Making: Investors, creditors, and management use net cash flow to assess the company’s ability to sustain operations, repay debts, and fund future projects.

    
    Net cash flow is a vital indicator of a <b>company’s cash generation</b> and usage during a period. By subtracting total cash outflows from inflows, it offers a clear picture of liquidity and operational efficiency.
    <p>Analyzing net cash flow alongside its components-operating, investing, and financing cash flows-enables stakeholders to understand the sources and uses of cash, guiding informed financial decisions and long-term planning.</p>

     """,unsafe_allow_html=True)
    
st.markdown("""
    <div class="info-container-green">
    <div style= 'text-align: left; color: #398D3D;'>
        <p>🧠<b> NET CASH FLOW FORMULA</b></p>
        <p> Net Cash Flow formula follows as = CFO + CFI + CFF</p>
        <p> <i>Where CFO, CFI, and CFF represent cash flows from operating, investing, and financing activities, respectively.</i></p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hover-row">
        🚧 <b>FREE CASH FLOW VALUATION</b><b> (hover to read)</b>
        <div class="hover-explanation">
            <p><b>FCFF</b>, also known as <b>Free Cash Flow to the Frim</b>, is a critical metric in company valuation because it represents the cash generated by the business that is available to all capital providers-both debt and equity holders-after covering operating expenses and necessary investments in working capital and fixed assets.</p>
            <p>FCFF provides a clear, cash-based measure of a company’s ability to generate sustainable value, making it the foundation of discounted cash flow (DCF) valuation models.
            By estimating the <b>present value of future FCFF discounted</b> at the weighted average cost of capital (WACC), analysts can determine the intrinsic value of the entire firm, independent of its capital structure.</p>
            <p>This approach is especially important when dividends are irregular or not paid, or when assessing the firm from a control perspective, as it captures the true cash-generating capacity and growth potential of the business</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="next-container">
    <div style= 'text-align: center; color: #45298B;'>
       <p><b>A Final Word</b></p>
            <p>Thank you for putting your trust and resources in me to help you with understanding financial analysis.
            I created this modul to help the beginners and finance student I was 8 years ago - someone who didn't know lots about corporate finances and had to go through hours of materials, the old school way, by reading lots of corporate finance handbooks.
            I also encourage you to dive deeper and take on few handbooks yourself.</p>
        <p> I've put everything I've learned throughout the years at the University as well as years at student jobs and regular jobs, into these modules, from my own mistakes and successes.
            Whether you're just starting your corporate career or just find finances interesting, I hope this module gives you the adequate tools and insights to help you analyse the financials of any company in the world.</p>
        <p>Analysing the Company’s financials can be dull and boring. I hope I’ve showed you few tips that will make financial analysis more fun and enjoyable.
</p>
        <p><b>All the best --Božidar</b>
</p>
    </div>
    """, unsafe_allow_html=True)


