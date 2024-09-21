from fasthtml.common import FastHTML, serve
from fasthtml.components import Script, Link, Title, Li, A, Body, Nav, Div, Ul, Span, Button, Input, Fieldset, Form, H4, \
    Hr, H3

app = FastHTML(
    hdrs=(
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit.min.js'),
        Script(src='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/js/uikit-icons.min.js'),
        Script(src='https://unpkg.com/hyperscript.org@0.9.12'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/uikit@3.21.12/dist/css/uikit.min.css'),
        Link(rel='preconnect', href='https://fonts.googleapis.com'),
        Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
        Link(rel='stylesheet',
             href='https://fonts.googleapis.com/css2?family=Playfair+Display+SC:ital,wght@0,700;0,900;1,'
                  '700&display=swap'),
        Title('Blue Chip Invest')
    ), surreal=False, pico=False
)

nav_link = lambda href, title: Li(
    A(title, href='#', data_uk_toggle=True)
)
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
calc_input = lambda label, icon, description: Div(
    Div(
        Span(data_uk_icon=f'icon: {icon}', cls='uk-form-icon'),
        Input(aria_label=label, placeholder=label, type='text', cls='uk-input'),
        cls='uk-inline'
    ),
    Div(description, cls='uk-text-small uk-padding-small uk-padding-remove-top'),
    cls='uk-margin'
)


@app.route('/')
def home():
    # html_content = (f'<!DOCTYPE html><html lang=\"en\">{head}<body>{nav}{potential_interest_calculators}{hero}{subhero}'
    #                 f'{advisor_section}{serve_section}{metric_section}{preserve_section}{whatwedo_section}'
    #                 f'{testimonials_section}{guides_section}{footer}'
    #                 f'</body></html>')
    return Body(
        Nav(
            Div(
                Div(
                    Div(
                        A(aria_haspopup='true', aria_label='Open menu', href='#', role='button',
                          uk_navbar_toggle_icon='',
                          cls='uk-navbar-toggle uk-navbar-toggle-animate uk-hidden@l uk-icon uk-navbar-toggle-icon'),
                        Div(
                            Ul(
                                Li(
                                    A('Culture', href='#')
                                ),
                                Li(
                                    A('Tailored Wealth Solutions', href='#')
                                ),
                                Li(
                                    A(
                                        'Precision Financial Tools',
                                        Span(uk_navbar_parent_icon=''),
                                        aria_haspopup='true',
                                        href='#',
                                        role='button'
                                    ),
                                    Div(
                                        Ul(
                                            Li('Potential Interest Calculators', cls='uk-nav-header'),
                                            *calculator_group1,
                                            Li(cls='uk-nav-divider'),
                                            Li('Return on Investment (ROI) Calculators', cls='uk-nav-header'),
                                            *calculator_group2,
                                            Li(cls='uk-nav-divider'),
                                            Li('Loan Amortisation Calculators', cls='uk-nav-header'),
                                            *calculator_group3,
                                            Li(cls='uk-nav-divider'),
                                            Li('Other Relevant Financial Metrics Calculators', cls='uk-nav-header'),
                                            *calculator_group4,
                                            cls='uk-nav uk-navbar-dropdown-nav'
                                        ),
                                        cls='uk-navbar-dropdown uk-drop uk-width-large'
                                    )
                                ),
                                Li(
                                    A('Research & Insights', href='#')
                                ),
                                Li(
                                    Button("Let's Talk", cls='uk-button uk-button-secondary uk-button-small')
                                ),
                                cls='uk-nav uk-navbar-dropdown-nav'
                            ),
                            cls='uk-navbar-dropdown uk-drop'
                        ),
                        A('Blue Chip Invest', aria_label='Back to Home', href='#',
                          style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                          cls='uk-navbar-item uk-logo'),
                        Ul(
                            Li(
                                A('Culture', href='#')
                            ),
                            Li(
                                A('Tailored Wealth Solutions', href='#')
                            ),
                            Li(
                                A(
                                    'Financial Tools',
                                    Span(uk_navbar_parent_icon=''),
                                    aria_haspopup='true',
                                    href='#',
                                    role='button'
                                ),
                                Div(
                                    Ul(
                                        Li('Potential Interest Calculators', cls='uk-nav-header'),
                                        *calculator_group1,
                                        Li(cls='uk-nav-divider'),
                                        Li('Return on Investment (ROI) Calculators', cls='uk-nav-header'),
                                        *calculator_group2,
                                        Li(cls='uk-nav-divider'),
                                        Li('Loan Amortisation Calculators', cls='uk-nav-header'),
                                        *calculator_group3,
                                        Li(cls='uk-nav-divider'),
                                        Li('Other Relevant Financial Metrics Calculators', cls='uk-nav-header'),
                                        *calculator_group4,
                                        cls='uk-nav uk-navbar-dropdown-nav'
                                    ),
                                    cls='uk-navbar-dropdown uk-drop uk-width-large'
                                )
                            ),
                            Li(
                                A('Research & Insights', href='#')
                            ),
                            cls='uk-navbar-nav uk-visible@l'
                        ),
                        cls='uk-navbar-left'
                    ),
                    Div(
                        Button("Let's Talk", cls='uk-button uk-button-secondary uk-button-small uk-visible@l'),
                        A(uk_icon='user', cls='uk-icon-button uk-button-secondary uk-icon'),
                        cls='uk-navbar-right'
                    ),
                    uk_navbar='mode: click; target: !.uk-navbar; align: center',
                    cls='uk-navbar'
                ),
                cls='uk-container'
            ),
            cls='uk-navbar-container'
        ),
        Div(
            Div(
                Button(type='button', uk_close='', cls='uk-modal-close-full uk-close-large'),
                Div(
                    Div(
                        H3('Potential Interest Calculators',
                           style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                           cls='uk-text-uppercase uk-text-bolder'),
                        Div('''These are tools designed to help individuals or businesses estimate the amount of 
                        interest they could earn or owe over time based on various financial scenarios. These 
                        calculators typically focus on interest accumulated from savings, loans, or investments and 
                        can be tailored for specific financial goals.''',
                            cls='uk-text-small uk-width-2-3@s'),
                        Div(
                            Div(
                                Div(
                                    H4('Simple Interest Calculator'),
                                    Form(
                                        Fieldset(
                                            calc_input(label='Principal (P)', icon='bag',
                                                       description='The initial amount of money that is being invested or loaned.'),
                                            calc_input(label='Interest Rate (R)', icon='arrow-up-right',
                                                       description='The annual interest rate, usually provided as a percentage (e.g., 5%)'),
                                            calc_input(label='Time (T)', icon='clock',
                                                       description='The time period for which the interest is calculated, typically in years.'),
                                            Div(
                                                Div('Result', cls='uk-text-bolder uk-text-small'),
                                                Hr(),
                                                Div(
                                                    Span('0.00', cls='uk-text-bolder'),
                                                    'per year'
                                                ),
                                                Hr(),
                                                cls='uk-margin'
                                            ),
                                            cls='uk-fieldset'
                                        )
                                    ),
                                    cls='uk-card uk-card-default uk-card-body'
                                )
                            ),
                            Div(
                                Div(
                                    H4('Compound Interest Calculator'),
                                    Form(
                                        Fieldset(
                                            calc_input(label='Principal (P)', icon='bag',
                                                       description='The initial amount of money that is being invested or loaned.'),
                                            calc_input(label='Interest Rate (R)', icon='arrow-up-right',
                                                       description='The annual interest rate, usually provided as a '
                                                                   'percentage (e.g., 5%)'),
                                            calc_input(label='Time (T)', icon='clock',
                                                       description='The time period for which the interest is '
                                                                   'calculated, typically in years.'),
                                            calc_input(label='Compounding Frequency (n)', icon='calendar',
                                                       description='The number of times the interest is compounded '
                                                                   'per year (e.g., annually, semi-annually, quarterly, monthly, daily).'),
                                            Div('Common values for compounding frequency:',
                                                cls='uk-text-small uk-padding-small uk-padding-remove-top'),
                                            Div(
                                                Ul(
                                                    Li('Annually (n = 1)'),
                                                    Li('Semi-Annually (n = 2)'),
                                                    Li('Quarterly (n = 4)'),
                                                    Li('Monthly (n = 12)'),
                                                    Li('Daily (n = 365)'),
                                                    cls='uk-list uk-list-collapse uk-list-disc'
                                                ),
                                                cls='uk-text-small uk-padding-small uk-padding-remove-top'
                                            ),
                                            Div(
                                                Div('Result', cls='uk-text-bolder uk-text-small'),
                                                Hr(),
                                                Div(
                                                    Span('0.00', cls='uk-text-bolder'),
                                                    'per year'
                                                ),
                                                Hr(),
                                                cls='uk-margin'
                                            ),
                                            cls='uk-fieldset'
                                        )
                                    ),
                                    cls='uk-card uk-card-default uk-card-body'
                                )
                            ),
                            Div(
                                Div(
                                    H4('Savings Interest Calculator'),
                                    Form(
                                        Fieldset(
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
                                                                   'per year (e.g., annually, semi-annually, quarterly, monthly, daily).'),
                                            Div('Common values for compounding frequency:',
                                                cls='uk-text-small uk-padding-small uk-padding-remove-top'),
                                            Div(
                                                Ul(
                                                    Li('Annually (n = 1)'),
                                                    Li('Semi-Annually (n = 2)'),
                                                    Li('Quarterly (n = 4)'),
                                                    Li('Monthly (n = 12)'),
                                                    Li('Daily (n = 365)'),
                                                    cls='uk-list uk-list-collapse uk-list-disc'
                                                ),
                                                cls='uk-text-small uk-padding-small uk-padding-remove-top'
                                            ),
                                            Div(
                                                Div('Result', cls='uk-text-bolder uk-text-small'),
                                                Hr(),
                                                Div(
                                                    Span('0.00', cls='uk-text-bolder'),
                                                    'per year'
                                                ),
                                                Hr(),
                                                cls='uk-margin'
                                            ),
                                            cls='uk-fieldset'
                                        )
                                    ),
                                    cls='uk-card uk-card-default uk-card-body'
                                )
                            ),
                            uk_grid='masonry: pack',
                            cls='uk-child-width-1-2@s uk-margin-medium-top'
                        ),
                        cls='uk-container'
                    ),
                    cls='uk-section uk-section-medium'
                ),
                cls='uk-modal-dialog'
            ),
            id='potential-interest-calculators',
            uk_modal='',
            cls='uk-modal-full'
        )
    )


serve()
