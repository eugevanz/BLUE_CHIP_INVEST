from os import environ

from fasthtml.components import Div, Ul, Li, A, Span, Nav, Button, H3, H4, Form, Fieldset, Hr, H1, Br, P, Input, \
    H2, Img, H5, Label
from supabase import create_client

SUPABASE_URL = environ.get('SUPABASE_URL')
SUPABASE_KEY = environ.get('SUPABASE_KEY')
supabase = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY)


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


def is_user_logged_in():
    response = supabase.auth.get_session()
    if response:
        return supabase.auth.get_user(response.access_token)
    return response


nav_link = lambda href, title: Li(
    A(title, href=href, data_uk_toggle=True)
)

return_button = Button(type='button', aria_label='Close', data_uk_icon='icon: chevron-left; ratio: 1.5',
                       data_uk_sticky='end: !.uk-section; offset: 80', cls='uk-icon-button',
                       _='on click go back')

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


def nav():
    return Nav(
        Div(
            Div(
                Div(
                    A(aria_haspopup='true', aria_label='Open menu', href='#', role='button',
                      data_uk_navbar_toggle_icon=True,
                      cls='uk-navbar-toggle uk-navbar-toggle-animate uk-hidden@l uk-icon uk-navbar-toggle-icon'),
                    Div(
                        Ul(
                            Li(A('Culture', href='#')),
                            Li(A('Tailored Wealth Solutions', href='#')),
                            precision_financial_tools(),
                            Li(
                                A('Research & Insights', href='#')
                            ),
                            Li(
                                Button("Let's Talk", cls='uk-button uk-button-small uk-light',
                                       style='background-color: #00213B')
                            ),
                            cls='uk-nav uk-navbar-dropdown-nav'
                        ),
                        cls='uk-navbar-dropdown uk-width-large'
                    ),
                    A('Blue Chip Invest', aria_label='Back to Home', href='#',
                      style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                      cls='uk-navbar-item uk-logo', hx_get='/home/', hx_target='#page', hx_swap='innerHTML'),
                    Ul(
                        Li(
                            A('Culture', href='#')
                        ),
                        Li(
                            A('Tailored Wealth Solutions', href='#')
                        ),
                        precision_financial_tools(),
                        Li(
                            A('Research & Insights', href='#')
                        ),
                        cls='uk-navbar-nav uk-visible@l'
                    ),
                    cls='uk-navbar-left'
                ),
                Div(
                    Button("Let's Talk", cls='uk-button uk-button-small uk-visible@l uk-light', hx_get='/contact-us/',
                           hx_target='#page', hx_swap='innerHTML', hx_push_url='true',
                           style='background-color: #00213B'),
                    A(data_uk_icon='user', cls='uk-icon-button uk-icon uk-light', hx_get='/admin/', hx_target='#page',
                      hx_swap='innerHTML', hx_push_url='true') if
                    is_user_logged_in() else Ul(
                        Li(
                            A(data_uk_icon='user', cls='uk-icon-button uk-icon',
                              style='background-color: #00213B'),
                            Form(
                                Div(
                                    Div('Welcome Back', cls='uk-heading-small uk-text-bolder uk-margin-remove-bottom'),
                                    Div('Please Enter your Account details'),
                                    cls='uk-margin-medium-bottom'
                                ),
                                Ul(
                                    Li(
                                        Label('Email', cls='uk-form-label'),
                                        Div(
                                            Span(cls='uk-form-icon', data_uk_icon='icon: user'),
                                            Input(cls='uk-input uk-form-width-large', type='text',
                                                  aria_label='Username', id='form-username'),
                                            cls='uk-inline'
                                        ),
                                        cls='uk-margin'
                                    ),
                                    Li(
                                        Label('Password', cls='uk-form-label'),
                                        Div(
                                            Span(cls='uk-form-icon uk-form-icon-flip', data_uk_icon='icon: lock'),
                                            Input(cls='uk-input uk-form-width-large', type='password',
                                                  aria_label='Password'),
                                            cls='uk-inline'
                                        ),
                                        A('Forgot password?', href='#', cls='uk-link-text uk-text-meta uk-float-right'),
                                        cls='uk-margin'
                                    ),
                                    Li(
                                        Button("Sign In",
                                               cls='uk-button uk-button-large uk-width-1-1 uk-light '
                                                   'uk-margin-medium-top',
                                               style='background-color: #00213B')
                                    ),
                                    cls='uk-nav uk-navbar-dropdown-nav'
                                ),
                                cls='uk-navbar-dropdown uk-width-large'
                            )
                        ),
                        cls='uk-iconnav'
                    ),
                    cls='uk-navbar-right'
                ),
                data_uk_navbar='mode: click;', cls='uk-navbar'
            ),
            cls='uk-container'
        ),
        cls='uk-navbar-container'
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
                                cls='uk-card uk-card-default uk-card-body uk-light', style='background-color: #00213B'
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
                                cls='uk-card uk-card-default uk-card-body uk-light', style='background-color: #00213B'
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
                                cls='uk-card uk-card-default uk-card-body uk-light', style='background-color: #00213B'
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


def hero():
    return Div(
        Div(
            Div(
                Div(cls='uk-card uk-card-body'),
                Div(
                    Div(
                        H1(
                            'Get a clear path to',
                            Br(),
                            Span('your financial goals.'),
                            cls='uk-text-bolder'
                        ),
                        P('Our Wealth Activating team can help you'),
                        Button('Get Started', cls='uk-button uk-button-small uk-light', hx_get='/contact-us/',
                               hx_target='#page', hx_swap='innerHTML', hx_push_url='true',
                               style='background-color: #00213B'),
                        cls='uk-card uk-card-body uk-margin-auto-vertical'
                    ),
                    style='min-height: max(0px, 60vh);',
                    data_uk_height_viewport='offset-bottom: 40',
                    cls='uk-flex'
                ),
                data_uk_grid=True,
                cls='uk-child-width-1-2@s'
            ),
            cls='uk-container'
        ),
        style=f'background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
              f'/marten-bjork-6dW3xyQvcYE-unsplash_6_11zon.webp); filter: grayscale(90%);',
        cls='uk-background-bottom-right uk-background-cover'
    )


def subhero():
    return Div(
        Div(
            Div(
                H2(
                    'Planning objective', Br(), Span('financial advice'),
                    cls='uk-text-bolder uk-margin-xlarge-left@s'
                ),
                Button('View All', cls='uk-button uk-button-text uk-margin-xlarge-left@s', hx_get='/services/',
                       hx_target='#page', hx_swap='innerHTML', hx_push_url='true'),
                cls='uk-margin-auto-vertical uk-card uk-card-body uk-card-large'
            ),
            cls='uk-width-2-5@m uk-light', style='background-color: #00213B'
        ),
        *[Div(
            Div(
                Span(data_uk_icon='icon: settings; ratio: 2', cls='uk-icon'),
                Div(
                    Span(title, cls='uk-text-primary'),
                    cls='uk-text-bolder uk-margin-small-top'
                ),
                Div(subtitle, cls='uk-text-small'),
                cls='uk-card uk-card-body'
            ),
            cls='uk-background-primary'
        ) for title, subtitle in [
            ('Risk Management', 'Risk management is critical to long-term success and sustainability'),
            ('Investment Analytics', 'Leveraging investment analytics and make more informed decisions'),
            ('Cash Flow', 'Effective cash flow management is crucial for business survival')
        ]],
        data_uk_grid=True,
        cls='uk-child-width-expand@s uk-grid-collapse uk-grid-match uk-light'
    )


def advisor_section():
    return Div(
        Div(
            *[Div(
                Div(style=f'height: {height}; background-image: url({img}); filter: grayscale(90%);',
                    cls='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle'),
                cls='uk-visible@s'
            ) for img, height in [
                ('https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/redd-f-5U_28ojjgms'
                 '-unsplash_10_11zon.webp', '100px'),
                ('https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/santi-vedri'
                 '-O5EMzfdxedg-unsplash_11_11zon.webp', '150px'),
                ('https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/youssef-naddam'
                 '-iJ2IG8ckCpA-unsplash_15_11zon.webp', '300px'),
                ('https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jakub-zerdzicki'
                 '-eGI0aGwuE-A-unsplash_29_11zon.webp', '120px'),
                ('https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/nandhu-kumar'
                 '-5NGTf4oD8RA-unsplash_8_11zon.webp', '180px'),
                ('https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/charlesdeluvio'
                 '-Lks7vei-eAg-unsplash_24_11zon.webp', '140px')
            ]],
            Div(
                Div(
                    H2(
                        Span('We Help', cls='uk-text-primary'),
                        ' financial',
                        Br(),
                        Span('Advisors that'),
                        Br(),
                        Span('exclusively serve.'),
                        cls='uk-text-bolder'
                    ),
                    P('We empower financial advisors dedicated to serving a select clientele',
                      cls='uk-width-medium'),
                    Button('Read More', type='button', cls='uk-button uk-button-text', hx_get='/advisors/',
                           hx_target='#page', hx_swap='innerHTML', hx_push_url='true'),
                    cls='uk-card uk-card-body'
                )
            ),
            style='height: 627px;',
            data_uk_grid='masonry: pack',
            cls='uk-child-width-1-2@s uk-child-width-1-3@m uk-grid-small uk-grid uk-flex-top uk-flex-wrap-top'
        ),
        id='advisor-section',
        cls='uk-container uk-margin-xlarge-top advisor-section'
    )


def advisor_section_read_more():
    return Div(
        Div(
            Div(
                Div(
                    data_src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/youssef'
                             '-naddam-iJ2IG8ckCpA-unsplash_15_11zon.webp',
                    data_uk_img=True,
                    cls='uk-height-large uk-flex uk-flex-center uk-flex-middle uk-background-cover'
                ),
                cls='uk-flex-last@s uk-card-media-right uk-cover-container'
            ),
            Div(
                Div(
                    H2(
                        Span('We Help', cls='uk-text-primary'), ' financial', Br(), Span('Advisors that'),
                        Br(), Span('exclusively serve.'),
                        cls='uk-text-bolder'
                    ),
                    P('Dedicated to the needs of financial advisors who serve clients exclusively, '
                      'we offer customized solutions and resources that enhance their practices. Our mission is '
                      'to equip advisors with the tools and support they need to foster meaningful client '
                      'relationships, allowing them to focus on delivering top-notch financial guidance and '
                      'personalized service.'),
                    Button('Talk to us', cls='uk-button uk-button-large uk-light', hx_get='/contact-us/',
                           hx_target='#page', hx_swap='innerHTML', hx_push_url='true',
                           style='background-color: #00213B'),
                    cls='uk-card-body'
                )
            ),
            data_uk_grid=True,
            cls='uk-card uk-card-small uk-grid-collapse uk-child-width-1-2@s uk-margin'
        ),
        data_uk_dropdown='mode: click; stretch: x; pos: top-left; boundary: !.advisor-section; flip: false'
    )


def serve_section():
    return Div(
        Div(
            H2(
                Span('Who', cls='uk-text-primary'), Span(' We Serve'),
                Hr(style='height: 0px; border: none; border-top: 2px solid;', cls='uk-width-small uk-text-primary'),
                cls='uk-text-bolder'
            ),
            P('Focused support for financial advisors with a unique clientele.', cls='uk-width-medium'),
            cls='uk-card uk-card-body uk-margin-auto-vertical'
        ),
        Div(
            *[Div(
                Div(
                    Div(style=f'height: 240px; background-image: url({img});mask-image: linear-gradient(to '
                              f'bottom, rgba(0,0,0,1), rgba(0,0,0,0)); filter: grayscale(90%);',
                        cls='uk-card-media-top uk-background-cover'),
                    Div(
                        H3(title, cls='uk-text-bolder'),
                        Button('Read More', cls='uk-button uk-button-text', hx_get=f'/who-we-serve/{title}',
                               hx_swap='innerHTML', hx_target='#page', hx_push_url='true'),
                        cls='uk-card-body'
                    ),
                    cls='uk-card uk-card-small'
                )
            ) for title, img in [
                ('Business Owners',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/ellicia-24HcJhf0u6M'
                 '-unsplash_26_11zon.webp'),
                ('Private Client',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jc-gellidon'
                 '-j_5sxxspFtc-unsplash_1_11zon.webp'),
                ('Pre-Retirees',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/birmingham-museums'
                 '-trust-T2AmpV9qWqw-unsplash_23_11zon.webp'),
                ('Retirees',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/huy-phan'
                 '-QCF2ykBsC2I-unsplash_28_11zon.webp'),
                ('Young Investor',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/ali-morshedlou'
                 '-WMD64tMfc4k-unsplash_19_11zon.webp')
            ]],
            data_uk_grid=True,
            cls='uk-child-width-1-5@m uk-child-width-1-3@s uk-child-width-1-2 uk-margin-medium-top'
        ),
        cls='uk-container serve-section'
    )


def metric_section():
    return Div(
        Div(
            Div(
                Div(
                    Div('$15B',
                        style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                        cls='uk-heading-small'),
                    Div('Assets Under Management', cls='uk-text-small'),
                    cls='uk-text-center'
                ),
                Div(
                    Div('56', style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                        cls='uk-heading-small'),
                    Div('Office Locations in RSA', cls='uk-text-small'),
                    cls='uk-text-center'
                ),
                Div(
                    Div('1995',
                        style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                        cls='uk-heading-small'),
                    Div('Year founded company', cls='uk-text-small'),
                    cls='uk-text-center'
                ),
                Div(
                    Div('2,541',
                        style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                        cls='uk-heading-small'),
                    Div('Clients represented through our firm', cls='uk-text-small'),
                    cls='uk-text-center'
                ),
                data_uk_grid=True,
                cls='uk-grid-divider uk-child-width-expand@s'
            ),
            cls='uk-container'
        ),
        cls='uk-section uk-section-large'
    )


def preserve_section():
    return Div(
        Div(
            style='background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public'
                  '/website_images/scott-webb-hDyO6rr3kqk-unsplash_12_11zon.webp); filter: grayscale(90%);',
            cls='uk-height-large uk-flex uk-flex-start uk-flex-middle uk-background-cover uk-background-center-center'
        ),
        Div(
            H1('Preserve and Grow Your Financial Legacy', cls='uk-text-primary uk-text-bolder uk-width-1-2'),
            Button('Contact Us', cls='uk-button uk-light', hx_get='/contact-us/', hx_target='#page',
                   hx_swap='innerHTML', hx_push_url='true', style='background-color: #00213B'),
            cls='uk-card uk-card-body uk-overlay', style='position: absolute; bottom: 0px;'
        ),
        cls='uk-container', style='position: relative;'
    )


def whatwedo_section():
    return Div(
        Div(
            Div(
                Div(
                    Div(
                        H2(
                            Span('What', cls='uk-text-primary'),
                            ' We Do',
                            Hr(style='height: 0px; border: none; border-top: 2px solid;',
                               cls='uk-width-small uk-text-primary'),
                            cls='uk-text-bolder'
                        ),
                        P('Providing tailored solutions for financial advisors to elevate client success.',
                          cls='uk-width-medium'),
                        Button('View All', cls='uk-button uk-button-text', hx_get='/services/', hx_target='#page',
                               hx_swap='innerHTML', hx_push_url='true'),
                        cls='uk-card uk-card-body uk-margin-auto-vertical uk-text-left uk-light',
                        style='background-color: #00213B'
                    ),
                    cls='uk-width-1-2@m'
                ),
                *[Div(
                    Div(
                        Span(data_uk_icon=f'icon: {icon}; ratio: 2.5', cls='uk-text-primary uk-icon'),
                        P(title, cls='uk-text-bolder'),
                        Div(subtitle, cls='uk-text-small'),
                        cls='uk-card uk-card-default uk-card-body'
                    ),
                    cls='uk-width-1-4@m uk-width-1-2@s'
                ) for icon, title, subtitle in [
                    ('crosshairs', 'Financial Planning', 'Comprehensive strategies to secure your financial future.'),
                    ('unlock', 'Retirement Planning', 'Creating personalized pathways to a secure and fulfilling '
                                                      'retirement.'),
                    ('file-text', 'Insurance', 'Protecting what matters most with tailored insurance solutions.'),
                    ('cart', 'Investment Management', 'Maximizing growth through strategic and personalized '
                                                      'investment.'),
                    ('search', 'Tax Planning', 'Optimizing your financial strategy with proactive tax planning '
                                               'solutions.'),
                    ('bag', 'Business Planning',
                     'Building robust strategies for sustainable business growth and success.')
                ]],
                data_uk_grid=True,
                cls='uk-grid-match uk-text-center'
            ),
            cls='uk-container'
        ),
        cls='uk-section uk-section-xlarge'
    )


def testimonials_section():
    return Div(
        Div(
            Div(
                Div('WHAT OUR CUSTOMERS SAY', cls='uk-text-small uk-text-bolder'),
                H2(
                    Span('Our', cls='uk-text-primary'),
                    ' Testimonials',
                    cls='uk-text-bolder uk-margin-remove-top'
                ),
                cls='uk-card uk-card-body uk-text-center'
            ),
            Div(
                *[Div(
                    Div(
                        Div(
                            *[Span(data_uk_icon='star', cls='uk-text-warning uk-icon') for _ in range(5)],
                        ),
                        P(
                            Span(title, cls='uk-text-bolder'),
                            Br(), subtext,
                            cls='uk-text-italic'
                        ),
                        Div(
                            Div(
                                Img(alt='Border pill', height='64',
                                    src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public'
                                        '/website_images/jurica-koletic-7YVZYZeITc8-unsplash_3_11zon.webp',
                                    style='filter: grayscale(90%);',
                                    width='64', cls='uk-border-circle'),
                                cls='uk-width-auto'
                            ),
                            Div(
                                Div(f'— {name}', cls='uk-text-bolder'),
                                Div(pos, cls='uk-text-small'),
                                cls='uk-margin-auto-vertical'
                            ),
                            data_uk_grid=True,
                            cls='uk-grid-small'
                        ),
                        cls='uk-card uk-card-default uk-card-body'
                    )
                ) for title, subtext, name, pos in [
                    ('Exceptional Guidance for Every Stage',
                     'Working with this company has been a game-changer for my practice. Their expertise in financial '
                     'and business planning helped me develop strategies tailored to my clients\' unique needs. The '
                     'personalized support and dedication to excellence have elevated the service I offer, '
                     'and my clients couldn\'t be happier.',
                     'Sarah T.', 'Financial Advisor'),
                    ('A True Partner in Growth',
                     'From investment management to retirement planning, they’ve provided me with the tools and '
                     'insights to serve my clients better.Their proactive approach to tax and insurance planning has '
                     'saved my clients both time and money, allowing me to build stronger, long-term '
                     'relationships.They’re not just a service provider; they’re a trusted partner in my success.',
                     'John M.', 'Certified Financial Planner'),
                    ('Unmatched Expertise and Support',
                     'The business planning strategies offered by this team have been instrumental in helping me grow'
                     ' my advisory firm.Their in -depth understanding of financial planning, combined with their '
                     'dedication to serving a niche clientele, has made all the difference. I highly recommend them '
                     'to any financial advisor looking to take their business to the next level.',
                     'Alex P.', 'Wealth Management Advisor')
                ]],
                data_uk_grid=True,
                cls='uk-grid-match uk-child-width-expand@m'
            ),
            cls='uk-container'
        ),
        cls='uk-section uk-light', style='background-color: #00213B'
    )


def guides_section():
    return Div(
        Div(
            Div(
                Div(
                    Div(
                        H2(
                            Span('Personal', cls='uk-text-primary'),
                            ' Finance Guides',
                            Hr(style='height: 0px; border: none; border-top: 2px solid;',
                               cls='uk-width-small uk-text-primary'),
                            cls='uk-text-bolder'
                        ),
                        Button('Read Our Blog', cls='uk-button uk-button-text', hx_get='/guides/', hx_target='#page',
                               hx_swap='innerHTML', hx_push_url='true'),
                        cls='uk-card uk-card-body'
                    ),
                    Div(
                        H5('Most Popular', cls='uk-text-bolder'),
                        Ul(
                            *[Li(
                                A(title, href=f'#{title}', cls='uk-link-muted', hx_get='/guides/', hx_target='#page',
                                  hx_swap='innerHTML', hx_push_url='true')
                            ) for title, href in [
                                ('What are Portfolio Accounting Systems', '#'),
                                ('Investing Basics for New Grads', '#'),
                                ('What is the Average Net Worth by Age', '#'),
                                ('Wealth Management vs. Investment Banking', '#'),
                                ('2024\'s Best Provinces to Retire in South Africa', '#')
                            ]],
                            cls='uk-list uk-list-disc uk-list-primary uk-text-small'
                        ),
                        cls='uk-card uk-card-body uk-margin-auto-vertical'
                    )
                ),
                *[Div(
                    Div(
                        Div(style=f'height: 320px; background-image: url({img}); filter: grayscale(90%);',
                            tabindex='0', cls='uk-background-cover'),
                        Div(
                            H4(title, cls='uk-card-title, uk-text-bolder'),
                            P(desc, cls='uk-text-small'),
                            cls='uk-card-body'
                        ),
                        cls='uk-card uk-card-small uk-card-body'
                    )
                ) for img, title, desc in [
                    (
                        'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/krzysztof'
                        '-hepner-o_x11ORH9vQ-unsplash_4_11zon.webp',
                        'How to Achieve True Wealth',
                        'Unlocking true wealth involves strategic planning, smart investments, and a holistic approach to '
                        'managing your financial resources. Discover the steps to build and sustain genuine financial '
                        'prosperity.'),
                    (
                        'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/pedro'
                        '-miranda-3QzMBrvCeyQ-unsplash_9_11zon.webp',
                        'Step Focused Planning',
                        'Achieve your financial goals with step-by-step, focused planning that guides you through every '
                        'stage of wealth building and preservation.')
                ]],
                data_uk_grid=True,
                cls='uk-grid-match uk-child-width-expand@s'
            ),
            cls='uk-container'
        ),
        cls='uk-section uk-section-xlarge'
    )


def footer():
    return Div(
        Div(
            Div(
                Div(
                    Div(
                        Div('Blue Chip Invest', aria_label='Back to Home',
                            style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                            cls='uk-heading-small uk-margin-small-bottom uk-width-small'),
                        Div('Building Your Legacy with Trusted Growth', cls='uk-text-small'),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div('Our Services', cls='uk-text-bolder uk-text-primary uk-text-large uk-margin-small-bottom'),
                        Ul(
                            Li(A('Financial Planning', href='#')),
                            Li(A('Investment Management', href='#')),
                            Li(A('Retirement Planning', href='#')),
                            Li(A('Investment Analysis', href='#')),
                            Li(A('Insurance', href='#')),
                            cls='uk-list uk-text-small'
                        ),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div('Explore', cls='uk-text-bolder uk-text-primary uk-text-large uk-margin-small-bottom'),
                        Ul(
                            Li(A('About', href='#')),
                            Li(A('Services', href='#')),
                            Li(A('Careers', href='#')),
                            Li(A("FAQ's", href='#')),
                            Li(A('Partner', href='#')),
                            cls='uk-list uk-text-small'
                        ),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div("Let's Talk", cls='uk-text-bolder uk-text-primary uk-text-large uk-margin-small-bottom'),
                        P('We\'re Here to Help You Grow Your Wealth, Plan Your Future, and Achieve Your Financial '
                          'Goals', cls='uk-text-small'),
                        Button('Start', cls='uk-button uk-button-primary',
                               hx_get='/contact-us/', hx_target='#page', hx_swap='innerHTML', hx_push_url='true'),
                        cls='uk-card uk-card-body'
                    )
                ),
                data_uk_grid=True,
                cls='uk-child-width-1-2 uk-child-width-1-4@l'
            ),
            Div(
                Div(
                    Div(
                        Div(data_uk_icon='icon: location; ratio: 1.8', cls='uk-icon'),
                        Div('Location', cls='uk-text-large uk-text-bolder'),
                        Div('No. 30 Pinetown, Durban 3610', cls='uk-text-small'),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(data_uk_icon='icon: receiver; ratio: 1.8', cls='uk-icon'),
                        Div('Phone', cls='uk-text-large uk-text-bolder'),
                        Div('0860 258 2447', cls='uk-text-small'),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(data_uk_icon='icon: mail; ratio: 1.8', cls='uk-icon'),
                        Div('Email', cls='uk-text-large uk-text-bolder'),
                        Div('admin@', Br(), 'bluechipinvest.co.za', cls='uk-text-small'),
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
        cls='uk-section uk-section-medium uk-light', style='background-color: #00213B'
    )
