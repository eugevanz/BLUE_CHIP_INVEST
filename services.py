from fasthtml.components import Div, H2, Br, Span, H3, Button, P

page = Div(
    Div(
        Div(
            H2(
                'Planning objective', Br(), Span('financial advice', cls='uk-light'),
                cls='uk-text-bolder', style='color: white;'
            ),
            cls='uk-card uk-card-body'
        ),
        Div(
            *[Div(
                Div(
                    Div(
                        style=f'background-image: url({img}); filter: grayscale(90%); opacity: 0.6;',
                        cls='uk-height-medium uk-flex uk-flex-start uk-flex-middle uk-background-cover uk-background-center-center'
                    ),
                    Div(
                        H3(title, cls='uk-text-bolder uk-width-1-2', style='color: white;'),
                        Button('Find Out More', cls='uk-button uk-text-bolder', hx_get='/contact-us/',
                               hx_target='#page',
                               hx_push_url='/services/',
                               style='background-color: #88A9C3'),
                        cls='uk-padding',
                        style='position: absolute; bottom: 0px;'
                    ),
                    style='position: relative;'
                ),
                Div(
                    Div(
                        P(subtitle, style='color: white;'),
                        cls='uk-card uk-card-body'
                    )
                )
            ) for title, subtitle, img in [
                ('Financial Planning', 'Financial planning is a tailored strategy to help you achieve your '
                                       'financial goals, make smart decisions, and secure your future with '
                                       'confidence.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/firmbee-com-jrh5lAq'
                 '-mIs-unsplash_27_11zon.webp'),
                ('Investment Management', 'Investment management optimizes your investments to grow your '
                                          'wealth, with a strategy tailored to your goals and risk '
                                          'tolerance.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jakub-zerdzicki'
                 '-eGI0aGwuE-A-unsplash_29_11zon.webp'),
                ('Retirement Planning', 'Retirement planning ensures you can live comfortably after you stop '
                                        'working by setting savings goals and managing your income, '
                                        'giving you peace of mind for the future.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/marc-najera'
                 '-SwK6MSxTLDE-unsplash_5_11zon.webp'),
                ('Investment Analysis', 'Investment analysis evaluates financial assets to inform your '
                                        'investment decisions, assessing risk and returns to identify '
                                        'opportunities that align with your goals. This helps maximize growth '
                                        'while minimizing risk.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/mehdi-mirzaie'
                 '-3Hgqb3xHfbA-unsplash_7_11zon.webp'),
                ('Insurance', 'Insurance protects against unexpected events, preventing financial loss and '
                              'ensuring peace of mind for you and your family.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jakub-zerdzicki'
                 '-GQn9GnMkVQg-unsplash_30_11zon.webp')
            ]],
            data_uk_grid=True, cls='uk-child-width-1-2@s uk-child-width-1-3@m'
        ),
        cls='uk-container'
    ),
    cls='uk-section', style='background-color: #091235'
)
