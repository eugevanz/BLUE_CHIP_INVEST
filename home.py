from fasthtml.components import Div, H1, Br, Span, P, Button, H2, H3, Hr, Img, H5, Ul, Li, A, H4

page = Div(
    Div(
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
                               hx_target='#page', hx_push_url='/home/',
                               style='background-color: #091235'),
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
    ),
    Div(
        Div(
            Div(
                H2(
                    'Planning objective', Br(), Span('financial advice', cls='uk-light'),
                    cls='uk-text-bolder uk-margin-xlarge-left@s'
                ),
                Button('View All', cls='uk-button uk-button-text uk-margin-xlarge-left@s', hx_get='/services/',
                       hx_target='#page', hx_push_url='/home/'),
                cls='uk-margin-auto-vertical uk-card uk-card-body uk-card-large'
            ),
            cls='uk-width-2-5@m uk-light', style='background-color: #091235'
        ),
        *[Div(
            Div(
                Span(data_uk_icon='icon: settings; ratio: 2', cls='uk-icon'),
                Div(
                    Span(title),
                    cls='uk-text-bolder uk-margin-small-top'
                ),
                Div(subtitle, cls='uk-text-small'),
                cls='uk-card uk-card-body', style='color: #36454F;'
            ),
            style='background-color: #88A9C3;'
        ) for title, subtitle in [
            ('Risk Management', 'Risk management is critical to long-term success and sustainability'),
            ('Investment Analytics', 'Leveraging investment analytics and make more informed decisions'),
            ('Cash Flow', 'Effective cash flow management is crucial for business survival')
        ]],
        data_uk_grid=True,
        cls='uk-child-width-expand@s uk-grid-collapse uk-grid-match uk-flex-middle', style='background-color: #88A9C3;'
    ),
    Div(
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
                        Span('We Help', style='color: #88A9C3;'),
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
                           hx_target='#page', hx_push_url='/home/'),
                    cls='uk-card uk-card-body'
                )
            ),
            style='height: 627px;',
            data_uk_grid='masonry: pack',
            cls='uk-child-width-1-2@s uk-child-width-1-3@m uk-grid-small uk-grid uk-flex-top uk-flex-wrap-top'
        ),
        id='advisor-section',
        cls='uk-container uk-margin-xlarge-top advisor-section'
    ),
    Div(
        Div(
            H2(
                Span('Who', style='color: #88A9C3;'), Span(' We Serve'),
                Hr(style='height: 0px; border: none; border-top: 2px solid; color: #88A9C3;', cls='uk-width-small'),
                cls='uk-text-bolder'
            ),
            P('Focused support for financial advisors with a unique clientele.', cls='uk-width-medium'),
            cls='uk-card uk-card-body uk-margin-auto-vertical'
        ),
        Div(
            *[Div(
                Div(
                    Div(
                        Div(
                            style=f'height: 240px; background-image: url({img});mask-image: linear-gradient(to '
                                  f'bottom, rgba(0,0,0,1), rgba(0,0,0,0)); filter: grayscale(90%);',
                            cls='uk-background-cover'),
                        H3(title, cls='uk-text-bolder uk-position-bottom', style='padding: 20px; padding-bottom: 38px; '
                                                                                 'line-height: 24px; color: #88A9C3;'),
                    ),
                    Div(
                        Button('Read More', cls='uk-button uk-button-text', hx_get=f'/who-we-serve/{title}',
                               hx_target='#page', hx_push_url='/home/'),
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
    ),
    Div(
        Div(
            Div(
                Div(
                    Div('R142M',
                        style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                        cls='uk-heading-small'),
                    Div('Assets Under Management', cls='uk-text-small'),
                    cls='uk-text-center'
                ),
                Div(
                    Div('6', style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                        cls='uk-heading-small'),
                    Div('Office Locations in RSA', cls='uk-text-small'),
                    cls='uk-text-center'
                ),
                Div(
                    Div('2019',
                        style='font-family: "Playfair Display SC", serif; font-weight: 700; font-style: normal;',
                        cls='uk-heading-small'),
                    Div('Year founded company', cls='uk-text-small'),
                    cls='uk-text-center'
                ),
                Div(
                    Div('1,097',
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
    ),
    Div(
        Div(
            style='background-image: url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public'
                  '/website_images/scott-webb-hDyO6rr3kqk-unsplash_12_11zon.webp); filter: grayscale(90%);',
            cls='uk-height-large uk-background-cover uk-background-center-center'
        ),
        Div(
            H1('Preserve and Grow Your Financial Legacy', cls='uk-text-bolder uk-width-1-2', style='color: #2A3A58;'),
            Button('Contact Us', cls='uk-button uk-light', hx_get='/contact-us/', hx_target='#page',
                   hx_push_url='/home/',
                   style='background-color: #091235'),
            cls='uk-card uk-card-body uk-overlay', style='position: absolute; bottom: 0px;'
        ),
        cls='uk-container', style='position: relative;'
    ),
    Div(
        Div(
            Div(
                Div(
                    Div(
                        H2(
                            Span('What', style='color: #88A9C3;'),
                            ' We Do',
                            Hr(style='height: 0px; border: none; border-top: 2px solid; color: #88A9C3;',
                               cls='uk-width-small'),
                            cls='uk-text-bolder'
                        ),
                        P('Providing tailored solutions for financial advisors to elevate client success.',
                          cls='uk-width-medium uk-light'),
                        Button('View All', cls='uk-button uk-button-text', hx_get='/services/', hx_target='#page',
                               hx_push_url='/home/',
                               ),
                        cls='uk-card uk-card-body uk-margin-auto-vertical uk-text-left uk-light',
                        style='background-color: #091235'
                    ),
                    cls='uk-width-1-2@m'
                ),
                *[Div(
                    Div(
                        Span(data_uk_icon=f'icon: {icon}; ratio: 2.5', cls='uk-icon', style='color: #88A9C3;'),
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
    ),
    Div(
        Div(
            Div(
                Div('WHAT OUR CUSTOMERS SAY', cls='uk-text-small uk-text-bolder uk-light'),
                H2(
                    Span('Our', style='color: #88A9C3;'),
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
        cls='uk-section uk-light', style='background-color: #091235'
    ),
    Div(
        Div(
            Div(
                Div(
                    Div(
                        H2(
                            Span('Personal', style='color: #88A9C3;'),
                            ' Finance Guides',
                            Hr(style='height: 0px; border: none; border-top: 2px solid; color: #88A9C3;',
                               cls='uk-width-small'),
                            cls='uk-text-bolder'
                        ),
                        Button('Read Our Blog', cls='uk-button uk-button-text', hx_get='/guides/', hx_target='#page',
                               hx_push_url='/home/'),
                        cls='uk-card uk-card-body'
                    ),
                    Div(
                        H5('Most Popular', cls='uk-text-bolder'),
                        Ul(
                            *[Li(
                                A(title, href=f'#{title}', cls='uk-link-muted', hx_get='/guides/', hx_target='#page',
                                  hx_push_url='/home/')
                            ) for title, href in [
                                ('What are Portfolio Accounting Systems', '#'),
                                ('Investing Basics for New Grads', '#'),
                                ('What is the Average Net Worth by Age', '#'),
                                ('Wealth Management vs. Investment Banking', '#'),
                                ('2024\'s Best Provinces to Retire in South Africa', '#')
                            ]],
                            cls='uk-list uk-list-disc uk-text-small', style='color: #88A9C3;'
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
)
