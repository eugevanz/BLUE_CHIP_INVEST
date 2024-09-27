from fasthtml.components import Div, Img, Canvas, H2, Span, Hr, H3, P, Button, Ul, Li, A

from interface import return_button

clientele = [
    ('Business Owners',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/ellicia-24HcJhf0u6M'
     '-unsplash.webp',
     'We offer tailored financial services for business owners, including comprehensive '
     'financial planning, tax strategy and compliance, retirement planning, '
     'and investment management. Our expertise extends to cash flow management, '
     'insurance solutions, and succession planning, ensuring that your business is '
     'protected and positioned for growth.',
     'Additionally, we provide employee benefits consulting and debt management strategies to help you attract talent '
     'and manage finances effectively. Let us partner with you to achieve your financial goals and '
     'secure a prosperous future for your business.'),
    ('Private Client',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jc-gellidon-j_5sxxspFtc'
     '-unsplash.webp',
     'For private clients, we provide personalized financial services designed to meet '
     'individual needs and goals. Our offerings include wealth management, '
     'estate planning, tax optimization, and investment strategies tailored to your '
     'financial situation.',
     'We focus on building long-term relationships, ensuring your '
     'assets are managed effectively while aligning with your life goals. Additionally, '
     'we offer retirement planning, insurance solutions, and philanthropic guidance, '
     'helping you create a legacy that reflects your values. Trust us to navigate your '
     'financial journey with expertise and care.'),
    ('Pre-Retirees',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/birmingham-museums-trust'
     '-T2AmpV9qWqw-unsplash.webp',
     'We specialize in helping you prepare for a financially secure retirement. Our '
     'services include retirement planning, investment strategy development, and income '
     'distribution planning to ensure your savings last throughout your retirement years. '
     'We provide personalized assessments of your financial situation, tax optimization '
     'strategies, and guidance on Social Security benefits.',
     ' Additionally, we focus on healthcare planning and long-term care options, helping you navigate the complexities '
     'of retirement. Let us partner with you to create a comprehensive plan that aligns with your retirement goals '
     'and lifestyle.'),
    ('Retirees',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/huy-phan-QCF2ykBsC2I'
     '-unsplash.webp',
     'We provide comprehensive financial services to retirees, ensuring a fulfilling and secure '
     'retirement. Our expertise includes income planning, investment management, '
     'and tax optimization to maximize retirement savings. We focus on creating a sustainable '
     'withdrawal strategy that allows assets to last while supporting your desired lifestyle. ',
     'Additionally, we assist with estate planning and healthcare considerations, navigating the '
     'complexities of long-term care and Medicare. Trust us for personalized support and '
     'guidance as you embrace this exciting new chapter in your life.'),
    ('Young Investor',
     'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/ali-morshedlou-WMD64tMfc4k'
     '-unsplash.webp',
     'We empower young investors with tailored financial services designed to build a '
     'solid foundation for future wealth. Our offerings include investment education, '
     'portfolio management, and personalized financial planning to help you set and '
     'achieve your financial goals.',
     'We focus on strategies for saving, budgeting, and understanding market dynamics, ensuring you feel confident in '
     'your investment choices. Additionally, we provide guidance on retirement accounts and long-term '
     'investment strategies, helping you cultivate a path toward financial independence. Let us support you on your '
     'journey to becoming a successful investor.')
]

page = Div(
    Div(
        return_button,
        Div(
            H2(
                Span('Who', cls='uk-text-primary'), Span(' We Serve'),
                Hr(style='height: 0px; border: none; border-top: 2px solid;', cls='uk-width-small uk-text-primary'),
                cls='uk-text-bolder'
            ),
            cls='uk-card uk-card-body'
        ),
        Div(
            *[Div(
                Div(
                    Div(
                        Img(src=img, alt='', data_uk_cover=True),
                        Canvas(width='600', height='400'),
                        cls='uk-card-media-top uk-cover-container'
                    ),
                    Div(
                        Div(
                            H3(name, cls='uk-text-bolder'),
                            Ul(
                                Li(
                                    A(desc, href='', cls='uk-accordion-title uk-text-default'),
                                    Div(
                                        P(subdesc),
                                        cls='uk-accordion-content'
                                    )
                                ),
                                data_uk_accordion=True
                            ),
                            Button('Talk to us', cls='uk-button uk-button-link uk-button-large',
                                   hx_get='/contact-us/', hx_target='#page', hx_swap='innerHTML',
                                   hx_push_url='true'),
                            cls='uk-card-body'
                        )
                    ),
                    cls='uk-card uk-card-small'
                )
            ) for name, img, desc, subdesc in clientele],
            data_uk_grid='masonry: pack', cls='uk-child-width-1-2@s uk-child-width-1-3@m'
        ),
        cls='uk-container'
    ),
    cls='uk-section'
)