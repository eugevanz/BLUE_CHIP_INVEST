import random
from datetime import datetime

from fasthtml.components import Div, Nav, Ul, Li, A, Span, P, H3, Img, Tr, Td, Tbody, Th, Thead, \
    Table, H2, Caption, Button

from interface import calendar_view, sign_out_button


def menu_card():
    return Div(
        Ul(
            Li('Menu', cls='uk-nav-header', style='color: white;'),
            Li(A(Span(data_uk_icon='icon: home', cls='uk-margin-small-right'), 'Dashboard',
                 cls='uk-flex uk-flex-middle')),
            Li(
                A(
                    Span(data_uk_icon='icon: credit-card', cls='uk-margin-small-right'), 'Transactions',
                    cls='uk-flex uk-flex-middle',
                    _='on click js const element = document.getElementById("transactions"); if (element) { '
                      'window.scrollTo({top: element.offsetTop - 96, behavior: "smooth"}); }'
                )
            ),
            Li(
                A(Span(data_uk_icon='icon: mail', cls='uk-margin-small-right'), 'Messages',
                  cls='uk-flex uk-flex-middle'),
                Div(
                    Ul(
                        Li('List item 1'),
                        Li('List item 2'),
                        Li('List item 3'),
                        cls='uk-list uk-list-divider'
                    ),
                    data_uk_drop='mode: click', cls='uk-card uk-card-body uk-card-default'),
                cls='uk-inline'
            ),
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
            Li(A('Contact Support')),
            Li(A('FAQs')),
            Li(A('Account Help')),
            Li(A('Investment FAQs')),
            Li(A('Service Status')),
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
                            'September',
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            'November',
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
            Div(
                Div(
                    Div(Div('142M'), Div('71M', cls='uk-margin-auto-vertical'), Div('0M'),
                        cls='uk-flex uk-flex-column uk-flex-between uk-text-bolder', style='font-size: 8px;'),
                    cls='uk-width-auto'
                ),
                Div(
                    Table(
                        Caption('Portfolio Value'),
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
                        cls='charts-css column multiple show-data-on-hover show-3-secondary-axes data-spacing-10 '
                            'show-labels',
                        style='--aspect-ratio: 4 / 2;'
                    )
                ),
                data_uk_grid=True,
                cls='uk-grid-divider uk-child-width-expand uk-grid-match uk-grid-small uk-margin-medium-top'
            ),
            # Div(Div('Jul'), Div('Aug'), Div('Sep'), Div('Oct'),
            #     cls='uk-flex uk-flex-around uk-text-bolder uk-text-small uk-margin-small uk-width-large',
            #     style='padding-left: 54px; padding-right: 128px;'),
            cls='uk-card-body'
        ),
        Div(
            Ul(
                *[Li(title, Span(amount, cls='uk-text-bolder uk-margin-small-left'))
                  for title, amount in [('Income', '$31,885'), ('Expenses', '$8,994')]],
                cls='charts-css legend legend-inline legend-square', style='border: 0'
            ),
            cls='uk-card-footer'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
    )


def transactions():
    return Div(
        Div(
            Div(
                Div('Recent Transactions', cls='uk-text-default uk-text-bolder'),
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
            Table(
                Thead(
                    Tr(
                        Th('Type'),
                        Th('Amount'),
                        Th('Method')
                    )
                ),
                Tbody(
                    *[Tr(
                        Td(
                            Span(
                                uk_icon=f'icon:  {"plus-circle" if tx_type[0] == "Received" else "minus-circle"}; ratio: 1.5',
                                cls=f'uk-text-{"success" if tx_type[0] == "Received" else "danger"}'),
                            Div(
                                Div(title, cls='uk-text-bolder'),
                                Div(f'{tx_type[0]} • {tx_type[1]}', cls='uk-text-small'),
                                cls='uk-margin-small-left'
                            ),
                            cls='uk-flex uk-flex-middle'
                        ),
                        Td(Div(f'R {amount[0]}', cls='uk-text-bolder'), Div(f'R {amount[1]}', cls='uk-text-small')),
                        Td(Div(method[0], cls='uk-text-bolder'), Div(method[1], cls='uk-text-small'))
                    ) for title, tx_type, amount, method in [
                        ('Company', ('Sent', 'Aug 24 2024'), (1500.00, 1371.81), ('Credit Card', '**** 3560')),
                        ('Revenue', ('Received', 'Aug 24 2024'), (1500.00, 1371.81), ('Bank Transfer', '**** 3560')),
                        ('Bonus', ('Received', 'Aug 24 2024'), (1500.00, 1371.81), ('Credit Card', '**** 3560')),
                        ('Dog food', ('Sent', 'Aug 24 2024'), (1500.00, 1371.81), ('Bank Transfer', '**** 3560')),
                        ('Company', ('Sent', 'Aug 24 2024'), (1500.00, 1371.81), ('Bank Transfer', '**** 3560'))
                    ]]
                ),
                cls='uk-table uk-table-divider'
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
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;', id='transactions'
    )


def holdings():
    return Div(
        Div(
            Div(
                Div('Holdings', cls='uk-text-default uk-text-bolder'),
                # Div(
                #     Span(data_uk_icon='icon: table;'),
                #     Span('Filter', cls='uk-margin-small-left'),
                #     cls='uk-text-small uk-flex uk-flex-middle'
                # ),
                cls='uk-flex uk-flex-between'
            ),
            cls='uk-card-header'
        ),
        Div(
            Div(
                Div(
                    Div('Stocks (Equities)', cls='uk-text-small'),
                    H2('R8,167,514.57',
                       cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                    Div('Compared to last month ', Span('+24.17%', cls='uk-text-success'),
                        cls='uk-text-small uk-margin-remove-top')
                ),
                Button('View All', style='background-color: #88A9C3; color: #091235', cls='uk-button uk-button-small'),
                cls='uk-flex uk-flex-between uk-flex-middle'
            ),
            Div(
                Div(
                    Table(
                        Caption('Portfolio Value'),
                        Tbody(
                            *[Tr(
                                Td(style=f'--start: {values[0]}; --end: {values[1]}')
                            ) for title, values in [
                                ('Apple Inc. (AAPL)', (0, 0.3)),
                                ('Tesla Inc. (TSLA)', (0.3, 0.44)),
                                ('Amazon.com Inc. (AMZN)', (0.44, 0.6)),
                                ('Microsoft Corp. (MSFT)', (0.6, 0.68)),
                                ('Alphabet Inc. (GOOGL)', (0.68, 1))
                            ]]
                        ),
                        cls='charts-css pie'
                    )
                ),
                Div(
                    Ul(
                        *[Li(title, Span(amount, cls='uk-text-bolder uk-margin-small-left'), cls='uk-text-small')
                          for title, amount in [
                              ('Apple Inc. (AAPL)', '$31,885'), ('Tesla Inc. (TSLA)', '$8,994'),
                              ('Amazon.com Inc. (AMZN)', '$8,994'), ('Microsoft Corp. (MSFT)', '$8,994'),
                              ('Alphabet Inc. (GOOGL)', '$8,994')
                          ]],
                        cls='charts-css legend legend-inline legend-square', style='border: 0'
                    )
                ),
                data_uk_grid=True,
                cls='uk-grid-divider uk-child-width-expand@m uk-grid-match uk-grid-small uk-margin-medium-top'
            ),
            cls='uk-card-body'
        ),
        Div(
            Nav(
                Ul(
                    Li(
                        A(
                            Span(data_uk_pagination_previous=True, cls='uk-margin-small-right'),
                            'Bonds (Fixed Income Securities)',
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            'Real Estate',
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
        Div(menu_card()), Div(overview_card()),
        Div(portfolio_value_card(), cls='uk-width-1-2@m'),
        # Div(assets_card()),
        Div(transactions(), cls='uk-width-1-2@m'),
        Div(holdings(), cls='uk-width-1-2@m'),
        data_uk_grid=True, cls='uk-padding uk-child-width-1-4@m uk-grid-small uk-grid-match uk-flex-right'
    ),
    style='background-color: #091235'
)
