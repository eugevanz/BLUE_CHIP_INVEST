import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Div(
                    **{'data-src': 'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                   '/youssef-naddam-iJ2IG8ckCpA-unsplash_15_11zon.webp'}, **{'data-uk-img': 'true'},
                    className='uk-height-large uk-flex uk-flex-center uk-flex-middle uk-background-cover')
            ], className='uk-flex-last@s uk-card-media-right uk-cover-container'),
            html.Div([
                html.Div([
                    html.H2([
                        html.Span(['We Help'], style={'color': '#88A9C3'}), ' financial', html.Br(),
                        html.Span(['Advisors that']),
                        html.Br(), html.Span(['exclusively serve.'])
                    ], className='uk-text-bolder'),
                    html.P(['Dedicated to the needs of financial advisors who serve clients exclusively, '
                            'we offer customized solutions and resources that enhance their practices. Our mission is '
                            'to equip advisors with the tools and support they need to foster meaningful client '
                            'relationships, allowing them to focus on delivering top-notch financial guidance and '
                            'personalized service.']),
                    html.A([
                        'Talk to us'
                    ], className='uk-button uk-button-large uk-text-bolder', href='/contact-us/',
                        style={'background-color': '#88A9C3', 'color': '#091235'})
                ], className='uk-card-body')
            ])
        ], **{'data-uk-grid': 'true'}, className='uk-card uk-grid-collapse uk-child-width-1-2@s uk-margin'),
        html.Div([
            html.H2([
                html.Span(['Meet'], style={'color': '#88A9C3'}), html.Span([' Our Team']),
                html.Hr(style={'height': '0px', 'border': 'none', 'border-top': '2px solid', 'color': '#88A9C3'},
                        className='uk-width-small')
            ],className='uk-text-bolder')
        ],className='uk-card uk-card-body'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div(style={'background-image': 'url(https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jurica-koletic-7YVZYZeITc8-unsplash_3_11zon.webp)',
                            'filter': 'grayscale(90%)'},className='uk-height-medium uk-flex uk-flex-start uk-flex-middle uk-background-cover uk-background-center-center'),
                    html.Div([
                        html.Div([name], className='uk-text-large uk-text-bolder'),
                        html.Div([pos], className='uk-text-small uk-text-bolder',
                                 style={'padding': '8px', 'background-color': '#88A9C3', 'color': '#091235'})
                    ],className='uk-card uk-card-small uk-card-body uk-overlay', style={'position': 'absolute', 'bottom': '0px'})
                ],style={'position': 'relative', 'color': 'white'})
            ]) for name, pos in [
                ('Aidan Mercer', 'Senior Investment Strategist'),
                ('Fiona Drake', 'Chief Financial Officer (CFO)'),
                ('Liam Caldwell', 'Wealth Management Advisor'),
                ('Chloe Rutherford', 'Portfolio Manager'),
                ('Ethan Carrington', 'Head of Corporate Finance'),
                ('Isabelle Thornton', 'Private Relationship Manager'),
                ('Marcus Ellison', 'Director of Risk Management'),
                ('Sophia Bennett', 'Chief Compliance Officer (CCO)')
            ]
        ],**{'data-uk-grid': 'true'},className='uk-grid-match uk-child-width-1-3@s uk-child-width-1-4@m')
    ], className='uk-container')
], className='uk-section uk-light', style={'background-color': '#091235'})
