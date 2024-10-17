import numpy as np
from fasthtml.components import Form, Div, Ul, Li, A, H1, Input, H2, Span, H3, Select, Option, Table, Thead, Tr, \
    Th, Tbody, Td, Nav

from interface import add_save_button
from utility_functions import get_profile_picture_url, get_profile_email, get_profile_first_name, get_profile_last_name, \
    get_profile_created_at, get_investments_from_data


def slider_item_account(client: dict, account_options: list):
    account_balance=np.sum()
    return Div(
        Div(
            Div(
                Div(
                    A(href='', data_uk_icon='icon: pencil; ratio: 1.5;', cls='uk-invisible-hover'),
                    data_src=get_profile_picture_url(client),
                    data_uk_img=True, style='width: 128px; height: 128px;',
                    cls='uk-flex uk-flex-center uk-flex-middle uk-background-cover uk-light '
                        'uk-border-circle uk-visible-toggle'
                ),
                cls='uk-width-auto'
            ),
            Div(
                H1(
                    Input(type='text', placeholder=get_profile_first_name(client),
                          aria_label=get_profile_first_name(client),
                          cls='uk-input uk-form-blank uk-text-bolder', style='height: 54px;'),
                    Input(type='text', placeholder=get_profile_last_name(client),
                          aria_label=get_profile_last_name(client),
                          cls='uk-input uk-form-blank', style='height: 54px;'),
                    cls='uk-margin-remove-top uk-margin-remove-bottom'
                )
            ),
            data_uk_grid=True,
            cls='uk-grid-divider uk-flex-middle uk-child-width-1-2'
        ),
        Div(
            f'Member since {get_profile_created_at(client)}',
            Div(get_profile_email(client), cls='uk-text-bolder', style='font-size: 11px'),
            cls='uk-text-small uk-margin-large-top'
        ),
        Div(
            Div(
                Div('Account Balance', cls='uk-text-small'),
                H2(f'R {get_accounts_from_data(client)}',
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


def slider_item_investments(client: dict, account_options: list):
    investment_amount = np.sum(investment.get('current_price', 0) for investment in get_investments_from_data(client))

    return Div(
        Div(
            Div(
                Div('Investment Amount', cls='uk-text-small'),
                H2(f'R {investment_amount}',
                   cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                Div('Compared to last month ',
                    Span(f'{get_portfolio_performance_return_on_investment(client)}%', cls='uk-text-success'),
                    cls='uk-text-small uk-margin-remove-top'),
                cls='uk-margin'
            ),
            Div(
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
                        )
                    ),
                    Div(
                        Div(
                            Div('Investment Amount', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=get_account_updated_at(client),
                                      aria_label=get_account_updated_at(client),
                                      cls='uk-input uk-form-blank uk-text-bolder'),
                                cls='uk-margin-remove-top'
                            )
                        ),
                        Div(
                            Div('Investment Start Date', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=get_account_updated_at(client),
                                      aria_label=get_account_updated_at(client),
                                      cls='uk-text-bolder uk-input uk-form-blank'),
                                cls='uk-margin-remove-top'
                            )
                        ),
                        Div(
                            Div('Investment End Date', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=get_account_updated_at(client),
                                      aria_label=get_account_updated_at(client),
                                      cls='uk-text-bolder uk-input uk-form-blank'),
                                cls='uk-margin-remove-top'
                            )
                        )
                    ),
                    data_uk_grid=True, cls='uk-child-width-1-2@m uk-grid-divider uk-margin'
                ),
                cls='uk-card uk-card-body uk-card-default', style='background-color: #88A9C3;'
            ),
            Div(
                Div('Expected Return Rate', cls='uk-text-small'),
                H3(
                    Input(type='text', placeholder=get_account_updated_at(client),
                          aria_label=get_account_updated_at(client),
                          cls='uk-text-bolder uk-input uk-form-blank'),
                    cls='uk-margin-remove-top'
                ),
                cls='uk-margin'
            ),
            cls='uk-card uk-card-body uk-card-default uk-margin'
        ),
        add_save_button()
    )


def slider_item_transactions():
    return Div(
        Div(
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
                            Td(Div(f'R {amount[0]}', cls='uk-text-bolder'),
                               Div(f'R {amount[1]}', cls='uk-text-small')),
                            Td(Div(method[0], cls='uk-text-bolder'), Div(method[1], cls='uk-text-small'))
                        ) for title, tx_type, amount, method in [
                            ('Company', ('Sent', 'Aug 24 2024'), (1500.00, 1371.81), ('Credit Card', '**** 3560')),
                            ('Revenue', ('Received', 'Aug 24 2024'), (1500.00, 1371.81),
                             ('Bank Transfer', '**** 3560')),
                            (
                                'Bonus', ('Received', 'Aug 24 2024'), (1500.00, 1371.81),
                                ('Credit Card', '**** 3560')),
                            ('Dog food', ('Sent', 'Aug 24 2024'), (1500.00, 1371.81),
                             ('Bank Transfer', '**** 3560')),
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
            cls='uk-card uk-card-body uk-card-default uk-margin uk-light', style='background-color: #88A9C3;'
        )
    )


def slider_item_client_goals(client: dict, account_options: list):
    return Div(
        Div(
            Div(
                Div('Progress (%)', cls='uk-text-small'),
                H2(f'{get_account_balance(client)}%',
                   cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                Div('Compared to last month ',
                    Span(f'{get_portfolio_performance_return_on_investment(client)}%', cls='uk-text-success'),
                    cls='uk-text-small uk-margin-remove-top'),
                cls='uk-margin'
            ),
            Div(
                Div(
                    Div(
                        Div('Goal Description', cls='uk-text-small'),
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
                        )
                    ),
                    Div(
                        Div(
                            Div('Target Amount', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=get_account_updated_at(client),
                                      aria_label=get_account_updated_at(client),
                                      cls='uk-input uk-form-blank uk-text-bolder'),
                                cls='uk-margin-remove-top'
                            )
                        ),
                        Div(
                            Div('Goal Timeline', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=get_account_updated_at(client),
                                      aria_label=get_account_updated_at(client),
                                      cls='uk-text-bolder uk-input uk-form-blank'),
                                cls='uk-margin-remove-top'
                            )
                        )
                    ),
                    data_uk_grid=True, cls='uk-child-width-1-2@m uk-grid-divider uk-margin'
                ),
                cls='uk-card uk-card-body uk-card-default', style='background-color: #88A9C3;'
            ),
            cls='uk-card uk-card-body uk-card-default uk-margin'
        ),
        add_save_button()
    )


def slider_item_payouts(client: dict):
    return Div(
        Div(
            Div(
                Div('Last Dividend Paid', cls='uk-text-small'),
                H2(f'R {get_account_balance(client)}',
                   cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                Div('Total payouts to date ',
                    Span(f'R {get_portfolio_performance_return_on_investment(client)}', cls='uk-text-success'),
                    cls='uk-text-small uk-margin-remove-top'),
                cls='uk-margin'
            ),
            Div(
                Div(
                    Div(
                        Div('Next Payout Date', cls='uk-text-small'),
                        H3(
                            Input(type='text', placeholder=get_account_updated_at(client),
                                  aria_label=get_account_updated_at(client),
                                  cls='uk-input uk-form-blank uk-text-bolder'),
                            cls='uk-margin-remove-top'
                        )
                    ),
                    Div(
                        Div(
                            Div('Payout Amount', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=get_account_updated_at(client),
                                      aria_label=get_account_updated_at(client),
                                      cls='uk-input uk-form-blank uk-text-bolder'),
                                cls='uk-margin-remove-top'
                            )
                        )
                    ),
                    data_uk_grid=True, cls='uk-child-width-1-2@m uk-grid-divider uk-margin'
                ),
                cls='uk-card uk-card-body uk-card-default', style='background-color: #88A9C3;'
            ),
            cls='uk-card uk-card-body uk-card-default uk-margin'
        ),
        add_save_button()
    )


def slider_item_advisors(client: dict):
    return Div(
        Div(
            Div(
                Div(
                    Div(
                        Div(
                            A(href='', data_uk_icon='icon: pencil; ratio: 1.5;', cls='uk-invisible-hover'),
                            data_src=get_profile_picture_url(client),
                            data_uk_img=True, style='width: 128px; height: 128px;',
                            cls='uk-flex uk-flex-center uk-flex-middle uk-background-cover uk-light '
                                'uk-border-circle uk-visible-toggle'
                        ),
                        cls='uk-width-auto'
                    ),
                    Div(
                        Div(get_profile_email(client), cls='uk-text-small uk-text-bolder'),
                        H2(
                            Span(get_profile_first_name(client), cls='uk-text-bolder'), Span(' '),
                            Span(get_profile_last_name(client)),
                            cls='uk-margin-remove-top uk-margin-remove-bottom'
                        )
                    ),
                    data_uk_grid=True, cls='uk-child-width-1-2@m uk-grid-divider uk-flex-middle uk-margin'
                ),
                cls='uk-card uk-card-body uk-card-default', style='background-color: #88A9C3;'
            ),
            cls='uk-card uk-card-body uk-card-default uk-margin'
        ),
        add_save_button()
    )


def page(client: dict):
    account_type = get_account_type(client)
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

    return Form(
        Div(
            Div(style='background-image: url('
                      'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/marten'
                      '-bjork-6dW3xyQvcYE-unsplash_6_11zon.webp); filter: grayscale(90%);',
                data_uk_height_viewport=True,
                cls='uk-background-cover uk-visible@m'),
            Div(
                Ul(
                    *[Li(A(title, href='#')) for title in [
                        'Account', 'Investments', 'Transactions', 'Client Goals',
                        'Dividends/Payouts', 'Advisors'
                    ]],
                    data_uk_tab='animation: uk-animation-slide-left-medium, uk-animation-slide-right-medium',
                    cls='uk-margin-large-bottom'
                ),
                Div(
                    slider_item_account(client=client, account_options=account_options),
                    slider_item_investments(client=client, account_options=account_options),
                    slider_item_transactions(),
                    slider_item_client_goals(client=client, account_options=account_options),
                    slider_item_payouts(client=client),
                    slider_item_advisors(client=client),
                    cls='uk-switcher uk-margin'
                ),
                cls='uk-padding-large'
            ),
            data_uk_grid=True,
            cls='uk-grid-collapse uk-child-width-1-2@m'
        )
    )
