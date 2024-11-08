import dash
from dash import html

dash.register_page(__name__)

from interface import calc_input, footer

calculator_tab = html.Div([
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

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.H3(['Potential Interest Calculators'], className='uk-text-uppercase uk-text-bolder'),
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
                    calculator_tab,
                    calculator_tab,
                    calculator_tab,
                    calculator_tab,
                ], className='uk-switcher uk-margin'),
            ], className='uk-container')
        ], className='uk-section')
    ]),
    footer()
])
