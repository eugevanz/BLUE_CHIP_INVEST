from fasthtml.components import Div, Img, H3, P, A, H2, Br, Span

from interface import return_button

page = Div(
    Div(
        return_button,
        Div(
            H2(
                'Planning objective', Br(), Span('financial advice'),
                cls='uk-text-bolder'
            ),
            cls='uk-card uk-card-body'
        ),
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
                        A('Find Out More', hx_get='/contact-us/', hx_target='#page', hx_push_url='true',
                          hx_swap='innerHTML', cls='uk-button uk-button-default'),
                        cls='uk-card-body uk-padding-remove uk-margin-top'
                    ),
                    cls='uk-card'
                )
            ) for title, subtitle, img in [
                ('Financial Planning', 'Financial planning is a tailored strategy to help you achieve your '
                                       'financial goals, make smart decisions, and secure your future with '
                                       'confidence.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/firmbee-com'
                 '-jrh5lAq-mIs-unsplash.webp'),
                ('Investment Management', 'Investment management optimizes your investments to grow your '
                                          'wealth, with a strategy tailored to your goals and risk '
                                          'tolerance.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jakub'
                 '-zerdzicki-eGI0aGwuE-A-unsplash.webp'),
                ('Retirement Planning', 'Retirement planning ensures you can live comfortably after you stop '
                                        'working by setting savings goals and managing your income, '
                                        'giving you peace of mind for the future.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/marc-najera'
                 '-SwK6MSxTLDE-unsplash.webp'),
                ('Investment Analysis', 'Investment analysis evaluates financial assets to inform your '
                                        'investment decisions, assessing risk and returns to identify '
                                        'opportunities that align with your goals. This helps maximize growth '
                                        'while minimizing risk.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/mehdi'
                 '-mirzaie-3Hgqb3xHfbA-unsplash.webp'),
                ('Insurance', 'Insurance protects against unexpected events, preventing financial loss and '
                              'ensuring peace of mind for you and your family.',
                 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jakub'
                 '-zerdzicki-GQn9GnMkVQg-unsplash.webp')
            ]],
            data_uk_grid=True, cls='uk-child-width-1-2@s uk-child-width-1-3@m'
        ),
        cls='uk-container'
    ),
    cls='uk-section uk-light', style='background-color: #00213B'
)
