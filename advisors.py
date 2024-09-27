from fasthtml.components import Div, H2, Span, Br, P, Button, Hr, Img, H3

from interface import return_button

page = Div(
    Div(
        return_button,
        Div(
            Div(
                Div(
                    data_src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/youssef'
                             '-naddam-iJ2IG8ckCpA-unsplash.webp',
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
            cls='uk-card uk-grid-collapse uk-child-width-1-2@s uk-margin'
        ),
        Div(
            H2(
                Span('Meet', cls='uk-text-primary'), Span(' Our Team'),
                Hr(style='height: 0px; border: none; border-top: 2px solid;', cls='uk-width-small uk-text-primary'),
                cls='uk-text-bolder'
            ),
            cls='uk-card uk-card-body'
        ),
        Div(
            *[Div(
                Div(
                    Div(
                        Img(src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                '/jurica-koletic-7YVZYZeITc8-unsplash.webp', width='1800', height='1200', alt=''),
                        cls='uk-card-media-top'
                    ),
                    Div(
                        H3(name, cls='uk-card-title'),
                        P(pos),
                        cls='uk-card-body'
                    ),
                    cls='uk-card uk-card-default'
                )
            ) for name, pos in [
                ('Aidan Mercer', 'Senior Investment Strategist'),
                ('Fiona Drake', 'Chief Financial Officer (CFO)'),
                ('Liam Caldwell', 'Wealth Management Advisor'),
                ('Chloe Rutherford', 'Portfolio Manager'),
                ('Ethan Carrington', 'Head of Corporate Finance'),
                ('Isabelle Thornton', 'Private Client Relationship Manager'),
                ('Marcus Ellison', 'Director of Risk Management'),
                ('Sophia Bennett', 'Chief Compliance Officer (CCO)')
            ]],
            data_uk_grid=True,
            cls='uk-grid-match uk-child-width-1-3@s uk-child-width-1-4@m'
        ),
        cls='uk-container'
    ),
    cls='uk-section'
)
