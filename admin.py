from datetime import datetime

from fasthtml.components import Div, Ul, Li, A, Span, Img, H3, P, Label, Button, Input, H2

from interface import create_graph, calendar_view

menu_card = Div(
    Div(
        Div(
            Ul(
                Li('Menu', cls='uk-nav-header', style='color: white;'),
                Li(A(Span(data_uk_icon='icon: home', cls='uk-margin-small-right'), 'Dashboard',
                     cls='uk-flex uk-flex-middle')),
                Li(A(Span(data_uk_icon='icon: credit-card', cls='uk-margin-small-right'), 'Transactions',
                     cls='uk-flex uk-flex-middle')),
                Li(A(Span(data_uk_icon='icon: star', cls='uk-margin-small-right'), 'My Goals',
                     cls='uk-flex uk-flex-middle')),
                Li(A(Span(data_uk_icon='icon: nut', cls='uk-margin-small-right'), 'Investment',
                     cls='uk-flex uk-flex-middle')),
                Li(A(Span(data_uk_icon='icon: file-text', cls='uk-margin-small-right'), 'Bills and Payment',
                     cls='uk-flex uk-flex-middle')),
                Li(A(Span(data_uk_icon='icon: settings', cls='uk-margin-small-right'), 'Analytics and Reports',
                     cls='uk-flex uk-flex-middle')),
                Li(cls='uk-nav-divider uk-margin'),
                Li(
                    Div(
                        Img(cls='uk-border-circle', width='44', height='44',
                            src='https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                '/jurica-koletic-7YVZYZeITc8-unsplash_3_11zon.webp', alt='profile-pic'),
                        cls='uk-width-auto'
                    ),
                    Div(
                        H3('Title', cls='uk-card-title uk-margin-remove-bottom', style='color: white;'),
                        P('April 01, 2016', cls='uk-text-meta uk-margin-remove-top'),
                        cls='uk-width-expand'
                    ),
                    cls='uk-grid-small uk-flex-middle uk-margin-left uk-margin-top', data_uk_grid=True
                ),
                Li(cls='uk-nav-divider uk-margin'),
                Li('Support', cls='uk-nav-header', style='color: white;'),
                Li(
                    A(Span(data_uk_icon='icon: mail', cls='uk-margin-small-right'), 'Send an invite',
                      cls='uk-flex uk-flex-middle'),
                    Div(
                        H3('Send an invite', cls='uk-card-title uk-margin-remove-bottom'),
                        P('Please enter the recipient\'s email address so we know who you’re sending to.',
                          cls='uk-text-small uk-margin-remove-top'),
                        Div(
                            Label('Email', cls='uk-form-label'),
                            Div(
                                Span(cls='uk-form-icon', data_uk_icon='icon: mail'),
                                Input(cls='uk-input', type='email',
                                      aria_label='form-invite-name', name='form-invite-name'),
                                cls='uk-inline'
                            ),
                            cls='uk-margin', style='color: #88A9C3;'
                        ),
                        Div(
                            Button("Send Invite",
                                   cls='uk-button uk-button-large uk-width-1-1 uk-light',
                                   style='background-color: #091235', hx_post='/send-invite/',
                                   hx_target='#invite-notifications',
                                   hx_include="[name='form-invite-name']"),
                            cls='uk-margin'
                        ),
                        P(id='invite-notifications', cls='uk-margin'),
                        cls='uk-card uk-card-body uk-card-default', data_uk_drop=True
                    ),
                    cls='uk-inline'
                ),
                cls='uk-nav uk-nav-default'
            ),
            cls='uk-card uk-card-body uk-card-default', style='background-color: #2A3A58'
        )
    ),
    Div(
        Div(
            Div(
                Div(
                    Div('Overview', cls='uk-text-default uk-text-bolder'),
                    Div(datetime.now().strftime('%B %Y'), cls='uk-text-small'),
                    cls='uk-flex uk-flex-between'
                ),
                cls='uk-card-header'
            ),
            Div(
                Div(
                    Div(
                        Div('40', cls='uk-text-large uk-text-bolder'),
                        Div('Transactions', cls='uk-text-truncate', style='font-size: 11px;')
                    ),
                    Div(Div('24', cls='uk-text-large uk-text-bolder'), Div('Income', style='font-size: 11px;')),
                    Div(Div('16', cls='uk-text-large uk-text-bolder'), Div('Outcome', style='font-size: 11px;')),
                    data_uk_grid=True, cls='uk-child-width-expand uk-text-center'
                ),
                cls='uk-card-body'
            ),
            Div(calendar_view(), cls='uk-card-footer'),
            cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
        ),
        style='width: 392px;'
    ),
    Div(
        Div(
            Div(
                Div(
                    Div('Your Balance', cls='uk-text-default uk-text-bolder'),
                    A('US Dollar', cls='uk-link-muted uk-text-small'),
                    Ul(
                        Li(A('US Dollar', cls='uk-link-muted uk-text-small')),
                        Li(A('ZA Rand', cls='uk-link-muted uk-text-small')),
                        Li(A('EURO', cls='uk-link-muted uk-text-small')),
                        Li(A('British Pound', cls='uk-link-muted uk-text-small')),
                        cls='uk-list uk-list-divider', data_uk_dropdown=True
                    ),
                    cls='uk-flex uk-flex-between'
                ),
                cls='uk-card-header'
            ),
            Div(
                Div('Balance', cls='uk-text-small'),
                H2('$20,088.38', cls='uk-text-bolder uk-margin-remove-top uk-text-truncate'),
                Div('Compared to last month ', Span('+24.17%', cls='uk-text-success'), cls='uk-text-small'),
                cls='uk-card-body'
            ),
            Div(
                cls='uk-card-footer uk-background-contain',
                style=f'height:256px; background-image: url({create_graph()});'
            ),
            cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
        )
    ),
    Div(
        Div('Item', cls='uk-card uk-card-default uk-card-body'),
    ),
    Div(
        Div('Item', cls='uk-card uk-card-default uk-card-body'),
        cls='uk-width-1-2@m'
    ),
    Div(
        Div('Item', cls='uk-card uk-card-default uk-card-body')
    ),
    data_uk_grid=True,
    cls='uk-child-width-1-4@m uk-grid-small uk-flex-right'
)

page = Div(
    Div(
        menu_card,
        cls='uk-padding'
    ),
    cls='uk-section', style='background-color: #091235'
)
