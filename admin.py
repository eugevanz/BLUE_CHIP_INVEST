import random
from datetime import datetime

from fasthtml.components import Div, Ul, Li, A, Span, Img, H3, P, Label, Button, Input, H2, Table, Thead, Tr, Th, \
    Caption, Tbody, Td, Br, Hr, Nav, H1, Form, Select, Option

from interface import calendar_view, sign_out_button, add_save_button
from utility_functions import get_clients, get_profile_picture_url, get_profile_first_name, get_profile_last_name, \
    get_account_updated_at, \
    get_account_balance, get_portfolio_performance_return_on_investment, get_profile_client_id, \
    get_profile_client_email, get_account_account_type, get_profile_created_at


def menu_card():
    return Div(
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
                            Input(cls='uk-input uk-form-blank', type='email',
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
            Li(A('Client Management')),
            Li(A('Audit Logs')),
            Li(A('Investment Reporting')),
            Li(A('Admin Support Hub')),
            sign_out_button(),
            cls='uk-nav uk-nav-default'
        ),
        cls='uk-card uk-card-body uk-card-default', style='background-color: #2A3A58'
    )


def overview_card():
    return Div(
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
        Div(
            calendar_view(),
            Nav(
                Ul(
                    Li(
                        A(
                            Span(data_uk_pagination_previous=True, cls='uk-margin-small-right'),
                            'Previous',
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            'Next',
                            Span(data_uk_pagination_next=True, cls='uk-margin-small-left'),
                            href='#'
                        ),
                        cls='uk-margin-auto-left'
                    ),
                    cls='uk-pagination', data_uk_margin=True
                ),
                cls='uk-margin-medium-top'
            ),
            A(
                Div(
                    Span(data_uk_icon='icon: mail', cls='uk-margin-small-right', style='color: #89CFF0;'),
                    cls='uk-width-auto'
                ),
                Div(
                    Div('Top 5 Portfolio Holdings: Tech Giants Lead with Apple, Tesla, and Amazon Driving Strong '
                        'Returns'[:80] + '...', style='color: #89CFF0;', cls='uk-text-bolder')
                ),
                data_uk_grid=True, cls='uk-child-width-expand uk-grid-small uk-margin-medium-top uk-text-muted'
            ),
            cls='uk-card-footer'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
    )


def portfolio_value_card():
    return Div(
        Div(
            Div(
                Div('Portfolio Value', cls='uk-text-default uk-text-bolder'),
                A('US Dollar', Span(data_uk_drop_parent_icon=True), cls='uk-link-muted uk-text-small'),
                Div(
                    Ul(
                        Li(A('US Dollar', cls='uk-link-muted uk-text-small')),
                        Li(A('ZA Rand', cls='uk-link-muted uk-text-small')),
                        Li(A('EURO', cls='uk-link-muted uk-text-small')),
                        Li(A('British Pound', cls='uk-link-muted uk-text-small')),
                        cls='uk-list uk-list-divider'
                    ),
                    cls='uk-card uk-card-body', style='background-color: #2A3A58;', data_uk_dropdown=True
                ),
                cls='uk-flex uk-flex-between'
            ),
            cls='uk-card-header'
        ),
        Div(
            Div('Balance', cls='uk-text-small'),
            H2('R8,167,514.57', cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
            Div('Compared to last month ', Span('+24.17%', cls='uk-text-success'),
                cls='uk-text-small uk-margin-remove-top'),
            cls='uk-card-body'
        ),
        Div(
            Ul(
                *[Li(title, Span(amount, cls='uk-text-bolder uk-margin-small-left'))
                  for title, amount in [('Income', '$31,885'), ('Expenses', '$8,994')]],
                cls='charts-css legend legend-inline legend-square uk-margin-bottom', style='border: 0'
            ),
            Div(
                Div(
                    Div(Div('142M'), Div('71M', cls='uk-margin-auto-vertical'), Div('0M'),
                        cls='uk-flex uk-flex-column uk-flex-between uk-text-bolder', style='font-size: 8px;'),
                    cls='uk-width-auto'
                ),
                Div(
                    Table(
                        Caption('2024 Revenue Table'),
                        Thead(
                            Tr(
                                *[Th(title, scope='col') for title in ['Month', 'Income', 'Expenses']]
                            )
                        ),
                        Tbody(
                            *[Tr(
                                Th(x['month'], scope='row'),
                                *[Td(style=f'--size: 0.{amount * 2}') for amount in x['data']]
                            ) for x in [
                                dict(month='Jul', data=[random.randint(1, 142), random.randint(1, 142)]),
                                dict(month='Aug', data=[random.randint(1, 142), random.randint(1, 142)]),
                                dict(month='Sep', data=[random.randint(1, 142), random.randint(1, 142)]),
                                dict(month='Oct', data=[random.randint(1, 142), random.randint(1, 142)])
                            ]]
                        ),
                        cls='charts-css column multiple show-data-on-hover show-3-secondary-axes data-spacing-10'
                    )
                ),
                data_uk_grid=True, cls='uk-grid-divider uk-child-width-expand uk-grid-match uk-grid-small'
            ),
            Div(Div('Jul'), Div('Aug'), Div('Sep'), Div('Oct'),
                cls='uk-flex uk-flex-around uk-text-bolder uk-text-small uk-margin-small', style='padding-left: 54px;'),
            cls='uk-card-footer'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
    )


def assets_card():
    return Div(
        Div(
            Div(
                Div('Asset Allocation', cls='uk-text-default uk-text-bolder'),
                Div(
                    Span(data_uk_icon='icon: table;'),
                    Span('Filter', cls='uk-margin-small-left'),
                    cls='uk-text-small uk-flex uk-flex-middle'
                ),
                cls='uk-flex uk-flex-between'
            ),
            cls='uk-card-header'
        ),
        Div(
            Div('Quarterly Growth Rate', cls='uk-text-small'),
            H2('+24.17%', cls='uk-text-bolder uk-margin-remove-top uk-text-success'),
            Div(Div('0M'), Div('71M'), Div('142M'),
                cls='uk-flex uk-flex-between uk-text-bolder', style='font-size: 8px;'),
            Hr(),
            Table(
                Caption('Asset Allocation'),
                Thead(
                    Tr(
                        *[Th(title, scope='col') for title in ['Asset', 'Value']]
                    ),
                ),
                Tbody(
                    Tr(
                        *[Td(
                            style=f'--size: {value};'
                        ) for value in [0.7, 0.5, 0.4, 0.3, 0.2]]
                    )
                ),
                cls='charts-css bar multiple stacked'
            ),
            Ul(
                *[Li(Div(title, Br(), Span(value, cls=' uk-text-bolder'), cls='uk-text-small'))
                  for title, value in [
                      ('Stocks (Equities)', '4,083,757.29 USD'),
                      ('Bonds (Fixed Income Securities)', '1,633,502.91 USD'),
                      ('Real Estate', '1,225,127.19 USD'),
                      ('Commodities', '816,751.46 USD'),
                      ('Cash and Cash Equivalents', '408,375.73 USD')
                  ]],
                cls='charts-css legend legend-square uk-margin', style='border: 0'
            ),
            cls='uk-card-body'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
    )


def performance_summary_card():
    return Div(
        Div(
            Div(
                Div('Performance Summary', cls='uk-text-default uk-text-bolder'),
                Div(
                    Span(data_uk_icon='icon: table;'),
                    Span('Filter', cls='uk-margin-small-left'),
                    cls='uk-text-small uk-flex uk-flex-middle'
                ),
                cls='uk-flex uk-flex-between'
            ),
            cls='uk-card-header'
        ),
        Div(
            Div(
                Div(
                    Div('Top Performer: Stocks (Equities)', cls='uk-text-small'),
                    H2('R8,167,514.57',
                       cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                    Div('Compared to last month ', Span('+24.17%', cls='uk-text-success'),
                        cls='uk-text-small uk-margin-remove-top')
                ),
                Button('View All', style='background-color: #88A9C3; color: #091235', cls='uk-button uk-button-small'),
                cls='uk-flex uk-flex-between uk-flex-middle'
            ),
            Ul(
                *[Li(title) for title in [
                    'Stocks (Equities)', 'Bonds (Fixed Income Securities)', 'Real Estate', 'Commodities',
                    'Cash and Cash Equivalents'
                ]],
                cls='charts-css legend legend-inline legend-square uk-margin', style='border: 0'
            ),
            Div(
                Div(
                    Div(Div('142M'), Div('71M', cls='uk-margin-auto-vertical'), Div('0M'),
                        cls='uk-flex uk-flex-column uk-flex-between uk-text-bolder', style='font-size: 8px;'),
                    cls='uk-width-auto'
                ),
                Div(
                    Table(
                        Caption('Performance Summary'),
                        Thead(
                            Tr(
                                *[Th(title, scope='col') for title in ['Asset', 'Value']]
                            ),
                        ),
                        Tbody(
                            *[Tr(
                                Th(asset, scope='row'),
                                *[Td(
                                    style=f'--start: {prev}; --end: {curr};'
                                ) for prev, curr in values]
                            ) for asset, values in [
                                ('Aug', [(0.5, 0.8), (0.2, 0.5), (0.4, 0.1), (0.3, 0.5), (0.7, 0.8)]),
                                ('Sep', [(0.8, 0.4), (0.5, 0.3), (0.1, 0.7), (0.5, 0.2), (0.8, 0.6)]),
                                ('Oct', [(0.4, 0.8), (0.3, 0.5), (0.7, 0.5), (0.2, 0.6), (0.6, 0.3)])
                            ]]
                        ),
                        cls='charts-css area multiple show-3-secondary-axes data-spacing-10'
                    )
                ),
                data_uk_grid=True, cls='uk-grid-divider uk-child-width-expand uk-grid-match uk-grid-small'
            ),
            Div(Div('Jul'), Div('Aug'), Div('Sep'), Div('Oct'),
                cls='uk-flex uk-flex-between uk-text-bolder uk-text-small uk-margin', style='padding-left: 54px;'),
            cls='uk-card-body'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
    )


def client_modal(client):
    account_type = get_account_account_type(client)
    account_options = [
        'Savings Account', 'Investment Account', 'Retirement Account',
        'Brokerage Account', 'Trust Account', 'Custodial Account',
        'Taxable Account', 'Tax-Deferred Account', 'Tax-Exempt Account',
        'Money Market Account', 'Certificate of Deposit (CD) Account',
        'Mutual Fund Account', 'Pension Account',
        'Self-Directed Investment Account', 'High-Yield Savings Account',
        'Fixed-Income Account', 'Annuity Account', 'Forex Trading Account',
        'Commodities Trading Account'
    ]
    if account_type not in account_options: account_options.insert(0, account_type)

    def slider_item_account():
        return Div(
            Div(
                Div(
                    Div(
                        A(href='', data_uk_icon='icon: pencil; ratio: 1.5;', cls='uk-invisible-hover'),
                        data_src=get_profile_picture_url(client),
                        data_uk_img=True, style='width: 200px; height: 200px;',
                        cls='uk-flex uk-flex-center uk-flex-middle uk-background-cover uk-light '
                            'uk-border-circle uk-visible-toggle'
                    ),
                    cls='uk-width-auto'
                ),
                Div(
                    Div(get_profile_client_email(client), cls='uk-text-small', style='margin-left: 14px;'),
                    H1(
                        Input(type='text', placeholder=get_profile_first_name(client),
                              aria_label=get_profile_first_name(client),
                              cls='uk-input uk-form-blank uk-text-bolder', style='height: 54px;'),
                        Input(type='text', placeholder=get_profile_last_name(client),
                              aria_label=get_profile_last_name(client),
                              cls='uk-input uk-form-blank', style='height: 54px;'),
                        cls='uk-margin-remove-top uk-margin-remove-bottom'
                    ),
                    Div(f'Member since {get_profile_created_at(client)}', cls='uk-text-small', style='margin-left: '
                                                                                                     '14px;')
                ),
                data_uk_grid=True,
                cls='uk-grid-divider uk-child-width-expand@m'
            ),
            # Div(
            #     Label('Home Address', cls='uk-form-label'),
            #     Textarea(placeholder=get_address(client), aria_label=get_address(client),
            #              cls='uk-textarea uk-form-blank',
            #              _='on input set my height to "auto" then set my height to my scrollHeight + "px"'),
            #     cls='uk-margin'
            # ),
            Div(
                Div(
                    Div('Account Balance', cls='uk-text-small'),
                    H2(f'R {get_account_balance(client)}',
                       cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                    Div('Compared to last month ',
                        Span(f'{get_portfolio_performance_return_on_investment(client)}%', cls='uk-text-success'),
                        cls='uk-text-small uk-margin-remove-top'),
                    cls='uk-margin'
                ),
                Div(
                    Div(
                        Div(
                            Div('Account Type', cls='uk-text-small'),
                            H3(
                                Select(
                                    *[Option(title) for title in account_options],
                                    aria_label='Custom controls',
                                    cls='uk-select uk-text-center'
                                ),
                                Span(
                                    Span(),
                                    Span(data_uk_icon='icon: pencil')
                                ),
                                cls='uk-text-bolder uk-margin-remove-top',
                                data_uk_form_custom='target: > * > span:first-child'
                            ),
                            cls='uk-card uk-card-body', style='background-color: #88A9C3;'
                        )
                    ),
                    Div(
                        Div(
                            Div('Last Updated', cls='uk-text-small'),
                            H3(get_account_updated_at(client),
                               cls='uk-text-bolder uk-margin-remove-top uk-text-truncate'),
                            cls='uk-card uk-card-body', style='background-color: #88A9C3;'
                        )
                    ),
                    data_uk_grid=True,
                    cls='uk-child-width-1-2@m uk-grid-match uk-margin'
                ),
                cls='uk-card uk-card-body uk-card-default uk-margin'
            ),
            add_save_button()
        )

    def slider_item_investments():
        return Div(
            Div(
                Div(
                    Div('Investment Amount', cls='uk-text-small'),
                    H2(f'R {get_account_balance(client)}',
                       cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                    Div('Compared to last month ',
                        Span(f'{get_portfolio_performance_return_on_investment(client)}%', cls='uk-text-success'),
                        cls='uk-text-small uk-margin-remove-top'),
                    cls='uk-margin'
                ),
                *[Div(
                    Div(
                        Div(
                            Div('Investment Type', cls='uk-text-small'),
                            H3(
                                Select(
                                    *[Option(title) for title in account_options],
                                    aria_label='Custom controls',
                                    cls='uk-select uk-text-center'
                                ),
                                Span(
                                    Span(),
                                    Span(data_uk_icon='icon: pencil')
                                ),
                                cls='uk-text-bolder uk-margin-remove-top',
                                data_uk_form_custom='target: > * > span:first-child'
                            ),
                            cls='uk-card uk-card-body', style='background-color: #88A9C3;'
                        )
                    ),
                    Div(
                        Div(
                            Div('Last Updated', cls='uk-text-small'),
                            H3(get_account_updated_at(client),
                               cls='uk-text-bolder uk-margin-remove-top uk-text-truncate'),
                            cls='uk-card uk-card-body', style='background-color: #88A9C3;'
                        )
                    ),
                    data_uk_grid=True, cls='uk-child-width-1-2@m uk-grid-divider uk-grid-match uk-margin',
                    style='background-color: #88A9C3;'
                ) for _ in range(3)],
                cls='uk-card uk-card-body uk-card-default uk-margin'
            ),
            add_save_button()
        )

    return Form(
        Div(
            Button(type='button', data_uk_close=True, cls='uk-modal-close-full uk-close-large'),
            Div(
                Div(style='background-image: url('
                          'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/marten'
                          '-bjork-6dW3xyQvcYE-unsplash_6_11zon.webp);',
                    data_uk_height_viewport=True,
                    cls='uk-background-cover uk-visible@m'),
                Div(
                    Ul(
                        *[Li(A(title, href='#')) for title in [
                            'Account', 'Investments', 'Transactions', 'Portfolio Performance', 'Client Goals',
                            'Dividends/Payouts', 'Advisors', 'Investment Products'
                        ]],
                        data_uk_tab='animation: uk-animation-slide-left-medium, uk-animation-slide-right-medium',
                        cls='uk-margin-large-bottom'
                    ),

                    Div(
                        slider_item_account(),
                        slider_item_investments(),
                        slider_item_account(),
                        slider_item_account(),
                        slider_item_account(),
                        slider_item_account(),
                        slider_item_account(),
                        slider_item_account(),
                        cls='uk-switcher uk-margin'
                    ),
                    cls='uk-padding-large'
                ),
                data_uk_grid=True,
                cls='uk-grid-collapse uk-child-width-1-2@m'
            ),
            cls='uk-modal-dialog'
        ),
        id=f'modal-{get_profile_client_id(client)}', data_uk_modal=True, cls='uk-modal-full'
    )


def client_insights_card():
    return Div(
        Div(
            Div(
                Div('Client Insights', cls='uk-text-default uk-text-bolder'),
                Div(
                    Span(data_uk_icon='icon: table;'),
                    Span('Filter', cls='uk-margin-small-left'),
                    cls='uk-text-small uk-flex uk-flex-middle'
                ),
                cls='uk-flex uk-flex-between'
            ),
            cls='uk-card-header'
        ),
        Div(
            Ul(
                *[Li(
                    A(
                        Div(
                            Div(
                                Img(cls='uk-border-circle', width='48', height='48',
                                    src=get_profile_picture_url(client),
                                    alt='profile-pic'),
                                cls='uk-width-auto'
                            ),
                            Div(
                                H3(Span(get_profile_first_name(client), cls='uk-text-bolder'), Span(' '),
                                   get_profile_last_name(client), cls='uk-card-title uk-margin-remove-bottom',
                                   style='color:white;'),
                                Div(get_profile_client_email(client), style='font-size: 11px;'),
                                P('Last active',
                                  Span(get_account_updated_at(client),
                                       cls='uk-text-default uk-text-bolder uk-margin-small-left'),
                                  cls='uk-text-meta uk-margin-remove-top'),
                                cls='uk-width-expand'
                            ),
                            cls='uk-grid-small uk-flex-middle', data_uk_grid=True
                        ),
                        Div(
                            Div(get_account_balance(client), cls='uk-text-lead uk-text-bolder'),
                            Span(get_portfolio_performance_return_on_investment(client),
                                 cls='uk-text-bolder uk-text-small uk-border-pill',
                                 style=f'background-color: #5F9EA0; padding: 3px;')
                        ),
                        href=f'#modal-{get_profile_client_id(client)}', data_uk_toggle=True,
                        cls='uk-flex uk-flex-between uk-link-toggle'
                    ),
                    client_modal(client)
                ) for client in get_clients()],
                cls='uk-list uk-list-divider'
            ),
            cls='uk-card-body'
        ),
        Div(
            Nav(
                Ul(
                    Li(
                        A(
                            Span(data_uk_pagination_previous=True, cls='uk-margin-small-right'),
                            'Previous',
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            'Next',
                            Span(data_uk_pagination_next=True, cls='uk-margin-small-left'),
                            href='#'
                        ),
                        cls='uk-margin-auto-left'
                    ),
                    cls='uk-pagination', data_uk_margin=True
                )
            ),
            cls='uk-card-footer'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
    )


page = Div(
    Div(
        Div(menu_card()), Div(overview_card()), Div(portfolio_value_card()),
        Div(assets_card()), Div(performance_summary_card(), cls='uk-width-1-2@m'),
        Div(client_insights_card(), cls='uk-width-1-2@m'),
        data_uk_grid=True, cls='uk-padding uk-child-width-1-4@m uk-grid-small uk-grid-match uk-flex-right'
    ),
    style='background-color: #091235'
)
