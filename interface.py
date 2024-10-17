import calendar
from datetime import datetime
from os import environ

from fasthtml.components import Div, Ul, Li, A, Span, Nav, Button, H3, H4, Form, Fieldset, Hr, Br, P, Input, Strong, \
    Label, Img
from supabase import create_client

SUPABASE_URL = environ.get('SUPABASE_URL')
SUPABASE_KEY = environ.get('SUPABASE_KEY')
SUPABASE_SERVICE_ROLE_KEY = environ.get('SUPABASE_SERVICE_ROLE_KEY')
supabase = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY)
supabase_admin = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_SERVICE_ROLE_KEY)
session_data = supabase.auth.get_session()


def calc_input(label, icon, description):
    return Div(
        Div(
            Span(data_uk_icon=f'icon: {icon}', cls='uk-form-icon'),
            Input(aria_label=label, placeholder=label, type='text', cls='uk-input'),
            cls='uk-inline'
        ),
        Div(description, cls='uk-text-small uk-padding-small uk-padding-remove-top'),
        cls='uk-margin'
    )


nav_link = lambda href, title: Li(
    A(title, href=href, data_uk_toggle=True)
)

return_button = A(
    Span(data_uk_icon='icon: chevron-left; ratio: 1.5', _='on click go back'),
    href='#'
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


def add_save_button():
    return Div(
        A(href='', data_uk_icon='icon: plus', cls='uk-icon-button'),
        Button('Save', cls='uk-button uk-button-small uk-text-bolder uk-button-secondary'),
        cls='uk-margin-medium-top uk-flex uk-flex-between'
    )


def calendar_view():
    current_year = datetime.now().year
    current_month = datetime.now().month
    days_in_month = calendar.monthrange(current_year, current_month)[1]
    days_list = list(range(1, days_in_month + 1))
    first_day_of_month = calendar.monthrange(current_year, current_month)[0] + 1
    days_list = [''] * first_day_of_month + days_list

    def highlight_date(day):
        return 'color: #CD5B45;' if day == datetime.now().day else None

    days = Div(
        *[Div(Span(day, cls='uk-text-muted uk-text-small')) for day in
          ['S', 'M', 'T', 'W', 'T', 'F', 'S']],
        cls='uk-grid-small uk-child-width-expand uk-text-center', data_uk_grid=True
    )
    weeks = [Div(
        *[Div(A(day, cls='uk-text-bolder', style=highlight_date(day))) for day in (days_list[i:i + 7] + [''] * (7 - len(
            days_list[i:i + 7])))],
        cls='uk-grid-small uk-child-width-expand uk-text-center', data_uk_grid=True
    ) for i in range(0, len(days_list), 7)]
    return Div(days, *weeks)


def sign_out_button():
    return Li(A(Span(data_uk_icon='icon:  sign-out', cls='uk-margin-small-right'), 'Sign Out',
                cls='uk-flex uk-flex-middle uk-text-danger uk-margin-top', hx_post='/home/',
                hx_target='#page', hx_vals='{"sign_out": "signed-out"}'))


def precision_financial_tools():
    return Li(
        A(
            'Financial Tools',
            Span(data_uk_navbar_parent_icon=True),
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
            cls='uk-navbar-dropdown uk-width-large'
        )
    )


def nav(user=None, history='/home/'):
    return Div(
        Nav(
            Div(
                Div(
                    Div(
                        Div(
                            A(
                                href='#', cls='uk-icon-link', data_uk_icon='icon: chevron-left; ratio: 3',
                                _='on click go back'
                            ) if history not in ['/home/'] else Img(
                                src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                    '/Blue%20Chip%20Invest%20Logo.001.png', width='60', height='60'
                            ),
                            A(
                                Div('BLUE CHIP INVESTMENTS', aria_label='Back to Home',
                                    style='font-family: "Noto Sans", sans-serif; font-optical-sizing: auto; '
                                          'font-weight: 400; font-style: normal; line-height: 22px; color: #091235; '
                                          'width: 164px;',
                                    cls='uk-link-text', hx_get='/home/',
                                    hx_target='#page')
                            ),
                            cls='uk-navbar-item uk-logo'
                        ),
                        cls='uk-navbar-left'
                    ),
                    Div(
                        A(aria_haspopup='true', aria_label='Open menu', href='#', role='button',
                          data_uk_navbar_toggle_icon=True,
                          cls='uk-navbar-toggle uk-navbar-toggle-animate uk-hidden@l uk-icon uk-navbar-toggle-icon'),
                        Div(
                            Ul(
                                Li(
                                    A('Culture', href='#')
                                ),
                                precision_financial_tools(),
                                Li(
                                    A('Research & Insights', href='#')
                                ),
                                Li(
                                    Button("Let's Talk", cls='uk-button uk-button-small uk-light',
                                           style='background-color: #091235'),
                                    cls='uk-margin'
                                ),
                                cls='uk-nav uk-navbar-dropdown-nav'
                            ),
                            cls='uk-navbar-dropdown uk-width-large'
                        ),
                        Ul(
                            Li(
                                A('Culture', href='#')
                            ),
                            precision_financial_tools(),
                            Li(
                                A('Research & Insights', href='#')
                            ),
                            cls='uk-navbar-nav uk-visible@l'
                        ),
                        Button("Let's Talk", cls='uk-button uk-button-small uk-visible@l uk-light',
                               hx_get='/contact-us/',
                               hx_target='#page', hx_push_url='/home/',
                               style='background-color: #091235'),
                        Button(data_uk_icon='close', cls='uk-icon-button uk-icon uk-light', hx_post='/admin/',
                               hx_target='#page') if user else
                        Div(
                            A(data_uk_icon='user', cls='uk-icon-button uk-icon',
                              style='background-color: #091235'),
                            Div(
                                H3('Welcome Back', cls='uk-card-title uk-text-bolder uk-margin-remove-bottom'),
                                P('Please enter your ', Strong('email address'),
                                  ' to log in. A magic link will be sent to your email, allowing you to securely '
                                  'access your account.',
                                  cls='uk-text-small uk-margin-remove-top', style='color: #091235'),
                                Div(
                                    Label('Email', cls='uk-form-label'),
                                    Div(
                                        Span(cls='uk-form-icon', data_uk_icon='icon: mail'),
                                        Input(cls='uk-input uk-form-width-large', type='email',
                                              aria_label='Username', name='form-username'),
                                        cls='uk-inline'
                                    ),
                                    cls='uk-margin'
                                ),
                                Div(
                                    Button("Send Code",
                                           cls='uk-button uk-button-large uk-width-1-1 uk-light',
                                           style='background-color: #091235', hx_post=f'/request-code/',
                                           hx_target='#code-notifications',
                                           hx_include="[name='form-username']"),
                                    cls='uk-margin'
                                ),
                                P(id='code-notifications'),
                                cls='uk-card uk-card-body uk-width-large uk-card-default', data_uk_drop=True
                            ),
                            cls='uk-inline'
                        ),
                        cls='uk-navbar-right'
                    ),
                    data_uk_navbar='mode: click;', cls='uk-navbar'
                ),
                cls='uk-container'
            ),
            cls='uk-navbar-container'
        ),
        data_uk_sticky='sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky;'
    )


def potential_interest_calculators():
    return Div(
        Div(
            Button(type='button', data_uk_close=True, cls='uk-modal-close-full uk-close-large'),
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
                                                   description='The initial amount of money that is being invested or '
                                                               'loaned.'),
                                        calc_input(label='Interest Rate (R)', icon='arrow-up-right',
                                                   description='The annual interest rate, usually provided as a '
                                                               'percentage (e.g., 5%)'),
                                        calc_input(label='Time (T)', icon='clock',
                                                   description='The time period for which the interest is calculated, '
                                                               'typically in years.'),
                                        Div(
                                            Div('Result', cls='uk-text-bolder uk-text-small'),
                                            Hr(),
                                            Div(
                                                Span('0.00', cls='uk-text-bolder'),
                                                ' per year'
                                            ),
                                            Hr(),
                                            cls='uk-margin'
                                        ),
                                        cls='uk-fieldset'
                                    )
                                ),
                                cls='uk-card uk-card-default uk-card-body uk-light',
                                style='background-color: #091235'
                            )
                        ),
                        Div(
                            Div(
                                H4('Compound Interest Calculator'),
                                Form(
                                    Fieldset(
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
                                                ' per year'
                                            ),
                                            Hr(),
                                            cls='uk-margin'
                                        ),
                                        cls='uk-fieldset'
                                    )
                                ),
                                cls='uk-card uk-card-default uk-card-body uk-light',
                                style='background-color: #091235'
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
                                                               'per year (e.g., annually, semi-annually, quarterly, '
                                                               'monthly, daily).'),
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
                                                ' per year'
                                            ),
                                            Hr(),
                                            cls='uk-margin'
                                        ),
                                        cls='uk-fieldset'
                                    )
                                ),
                                cls='uk-card uk-card-default uk-card-body uk-light',
                                style='background-color: #091235'
                            )
                        ),
                        data_uk_grid='masonry: pack',
                        cls='uk-child-width-1-2@m uk-margin-medium-top'
                    ),
                    cls='uk-container'
                ),
                cls='uk-section uk-section-medium'
            ),
            cls='uk-modal-dialog'
        ),
        id='potential-interest-calculators',
        data_uk_modal=True,
        cls='uk-modal-full'
    )


def footer():
    return Div(
        Div(
            Hr(),
            Div(
                Div('BLUE CHIP INVESTMENTS', aria_label='Back to Home',
                    style='font-family: "Noto Sans", sans-serif; font-optical-sizing: auto; font-weight: 400; '
                          'font-style: normal;',
                    cls='uk-heading-small uk-margin-small-bottom uk-width-medium', hx_get='/home/',
                    hx_target='#page'),
                Div('Building Your Legacy with Trusted Growth', cls='uk-text-small'),
                cls='uk-card uk-card-body'
            ),
            Div(
                Div(
                    Div(
                        Div('Our Services',
                            cls='uk-text-bolder uk-text-large uk-margin-small-bottom', style='color: #88A9C3;'),
                        Ul(
                            Li(A('Financial Planning', href='#')),
                            Li(A('Investment Management', href='#')),
                            Li(A('Retirement Planning', href='#')),
                            Li(A('Investment Analysis', href='#')),
                            Li(A('Insurance', href='#')),
                            cls='uk-list uk-text-small'
                        ),
                        cls='uk-card uk-card-body'
                    ),
                    cls='uk-width-auto'
                ),
                Div(
                    Div(
                        Div('Explore', cls='uk-text-bolder uk-text-large uk-margin-small-bottom',
                            style='color: #88A9C3;'),
                        Ul(
                            Li(A('About', href='#')),
                            Li(A('Services', href='#')),
                            Li(A('Careers', href='#')),
                            Li(A("FAQ's", href='#')),
                            Li(A('Partner', href='#')),
                            cls='uk-list uk-text-small'
                        ),
                        cls='uk-card uk-card-body'
                    ),
                    cls='uk-width-auto'
                ),
                Div(
                    Div(
                        Div("Let's Talk",
                            cls='uk-text-bolder uk-text-large uk-margin-small-bottom', style='color: #88A9C3;'),
                        P('We\'re Here to Help You Grow Your Wealth, Plan Your Future, and Achieve Your Financial '
                          'Goals', cls='uk-text-small uk-light'),
                        Button('Start', cls='uk-button uk-light uk-text-bolder',
                               style='background-color: #88A9C3; color: #091235',
                               hx_get='/contact-us/', hx_target='#page', hx_push_url='/home/'),
                        cls='uk-card uk-card-body'
                    )
                ),
                data_uk_grid=True,
                cls='uk-child-width-1-2 uk-child-width-1-3@l'
            ),
            Div(
                Div(
                    Div(
                        Div(data_uk_icon='icon: location; ratio: 1.8', cls='uk-icon', style='color: #88A9C3'),
                        Div('Location', cls='uk-text-large uk-text-bolder uk-light'),
                        Div('Unit 17, No.30 Surprise Road, Pinetown, 3610', cls='uk-text-small uk-light'),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(data_uk_icon='icon: receiver; ratio: 1.8', cls='uk-icon'),
                        Div('Phone', cls='uk-text-large uk-text-bolder uk-light'),
                        Div('0860 258 2447', cls='uk-text-small uk-light'),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(data_uk_icon='icon: mail; ratio: 1.8', cls='uk-icon'),
                        Div('Email', cls='uk-text-large uk-text-bolder'),
                        Div('info@', Br(), 'bluechipinvest.co.za', cls='uk-text-small'),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(data_uk_icon='icon: social; ratio: 1.8', cls='uk-icon'),
                        Div('Social', cls='uk-text-large uk-text-bolder', style='margin-bottom: 4px;'),
                        Div(
                            Div(Span(data_uk_icon='icon: facebook', cls='uk-icon-button uk-icon')),
                            Div(Span(data_uk_icon='icon: linkedin', cls='uk-icon-button uk-icon')),
                            Div(Span(data_uk_icon='icon: instagram', cls='uk-icon-button uk-icon')),
                            Div(Span(data_uk_icon='icon: x', cls='uk-icon-button uk-icon')),
                            data_uk_grid=True,
                            cls='uk-grid-small uk-child-width-auto'
                        ),
                        cls='uk-card uk-card-body'
                    )
                ),
                data_uk_grid=True,
                cls='uk-child-width-1-2 uk-child-width-1-4@l'
            ),
            cls='uk-container'
        ),
        cls='uk-section uk-section-large uk-light', style='background-color: #091235'
    )
