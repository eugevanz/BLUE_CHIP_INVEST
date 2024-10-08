from fasthtml.components import Div, H2, Span, Br, P, Button, Hr

page = Div(
    Div(
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
                        Span('We Help', style='color: #88A9C3'), ' financial', Br(), Span('Advisors that'),
                        Br(), Span('exclusively serve.'),
                        cls='uk-text-bolder'
                    ),
                    P('Dedicated to the needs of financial advisors who serve clients exclusively, '
                      'we offer customized solutions and resources that enhance their practices. Our mission is '
                      'to equip advisors with the tools and support they need to foster meaningful client '
                      'relationships, allowing them to focus on delivering top-notch financial guidance and '
                      'personalized service.'),
                    Button('Talk to us', cls='uk-button uk-button-large uk-text-bolder', hx_get='/contact-us/',
                           hx_target='#page', hx_push_url='/advisors/',
                           style='background-color: #88A9C3; color: #091235'),
                    cls='uk-card-body'
                )
            ),
            data_uk_grid=True,
            cls='uk-card uk-grid-collapse uk-child-width-1-2@s uk-margin'
        ),
        Div(
            H2(
                Span('Meet', style='color: #88A9C3'), Span(' Our Team'),
                Hr(style='height: 0px; border: none; border-top: 2px solid; color: #88A9C3', cls='uk-width-small'),
                cls='uk-text-bolder'
            ),
            cls='uk-card uk-card-body'
        ),
        Div(
            *[Div(
                Div(
                    Div(
                        style='background-image: url('
                              'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jurica'
                              '-koletic-7YVZYZeITc8-unsplash_3_11zon.webp); filter: grayscale(90%);',
                        cls='uk-height-medium uk-flex uk-flex-start uk-flex-middle uk-background-cover uk-background-center-center'
                    ),
                    Div(
                        Div(name, cls='uk-text-large uk-text-bolder'),
                        Div(pos, cls='uk-text-small uk-text-bolder',
                            style='padding: 8px; background-color: #88A9C3; color: #091235'),
                        cls='uk-card uk-card-small uk-card-body uk-overlay', style='position: absolute; bottom: 0px;'
                    ),
                    style='position: relative; color: white;'
                )
            ) for name, pos in [
                ('Aidan Mercer', 'Senior Investment Strategist'),
                ('Fiona Drake', 'Chief Financial Officer (CFO)'),
                ('Liam Caldwell', 'Wealth Management Advisor'),
                ('Chloe Rutherford', 'Portfolio Manager'),
                ('Ethan Carrington', 'Head of Corporate Finance'),
                ('Isabelle Thornton', 'Private Relationship Manager'),
                ('Marcus Ellison', 'Director of Risk Management'),
                ('Sophia Bennett', 'Chief Compliance Officer (CCO)')
            ]],
            data_uk_grid=True,
            cls='uk-grid-match uk-child-width-1-3@s uk-child-width-1-4@m'
        ),
        cls='uk-container'
    ),
    cls='uk-section uk-light', style='background-color: #091235'
)
