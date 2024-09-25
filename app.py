from fasthtml.common import FastHTML, serve
from fasthtml.components import Script, Link, Li, A, Body, Nav, Div, Ul, Span, Button, Input, Fieldset, Form, H4, \
    Hr, H3, H1, Br, P, H2, H5, Img, Textarea, Title, Canvas

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
                  '700&display=swap')
    ), surreal=False, pico=False, default_hdrs=False
)

nav_link = lambda href, title: Li(
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

images = [f'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/image_{x}.webp' for x in
          range(1, 31)]


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
                                Button("Let's Talk", cls='uk-button uk-button-small uk-light',
                                       style='background-color: #00213B')
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
                    Button("Let's Talk", cls='uk-button uk-button-small uk-visible@l uk-light',
                           data_uk_toggle='target: #contact-us', style='background-color: #00213B'),
                    A(data_uk_icon='user', cls='uk-icon-button uk-icon uk-light', style='background-color: #00213B'),
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
                        Button('Get Started', cls='uk-button uk-button-small uk-light',
                               data_uk_toggle='target: #contact-us', style='background-color: #00213B'),
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
        style=f'background-image: url({images[20]}); filter: grayscale(90%);',
        cls='uk-background-bottom-right uk-background-cover'
    )


def contact_us():
    return Div(
        Div(
            Button(type='button', data_uk_close=True, cls='uk-offcanvas-close'),
            H3(Span('Request', cls='uk-text-muted'), ' an', Br(), 'Appointment', cls='uk-text-bolder'),
            Hr(style='height: 0px; border: none; border-top: 2px solid;', cls='uk-width-small uk-text-primary'),
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
            cls='uk-offcanvas-bar', style='background-color: #00213B'
        ),
        id='contact-us',
        data_uk_offcanvas='mode: push; overlay: true'
    )


def subhero():
    return Div(
        Div(
            Div(
                H2(
                    'Planning objective', Br(), Span('financial advice'),
                    cls='uk-text-bolder uk-margin-xlarge-left'
                ),
                Button('View All', cls='uk-button uk-button-text uk-margin-xlarge-left'),
                services(),
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
                cls='uk-margin-auto-vertical uk-card uk-card-body'
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


def services():
    return Div(
        Div(
            Div(
                Div(
                    *[Div(
                        Div(
                            Div(
                                Img(src=img, width='1800', height='1200', alt=''),
                                cls='uk-card-media-top'
                            ),
                            Div(
                                H3(title, cls='uk-card-title'),
                                P(subtitle),
                                A('Find Out More', href='#', cls='uk-button uk-button-default',
                                  data_uk_toggle='target: #contact-us'),
                                cls='uk-card-body uk-padding-remove uk-margin-top'
                            ),
                            cls='uk-card'
                        )
                    ) for title, subtitle, img in [
                        ('Financial Planning', 'Financial planning is a tailored strategy to help you achieve your '
                                               'financial goals, make smart decisions, and secure your future with '
                                               'confidence.', images[11]),
                        ('Investment Management', 'Investment management optimizes your investments to grow your '
                                                  'wealth, with a strategy tailored to your goals and risk '
                                                  'tolerance.', images[13]),
                        ('Retirement Planning', 'Retirement planning ensures you can live comfortably after you stop '
                                                'working by setting savings goals and managing your income, '
                                                'giving you peace of mind for the future.', images[19]),
                        ('Investment Analysis', 'Investment analysis evaluates financial assets to inform your '
                                                'investment decisions, assessing risk and returns to identify '
                                                'opportunities that align with your goals. This helps maximize growth '
                                                'while minimizing risk.', images[21]),
                        ('Insurance', 'Insurance protects against unexpected events, preventing financial loss and '
                                      'ensuring peace of mind for you and your family.', images[14])
                    ]],
                    cls='uk-slider-items uk-child-width-1-4@m uk-grid'
                ),
                A(href='#', data_uk_slidenav_previous=True, data_uk_slider_item='previous',
                  cls='uk-position-center-left uk-position-small uk-hidden-hover'),
                A(href='#', data_uk_slidenav_next=True, data_uk_slider_item='next',
                  cls='uk-position-center-right uk-position-small uk-hidden-hover'),
                tabindex='-1',
                cls='uk-position-relative uk-visible-toggle'
            ),
            Ul(cls='uk-slider-nav uk-dotnav uk-flex-center uk-margin'),
            data_uk_slider=True,
            cls='uk-slider-container-offset'
        ),
        data_uk_dropdown='boundary: !.uk-grid; stretch: x; flip: false; mode: click',
        cls='uk-light', style='background-color: #00213B'
    )


def advisor_section():
    return Div(
        Div(
            *[Div(
                Div(style=f'height: {height}; background-image: url({img}); filter: grayscale(90%);',
                    cls='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle'),
                cls='uk-visible@s uk-first-column'
            ) for img, height in
                [(images[24], '100px'), (images[25], '150px'), (images[28], '300px'), (images[8], '120px'),
                 (images[22], '180px'), (images[1], '140px')]
            ],
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
                    Button('Read More', type='button', cls='uk-button uk-button-text'),
                    advisor_section_read_more(),
                    cls='uk-card uk-card-body uk-margin-auto-vertical'
                ),
                cls='uk-grid-margin uk-first-column'
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
                    *[Div(
                        Div(style=f'height: {height}; background-image: url({img})', tabindex='0',
                            cls='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle')
                    ) for height, img in
                        [('100px', images[0]), ('150px', images[22]), ('120px', images[27]), ('180px', images[4]),
                         ('140px', images[9])]
                    ],
                    data_uk_grid='masonry: pack',
                    cls='uk-visible@s uk-child-width-1-2@s'
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
                    Button('Talk to us', cls='uk-button uk-button-large uk-light',
                           data_uk_toggle='target: #contact-us', style='background-color: #00213B'),
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
                        Button('Read More', cls='uk-button uk-button-text'),
                        serve_section_read_more(title),
                        cls='uk-card-body'
                    ),
                    cls='uk-card uk-card-small'
                )
            ) for title, img in [
                ('Business Owners', images[10]),
                ('Private Client', images[15]),
                ('Pre-Retirees', images[7]),
                ('Retirees', images[12]),
                ('Young Investor', images[3])
            ]],
            data_uk_grid=True,
            cls='uk-child-width-1-5@m uk-child-width-1-3@s uk-child-width-1-2 uk-margin-medium-top'
        ),
        cls='uk-container serve-section'
    )


def serve_section_read_more(title):
    clientele = dict(
        business_owners=dict(name='Business Owners',
                             img=images[10],
                             desc='We offer tailored financial services for business owners, including comprehensive '
                                  'financial planning, tax strategy and compliance, retirement planning, '
                                  'and investment management. Our expertise extends to cash flow management, '
                                  'insurance solutions, and succession planning, ensuring that your business is '
                                  'protected and positioned for growth. Additionally, we provide employee benefits '
                                  'consulting and debt management strategies to help you attract talent and manage '
                                  'finances effectively. Let us partner with you to achieve your financial goals and '
                                  'secure a prosperous future for your business.'),
        private_client=dict(name='Private Client',
                            img=images[15],
                            desc='For private clients, we provide personalized financial services designed to meet '
                                 'individual needs and goals. Our offerings include wealth management, '
                                 'estate planning, tax optimization, and investment strategies tailored to your '
                                 'financial situation. We focus on building long-term relationships, ensuring your '
                                 'assets are managed effectively while aligning with your life goals. Additionally, '
                                 'we offer retirement planning, insurance solutions, and philanthropic guidance, '
                                 'helping you create a legacy that reflects your values. Trust us to navigate your '
                                 'financial journey with expertise and care.'),
        pre_retirees=dict(name='Pre-Retirees',
                          img=images[7],
                          desc='We specialize in helping you prepare for a financially secure retirement. Our '
                               'services include retirement planning, investment strategy development, and income '
                               'distribution planning to ensure your savings last throughout your retirement years. '
                               'We provide personalized assessments of your financial situation, tax optimization '
                               'strategies, and guidance on Social Security benefits. Additionally, we focus on '
                               'healthcare planning and long-term care options, helping you navigate the complexities '
                               'of retirement. Let us partner with you to create a comprehensive plan that aligns '
                               'with your retirement goals and lifestyle.'),
        retirees=dict(name='Retirees',
                      img=images[12],
                      desc='We provide comprehensive financial services to retirees, ensuring a fulfilling and secure '
                           'retirement. Our expertise includes income planning, investment management, '
                           'and tax optimization to maximize retirement savings. We focus on creating a sustainable '
                           'withdrawal strategy that allows assets to last while supporting your desired lifestyle. '
                           'Additionally, we assist with estate planning and healthcare considerations, navigating the '
                           'complexities of long-term care and Medicare. Trust us for personalized support and '
                           'guidance as you embrace this exciting new chapter in your life.'),
        young_investor=dict(name='Young Investor',
                            img=images[3],
                            desc='We empower young investors with tailored financial services designed to build a '
                                 'solid foundation for future wealth. Our offerings include investment education, '
                                 'portfolio management, and personalized financial planning to help you set and '
                                 'achieve your financial goals. We focus on strategies for saving, budgeting, '
                                 'and understanding market dynamics, ensuring you feel confident in your investment '
                                 'choices. Additionally, we provide guidance on retirement accounts and long-term '
                                 'investment strategies, helping you cultivate a path toward financial independence. '
                                 'Let us support you on your journey to becoming a successful investor.')
    )
    arg = next((value for value in clientele.values() if value['name'] == title), 'Business Owners')
    return Div(
        Div(
            Div(
                Img(src=arg['img'], alt='', data_uk_cover=True),
                Canvas(width='600', height='400'),
                cls='uk-card-media-left uk-cover-container'
            ),
            Div(
                Div(
                    H3(arg['name'], cls='uk-text-bolder'),
                    P(arg['desc'], cls='uk-width-2-3@m'),
                    Button('Talk to us', cls='uk-button uk-button-default uk-button-large',
                           data_uk_toggle='target: #contact-us'),
                    cls='uk-card-body'
                )
            ),
            data_uk_grid=True,
            cls='uk-card uk-grid-collapse uk-child-width-1-2@s uk-margin uk-light', style='background-color: #00213B'
        ),
        data_uk_dropdown='mode: click; stretch: x; pos: top-left; boundary: !.serve-section; flip: false',
        cls='uk-light', style='background-color: #00213B'
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
                H1('Preserve and Grow Your Financial Legacy', cls='uk-text-secondary uk-text-bolder'),
                Button('Contact Us', cls='uk-button uk-light', data_uk_toggle='target: #contact-us',
                       style='background-color: #00213B'),
                cls='uk-card uk-card-body uk-width-1-2@s'
            ),
            style=f'background-image: url({images[26]}); filter: grayscale(90%);',
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
                            Span('What', cls='uk-text-primary'),
                            ' We Do',
                            Hr(style='height: 0px; border: none; border-top: 2px solid;',
                               cls='uk-width-small uk-text-primary'),
                            cls='uk-text-bolder'
                        ),
                        P('Providing tailored solutions for financial advisors to elevate client success.',
                          cls='uk-width-medium'),
                        Button('View All', cls='uk-button uk-button-text'),
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
                            *[Span(uk_icon='star', cls='uk-text-warning uk-icon') for _ in range(5)],
                        ),
                        P(
                            Span(title, cls='uk-text-bolder'),
                            Br(), subtext,
                            cls='uk-text-italic'
                        ),
                        Div(
                            Div(
                                Img(alt='Border pill', height='64',
                                    src=images[17], style='filter: grayscale(90%);',
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
                        Button('Read Our Blog', cls='uk-button uk-button-text'),
                        cls='uk-card uk-card-body uk-margin-auto-vertical'
                    ),
                    Div(
                        H5('Most Popular', cls='uk-text-bolder'),
                        Ul(
                            *[Li(
                                A(title, href=href, cls='uk-link-muted')
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
                    (images[18], 'How to Achieve True Wealth',
                     'Unlocking true wealth involves strategic planning, smart investments, and a holistic approach to '
                     'managing your financial resources. Discover the steps to build and sustain genuine financial '
                     'prosperity.'),
                    (images[23], 'Step Focused Planning',
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
                            cls='uk-heading-small uk-margin-small-bottom'),
                        Div('Building Your Legacy with Trusted Growth', cls='uk-text-small'),
                        cls='uk-card uk-card-body'
                    )
                ),
                Div(
                    Div(
                        Div('Our Services', cls='uk-text-bolder uk-text-primary uk-text-large uk-margin-medium-bottom'),
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
                        Div('Explore', cls='uk-text-bolder uk-text-primary uk-text-large uk-margin-medium-bottom'),
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
                        Div("Let's Talk", cls='uk-text-bolder uk-text-primary uk-text-large uk-margin-medium-bottom'),
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
                        Div('Social', cls='uk-text-large uk-text-bolder uk-margin-small'),
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
        cls='uk-section uk-section-medium uk-light', style='background-color: #00213B'
    )


@app.route('/')
def home():
    return Title('Blue Chip Invest'), Body(
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
