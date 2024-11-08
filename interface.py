from dash import html, dcc


def calc_input(label, icon, description):
    return html.Div([
        html.Div([
            html.Span(**{'data-uk-icon': f'icon: {icon}'}, className='uk-form-icon'),
            dcc.Input(placeholder=label, type='text', className='uk-input')
        ], className='uk-inline'),
        html.Div(description, className='uk-text-small uk-padding-small uk-padding-remove-top')
    ], className='uk-margin')


nav_link = lambda href, title: html.Li(
    html.A(title, href=href)
)

return_button = html.A([
    html.Span(**{'data-uk-icon': 'icon: chevron-left; ratio: 1.5'})
], href='#')

calculator_group1 = [nav_link(href, title) for href, title in [
    ("#potential-interest-calculators", "Simple Interest Calculator"),
    ("#potential-interest-calculators", "Compound Interest Calculator"),
    ("#potential-interest-calculators", "Savings Interest Calculator")
]]
calculator_group2 = [nav_link(href, title) for href, title in [
    ("#return-on-investment-calculators", "Basic ROI Calculator"),
    ("#return-on-investment-calculators", "Annualised ROI Calculator"),
    ("#return-on-investment-calculators", "Adjusted ROI for Taxes and Fees")
]]
calculator_group3 = [nav_link(href, title) for href, title in [
    ("#loan-amortisation-calculators", "Fixed-Rate Loan Amortization Calculator"),
    ("#loan-amortisation-calculators", "Adjustable-Rate Loan Amortization Calculator"),
    ("#loan-amortisation-calculators", "Mortgage Loan Amortization Calculator"),
    ("#loan-amortisation-calculators", "Car Loan Amortization Calculator")
]]
calculator_group4 = [nav_link(href, title) for href, title in [
    ("#other-relevant-financial-metrics-calculators", "Net Present Value (NPV) Calculator"),
    ("#other-relevant-financial-metrics-calculators", "Internal Rate of Return (IRR) Calculator"),
    ("#other-relevant-financial-metrics-calculators", "Debt-to-Income Ratio Calculator"),
    ("#other-relevant-financial-metrics-calculators", "Break-Even Point Calculator"),
    ("#other-relevant-financial-metrics-calculators", "Future Value (FV) Calculator"),
    ("#other-relevant-financial-metrics-calculators", "Cash Flow Calculator"),
    ("#other-relevant-financial-metrics-calculators", "Payback Period Calculator"),
    ("#other-relevant-financial-metrics-calculators", "Profit Margin Calculator")
]]

potential_interest_calculator_tab = html.Div([
    html.Div([
        html.Div([
            html.H4('Simple Interest Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Principal (P)', icon='bag',
                               description='The initial amount of money that is being invested or '
                                           'loaned.'),
                    calc_input(label='Interest Rate (R)', icon='arrow-up-right',
                               description='The annual interest rate, usually provided as a '
                                           'percentage (e.g., 5%)'),
                    calc_input(label='Time (T)', icon='clock',
                               description='The time period for which the interest is calculated, '
                                           'typically in years.'),
                    html.Div([
                        html.Div(['Result'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' per year'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4(['Compound Interest Calculator']),
            html.Form([
                html.Fieldset([
                    calc_input(label='Principal (P)', icon='bag',
                               description='The initial amount of money that is being invested or '
                                           'loaned.'),
                    calc_input(label='Interest Rate (R)', icon='arrow-up-right',
                               description='The annual interest rate, usually provided as a '
                                           'percentage (e.g., 5%)'),
                    calc_input(label='Time (T)', icon='clock',
                               description='The time period for which the interest is '
                                           'calculated, typically in years.'),
                    calc_input(label='Compounding Frequency (n)', icon='calendar',
                               description='The number of times the interest is compounded '
                                           'per year (e.g., annually, semi-annually, quarterly, '
                                           'monthly, daily).'),
                    html.Div(['Common values for compounding frequency:'],
                             className='uk-text-small uk-padding-small uk-padding-remove-top'),
                    html.Div([
                        html.Ul([
                            html.Li(['Annually (n = 1)']),
                            html.Li(['Semi-Annually (n = 2)']),
                            html.Li(['Quarterly (n = 4)']),
                            html.Li(['Monthly (n = 12)']),
                            html.Li(['Daily (n = 365)'])
                        ], className='uk-list uk-list-collapse uk-list-disc')
                    ], className='uk-text-small uk-padding-small uk-padding-remove-top'),
                    html.Div([
                        html.Div(['Result'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span('0.00', className='uk-text-bolder'), ' per year'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4(['Savings Interest Calculator']),
            html.Form([
                html.Fieldset([
                    calc_input(label='Principal (P)', icon='bag',
                               description='The initial amount of money that is being '
                                           'invested or loaned.'),
                    calc_input(label='Monthly Contributions (C)', icon='mail',
                               description='The amount of money added to the account each '
                                           'month, if applicable.'),
                    calc_input(label='Annual Interest Rate (R)', icon='mail',
                               description='The interest rate provided by the savings '
                                           'account, usually expressed as a percentage.'),
                    calc_input(label='Time (T)', icon='clock',
                               description='The duration for which the savings will '
                                           'accumulate interest, typically measured in years.'),
                    calc_input(label='Compounding Frequency (n)', icon='calendar',
                               description='The number of times the interest is compounded '
                                           'per year (e.g., annually, semi-annually, quarterly, '
                                           'monthly, daily).'),
                    html.Div(['Common values for compounding frequency:'],
                             className='uk-text-small uk-padding-small uk-padding-remove-top'),
                    html.Div([
                        html.Ul([
                            html.Li(['Annually (n = 1)']),
                            html.Li(['Semi-Annually (n = 2)']),
                            html.Li(['Quarterly (n = 4)']),
                            html.Li(['Monthly (n = 12)']),
                            html.Li(['Daily (n = 365)'])
                        ], className='uk-list uk-list-collapse uk-list-disc'),
                    ], className='uk-text-small uk-padding-small uk-padding-remove-top'),
                    html.Div([
                        html.Div(['Result'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span('0.00', className='uk-text-bolder'), ' per year'
                        ]),
                        html.Hr()
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ])
], **{'data-uk-grid': 'masonry: pack'}, className='uk-child-width-1-2@m uk-margin-medium-top')

return_on_investment_calculator_tab = html.Div([
    html.Div([
        html.Div([
            html.H4('Basic ROI Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Initial Investment (I)', icon='bag',
                               description='The starting amount of money invested.'),
                    calc_input(label='Final Value (F)', icon='arrow-up-right',
                               description='The value of the investment after it has matured.'),
                    html.Div([
                        html.Div(['Result'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00%'], className='uk-text-bolder'), ' ROI'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Annualised ROI Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Initial Investment (I)', icon='bag',
                               description='The starting amount of money invested.'),
                    calc_input(label='Final Value (F)', icon='arrow-up-right',
                               description='The value of the investment at the end of the period.'),
                    calc_input(label='Number of Years (N)', icon='clock',
                               description='The total number of years the investment was held.'),
                    html.Div([
                        html.Div(['Result'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00%'], className='uk-text-bolder'), ' Annualised ROI'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Adjusted ROI Calculator for Taxes and Fees'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Initial Investment (I)', icon='bag',
                               description='The starting amount of money invested.'),
                    calc_input(label='Final Value (F)', icon='arrow-up-right',
                               description='The value of the investment at the end of the period.'),
                    calc_input(label='Number of Years (N)', icon='clock',
                               description='The total number of years the investment was held.'),
                    calc_input(label='Taxes (%)', icon='tag',
                               description='The percentage of taxes applied to the profit.'),
                    calc_input(label='Fees (%)', icon='credit-card',
                               description='The percentage of fees applied to the profit.'),
                    html.Div([
                        html.Div(['Result'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00%'], className='uk-text-bolder'), ' Adjusted ROI after Taxes and Fees'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ])
], **{'data-uk-grid': 'masonry: pack'}, className='uk-child-width-1-2@m uk-margin-medium-top')

loan_amortisation_calculator_tab = html.Div([
    html.Div([
        html.Div([
            html.H4('Fixed-Rate Loan Amortisation Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Loan Amount (Principal)', icon='credit-card',
                               description='The total amount of the loan.'),
                    calc_input(label='Annual Interest Rate (%)', icon='tag',
                               description='The annual fixed interest rate of the loan.'),
                    calc_input(label='Loan Term (Years)', icon='calendar',
                               description='The number of years to pay off the loan.'),
                    html.Div([
                        html.Div(['Monthly Payment'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' per month'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Mortgage Loan Amortisation Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Home Price', icon='home',
                               description='The total price of the home being purchased.'),
                    calc_input(label='Down Payment (%)', icon='credit-card',
                               description='The percentage of the home price paid upfront.'),
                    calc_input(label='Loan Term (Years)', icon='calendar',
                               description='The number of years over which the mortgage will be repaid.'),
                    calc_input(label='Annual Interest Rate (%)', icon='tag',
                               description='The yearly interest rate of the mortgage.'),
                    html.Div([
                        html.Div(['Monthly Mortgage Payment'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' per month'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Car Loan Amortisation Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Car Price', icon='cart',
                               description='The total cost of the car being financed.'),
                    calc_input(label='Down Payment (%)', icon='credit-card',
                               description='The initial payment made, expressed as a percentage of the car price.'),
                    calc_input(label='Loan Term (Years)', icon='calendar',
                               description='The number of years over which the car loan will be repaid.'),
                    calc_input(label='Annual Interest Rate (%)', icon='tag',
                               description='The yearly interest rate applied to the car loan.'),
                    html.Div([
                        html.Div(['Monthly Car Loan Payment'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' per month'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ])
], **{'data-uk-grid': 'masonry: pack'}, className='uk-child-width-1-2@m uk-margin-medium-top')

other_relevant_financial_metrics_calculator_tab = html.Div([
    html.Div([
        html.Div([
            html.H4('Net Present Value (NPV) Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Initial Investment', icon='bag',
                               description='The initial amount invested at the start of the project.'),
                    calc_input(label='Discount Rate (%)', icon='shrink',
                               description='The rate of return used to discount future cash flows.'),
                    calc_input(label='Cash Flow Year 1', icon='calendar',
                               description='The cash inflow/outflow for the first year.'),
                    calc_input(label='Cash Flow Year 2', icon='calendar',
                               description='The cash inflow/outflow for the second year.'),
                    calc_input(label='Cash Flow Year 3', icon='calendar',
                               description='The cash inflow/outflow for the third year.'),
                    html.Div([
                        html.Div(['Net Present Value (NPV)'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' currency units'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Internal Rate of Return (IRR) Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Initial Investment', icon='bag',
                               description='The initial amount invested at the start of the project.'),
                    calc_input(label='Cash Flow Year 1', icon='calendar',
                               description='The cash inflow/outflow for the first year.'),
                    calc_input(label='Cash Flow Year 2', icon='calendar',
                               description='The cash inflow/outflow for the second year.'),
                    calc_input(label='Cash Flow Year 3', icon='calendar',
                               description='The cash inflow/outflow for the third year.'),
                    calc_input(label='Cash Flow Year 4', icon='calendar',
                               description='The cash inflow/outflow for the fourth year.'),
                    calc_input(label='Cash Flow Year 5', icon='calendar',
                               description='The cash inflow/outflow for the fifth year.'),
                    html.Div([
                        html.Div(['Internal Rate of Return (IRR)'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' %'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Debt-to-Income (DTI) Ratio Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Total Monthly Debt Payments', icon='credit-card',
                               description='The total monthly payments for all your debts, including mortgages, '
                                           'loans, credit cards, etc.'),
                    calc_input(label='Gross Monthly Income', icon='users',
                               description='Your total monthly income before taxes and deductions.'),
                    html.Div([
                        html.Div(['Debt-to-Income Ratio (DTI)'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' %'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Break-Even Point (BEP) Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Fixed Costs', icon='cloud-upload',
                               description='These are the costs that remain constant regardless of the production or sales '
                                           'volume, such as rent, salaries, utilities, etc.'),
                    calc_input(label='Variable Cost per Unit', icon='bag',
                               description='The costs that vary with the production or sales volume, such as materials '
                                           'or labor costs for each unit produced or sold.'),
                    calc_input(label='Price per Unit', icon='credit-card',
                               description='The selling price for each unit of product or service.'),
                    html.Div([
                        html.Div(['Break-Even Point (Units)'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' units'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Future Value (FV) Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Present Value (PV)', icon='calendar',
                               description='The initial investment or principal amount at the beginning of the time period.'),
                    calc_input(label='Annual Interest Rate (r)', icon='arrow-up-right',
                               description='The annual interest rate, typically expressed as a percentage (e.g., 5%).'),
                    calc_input(label='Number of Periods (t)', icon='clock',
                               description='The number of time periods (usually years) for which the investment will grow.'),
                    calc_input(label='Compounding Frequency (n)', icon='refresh',
                               description='The number of times the interest is compounded per year (e.g., monthly = 12, quarterly = 4).'),
                    html.Div([
                        html.Div(['Future Value (FV)'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' currency'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Cash Flow Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Cash Inflows', icon='arrow-right',
                               description='The total income or revenue received over a given period.'),
                    calc_input(label='Cash Outflows', icon='arrow-left',
                               description='The total expenses or payments made over a given period.'),
                    html.Div([
                        html.Div(['Net Cash Flow'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' currency'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Payback Period Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Initial Investment', icon='bag',
                               description='The total amount of money invested at the start.'),
                    calc_input(label='Annual Cash Inflows', icon='arrow-right',
                               description='The cash inflows or profits generated annually from the investment.'),
                    html.Div([
                        html.Div(['Payback Period'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' years'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ]),
    html.Div([
        html.Div([
            html.H4('Profit Margin Calculator'),
            html.Form([
                html.Fieldset([
                    calc_input(label='Revenue', icon='bag',
                               description='The total revenue or sales from which profit is derived.'),
                    calc_input(label='Net Profit', icon='crosshairs',
                               description='The profit after subtracting expenses, taxes, and other costs from revenue.'),
                    html.Div([
                        html.Div(['Profit Margin'], className='uk-text-bolder uk-text-small'),
                        html.Hr(),
                        html.Div([
                            html.Span(['0.00'], className='uk-text-bolder'), ' %'
                        ]),
                        html.Hr(),
                    ], className='uk-margin'),
                ], className='uk-fieldset')
            ]),
        ], className='uk-card uk-card-default uk-card-body uk-light', style={'background-color': '#091235'})
    ])
], **{'data-uk-grid': 'masonry: pack'}, className='uk-child-width-1-2@m uk-margin-medium-top')


def nav():
    return html.Div([
        html.Nav([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Img(
                                src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                    '/Blue%20Chip%20Invest%20Logo.001.png', width='60', height='60'),
                            html.A([
                                html.Div([
                                    'BLUE CHIP INVESTMENTS'
                                ], style={'font-family': '"Noto Sans", sans-serif', 'font-optical-sizing': 'auto',
                                          'font-weight': '400', 'font-style': 'normal', 'line-height': '22px',
                                          'color': '#091235', 'width': '164px'})
                            ], className='uk-link-text', href='/')
                        ], className='uk-navbar-item uk-logo')
                    ], className='uk-navbar-left'),
                    html.Div([
                        html.A(href='#', role='button',
                               **{'data-uk-navbar-toggle-icon': 'true'},
                               className='uk-navbar-toggle uk-navbar-toggle-animate uk-hidden@l uk-icon uk-navbar-toggle-icon'),
                        html.Div([
                            html.Ul([
                                html.Li(
                                    html.A(['Culture'], href='#')
                                ),
                                html.Li(
                                    html.A(['Financial Tools'], href='/financial-tools/')
                                ),
                                # precision_financial_tools(),,
                                html.Li(
                                    html.A(['Research & Insights'], href='#')
                                ),
                                html.Li([
                                    html.A(["Let's Talk"], className='uk-button uk-button-small uk-light',
                                           style={'background-color': '#091235'}, href='/contact-us/')
                                ], className='uk-margin')
                            ], className='uk-nav uk-navbar-dropdown-nav')
                        ], className='uk-navbar-dropdown uk-width-large'),
                        html.Ul([
                            html.Li(
                                html.A('Culture', href='#')
                            ),
                            html.Li(
                                html.A('Financial Tools', href='/financial-tools/')
                            ),
                            html.Li(
                                html.A('Research & Insights', href='#')
                            )
                        ], className='uk-navbar-nav uk-visible@l'),
                        html.A(["Let's Talk"], className='uk-button uk-button-small uk-visible@l uk-light',
                               href='/contact-us/', style={'background-color': '#091235'})
                    ], className='uk-navbar-right')
                ], **{'data-uk-navbar': 'mode: click'}, className='uk-navbar')
            ], className='uk-container')
        ], className='uk-navbar-container')
    ], **{'data-uk-sticky': 'sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky'})


def footer():
    return html.Div([
        html.Div([
            html.Hr(),
            html.Div([
                html.A(['BLUE CHIP INVESTMENTS'],
                       style={'font-family': '"Noto Sans", sans-serif', 'font-optical-sizing': 'auto',
                              'font-weight': '400', 'font-style': 'normal'},
                       className='uk-heading-small uk-margin-small-bottom', href='/'),
                html.Div(['Building Your Legacy with Trusted Growth'], className='uk-text-small')
            ], className='uk-card uk-card-body uk-width-large'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div(['Our Services'],
                                 className='uk-text-bolder uk-text-large uk-margin-small-bottom',
                                 style={'color': '#88A9C3'}),
                        html.Ul([
                            html.Li(html.A('Financial Planning', href='#')),
                            html.Li(html.A('Investment Management', href='#')),
                            html.Li(html.A('Retirement Planning', href='#')),
                            html.Li(html.A('Investment Analysis', href='#')),
                            html.Li(html.A('Insurance', href='#'))
                        ], className='uk-list uk-text-small')
                    ], className='uk-card uk-card-body')
                ], className='uk-width-auto'),
                html.Div([
                    html.Div([
                        html.Div(['Explore'], className='uk-text-bolder uk-text-large uk-margin-small-bottom',
                                 style={'color': '#88A9C3'}),
                        html.Ul([
                            html.Li(html.A('About', href='#')),
                            html.Li(html.A('Services', href='#')),
                            html.Li(html.A('Careers', href='#')),
                            html.Li(html.A("FAQ's", href='#')),
                            html.Li(html.A('Partner', href='#'))
                        ], className='uk-list uk-text-small')
                    ], className='uk-card uk-card-body')
                ], className='uk-width-auto'),
                html.Div([
                    html.Div([
                        html.Div("Let's Talk",
                                 className='uk-text-bolder uk-text-large uk-margin-small-bottom',
                                 style={'color': '#88A9C3'}),
                        html.P('We\'re Here to Help You Grow Your Wealth, Plan Your Future, and Achieve Your Financial '
                               'Goals', className='uk-text-small uk-light'),
                        html.A('Start', className='uk-button uk-light uk-text-bolder',
                               style={'background-color': '#88A9C3', 'color': '#091235'}, href='/contact-us/')
                    ], className='uk-card uk-card-body')
                ])
            ], **{'data-uk-grid': 'true'}, className='uk-child-width-1-2 uk-child-width-1-3@l'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div(**{'data-uk-icon': 'icon: location; ratio: 1.8'}, className='uk-icon',
                                 style={'color': '#88A9C3'}),
                        html.Div('Location', className='uk-text-large uk-text-bolder uk-light'),
                        html.Div('Unit 17, No.30 Surprise Road, Pinetown, 3610', className='uk-text-small uk-light')
                    ], className='uk-card uk-card-body')
                ]),
                html.Div([
                    html.Div([
                        html.Div(**{'data-uk-icon': 'icon: receiver; ratio: 1.8'}, className='uk-icon'),
                        html.Div('Phone', className='uk-text-large uk-text-bolder uk-light'),
                        html.Div('0860 258 2447', className='uk-text-small uk-light')
                    ], className='uk-card uk-card-body')
                ]),
                html.Div([
                    html.Div([
                        html.Div(**{'data-uk-icon': 'icon: mail; ratio: 1.8'}, className='uk-icon'),
                        html.Div('Email', className='uk-text-large uk-text-bolder'),
                        html.Div(['info@', html.Br()], 'bluechipinvest.co.za', className='uk-text-small')
                    ], className='uk-card uk-card-body')
                ]),
                html.Div([
                    html.Div([
                        html.Div(**{'data-uk-icon': 'icon: social; ratio: 1.8'}, className='uk-icon'),
                        html.Div('Social', className='uk-text-large uk-text-bolder', style={'margin-bottom': '4px'}),
                        html.Div([
                            html.Div(
                                html.Span(**{'data-uk-icon': 'icon: facebook'}, className='uk-icon-button uk-icon')),
                            html.Div(
                                html.Span(**{'data-uk-icon': 'icon: linkedin'}, className='uk-icon-button uk-icon')),
                            html.Div(
                                html.Span(**{'data-uk-icon': 'icon: instagram'}, className='uk-icon-button uk-icon')),
                            html.Div(html.Span(**{'data-uk-icon': 'icon: x'}, className='uk-icon-button uk-icon'))
                        ], **{'data-uk-grid': 'true'}, className='uk-grid-small uk-child-width-auto')
                    ], className='uk-card uk-card-body')
                ])
            ], **{'data-uk-grid': 'true'}, className='uk-child-width-1-2 uk-child-width-1-4@l')
        ], className='uk-container')
    ], className='uk-section uk-section-large uk-light', style={'background-color': '#091235'})
