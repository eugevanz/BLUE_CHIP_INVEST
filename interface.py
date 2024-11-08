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


def precision_financial_tools():
    return html.Li(
        html.A([
            'Financial Tools',
            html.Span(**{'data-uk-navbar-parent-icon': 'true'})
        ], href='#'),
        html.Div([
            html.Ul([
                html.Li('Potential Interest Calculators', className='uk-nav-header'),
                *calculator_group1,
                html.Li(className='uk-nav-divider'),
                html.Li('Return on Investment (ROI) Calculators', className='uk-nav-header'),
                *calculator_group2,
                html.Li(className='uk-nav-divider'),
                html.Li('Loan Amortisation Calculators', className='uk-nav-header'),
                *calculator_group3,
                html.Li(className='uk-nav-divider'),
                html.Li('Other Relevant Financial Metrics Calculators', className='uk-nav-header'),
                *calculator_group4
            ], className='uk-nav uk-navbar-dropdown-nav')
        ], className='uk-navbar-dropdown uk-width-large')
    )


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
    ], className='uk-section uk-section-large uk-light', style={'background-color': '#091235'},
        **{'data-uk-scrollspy': 'cls: uk-animation-slide-bottom; repeat: true'})
