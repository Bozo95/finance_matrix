import streamlit as st

# Page config
st.set_page_config(
    page_title="Chapter 3: Balance Sheet Ratios",
    page_icon="📈",
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
st.markdown("<h1 style='text-align:center; margin-top: 2rem;'>📈 Chapter 3: Balance Sheet Ratios</h1>", unsafe_allow_html=True)

# Content sections

st.markdown("""
<div style = 'text-align: center;'>
           <p>Balance sheet ratios will give you straight insight into company's actual state. But do not get fooled. You need to dive in, to understand the underlying facts.</p>
        </div>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p>💬 Most commonly used balance sheet ratios are: <b> Working Capital Ratio </b>, <b> Current Ratio </b> and <b> Debt to Equity Ratio </b></p>
        <p>Balance sheet ratios are essential tools that help assess a company’s financial position at a specific point in time by analyzing the relationship between key balance sheet items such as assets, liabilities, and shareholders’ equity.</p>
        <p>These ratios provide deeper insight beyond the raw numbers, allowing investors, managers, and creditors to evaluate a company’s liquidity (ability to meet short-term obligations), leverage (use of debt financing), and overall financial stability.</p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("📘 **WORKING CAPITAL**", expanded=True):
    st.markdown("""


    <i>The working capital ratio is a fundamental measure of a company’s short-term financial health and liquidity. It is calculated by dividing current assets by current liabilities.</i>
    <i>Current assets include accounts receivable, inventory, and other assets expected to be converted into cash within a year, while current liabilities are obligations due within the same period, such as accounts payable and accrued expenses.</i>

    <i><b>Note:</b> Sometimes analysts also include cash items in the calculation of the working capital. I preffer the calculation without the cash items. This way i get more robust and <b>true</b> value of the working capital.</i>  

""",unsafe_allow_html=True)

#---WC comparison between the companies ----

st.image("wc_example.png", caption = "Example of a Working capital calculation",
    use_container_width=True)

st.markdown("""
    <div class="hover-row">
        🚧 <b>Working Capital</b> - Variations <b>(hover to read)</b>
        <div class="hover-explanation">
            <p><b>Working capital</b> varys due to specific industry company operates in. For example, working capital of the company XY Ltd. is very low (in relative terms to the Net Sales figure). On average it amounts to 3,8%.</p>
            <p> Observed company reports <b>no or very little inventories</b>. That indicates that we are dealing with a <b>service company</b>. On the other hand production companies report high amount of inventories, making a working capital figure bigger at the end.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p>💬 <b>Note to your future self:</b> Working capital projections play a major role in the company valuation, as it affects the net cash flow of the company. If the working capital is projected to increase over time,
            meaning that the company will need more cash to finance that increase, the calculated Enterprise Value of the company will be lower.</p>
        <p> So make sure to perform a thorough "working capital" analysis, based on the historic
            data for the company, as well as the projections of future operations.</p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("🏗️ **WORKING CAPITAL ADJUSTMENTS - IMPORTANT** ⚠️", expanded=True):
    st.markdown("""


    <i>Sometimes you will have to adjust the reported working capital to the "actual" working capital.</i>
    <i>By that I meand, that you will have to look at the ageing structure of the company's short term operating receivables and short term operating liabilities. Usually we discard items that are older or past due for more than 180 days (approx. 6 months).</i>

    <i><b>Note:</b> If you are not sure about the adjustments speak with the company's managament for additional explanations about the receivables and liabilities that are past due.</i>  

""",unsafe_allow_html=True)

    

with st.expander("️🚀 **CURRENT RATIO**", expanded=False):
    st.markdown("""

    <p><i>The current ratio is one of the most fundamental liquidity ratios used in financial analysis. It measures a company’s ability to meet its short-term obligations with its short-term assets. In simple terms, it tells us whether a business has enough resources that can be quickly converted into cash to pay off debts and liabilities due within one year.</i></p>
     
    <p><i><b>Current assets</b> include cash, marketable securities, accounts receivable, inventory, and prepaid expenses-basically assets expected to be converted into cash or used up within a year.</i></p>

    <p><i><b>Current liabilities</b> consist of accounts payable, short-term debt, accrued expenses, taxes payable, and the current portion of long-term debt-obligations due within the same timeframe.</i></p>

    **Interpretation of the Current Ratio**
    
    - Ratio > 1: The company has more current assets than current liabilities and can generally meet its short-term obligations without liquidity issues.
    - Ratio = 1: Current assets exactly cover current liabilities. This is a borderline position where the company can just meet its short-term debts but has little margin for error.
    - Ratio < 1: The company may struggle to pay off its short-term debts, indicating potential liquidity problems. However, some businesses with fast inventory turnover or quick receivables collection can operate safely with ratios below 1.

    **Industry and Context Matter**
    
    The “ideal” current ratio varies by industry and business model.

    For example:
    
    <b>Retail companies</b> often have higher ratios due to significant inventory and cash holdings.
    <b>Service companies</b> may have lower ratios because they hold less inventory and have faster cash conversion cycles.
    Companies with strong cash flows and rapid receivables collection can afford lower current ratios without risking liquidity.

    **Limitations of the Current Ratio**
    
    It treats all current assets equally, but some (like inventory or prepaid expenses) may not be easily or quickly converted to cash.
    It provides a snapshot at one point in time and may not reflect seasonal fluctuations or timing differences in cash flows.
    It does not measure the quality of assets or liabilities, so a high ratio could sometimes indicate inefficient use of resources or excess idle cash.
    For a more conservative view of liquidity, analysts often use the quick ratio, which excludes inventory and prepaid expenses from current assets.

    **Why Is the Current Ratio Important?**
    
    1. <b>For creditors and lenders:</b> It indicates the company’s ability to repay short-term debts, influencing credit decisions and loan terms.
    2. <b>For management:</b> It helps monitor operational efficiency and working capital management, guiding decisions on inventory, receivables, and payables.
    3. <b>For investors:</b> It signals financial health and risk, affecting investment decisions and valuation.


""",unsafe_allow_html=True)

st.markdown("""
    <div class="info-container-green">
    <div style= 'text-align: left; color: #398D3D;'>
        <p>💬<b> My take on Current Ratio:</b></p>
        <p> Current ratio will give you a general overview weather company is struggling to meet it's short term liabilities.</p>
        <p> As mentioned before, companies with high turnover rate of inventories, might report a negative current ratio. On paper it looks bad, but in reality you have to understand how the company operates day to day</p>
    </div>
""", unsafe_allow_html=True)



with st.expander("💸 **DEBT TO EQUITY RATIO**", expanded=False):
    st.markdown("""

    <p><i>The debt-to-equity ratio (D/E) is a key financial metric used to evaluate a company’s financial leverage and capital structure. It measures the relative proportion of debt and equity that a company uses to finance its assets and operations.</i></p>
    

    **What Does the Debt-to-Equity Ratio Tell Us?**

    - The debt-to-equity ratio answers the question: “For every dollar of equity contributed by shareholders, how many dollars of debt does the company have?” For example, a ratio of 2.0 means the company has 2 dollars of debt for every 1 dollar of equity.
    - A higher ratio indicates greater financial leverage (gearing), meaning the company relies more on borrowed funds. This can amplify returns during good times but also increases financial risk if earnings decline or cash flow tightens.
    - A lower ratio suggests a more conservative capital structure, with less reliance on debt and potentially lower financial risk, but possibly higher cost of capital since equity financing is often more expensive.

    **Why Is the Debt-to-Equity Ratio Important?**

    1. **Risk Assessment:** Creditors and investors use the D/E ratio to assess the company’s risk profile. A highly leveraged company may face difficulties meeting debt obligations during downturns, increasing the risk of insolvency.
    2. **Capital Structure Decisions:** Management uses this ratio to balance debt and equity financing, optimizing the cost of capital and financial flexibility.
    3. **Industry Context:** The "ideal" debt-to-equity ratio varies widely by industry. Capital-intensive sectors like utilities or telecommunications often operate with higher ratios, while technology or service companies tend to have lower ratios.


    **Key points for memorization**
    
    - The debt-to-equity ratio measures how a company finances its operations through debt versus equity.
    - It is a critical indicator of financial risk and leverage.
    - Interpretation depends on industry norms and company strategy.
    - A balanced ratio supports growth while managing risk; an excessively high ratio can signal financial distress.
    - Always consider this ratio alongside other financial metrics for a comprehensive analysis.
    - Understanding the debt-to-equity ratio equips you with insight into a company’s financial structure, risk exposure, and capital management strategy-essential knowledge for financial analysis and decision-making.

""",unsafe_allow_html=True)

st.markdown("""
    <div class="info-container-red">
    <div style= 'text-align: left; color: #C52A2A;'>
        <p>🧮<b> Debt to Equity (D/E) formula:</b></p>
        <p> D/E = Total Liabilities (L-T & S-T Financial liabilities) / Shareholder's Equity</p>
        <p><i> Note: Higher the D/E ratio, higher is the amount of debt in the capital strucutre of the company.</i></p>
        
    </div>
""", unsafe_allow_html=True)


#---Example of calculation --- hover

st.markdown("""
    <div class="hover-row">
        🚧 <b>Debt to equity ratio calculation </b> - EXAMPLE <b>(hover to read)</b>
        <div class="hover-explanation">
            <p> Suppose a company has total liabilities of $75 million and shareholders’ equity of $55 million.</p>
            <p> Debt to equity (D/E) calculation would imply that: </p>
            <p><b> D/E ratio = Total Liabilities / Equity = 75 million / 55 million = 1,36x.</b></p>
            <p><i> Latter implys rather high value of D/E ratio, which increases the "risk" of the company.</i></p>
        </div>
    </div>
""", unsafe_allow_html=True)

with st.expander("📊 **NET DEBT RATIO**", expanded=False):
    st.markdown("""

    <p><i>The net debt ratio is a key financial metric that measures a company’s overall indebtedness after accounting for its liquid assets, primarily cash and cash equivalents.</i></p>
    <p><i>It provides a clearer picture of the company’s true debt burden by subtracting highly liquid assets from total debt, reflecting how much debt would remain if the company used its cash reserves to pay down liabilities.</i></p>
    
    **What Does the Net Debt Ratio Tell Us?**

    The net debt ratio expresses net debt as a proportion of a relevant base, often total equity or EBITDA, to assess leverage and financial risk. It answers the question: After using all available cash, how much debt does the company still carry relative to its size or earnings?
    A low or negative net debt (where cash exceeds debt) indicates strong liquidity and financial flexibility. Such companies can easily cover their debts or even have surplus cash for investments.
    A high net debt signals greater leverage, implying higher financial risk and potential difficulty in meeting debt obligations during downturns.

    **Why Is the Net Debt Ratio Important?**

    1. **More Accurate Leverage Measure:** Unlike gross debt ratios, net debt accounts for cash reserves that could be used to pay down debt, providing a realistic view of financial obligations.
    2. **Liquidity Insight:** It shows how much debt remains after liquid assets are considered, helping assess the company’s ability to handle debt payments without raising additional funds.
    3. **Credit and Investment Decisions:** Lenders and investors use the net debt ratio to evaluate creditworthiness and financial stability, influencing borrowing costs and investment attractiveness.
    4. **Valuation and Enterprise Value:** Net debt is used in calculating enterprise value, which is crucial for mergers, acquisitions, and valuation analyses.

    **Key points for memorization**

    - The net debt ratio refines traditional debt measures by subtracting cash and equivalents from total debt.
    - It provides a realistic view of a company’s indebtedness and liquidity position.

    <p>A low or negative net debt ratio signals strong financial health, while a high ratio indicates greater leverage and risk.</p>
    <p>This ratio is vital for creditors, investors, and management to evaluate financial risk, borrowing capacity, and strategic decisions.
    Understanding the net debt ratio <b>equips you to analyze a company’s true leverage and financial resilience</b> beyond simple debt figures, making it an essential tool in financial analysis and corporate finance.</p>

""",unsafe_allow_html=True)

st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p>🧮<b> Net Debt Calculation - Example</b></p>
        <p> Suppose our observed company has:</p>
        <ul>
        <li> Short term debt: $350.000 </li>
        <li> Long term debt: $1.100.000 </li>
        <li> Cash items: $35.500 </li>
        <li> Short term financial investments (loans given to related companies): $50.000 </li>
        </ul>
        <p> Net debt would therefore be: 350.000 + 1.100.000 - 35.500 - 50.000 = <b>1.364.500</b></p>
        <p> This means the company effectively <b>still owes $1.364.500</b>, after using its cash and short term financial investments to pay down debt.</p>
        
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hover-row">
        🚧 <b> Use of Net Debt in Valuations</b><b> (hover to read)</b>
        <div class="hover-explanation">
            <p> In the first step of company valuation we compute the Enterprise value (EV).</p>
            <p> Than we add or substract the net debt number from the EV number. If the net debt is <b>positive</b>, meaning that it effectively ows X amount of $, we than <b>substract</b> that number from the EV number.</p>
            <p>If company holds for example $0 of debt items and
            $50.000 of cash items, we would add an addition of 50.000 to our EV value. In this case company reports <b>negative</b> value of net debt.</p>
            <p> Make sure to calculate the net debt value carefuly, in order to compute true EV of the company.</p>
        </div>
    </div>
""", unsafe_allow_html=True)



st.markdown("""
    <div class="next-container">
    <div style= 'text-align: left; color: #45298B;'>
       <p><b>Next: Profit & Loss Statement</b></p>
            <p>Now when you know which assets and liabilities company uses in it’s day to day operations, you are ready to learn, how effectively it uses them to generate revenues. You will learn to: </p>
            <ul>
            <li>︎Understand the company's business model</li>
            <li>︎Decide on the company's performance and profitability</li>
            <li>︎Calculate the net profit for the shareholders of the company</li>
            </ul>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

#with col1:
 #   st.markdown(
  #      "<div style='display: flex; justify-content: flex-start;'>",
   #     unsafe_allow_html=True)
    #if st.button("Go Back"):
     #   st.session_state.page = ""  # or your landing page
      #  st.rerun()
    #st.markdown("</div>", unsafe_allow_html=True)

with col2:
        # Align the button to the right in the column
    st.markdown(
        "<div style='display: flex; justify-content: flex-end;'>",
        unsafe_allow_html=True)
    if st.button("Next up: P&L Statement"):
        st.switch_page("pages/P&L Statement.py")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# Next up button aligned right
#with st.container():
 #   col1, col2 = st.columns([4,1])
  #  with col2:
   #     if st.button("Next up: P&L Statement"):
            # Replace with your actual next page name or session state logic
    #        st.switch_page("pages/P&L Statement.py")
     #       st.rerun()
