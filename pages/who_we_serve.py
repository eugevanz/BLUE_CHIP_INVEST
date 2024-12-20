import dash
from dash import html

from interface import footer

dash.register_page(__name__)


def shorten_text(text: str):
    return f'{text[:70]}...' if len(text) > 70 else text


clientele = [
    ('Business Owners',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/ellicia-24HcJhf0u6M'
     '-unsplash_26_11zon.webp',
     'We provide tailored financial services for business owners, including financial planning, tax strategy, '
     'retirement planning, and investment management.',
     'Our expertise extends to cash flow management, '
     'insurance solutions, and succession planning, ensuring that your business is '
     'protected and positioned for growth. Additionally, we provide employee benefits consulting and debt management '
     'strategies to help you attract talent '
     'and manage finances effectively. Let us partner with you to achieve your financial goals and '
     'secure a prosperous future for your business.'),
    ('Private Client',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jc-gellidon-j_5sxxspFtc'
     '-unsplash_1_11zon.webp',
     'For private clients, we provide personalized financial services designed to meet individual needs and goals.',
     'Our offerings include wealth management, estate planning, tax optimization, and investment strategies tailored '
     'to your financial situation. We focus on building long-term relationships, ensuring your '
     'assets are managed effectively while aligning with your life goals. Additionally, '
     'we offer retirement planning, insurance solutions, and philanthropic guidance, '
     'helping you create a legacy that reflects your values. Trust us to navigate your '
     'financial journey with expertise and care.'),
    ('Pre-Retirees',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/birmingham-museums-trust'
     '-T2AmpV9qWqw-unsplash_23_11zon.webp',
     'We specialize in helping you prepare for a financially secure retirement. ',
     'Our services include retirement planning, investment strategy development, and income '
     'distribution planning to ensure your savings last throughout your retirement years. '
     'We provide personalized assessments of your financial situation, tax optimization '
     'strategies, and guidance on Social Security benefits. Additionally, we focus on healthcare planning and '
     'long-term care options, helping you navigate the complexities of retirement. Let us partner with you to create '
     'a comprehensive plan that aligns with your retirement goals and lifestyle.'),
    ('Retirees',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/huy-phan-QCF2ykBsC2I'
     '-unsplash_28_11zon.webp',
     'We provide comprehensive financial services to retirees, ensuring a fulfilling and secure '
     'retirement.',
     ' Our expertise includes income planning, investment management, '
     'and tax optimization to maximize retirement savings. We focus on creating a sustainable '
     'withdrawal strategy that allows assets to last while supporting your desired lifestyle. Additionally, '
     'we assist with estate planning and healthcare considerations, navigating the '
     'complexities of long-term care and Medicare. Trust us for personalized support and '
     'guidance as you embrace this exciting new chapter in your life.'),
    ('Young Investor',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/ali-morshedlou-WMD64tMfc4k'
     '-unsplash_19_11zon.webp',
     'We empower young investors with tailored financial services designed to build a solid foundation for future '
     'wealth.',
     'Our offerings include investment education, '
     'portfolio management, and personalized financial planning to help you set and '
     'achieve your financial goals. We focus on strategies for saving, budgeting, and understanding market dynamics, '
     'ensuring you feel confident in your investment choices. Additionally, we provide guidance on retirement '
     'accounts and long-term investment strategies, helping you cultivate a path toward financial independence. Let '
     'us support you on your journey to becoming a successful investor.')
]

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.H2([
                    html.Span(['Who'], style={'color': '#88A9C3'}), html.Span([' We Serve']),
                    html.Hr(style={'height': '0px', 'border': 'none', 'border-top': '2px solid', 'color': '#88A9C3'},
                            className='uk-width-small')
                ], className='uk-text-bolder')
            ], className='uk-card uk-card-body'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div(
                            style={'background-image': f'url({img})', 'filter': 'grayscale(90%)', 'opacity': '0.7'},
                            className='uk-height-medium uk-flex uk-flex-start uk-flex-middle uk-background-cover '
                                      'uk-background-center-center'),
                        html.Div([
                            html.H3([name], className='uk-text-bolder'),
                            html.A(['Talk to us'], className='uk-button uk-text-bolder uk-light', href='/contact-us/',
                                   style={'background-color': '#88A9C3', 'color': '#091235'})
                        ], className='uk-card uk-card-body uk-width-1-2@s uk-overlay',
                            style={'position': 'absolute', 'bottom': '0px'})
                    ], style={'position': 'relative'}),
                    html.Div([
                        html.Div([
                            html.P(desc, className='uk-text-bolder'),
                            html.P(subdesc, style={'color': 'white'})
                        ], className='uk-card uk-card-body')
                    ])
                ], **{'data-uk-grid': 'true'},
                    className='uk-grid-collapse uk-child-width-1-2@m uk-margin uk-flex-middle')
                for name, img, desc, subdesc in clientele
            ])
        ], className='uk-container')
    ], className='uk-section uk-light', style={'background-color': '#091235'}),
    footer()
])
