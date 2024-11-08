import dash
from dash import html

dash.register_page(__name__)

from interface import footer, potential_interest_calculator_tab, return_on_investment_calculator_tab, \
    loan_amortisation_calculator_tab, other_relevant_financial_metrics_calculator_tab

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.H3(['Comprehensive Financial Calculators'], className='uk-text-uppercase uk-text-bolder'),
                html.Div([
                    '''These are tools designed to help individuals or businesses estimate the amount of 
                            interest they could earn or owe over time based on various financial scenarios. These 
                            calculators typically focus on interest accumulated from savings, loans, or investments and 
                            can be tailored for specific financial goals.'''
                ], className='uk-text-small uk-width-2-3@s'),
                html.Ul([
                    html.Li(html.A('Potential Interest')),
                    html.Li(html.A('Return on Investment (ROI)')),
                    html.Li(html.A('Loan Amortisation')),
                    html.Li(html.A('Other Relevant Financial Metrics'))
                ], **{'data-uk-tab': 'animation: uk-animation-slide-left-medium, uk-animation-slide-right-medium'}),
                html.Div([
                    potential_interest_calculator_tab,
                    return_on_investment_calculator_tab,
                    loan_amortisation_calculator_tab,
                    other_relevant_financial_metrics_calculator_tab,
                ], className='uk-switcher uk-margin'),
            ], className='uk-container')
        ], className='uk-section')
    ]),
    footer()
])
