import dash
from dash import html, dcc

from interface import footer

dash.register_page(__name__)

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H3([
                            html.Span('Request', style={'color': '#88A9C3'}), ' an', html.Br(), 'Appointment'
                        ], className='uk-text-bolder'),
                        html.Hr(
                            style={'height': '0px', 'border': 'none', 'border-top': '2px solid', 'color': '#88A9C3'},
                            className='uk-width-small'),
                        html.P(['Need help with something? Want a demo? Reach out to our friendly team, and we\'ll get '
                                'back to you in no time.']),
                        html.Div([
                            html.Div([
                                html.Div(**{'data-uk-icon': 'icon: location; ratio: 1.8'}, className='uk-icon'),
                                html.Div(['Location'], className='uk-text-large uk-text-bolder'),
                                html.Div(['Unit 17, No.30 Surprise Road, Pinetown, 3610'], className='uk-text-small')
                            ]),
                            html.Div([
                                html.Div(**{'data-uk-icon': 'icon: receiver; ratio: 1.8'}, className='uk-icon'),
                                html.Div(['Phone'], className='uk-text-large uk-text-bolder'),
                                html.Div(['0860 258 2447'], className='uk-text-small')
                            ]),
                            html.Div([
                                html.Div(**{'data-uk-icon': 'icon: mail; ratio: 1.8'}, className='uk-icon'),
                                html.Div(['Email'], className='uk-text-large uk-text-bolder'),
                                html.Div(['info@', html.Br(), 'bluechipinvest.co.za'], className='uk-text-small')
                            ]),
                            html.Div([
                                html.Div(**{'data-uk-icon': 'icon: mail; ratio: 1.8'}, className='uk-icon'),
                                html.Div(['Open hours'], className='uk-text-large uk-text-bolder'),
                                html.Div(['Mon - Sat, 08:00 - 16:00'], className='uk-text-small')
                            ])
                        ], **{'data-uk-grid': 'true'}, className='uk-grid-match uk-child-width-1-2')
                    ], className='uk-card uk-card-body uk-light')
                ]),
                html.Div([
                    html.Div([
                        html.Form([
                            html.Div([
                                html.Div([
                                    html.Span(**{'data-uk-icon': 'icon: user'}, className='uk-form-icon'),
                                    dcc.Input(type='text', placeholder='Your name',
                                              className='uk-input uk-width-large'),
                                ], className='uk-inline')
                            ], className='uk-margin'),
                            html.Div([
                                html.Div([
                                    html.Span(**{'data-uk-icon': 'icon: mail'}, className='uk-form-icon'),
                                    dcc.Input(type='text', placeholder='you@company.com',
                                              className='uk-input uk-width-large'),
                                ], className='uk-inline')
                            ], className='uk-margin'),
                            html.Div([
                                dcc.Textarea(rows='5', placeholder='Leave a message', className='uk-textarea'),
                            ], className='uk-margin'),
                            html.Div(['No worries, your info stays with us. We don’t do the oversharing thing.'],
                                     className='uk-text-small uk-margin'),
                            html.Button(['Send your message'],
                                        className='uk-button uk-button-large uk-width-1-1 uk-margin-top uk-text-bolder',
                                        style={'color': '#88A9C3', 'background-color': '#091235'})
                        ])
                    ], className='uk-card uk-card-body uk-card-default')
                ])
            ], **{'data-uk-grid': 'true'}, className='uk-child-width-1-2@m')
        ], className='uk-container')
    ], className='uk-section', style={'background-color': '#091235'}),
    footer()
])
