import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.Div([
        html.Div([
            html.H2([
                'Planning objective', html.Br(), html.Span(['financial advice (Services)'], className='uk-light')
            ], className='uk-text-bolder', style={'color': 'white'})
        ], className='uk-card uk-card-body'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div(
                        style={'background-image': f'url({img})', 'filter': 'grayscale(90%)', 'opacity': '0.6'},
                        className='uk-height-medium uk-flex uk-flex-start uk-flex-middle uk-background-cover '
                                  'uk-background-center-center'
                    ),
                    html.Div([
                        html.H3([title], className='uk-text-bolder uk-width-1-2', style={'color': 'white'}),
                        html.A(['Find Out More'], className='uk-button uk-text-bolder', href='/contact-us/',
                               style={'background-color': '#88A9C3'})
                    ], className='uk-padding', style={'position': 'absolute', 'bottom': '0px'})
                ], style={'position': 'relative'}),
                html.Div([
                    html.Div([
                        html.P([subtitle], style={'color': 'white'})
                    ], className='uk-card uk-card-body')
                ])
            ]) for title, subtitle, img in [
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
            ]
        ], **{'data-uk-grid': 'true'}, className='uk-child-width-1-2@s uk-child-width-1-3@m')
    ], className='uk-container')
], className='uk-section', style={'background-color': '#091235'})
