import streamlit as st

# Page config
st.set_page_config(
    page_title="Chapter 4: Profit & Loss Statement",
    page_icon="💸",
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
.info-container-green {
    background-color: #E0EFE1;          /* White background */
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
st.markdown("<h1 style='text-align:center; margin-top: 2rem;'>💸 Chapter 4: Profit & Loss Statement</h1>", unsafe_allow_html=True)





# Content sections

st.markdown("""
<div style = 'text-align: center;'>
           <p>Profit & loss statement is the true indicator of the company's performance Something like a scoreboard in sports.</p>
        </div>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="info-container">
    <div style= 'text-align: left; color: #000000;'>
        <p>💬 The profit and loss statement-also known as the P&L, income statement, or statement of operations-is a <b>core financial report</b> that summarizes a company’s revenues, expenses, and resulting net profit or loss over a specific period, such as a month, quarter, or year.</p>
        <p>Unlike the balance sheet, which provides a snapshot at a single point in time, the P&L statement reveals how a business performed financially <b>during the period</b>, showing whether it generated profit or incurred a loss.</p>
        <p>By detailing key components like revenue, cost of goods sold, gross profit, operating expenses, and net income, the P&L offers vital insights into a company’s ability to generate earnings, control costs, and sustain growth.</p>
        <p>This statement is essential for business owners, investors, and creditors to assess financial health, make informed decisions, and <b>plan for the future.</b></i>
    </div>
    """, unsafe_allow_html=True)

with st.expander("💰 **NET SALES**", expanded=True):
    st.markdown("""


    <i>Net sales represent the total revenue a company earns from selling its goods or services after deducting returns, allowances, and discounts. It is a critical figure on the Profit & Loss (P&L) statement because it reflects the actual income generated from core business operations, providing a more accurate measure of sales performance than gross sales.</i>

    <i>On the P&L statement, net sales are typically reported near the top, immediately following or replacing the gross sales figure.</i>
   
    **Components and Considerations**

    1. **Gross Sales:** The total invoiced amount before any deductions.
    2. **Sales Returns:** Value of products customers have returned.
    3. **Sales Allowances:** Price reductions granted to customers for damaged or unsatisfactory goods.
    4. **Sales Discounts:** Reductions offered to customers for early payment or promotional reasons.

    **More on the individual components**
    
    - Returns and Allowances: These reduce revenue because they represent products that did not result in final sales or were sold at a reduced price.
    - Discounts: These encourage timely payment or bulk purchases but lower the net revenue realized.
    - Revenue Recognition: Companies must follow accounting standards (e.g., IFRS 15 or ASC 606) to recognize revenue accurately, ensuring net sales reflect earned income during the reporting period.

    **Importace of Net Sales** 

    <p>Net sales provide a realistic view of the revenue actually earned and collectible, serving as the foundation for calculating gross profit and subsequent profitability metrics.</p>
    <p>Analysts and managers closely monitor net sales trends to evaluate business growth, pricing strategies, and customer satisfaction.</p>
    <p>In summary, net sales are the true revenue figure after adjusting for all sales-related deductions, making them a vital starting point for understanding a company’s financial performance on the P&L statement.</p>


""",unsafe_allow_html=True)

st.markdown("""
    <div class="hover-row">
        🚧 <b>REVENUE PROJECTIONS</b><b> (hover to read)</b>
        <div class="hover-explanation">
            <p><b>Revenue Projections</b> play a crucial role in the valuation of a company because they provide a forward-looking estimate of the business’s ability to generate income and profits in the future.
            Accurate and well-supported revenue forecasts help investors, analysts, and stakeholders assess the company’s growth potential, market demand, and overall financial health, which are fundamental drivers of its value.</p>
            <p> Since valuation methods like <b>discounted cash flow (DCF)</b> rely heavily on future cash flows derived from revenue projections, the quality and realism of these projections directly influence the estimated worth of the company.</p>
            <p> Projections based on historical performance, market trends, and strategic plans create a clearer picture of expected revenue growth, profitability margins, and capital needs, allowing for a more reliable valuation.</p>
    </div>
""", unsafe_allow_html=True)
  

with st.expander("📚 **EXPENSES**", expanded=False):
    st.markdown("""

    <i>Expenses represent the costs a company incurs to operate its business and generate revenue during a specific period. They are a crucial part of the profit and loss (P&L) statement because they directly impact profitability by reducing the total revenue to arrive at net income or loss.
    Expenses cover a wide range of outflows, from direct costs associated with producing goods or services to indirect costs necessary for running the business.</i>

    **Categories of Expenses**

    Expenses on the P&L are typically broken down into several main categories:
    
    1. **Cost of Goods Sold (COGS):** These are direct costs tied to producing or purchasing the products sold by the company, such as raw materials, manufacturing labor, and shipping. COGS is subtracted from net sales to calculate gross profit.
    2. **Operating Expenses:** These include all costs required to run the business that are not directly linked to production. Common examples are:
        Selling Expenses: Advertising, marketing, sales commissions.
    4. **General and Administrative Expenses (G&A):** Salaries of administrative staff, office rent, utilities, insurance, professional fees, and office supplies.
    5. **Depreciation and Amortization:** Non-cash expenses that allocate the cost of tangible and intangible assets over their useful lives, reflecting wear, tear, and obsolescence.

    **How Expenses Are Reported?**

    Expenses are recorded on the P&L statement in the period they are incurred, following the accrual accounting principle. This means expenses are matched to the revenues they help generate, regardless of when the cash payment occurs. This matching provides a more accurate picture of profitability for the period.

    **Why Understanding Expenses Matters**

    Profitability Analysis: Expenses directly reduce gross and net profit, so controlling costs is vital for maintaining healthy margins.
    Operational Efficiency: Breaking down expenses helps identify areas where the company can improve efficiency or reduce waste.
    Budgeting and Forecasting: Historical expense data guides future budgeting, helping management plan resources and investments.
    Investor Insight: Investors and creditors analyze expense trends to assess management effectiveness and financial stability.

    **Examples of Expense Items**

    - Employee wages and benefits
    - Rent and utilities
    - Advertising and marketing campaigns
    - Office supplies and equipment maintenance
    - Professional services (accounting, legal)
    - Depreciation of machinery or software (non cash expense)

    
    <p> Expenses encompass all costs a company incurs to operate and generate revenue. They are categorized into <b>direct costs</b> like COGS and <b>indirect</b> operating expenses, including depreciation and interest.</p>
    <p> Properly tracking and managing expenses is essential for understanding profitability, improving efficiency, and making informed financial decisions.</p>
    <p> The P&L statement’s expense section provides a detailed view of where money is spent and how it affects the <b>company’s bottom line.</b></p>

""",unsafe_allow_html=True)


#---EXPENSES composition PICTURE-----

st.image("expenses.png", caption = "Example of Operating Expenses composition",
    use_container_width=True)

with st.expander("💸 **EBIT AND EBITDA**", expanded=False):
    st.markdown("""

    <p> To understand <b>EBIT</b> and <b>EBITDA</b>, it’s important to start with the company’s revenue and expenses as reported on the income (profit and loss) statement.</p>
    <p> The process begins with gross profit, which is calculated by subtracting the cost of goods sold (COGS) from total revenue.</p>
    
    <b>Next,</b> we subtract operating expenses-such as selling, general, and administrative expenses (SG&A)-from gross profit to arrive at EBIT (Earnings Before Interest and Taxes).
   
    <i>Alternatively, EBIT can be calculated starting from net income by adding back interest expense and tax expense.</i>
    
    <i>Alternatively, EBITDA can be derived directly from net income by adding back interest, taxes, depreciation, and amortization.</i>

    <p><b>EBIT</b> (Earnings Before Interest and Taxes) measures a company’s profitability from its core operations before deducting interest expenses and income taxes. It reflects operating income and shows how well the company generates profit from its business activities, regardless of its financing structure or tax situation.</p>
    <p><b>EBITDA</b> (Earnings Before Interest, Taxes, Depreciation, and Amortization) goes a step further by also excluding non-cash expenses-depreciation and amortization-from EBIT. This metric focuses on cash profitability by removing accounting charges related to asset wear and intangible asset amortization.</p>

    EBIT reflects the company’s operating profitability before the effects of financing costs and taxes, showing how well the core business is performing.

    **What They Represent?**

    EBIT represents operating profit, showing how efficiently a company runs its core business before financing and tax costs. It includes the impact of depreciation and amortization, which reflect the consumption of tangible and intangible assets.
    EBITDA approximates operating cash flow by excluding non-cash expenses, providing insight into the company’s ability to generate cash from operations. It is often preferred for comparing companies with different capital structures or asset bases.

    **Pratical use**
    
    EBIT is useful for analyzing profitability and operational efficiency, helping investors understand how well a company controls costs and generates earnings from its core activities.
    EBITDA is widely used in valuation and credit analysis because it highlights cash-generating ability, ignoring accounting policies and capital investment differences. It is especially valuable for companies with significant depreciation and amortization expenses.
    

""",unsafe_allow_html=True)

#----EBITDA and EBITDA % picture ------

st.image("EBITDA.png", caption = "Example of a EBITDA and EBITDA margin",
    use_container_width=True)

st.markdown("""
    <div class="hover-row">
        🚧 <b>EBITDA MULTIPLES</b><b> (hover to read)</b>
        <div class="hover-explanation">
            <p><b>EBITDA Multiple</b>, also known as the enterprise multiple, is a financial ratio that compares a company's enterprise value (EV) to its annual earnings before interest, taxes, depreciation, and amortization (EBITDA).</p>
            <p> This metric is widely used in <b>company valuation</b> because it provides a normalized way to compare the value of different businesses, regardless of their capital structure, tax environment, or accounting policies.</p>
    </div>
""", unsafe_allow_html=True)


with st.expander("⚖️ **FINANCIAL RESULT**", expanded=False):
    st.markdown("""

    <i>Financial revenues and financial expenses are components of a company’s profit and loss (P&L) statement that reflect income and costs related to the company’s financing activities rather than its core operations.</i>

    They arise primarily from interest, investments, and other financial transactions.

    - <p><b>Financial Revenues</b> typically include interest income earned on cash deposits, returns from investments, dividends received, and gains from financial instruments.</p>
    - <p><b>Financial Expenses</b> mainly consist of interest paid on borrowed funds (loans, bonds), bank fees, and losses on financial investments or currency exchange.</p>

    **How Are They Created?**

    These items are generated through a company’s financing and investing activities outside its primary business operations.

    **For example:**
    - When a company borrows money, it incurs interest expenses as a cost of financing ✅
    - When it holds cash or invests surplus funds, it may earn interest or dividends, recorded as financial revenues❌

    Gains or losses from selling financial assets or currency fluctuations also impact financial revenues or expenses.

    **What Do They Represent?**

    Financial revenues represent the income earned from managing the company’s financial resources, while financial expenses represent the costs of financing those resources. They reflect how effectively a company manages its capital structure and investment portfolio.

    **How Do They Affect the P&L Statement?**

    Financial revenues and expenses are reported below the operating profit line on the P&L statement, typically under a section called “financial result” or “net financial income/expense.” Their net effect-financial revenues minus financial expenses-impacts the company’s profit before tax but does not affect operating profit or core business profitability.

    1. <b>A positive net financial result</b> (more financial revenues than expenses) increases overall profitability.
    2. <b>A negative net financial result</b> (more financial expenses than revenues) reduces net profit and may signal higher borrowing costs or financial risk.

    **Why Are They Important?**

    <p>Investors and analysts pay attention to financial results to understand the impact of financing decisions on a company’s bottom line.</p>
    <p>High financial expenses can erode profits even if operating performance is strong, while strong financial revenues can boost overall earnings. However, because these items often stem from non-operating activities, they are analyzed separately from operating results to assess the company’s core business performance accurately.</p>

""",unsafe_allow_html=True)

with st.expander("✂️ **TAXES**", expanded=False):
    st.markdown("""

    <p><i>Income tax expense represents the <b>amount a company owes</b> to tax authorities based on its taxable income for the reporting period.
    It is recorded on the Profit & Loss (P&L) statement as a separate line item, typically <b>near the bottom</b>, after operating profit and financial results but before net income.</i></p>

    <p><i>Income tax expense includes both current taxes payable for the period and deferred taxes arising from timing differences between accounting income and taxable income.</i></p>

    **How Income Taxes Affect the P&L Statement**

    <p>Income tax expense <b>reduces pre-tax profit</b> to arrive at net profit or net income-the “bottom line” of the P&L. Because taxes are a significant cost, they have a direct impact on profitability and cash flow.</p>
    <p>Companies must estimate and record tax expenses accurately to reflect their true financial position and comply with accounting standards.</p>

    **Different Corporate Tax Rates Around the World**

    Corporate income tax rates vary significantly across countries, influencing where companies choose to operate and how they plan their finances:

    - **United States:** The federal corporate tax rate is 21%, with additional state taxes varying by state.
    - **European Union:** Rates differ widely; for example, Ireland has a low corporate tax rate of 12.5%, while France and Germany have rates around 25-30%.
    - **Asia:** Countries like Singapore and Hong Kong offer competitive rates around 17%, while others like Japan have rates closer to 30%.
    - **Emerging Markets:** Rates can range broadly, often between 20% and 30%, with some countries offering incentives or lower rates to attract investment.

    These differences affect multinational companies’ tax planning and profitability. Lower tax jurisdictions may attract more investment but also face scrutiny over tax avoidance.

    **Why Understanding Income Tax Is Important**

    - **Profitability Analysis:** Taxes significantly affect net income and shareholder returns.
    - **Cash Flow Planning:** Tax payments impact cash availability and financial strategy.
    - **Valuation:** Effective tax rates influence company valuations and investment decisions.
    - **Compliance and Risk:** Accurate tax expense reporting ensures compliance and reduces risk of penalties.

    Income tax expense on the P&L statement reflects the company’s tax obligations based on taxable income and varies according to local tax laws. It reduces pre-tax profit to net income and plays a crucial role in financial performance analysis. Understanding global corporate tax rate differences helps explain variations in profitability and informs strategic financial planning.

""",unsafe_allow_html=True)

st.markdown("""
    <div class="hover-row">
        🚧 <b>TAX RELIEFS</b><b> (hover to read)</b>
        <div class="hover-explanation">
            <p><b>Tax relief</b> refers to various government measures-such as tax deductions, credits, and exemptions-that reduce the amount of tax an individual or business owes.
            These reliefs lower taxable income or directly decrease the tax bill, thereby reducing the overall tax amount payable.</p>
            <p>By applying tax reliefs, companies can <b>significantly decrease</b> their tax burden, improve cash flow, and incentivize certain behaviors like , investing, or charitable giving.</p>
            <p><b>Examples include:</b> reliefs for investment in PPE items, investments in R&D, employing disabled persons etc.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="next-container">
    <div style= 'text-align: left; color: #45298B;'>
       <p><b>Next: Cash Flow Statement</b></p>
            <p>In the next chapter you will learn to tie it all up. Cash flow statement can show you company’s hidden secretes. You will learn to:</p>
            <ul>
            <li>︎Decide on the fact if company is actually making or losing money</li>
            <li>︎Understand how company uses the debt (for investments or business financing)</li>
            <li>︎Identify dividends payout</li>
            </ul>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

#with col1:
 #  st.markdown(
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
    if st.button("Next up: Cash Flow Statement"):
        st.switch_page("pages/Cash Flow Statement.py")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# Next up button aligned right
#with st.container():
 #   col1, col2 = st.columns([4,1])
  #  with col2:
   #     if st.button("Next up: Cash Flow Statement"):
            # Replace with your actual next page name or session state logic
    #        st.switch_page("pages/Cash Flow Statement.py")
     #       st.rerun()
