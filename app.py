from fasthtml.common import FastHTML, serve
from fasthtml.components import Script, Link, Li, A, Body, Nav, Div, Ul, Span, Button, Input, Fieldset, Form, H4, \
    Hr, H3, H1, Br, P, H2, H5, Img, Textarea, Title
from fasthtml.xtend import Titled

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
    ), surreal=False, pico=False, default_hdrs=False
)


def nav_link(href, title):
    return Li(
        A(title, href=href, data_uk_toggle=True)
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
                            Li(
                                A('Culture', href='#')
                            ),
                            Li(
                                A('Tailored Wealth Solutions', href='#')
                            ),
                            Li(
                                A(
                                    'Precision Financial Tools',
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
                    Button("Let's Talk", cls='uk-button uk-button-secondary uk-button-small uk-visible@l',
                           data_uk_toggle='target: #contact-us'),
                    A(data_uk_icon='user', cls='uk-icon-button uk-button-secondary uk-icon'),
                    cls='uk-navbar-right'
                ),
                data_uk_navbar='mode: click; target: !.uk-navbar; align: center',
                cls='uk-navbar'
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
                                cls='uk-card uk-card-default uk-card-body uk-card-secondary'
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
                                cls='uk-card uk-card-default uk-card-body uk-card-secondary'
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
                                cls='uk-card uk-card-default uk-card-body uk-card-secondary'
                            )
                        ),
                        data_uk_grid='masonry: pack',
                        cls='uk-child-width-1-2@s uk-margin-medium-top'
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
                        Button('Get Started', cls='uk-button uk-button-secondary uk-button-small',
                               data_uk_toggle='target: #contact-us'),
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
        style='background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
              '/marten-bjork-6dW3xyQvcYE-unsplash.jpg)',
        tabindex='0',
        cls='uk-background-bottom-right uk-background-cover'
    )


def contact_us():
    return Div(
        Div(
            Button(type='button', data_uk_close=True, cls='uk-offcanvas-close'),
            H3('Chat to our team', cls='uk-text-bolder'),
            P('Need help with something? Want a demo? Reach out to our friendly team, and we\'ll get back to you in '
              'no time.'),
            Form(
                Div(
                    Div(
                        Span(uk_icon='icon: user', cls='uk-form-icon'),
                        Input(type='text', placeholder='Your name', aria_label='Not clickable icon',
                              cls='uk-input uk-width-large'),
                        cls='uk-inline'
                    ),
                    cls='uk-margin'
                ),
                Div(
                    Div(
                        Span(uk_icon='icon: mail', cls='uk-form-icon'),
                        Input(type='text', placeholder='you@company.com', aria_label='Email',
                              cls='uk-input uk-width-large'),
                        cls='uk-inline'
                    ),
                    cls='uk-margin'
                ),
                Div(
                    Textarea(rows='5', placeholder='Leave a message', aria_label='Message', cls='uk-textarea'),
                    cls='uk-margin'
                ),
                Div('No worries, your info stays with us. We don’t do the oversharing thing.',
                    cls='uk-text-small uk-margin'),
                Button('Send your message', cls='uk-button uk-button-default uk-width-1-1'),
                cls='uk-margin-large-top'
            ),
            cls='uk-offcanvas-bar'
        ),
        id='contact-us',
        data_uk_offcanvas='mode: push; overlay: true'
    )


def subhero():
    return Div(
        Div(
            Div(
                H2(
                    'Planning objective',
                    Br(),
                    Span('financial advice'),
                    cls='uk-text-bolder uk-margin-xlarge-left'
                ),
                Button('View All', cls='uk-button uk-button-text uk-margin-xlarge-left'),
                services(),
                cls='uk-margin-auto-vertical uk-card uk-card-body uk-card-large'
            ),
            cls='uk-background-secondary uk-width-2-5@m'
        ),
        Div(
            Div(
                Span(data_uk_icon='icon: settings; ratio: 2', cls='uk-icon'),
                Div(
                    Span('Risk Management', cls='uk-text-success'),
                    cls='uk-text-bolder uk-margin-small-top'
                ),
                Div('Risk management is critical to long-term success and sustainability', cls='uk-text-small'),
                cls='uk-margin-auto-vertical uk-card uk-card-body'
            ),
            cls='uk-background-primary'
        ),
        Div(
            Div(
                Span(data_uk_icon='icon: image; ratio: 2', cls='uk-icon'),
                Div(
                    Span('Investment Analytics', cls='uk-text-success'),
                    cls='uk-text-bolder uk-margin-small-top'
                ),
                Div('Leveraging investment analytics and make more informed decisions', cls='uk-text-small'),
                cls='uk-margin-auto-vertical uk-card uk-card-body'
            ),
            cls='uk-background-primary'
        ),
        Div(
            Div(
                Span(data_uk_icon='icon: credit-card; ratio: 2', cls='uk-icon'),
                Div(
                    Span('Cash Flow', cls='uk-text-success'),
                    cls='uk-text-bolder uk-margin-small-top'
                ),
                Div('Effective cash flow management is crucial for business survival', cls='uk-text-small'),
                cls='uk-margin-auto-vertical uk-card uk-card-body'
            ),
            cls='uk-background-primary'
        ),
        data_uk_grid=True,
        cls='uk-child-width-expand@s uk-grid-collapse uk-grid-match uk-light'
    )


def services():
    return Div(
        Ul(
            Li(
                A('Active', href='#'),
                cls='uk-active'
            ),
            Li(
                A('Item', href='#')
            ),
            Li('Header', cls='uk-nav-header'),
            Li(
                A('Item', href='#')
            ),
            Li(
                A('Item', href='#')
            ),
            Li(cls='uk-nav-divider'),
            Li(
                A('Item', href='#')
            ),
            cls='uk-nav uk-dropdown-nav'
        ),
        data_uk_dropdown='boundary: !.uk-navbar; stretch: x; flip: false; mode: click',
        cls='uk-navbar-dropdown'
    )


def advisor_section():
    return Div(
        Div(
            Div(
                Div(
                    Div(style='height: 100px; background-image: url('
                              'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/redd'
                              '-f-5U_28ojjgms-unsplash.jpg)',
                        tabindex='0',
                        cls='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle'),
                    style='transform: translate(0px, 0px);',
                    cls='uk-visible@s uk-first-column'
                ),
                Div(
                    Div(style='height: 150px; background-image: url('
                              'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/santi'
                              '-vedri-O5EMzfdxedg-unsplash.jpg)',
                        tabindex='0',
                        cls='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle'),
                    style='transform: translate(0px, 0px);',
                    cls='uk-visible@s'
                ),
                Div(
                    Div(style='height: 300px; background-image: url('
                              'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                              '/youssef-naddam-iJ2IG8ckCpA-unsplash.jpg);',
                        tabindex='0',
                        cls='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle'),
                    style='transform: translate(0px, 0px);',
                    cls='uk-visible@s'
                ),
                Div(
                    Div(style='height: 120px; background-image: url('
                              'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jakub'
                              '-zerdzicki-eGI0aGwuE-A-unsplash.jpg);',
                        tabindex='0',
                        cls='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle'),
                    style='transform: translate(0px, -200px);',
                    cls='uk-visible@s uk-grid-margin uk-first-column'
                ),
                Div(
                    Div(style='height: 180px; background-image: url('
                              'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                              '/nandhu-kumar-5NGTf4oD8RA-unsplash.jpg)',
                        tabindex='0',
                        cls='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle'),
                    style='transform: translate(0px, -150px);',
                    cls='uk-visible@s uk-grid-margin'
                ),
                Div(
                    Div(style='height: 140px; background-image: url('
                              'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                              '/accuray-5VkNa1LrS8A-unsplash.jpg)',
                        tabindex='0',
                        cls='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle'),
                    style='transform: translate(-810px, -65px);',
                    cls='uk-visible@s uk-grid-margin'
                ),
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
                        Button('Read More', cls='uk-button uk-button-text'),
                        cls='uk-card uk-card-body uk-margin-auto-vertical'
                    ),
                    style='transform: translate(810px, -195px);',
                    cls='uk-grid-margin uk-first-column'
                ),
                style='height: 627px;',
                data_uk_grid='masonry: pack',
                cls='uk-child-width-1-2@s uk-child-width-1-3@m uk-grid-small uk-grid uk-flex-top uk-flex-wrap-top'
            ),
            cls='uk-container'
        ),
        cls='uk-section uk-section-xlarge uk-padding-remove-bottom'
    )


def serve_section():
    return Div(
        Div(
            Div(
                H2(
                    Span('Who', cls='uk-text-success'),
                    Span('We Serve'),
                    Hr(style='height: 0px; border: none; border-top: 2px solid;', cls='uk-width-small uk-text-success'),
                    cls='uk-text-bolder'
                ),
                P('Focused support for financial advisors with a unique clientele.', cls='uk-width-medium'),
                cls='uk-card uk-card-body uk-margin-auto-vertical'
            ),
            Div(
                Div(
                    Div(
                        Div(style='height: 240px; background-image: url('
                                  'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                  '/ellicia-24HcJhf0u6M-unsplash.jpg);mask-image: linear-gradient(to bottom, rgba(0,0,'
                                  '0,1), rgba(0,0,0,0));',
                            tabindex='0', cls='uk-card-media-top uk-background-cover'),
                        Div(
                            H3('Business Owners', cls='uk-text-bolder'),
                            Button('Read More', cls='uk-button uk-button-text'),
                            cls='uk-card-body'
                        ),
                        cls='uk-card uk-card-small'
                    )
                ),
                Div(
                    Div(
                        Div(style='height: 240px; background-image: url('
                                  'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                  '/jc-gellidon-j_5sxxspFtc-unsplash.jpg);mask-image: linear-gradient(to bottom, '
                                  'rgba(0,0,0,1), rgba(0,0,0,0));',
                            tabindex='0', cls='uk-card-media-top uk-background-cover'),
                        Div(
                            H3('Private Client', cls='uk-text-bolder'),
                            Button('Read More', cls='uk-button uk-button-text'),
                            cls='uk-card-body'
                        ),
                        cls='uk-card uk-card-small'
                    )
                ),
                Div(
                    Div(
                        Div(style='height: 240px; background-image: url('
                                  'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                  '/birmingham-museums-trust-T2AmpV9qWqw-unsplash.jpg);mask-image: linear-gradient(to '
                                  'bottom, rgba(0,0,0,1), rgba(0,0,0,0));',
                            tabindex='0', cls='uk-card-media-top uk-background-cover'),
                        Div(
                            H3('Pre-Retirees', cls='uk-text-bolder'),
                            Button('Read More', cls='uk-button uk-button-text'),
                            cls='uk-card-body'
                        ),
                        cls='uk-card uk-card-small'
                    )
                ),
                Div(
                    Div(
                        Div(style='height: 240px; background-image: url('
                                  'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                  '/huy-phan-QCF2ykBsC2I-unsplash.jpg); mask-image: linear-gradient(to bottom, rgba(0,'
                                  '0,0,1), rgba(0,0,0,0));',
                            tabindex='0', cls='uk-card-media-top uk-background-cover'),
                        Div(
                            H3('Retirees', cls='uk-text-bolder'),
                            Button('Read More', cls='uk-button uk-button-text'),
                            cls='uk-card-body'
                        ),
                        cls='uk-card uk-card-small'
                    )
                ),
                Div(
                    Div(
                        Div(style='height: 240px; background-image: url('
                                  'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                  '/ali-morshedlou-WMD64tMfc4k-unsplash.jpg); mask-image: linear-gradient(to bottom, '
                                  'rgba(0,0,0,1), rgba(0,0,0,0));',
                            tabindex='0', cls='uk-card-media-top uk-background-cover'),
                        Div(
                            H3('Young Investor', cls='uk-text-bolder'),
                            Button('Read More', cls='uk-button uk-button-text'),
                            cls='uk-card-body'
                        ),
                        cls='uk-card uk-card-small'
                    )
                ),
                data_uk_grid=True,
                cls='uk-child-width-1-5@m uk-child-width-1-3@s uk-child-width-1-2 uk-margin-medium-top'
            ),
            cls='uk-container'
        ),
        cls='uk-section uk-padding-remove-vertical'
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
            Div(
                H1('Preserve and Grow Your Financial Legacy', cls='uk-text-success uk-text-bolder'),
                Button('Contact Us', cls='uk-button uk-button-secondary', data_uk_toggle='target: #contact-us'),
                cls='uk-card uk-card-body uk-width-1-2@s'
            ),
            style='background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public'
                  '/website_images/scott-webb-hDyO6rr3kqk-unsplash.jpg)',
            tabindex='0',
            cls='uk-height-medium uk-flex uk-flex-start uk-flex-middle uk-background-cover uk-background-center-center'
        ),
        cls='uk-container'
    )


def whatwedo_section():
    return Div(
        Div(
            Div(
                Div(
                    Div(
                        H2(
                            Span('What', cls='uk-text-success'),
                            'We Do',
                            Hr(style='height: 0px; border: none; border-top: 2px solid;',
                               cls='uk-width-small uk-text-success'),
                            cls='uk-text-bolder'
                        ),
                        P('Providing tailored solutions for financial advisors to elevate client success.',
                          cls='uk-width-medium'),
                        Button('View All', cls='uk-button uk-button-text'),
                        cls='uk-card uk-card-body uk-card-secondary uk-margin-auto-vertical uk-text-left'
                    ),
                    cls='uk-width-1-2@m'
                ),
                Div(
                    Div(
                        Span(uk_icon='icon: crosshairs; ratio: 2.5', cls='uk-text-primary uk-icon'),
                        P('Financial Planning', cls='uk-text-bolder'),
                        Div('Comprehensive strategies to secure your financial future.', cls='uk-text-small'),
                        cls='uk-card uk-card-default uk-card-body'
                    ),
                    cls='uk-width-1-4@m uk-width-1-2@s'
                ),
                Div(
                    Div(
                        Span('<', data_uk_icon='icon: unlock; ratio: 2.5', cls='uk-text-primary uk-icon'),
                        P('Retirement Planning', cls='uk-text-bolder'),
                        Div('Creating personalized pathways to a secure and fulfilling retirement.',
                            cls='uk-text-small'),
                        cls='uk-card uk-card-default uk-card-body'
                    ),
                    cls='uk-width-1-4@m uk-width-1-2@s'
                ),
                Div(
                    Div(
                        Span(uk_icon='icon: file-text; ratio: 2.5', cls='uk-text-primary uk-icon'),
                        P('Insurance', cls='uk-text-bolder'),
                        Div('Protecting what matters most with tailored insurance solutions.', cls='uk-text-small'),
                        cls='uk-card uk-card-default uk-card-body'
                    ),
                    cls='uk-width-1-4@m uk-width-1-2@s'
                ),
                Div(
                    Div(
                        Span(uk_icon='icon: cart; ratio: 2.5', cls='uk-text-primary uk-icon'),
                        P('Investment Management', cls='uk-text-bolder'),
                        Div('Maximizing growth through strategic and personalized investment.', cls='uk-text-small'),
                        cls='uk-card uk-card-default uk-card-body'
                    ),
                    cls='uk-width-1-4@m uk-width-1-2@s'
                ),
                Div(
                    Div(
                        Span(uk_icon='icon: search; ratio: 2.5', cls='uk-text-primary uk-icon'),
                        P('Tax Planning', cls='uk-text-bolder'),
                        Div('Optimizing your financial strategy with proactive tax planning solutions.',
                            cls='uk-text-small'),
                        cls='uk-card uk-card-default uk-card-body'
                    ),
                    cls='uk-width-1-4@m uk-width-1-2@s'
                ),
                Div(
                    Div(
                        Span(uk_icon='icon: bag; ratio: 2.5', cls='uk-text-primary uk-icon'),
                        P('Business Planning', cls='uk-text-bolder'),
                        Div('Building robust strategies for sustainable business growth and success.',
                            cls='uk-text-small'),
                        cls='uk-card uk-card-default uk-card-body'
                    ),
                    cls='uk-width-1-4@m uk-width-1-2@s'
                ),
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
                    Span('Our', cls='uk-text-success'),
                    'Testimonials',
                    cls='uk-text-bolder uk-margin-remove-top'
                ),
                cls='uk-card uk-card-body uk-text-center'
            ),
            Div(
                Div(
                    Div(
                        Div(
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon')
                        ),
                        P(
                            Span('Exceptional Guidance for Every Stage', cls='uk-text-bolder'),
                            Br(),
                            '''Working with this company has been a game-changer for my practice. Their expertise in 
                            financial and business planning helped me develop strategies tailored to my clients’ 
                            unique needs. The personalized support and dedication to excellence have elevated the 
                            service I offer, and my clients couldn't be happier.''',
                            cls='uk-text-italic'
                        ),
                        Div(
                            Div(
                                Img(alt='Border pill', height='64',
                                    src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public'
                                        '/website_images/jurica-koletic-7YVZYZeITc8-unsplash.jpg',
                                    width='64', cls='uk-border-circle'),
                                cls='uk-width-auto'
                            ),
                            Div(
                                Div('— Sarah T.', cls='uk-text-bolder'),
                                Div('Financial Advisor', cls='uk-text-small'),
                                cls='uk-margin-auto-vertical'
                            ),
                            data_uk_grid=True,
                            cls='uk-grid-small'
                        ),
                        cls='uk-card uk-card-default uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon')
                        ),
                        P(
                            Span('A True Partner in Growth', cls='uk-text-bolder'),
                            Br(),
                            '''From investment management to retirement planning, they’ve provided me with the tools 
                            and insights to serve my clients better. Their proactive approach to tax and insurance 
                            planning has saved my clients both time and money, allowing me to build stronger, 
                            long-term relationships. They’re not just a service provider; they’re a trusted partner 
                            in my success.''',
                            cls='uk-text-italic'
                        ),
                        Div(
                            Div(
                                Img(alt='Border pill', height='64',
                                    src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public'
                                        '/website_images/jurica-koletic-7YVZYZeITc8-unsplash.jpg',
                                    width='64', cls='uk-border-circle'),
                                cls='uk-width-auto'
                            ),
                            Div(
                                Div('— John M.', cls='uk-text-bolder'),
                                Div('Certified Financial Planner', cls='uk-text-small'),
                                cls='uk-margin-auto-vertical'
                            ),
                            data_uk_grid=True,
                            cls='uk-grid-small'
                        ),
                        cls='uk-card uk-card-default uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon'),
                            Span(uk_icon='star', cls='uk-text-warning uk-icon')
                        ),
                        P(
                            Span('Unmatched Expertise and Support', cls='uk-text-bolder'),
                            Br(),
                            '''The business planning strategies offered by this team have been instrumental in 
                            helping me grow my advisory firm. Their in-depth understanding of financial planning, 
                            combined with their dedication to serving a niche clientele, has made all the difference. 
                            I highly recommend them to any financial advisor looking to take their business to the 
                            next level.''',
                            cls='uk-text-italic'
                        ),
                        Div(
                            Div(
                                Img(alt='Border pill', height='64',
                                    src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public'
                                        '/website_images/jurica-koletic-7YVZYZeITc8-unsplash.jpg',
                                    width='64', cls='uk-border-circle'),
                                cls='uk-width-auto'
                            ),
                            Div(
                                Div('— Alex P.', cls='uk-text-bolder'),
                                Div('Wealth Management Advisor', cls='uk-text-small'),
                                cls='uk-margin-auto-vertical'
                            ),
                            data_uk_grid=True,
                            cls='uk-grid-small'
                        ),
                        cls='uk-card uk-card-default uk-card-body'
                    )
                ),
                data_uk_grid=True,
                cls='uk-grid-match uk-child-width-expand@m'
            ),
            cls='uk-container'
        ),
        cls='uk-section uk-section-secondary'
    )


def guides_section():
    return Div(
        Div(
            Div(
                Div(
                    Div(
                        H2(
                            Span('Personal', cls='uk-text-success'),
                            'Finance Guides',
                            Hr(style='height: 0px; border: none; border-top: 2px solid;',
                               cls='uk-width-small uk-text-success'),
                            cls='uk-text-bolder'
                        ),
                        Button('Read Our Blog', cls='uk-button uk-button-text'),
                        cls='uk-card uk-card-body uk-margin-auto-vertical'
                    ),
                    Div(
                        H5('Most Popular', cls='uk-text-bolder'),
                        Ul(
                            Li(
                                A('What are Portfolio Accounting Systems', href='#', cls='uk-link-muted')
                            ),
                            Li(
                                A('Investing Basics for New Grads', href='#', cls='uk-link-muted')
                            ),
                            Li(
                                A('What is the Average Net Worth by Age', href='#', cls='uk-link-muted')
                            ),
                            Li(
                                A('Wealth Management vs. Investment Banking', href='#', cls='uk-link-muted')
                            ),
                            Li(
                                A("2024's Best Provinces to Retire in South Africa", href='#', cls='uk-link-muted')
                            ),
                            cls='uk-list uk-list-disc uk-list-primary uk-text-small'
                        ),
                        cls='uk-card uk-card-body uk-margin-auto-vertical'
                    )
                ),
                Div(
                    Div(
                        Div(style='height: 320px; background-image: url('
                                  'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                  '/krzysztof-hepner-o_x11ORH9vQ-unsplash.jpg)',
                            tabindex='0', cls='uk-background-cover'),
                        Div(
                            H4('How to Achieve True Wealth', cls='uk-card-title, uk-text-bolder'),
                            P('''Unlocking true wealth involves strategic planning, smart investments, and a holistic 
                            approach to managing your financial resources. Discover the steps to build and sustain 
                            genuine financial prosperity.''',
                              cls='uk-text-small'),
                            cls='uk-card-body'
                        ),
                        cls='uk-card uk-card-small uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(style='height: 320px; background-image: url('
                                  'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                  '/pedro-miranda-3QzMBrvCeyQ-unsplash.jpg)',
                            tabindex='0', cls='uk-background-cover'),
                        Div(
                            H4('Step Focused Planning', cls='uk-card-title, uk-text-bolder'),
                            P('''Achieve your financial goals with step-by-step, focused planning that guides you 
                            through every stage of wealth building and preservation.''',
                              cls='uk-text-small'),
                            cls='uk-card-body'
                        ),
                        cls='uk-card uk-card-small uk-card-body'
                    )
                ),
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
                            cls='uk-heading-small uk-margin-small-bottom'),
                        Div('Building Your Legacy with Trusted Growth', cls='uk-text-small'),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div('Our Services', cls='uk-text-bolder uk-text-success uk-text-large uk-margin-medium-bottom'),
                        Ul(
                            Li(
                                A('Financial Planning', href='#')
                            ),
                            Li(
                                A('Investment Management', href='#')
                            ),
                            Li(
                                A('Retirement Planning', href='#')
                            ),
                            Li(
                                A('Investment Analysis', href='#')
                            ),
                            Li(
                                A('Insurance', href='#')
                            ),
                            cls='uk-list uk-text-small'
                        ),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div('Explore', cls='uk-text-bolder uk-text-success uk-text-large uk-margin-medium-bottom'),
                        Ul(
                            Li(
                                A('About', href='#')
                            ),
                            Li(
                                A('Services', href='#')
                            ),
                            Li(
                                A('Careers', href='#')
                            ),
                            Li(
                                A("FAQ's", href='#')
                            ),
                            Li(
                                A('Partner', href='#')
                            ),
                            cls='uk-list uk-text-small'
                        ),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div("Let's Talk", cls='uk-text-bolder uk-text-success uk-text-large uk-margin-medium-bottom'),
                        Div('We\'re Here to Help You Grow Your Wealth, Plan Your Future, and Achieve Your Financial '
                            'Goals', cls='uk-text-small'),
                        Button('Contact Us', cls='uk-button uk-button-primary uk-button-large uk-margin-top',
                               data_uk_toggle='target: #contact-us'),
                        cls='uk-card uk-card-body'
                    )
                ),
                data_uk_grid=True,
                cls='uk-grid-match uk-child-width-1-3@s uk-child-width-1-4@l'
            ),
            Div(
                Div(
                    Div(
                        Div(
                            Div(
                                Span(uk_icon='icon: location; ratio: 1.8', cls='uk-icon'),
                                cls='uk-width-auto'
                            ),
                            Div(
                                Div('Location', cls='uk-text-large uk-text-bolder'),
                                Div('No. 30 Pinetown, Durban 3610', cls='uk-text-small'),
                                cls='uk-margin-auto-vertical'
                            ),
                            cls='uk-child-width-1-2 uk-grid-small'
                        ),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(
                            Div(
                                Span(uk_icon='icon: receiver; ratio: 1.8', cls='uk-icon'),
                                cls='uk-width-auto'
                            ),
                            Div(
                                Div('Phone', cls='uk-text-large uk-text-bolder'),
                                Div('0860 258 2447', cls='uk-text-small'),
                                cls='uk-margin-auto-vertical'
                            ),
                            cls='uk-child-width-1-2 uk-grid-small'
                        ),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(
                            Div(
                                Span(uk_icon='icon: mail; ratio: 1.8', cls='uk-icon'),
                                cls='uk-width-auto'
                            ),
                            Div(
                                Div('Email', cls='uk-text-large uk-text-bolder'),
                                Div(
                                    'admin',
                                    Br(),
                                    '@bluechipinvest',
                                    Br(),
                                    '.co.za',
                                    cls='uk-text-small'
                                ),
                                cls='uk-margin-auto-vertical'
                            ),
                            cls='uk-child-width-1-2 uk-grid-small'
                        ),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div(
                            Div(
                                Span(uk_icon='icon: facebook', cls='uk-icon-button uk-icon')
                            ),
                            Div(
                                Span(uk_icon='icon: linkedin', cls='uk-icon-button uk-icon')
                            ),
                            Div(
                                Span(uk_icon='icon: instagram', cls='uk-icon-button uk-icon')
                            ),
                            Div(
                                Span(uk_icon='icon: x', cls='uk-icon-button uk-icon')
                            ),
                            data_uk_grid=True,
                            cls='uk-grid-small uk-child-width-auto'
                        ),
                        cls='uk-card uk-card-body'
                    )
                ),
                data_uk_grid=True,
                cls='uk-grid-match uk-child-width-1-2 uk-child-width-1-3@s uk-child-width-1-4@l'
            ),
            cls='uk-container'
        ),
        cls='uk-section uk-section-medium uk-section-secondary'
    )


@app.route('/')
def home():
    return Body(
        nav(),
        potential_interest_calculators(),
        hero(),
        contact_us(),
        subhero(),
        advisor_section(),
        serve_section(),
        metric_section(),
        preserve_section(),
        whatwedo_section(),
        testimonials_section(),
        guides_section(),
        footer()
    )


serve()
