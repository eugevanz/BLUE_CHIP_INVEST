import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H1([
                            html.Span(['Get a clear path to']),
                            html.Br(),
                            html.Span(['your financial goals.'])
                        ], className='uk-text-bolder'),
                        html.P(['Our Wealth Activating team can help you']),
                        html.A(['Get Started'], className='uk-button uk-button-small uk-light', href='/contact-us/',
                               style={'background-color': '#091235'})
                    ], className='uk-card uk-card-body uk-margin-auto-vertical')
                ], style={'min-height': 'max(0px, 60vh)'}, **{'data-uk-height-viewport': 'offset-bottom: 40'},
                    className='uk-flex')
            ], **{'data-uk-grid': 'true'}, className='uk-child-width-1-2@s uk-flex-right')
        ], className='uk-container')
    ], style={
        'background-image': 'url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                            '/marten-bjork-6dW3xyQvcYE-unsplash_6_11zon.webp)', 'filter': 'grayscale(90%)'},
        className='uk-background-bottom-right uk-background-cover'),
    html.Div([
        html.Div([
            html.Div([
                html.H2([
                    'Planning objective', html.Br(), html.Span(['financial advice'], className='uk-light')
                ], className='uk-text-bolder uk-margin-xlarge-left@s'),
                html.A('View All', className='uk-button uk-button-text uk-margin-xlarge-left@s', href='/services/')
            ], className='uk-margin-auto-vertical uk-card uk-card-body uk-card-large')
        ], className='uk-width-2-5@m uk-light', style={'background-color': '#091235'}),
        *[html.Div([
            html.Div([
                html.Span(**{'data-uk-icon': 'icon: settings; ratio: 2'}, className='uk-icon'),
                html.Div([
                    html.Span(title)
                ], className='uk-text-bolder uk-margin-small-top'),
                html.Div(subtitle, className='uk-text-small')
            ], className='uk-card uk-card-body', style={'color': '#36454F'})
        ], style={'background-color': '#88A9C3'}) for title, subtitle in [
            ('Risk Management', 'Risk management is critical to long-term success and sustainability'),
            ('Investment Analytics', 'Leveraging investment analytics and make more informed decisions'),
            ('Cash Flow', 'Effective cash flow management is crucial for business survival')
        ]]
    ], **{'data-uk-grid': 'true'}, className='uk-child-width-expand@s uk-grid-collapse uk-grid-match uk-flex-middle',
        style={'background-color': '#88A9C3'}),
    html.Div([
        html.Div([
            *[html.Div([
                html.Div(style={'height': height, 'background-image': f'url({img})', 'filter': 'grayscale(90%)'},
                         className='uk-background-cover uk-card uk-card-default uk-flex uk-flex-center uk-flex-middle')
            ], className='uk-visible@s') for img, height in [
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
            html.Div([
                html.Div([
                    html.H2([
                        html.Span(['We Help'], style={'color': '#88A9C3'}),
                        ' financial',
                        html.Br(),
                        html.Span(['Advisors that']),
                        html.Br(),
                        html.Span(['exclusively serve.'])
                    ], className='uk-text-bolder'),
                    html.P([
                        'We empower financial advisors dedicated to serving a select clientele'
                    ], className='uk-width-medium'),
                    html.A(['Read More'], className='uk-button uk-button-text', href='/advisors/')
                ], className='uk-card uk-card-body')
            ])
        ], style={'height': '627px'}, **{'data-uk-grid': 'masonry: pack'},
            className='uk-child-width-1-2@s uk-child-width-1-3@m uk-grid-small uk-grid uk-flex-top uk-flex-wrap-top')
    ], id='advisor-section', className='uk-container uk-margin-xlarge-top advisor-section'),
    html.Div([
        html.Div([
            html.H2([
                html.Span(['Who'], style={'color': '#88A9C3'}),
                html.Span([' We Serve']),
                html.Hr(style={'height': '0px', 'border': 'none', 'border-top': '2px solid', 'color': '#88A9C3'},
                        className='uk-width-small')
            ], className='uk-text-bolder'),
            html.P('Focused support for financial advisors with a unique clientele.', className='uk-width-medium')
        ], className='uk-card uk-card-body uk-margin-auto-vertical'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div(
                            style={'height': '240px', 'background-image': f'url({img})', 'mask-image':
                                'linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0))', 'filter': 'grayscale(90%)'},
                            className='uk-background-cover'),
                        html.H3([title], className='uk-text-bolder uk-position-bottom',
                                style={'padding': '20px', 'padding-bottom': '38px', 'line-height': '24px',
                                       'color': '#88A9C3'}),
                    ]),
                    html.Div([
                        html.A(['Read More'], className='uk-button uk-button-text', href='/who-we-serve/')
                    ], className='uk-card-body')
                ], className='uk-card uk-card-small')
            ]) for title, img in [
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
            ]
        ], **{'data-uk-grid': 'true'},
            className='uk-child-width-1-5@m uk-child-width-1-3@s uk-child-width-1-2 uk-margin-medium-top')
    ], className='uk-container serve-section'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div(['R142M'],
                             style={'font-family': '"Playfair Display SC", serif', 'font-weight': '700',
                                    'font-style': 'normal'},
                             className='uk-heading-small'),
                    html.Div(['Assets Under Management'], className='uk-text-small')
                ], className='uk-text-center'),
                html.Div([
                    html.Div(['6'],
                             style={'font-family': '"Playfair Display SC", serif', 'font-weight': '700',
                                    'font-style': 'normal'},
                             className='uk-heading-small'),
                    html.Div(['Office Locations in RSA'], className='uk-text-small')
                ], className='uk-text-center'),
                html.Div([
                    html.Div(['2019'],
                             style={'font-family': '"Playfair Display SC", serif', 'font-weight': '700',
                                    'font-style': 'normal'},
                             className='uk-heading-small'),
                    html.Div(['Year founded company'], className='uk-text-small')
                ], className='uk-text-center'),
                html.Div([
                    html.Div(['1,097'],
                             style={'font-family': '"Playfair Display SC", serif', 'font-weight': '700',
                                    'font-style': 'normal'},
                             className='uk-heading-small'),
                    html.Div(['Clients represented through our firm'], className='uk-text-small')
                ], className='uk-text-center')
            ], **{'data-uk-grid': 'true'}, className='uk-grid-divider uk-child-width-expand@s')
        ], className='uk-container')
    ], className='uk-section uk-section-large'),
    html.Div([
        html.Div(
            style={'background-image': 'url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public'
                                       '/website_images/scott-webb-hDyO6rr3kqk-unsplash_12_11zon.webp)',
                   'filter': 'grayscale(90%)'},
            className='uk-height-large uk-background-cover uk-background-center-center'
        ),
        html.Div([
            html.H1([
                'Preserve and Grow Your Financial Legacy'
            ], className='uk-text-bolder uk-width-1-2', style={'color': '#2A3A58'}),
            html.A(['Contact Us'], className='uk-button uk-light', href='/contact-us/',
                   style={'background-color': '#091235'})
        ], className='uk-card uk-card-body uk-overlay', style={'position': 'absolute', 'bottom': '0px'})
    ], className='uk-container', style={'position': 'relative'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H2([
                            html.Span(['What'], style={'color': '#88A9C3'}),
                            ' We Do',
                            html.Hr(style={'height': '0px', 'border': 'none', 'border-top': '2px solid',
                                           'color': '#88A9C3'},
                                    className='uk-width-small')
                        ], className='uk-text-bolder'),
                        html.P(['Providing tailored solutions for financial advisors to elevate client success.'],
                               className='uk-width-medium uk-light'),
                        html.A(['View All'], className='uk-button uk-button-text', href='/services/')
                    ], className='uk-card uk-card-body uk-margin-auto-vertical uk-text-left uk-light',
                        style={'background-color': '#091235'})
                ], className='uk-width-1-2@m'),
                *[html.Div([
                    html.Div([
                        html.Span(**{'data-uk-icon': f'icon: {icon}; ratio: 2.5'}, className='uk-icon', style={
                            'color': '#88A9C3'}),
                        html.P([title], className='uk-text-bolder'),
                        html.Div([subtitle], className='uk-text-small')
                    ], className='uk-card uk-card-default uk-card-body')
                ], className='uk-width-1-4@m uk-width-1-2@s') for icon, title, subtitle in [
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
                ]]
            ], **{'data-uk-grid': 'true'}, className='uk-grid-match uk-text-center')
        ], className='uk-container')
    ], className='uk-section uk-section-xlarge'),
    html.Div([
        html.Div([
            html.Div([
                html.Div(['WHAT OUR CUSTOMERS SAY'], className='uk-text-small uk-text-bolder uk-light'),
                html.H2([
                    html.Span('Our', style={'color': '#88A9C3'}),
                    ' Testimonials'
                ], className='uk-text-bolder uk-margin-remove-top')
            ], className='uk-card uk-card-body uk-text-center'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Span(**{'data-uk-icon': 'icon: star'}, className='uk-text-warning uk-icon') for _ in
                            range(5)
                        ]),
                        html.P([
                            html.Span([title], className='uk-text-bolder'),
                            html.Br(), subtext
                        ], className='uk-text-italic'),
                        html.Div([
                            html.Div([
                                html.Img(alt='Border pill', height='64',
                                         src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public'
                                             '/website_images/jurica-koletic-7YVZYZeITc8-unsplash_3_11zon.webp',
                                         style={'filter': 'grayscale(90%)'},
                                         width='64', className='uk-border-circle')
                            ], className='uk-width-auto'),
                            html.Div([
                                html.Div([f'— {name}'], className='uk-text-bolder'),
                                html.Div([pos], className='uk-text-small')
                            ], className='uk-margin-auto-vertical')
                        ], **{'data-uk-grid': 'true'}, className='uk-grid-small')
                    ], className='uk-card uk-card-default uk-card-body')
                ]) for title, subtext, name, pos in [
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
                ]
            ], **{'data-uk-grid': 'true'}, className='uk-grid-match uk-child-width-expand@m')
        ], className='uk-container')
    ], className='uk-section uk-light', style={'background-color': '#091235'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H2([
                            html.Span(['Personal'], style={'color': '#88A9C3'}),
                            ' Finance Guides',
                            html.Hr(style={'height': '0px', 'border': 'none', 'border-top': '2px solid',
                                           'color': '#88A9C3'},
                                    className='uk-width-small')
                        ], className='uk-text-bolder'),
                        html.A('Read Our Blog', className='uk-button uk-button-text', href='/guides/')
                    ], className='uk-card uk-card-body'),
                    html.Div([
                        html.H5(['Most Popular'], className='uk-text-bolder'),
                        html.Ul([
                            html.Li([
                                html.A(title, id=id, className='uk-link-muted', href='/guides/')
                            ]) for title, id in [
                                ('What are Portfolio Accounting Systems', '#'),
                                ('Investing Basics for New Grads', '#'),
                                ('What is the Average Net Worth by Age', '#'),
                                ('Wealth Management vs. Investment Banking', '#'),
                                ('2024\'s Best Provinces to Retire in South Africa', '#')
                            ]
                        ], className='uk-list uk-list-disc uk-text-small', style={'color': '#88A9C3'})
                    ], className='uk-card uk-card-body uk-margin-auto-vertical')
                ]),
                *[html.Div([
                    html.Div([
                        html.Div(
                            style={'height': '320px', 'background-image': f'url({img})', 'filter': 'grayscale(90%)'},
                            className='uk-background-cover'),
                        html.Div([
                            html.H4([title], className='uk-card-title, uk-text-bolder'),
                            html.P([desc], className='uk-text-small')
                        ], className='uk-card-body')
                    ], className='uk-card uk-card-small uk-card-body')
                ]) for img, title, desc in [
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
                ]]
            ], **{'data-uk-grid': 'true'}, className='uk-grid-match uk-child-width-expand@s')
        ], className='uk-container')
    ], className='uk-section uk-section-xlarge')
], className='uk-animation-fade')
