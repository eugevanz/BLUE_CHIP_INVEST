from datetime import datetime

from fasthtml.components import Div, Nav, Ul, Li, A, Span, P, H3, Img, Tr, Td, Tbody, Th, Thead, \
    Table

from interface import calendar_view


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
                        Th('Status'),
                        Th('Method')
                    )
                ),
                Tbody(
                    *[Tr(
                        Td(
                            Span(uk_icon='icon:  plus-circle; ratio: 2', cls='uk-text-success'),
                            Div(
                                Div(title, cls='uk-text-bolder'),
                                Div('Sent • Aug 24 2024', cls='uk-text-small'),
                                cls='uk-margin-small-left'
                            ),
                            cls='uk-flex uk-flex-middle'
                        ),
                        Td('Table Data'),
                        Td('Table Data'),
                        Td('Table Data')
                    ) for title in ['Company', 'Revenue', 'Bonus', 'Dog food']]
                ),
                cls='uk-table uk-table-divider'
            ),
            cls='uk-card-body'
        ),
        cls='uk-card uk-card-default uk-light', style='background-color: #172031;'
    )


page = Div(
    Div(
        Div(menu_card()), Div(overview_card()),
        # Div(portfolio_value_card()),
        # Div(assets_card()),
        Div(transactions(), cls='uk-width-1-2@m'),
        # Div(client_insights_card(), cls='uk-width-1-2@m'),
        data_uk_grid=True, cls='uk-padding uk-child-width-1-4@m uk-grid-small uk-grid-match uk-flex-right'
    ),
    style='background-color: #091235'
)
