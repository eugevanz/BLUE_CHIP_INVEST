import random
from datetime import datetime

import numpy as np
from fasthtml.components import Div, Ul, Li, A, Span, Img, H3, P, Label, Button, Input, H2, Table, Thead, Tr, Th, \
    Caption, Tbody, Td, Br, Hr, Nav

from interface import calendar_view, sign_out_button
from utility_functions import get_clients, dt_object


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


def client_insights_card(clients: list, user: dict):
    balance = lambda accounts: np.sum([
        account['balance'] for account in accounts
    ], dtype=np.float16) if accounts else 0.0

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
                                Img(
                                    cls='uk-border-circle', width='48', height='48',
                                    src=client['profile_picture_url'],
                                    alt='profile-pic'
                                ) if client['profile_picture_url'] else Span(data_uk_icon='icon: user; ratio: 4;'),
                                cls='uk-width-auto'
                            ),
                            Div(
                                H3(
                                    Span(
                                        client['first_name'] if client['first_name'] else 'First name',
                                        cls='uk-text-bolder'
                                    ),
                                    Span(' '),
                                    client['last_name'] if client['last_name'] else 'Last name',
                                    cls='uk-card-title uk-margin-remove-bottom', style='color:white;'
                                ),
                                Div(client['email'], style='font-size: 11px;'),
                                P('Last active',
                                  Span(dt_object(client['created_at']),
                                       cls='uk-text-default uk-text-bolder uk-margin-small-left'),
                                  cls='uk-text-meta uk-margin-remove-top'),
                                cls='uk-width-expand'
                            ),
                            cls='uk-grid-small uk-flex-middle', data_uk_grid=True
                        ),
                        Div(
                            Div(f'R {balance(client["accounts"])}', cls='uk-text-lead uk-text-bolder')
                        ),
                        cls='uk-flex uk-flex-between', hx_get=f'/edit-client/{client["id"]}/', hx_target='#page',
                        hx_push_url='/admin/'
                    ),
                ) for client in clients] if clients else Div(),
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


def page(user: dict):
    clients = get_clients()

    return Div(
        Div(
            Div(menu_card()), Div(overview_card()), Div(portfolio_value_card()),
            Div(assets_card()), Div(performance_summary_card(), cls='uk-width-1-2@m'),
            Div(client_insights_card(clients=clients, user=user), cls='uk-width-1-2@m'),
            data_uk_grid=True, cls='uk-padding uk-child-width-1-4@m uk-grid-small uk-grid-match uk-flex-right'
        ),
        style='background-color: #091235'
    )
