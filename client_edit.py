from datetime import datetime

import numpy as np
from fasthtml.components import Div, Ul, Li, A, H1, Input, H2, Span, H3, Select, Option, Table, Thead, Tr, \
    Th, Tbody, Td, Nav, P, Strong

from interface import add_save_button
from utility_functions import get_accounts, get_investments, get_transactions, get_client_goals, \
    get_dividends_and_payouts, dt_object


def slider_item_account(client: dict, accounts: list):
    return Div(
        Div(
            Div(
                Div(
                    A(href='', data_uk_icon='icon: pencil; ratio: 1.5;', cls='uk-invisible-hover'),
                    data_src=client['profile_picture_url'],
                    data_uk_img=True, style='width: 128px; height: 128px;',
                    cls='uk-flex uk-flex-center uk-flex-middle uk-background-cover uk-light '
                        'uk-border-circle uk-visible-toggle'
                ) if client['profile_picture_url'] else Div(
                    Span(data_uk_icon='icon: user; ratio: 7;'),
                    Div(Input(type='file'),
                        A(href='', data_uk_icon='icon: pencil; ratio: 1.5;', cls='uk-invisible-hover uk-link'),
                        data_uk_form_custom=True),
                    cls='uk-flex uk-flex-center uk-flex-middle uk-visible-toggle js-upload uk-placeholder'
                ),
                cls='uk-width-auto'
            ),
            Div(
                H1(
                    Input(type='text', placeholder=client['first_name'] if client['first_name'] else 'First Name',
                          aria_label='First Name',
                          cls='uk-input uk-form-blank uk-text-bolder', style='height: 54px;'),
                    Input(type='text', placeholder=client['last_name'] if client['last_name'] else 'Last Name',
                          aria_label='Last Name',
                          cls='uk-input uk-form-blank', style='height: 54px;'),
                    cls='uk-margin-remove-top uk-margin-remove-bottom'
                )
            ),
            data_uk_grid=True,
            cls='uk-grid-divider uk-flex-middle uk-child-width-1-2'
        ),
        Div(
            f'Member since {dt_object(client["created_at"])}',
            Div(client['email'], cls='uk-text-bolder', style='font-size: 11px'),
            cls='uk-text-small uk-margin-large-top'
        ),
        *[Div(
            Div(
                Div('Account Balance', cls='uk-text-small'),
                H2(f'R {account["balance"]}',
                   cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                cls='uk-margin'
            ),
            Div(
                Div(
                    Div(
                        Div('Account Type', cls='uk-text-small'),
                        H3(account['account_type']),
                        cls='uk-card uk-card-body', style='background-color: #88A9C3;'
                    )
                ),
                Div(
                    Div(
                        Div('Last Updated', cls='uk-text-small'),
                        H3(account['updated_at'],
                           cls='uk-text-bolder uk-margin-remove-top uk-text-truncate'),
                        cls='uk-card uk-card-body', style='background-color: #88A9C3;'
                    )
                ),
                data_uk_grid=True,
                cls='uk-child-width-1-2@m uk-grid-match uk-margin'
            ),
            cls='uk-card uk-card-body uk-card-default uk-margin'
        ) for account in accounts] if accounts else Div(),
        P('A financial ',
          Strong('account'),
          ' manages your assets, such as stocks, bonds, and savings. It tracks transactions, portfolio performance, '
          'and balance, while providing advisory services to support your financial goals.',
          cls='uk-text-small', id='account-desc'),
        add_save_button('Add account')
    )


def slider_item_investments(investments: list):
    investment_options = ['Stocks (Equities)', 'Bonds (Fixed Income)', 'Mutual Funds', 'Exchange-Traded Funds (ETFs)',
                          'Real Estate', 'Commodities', 'Cryptocurrency', 'Private Equity', 'Hedge Funds',
                          'Savings Accounts & Certificates of Deposit (CDs)', 'Annuities', 'Options']

    return Div(
        *[Div(
            Div(
                Div('Investment Amount', cls='uk-text-small'),
                H2(f'R {investment["current_price"]}',
                   cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                Div('Compared to purchase value ',
                    Span(f'R {investment["purchase_price"]}', cls='uk-text-success'),
                    cls='uk-text-small uk-margin-remove-top'),
                cls='uk-margin'
            ),
            Div(
                Div(
                    Div(
                        Div('Investment Type', cls='uk-text-small'),
                        H3(
                            Select(
                                *[Option(title) for title in investment_options],
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
                            Div('Investment Purchase Price', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=investment['purchase_price'],
                                      aria_label=investment['purchase_price'],
                                      cls='uk-input uk-form-blank uk-text-bolder'),
                                cls='uk-margin-remove-top'
                            )
                        ),
                        Div(
                            Div('Investment Start Date', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=investment['purchase_date'],
                                      aria_label=investment['purchase_date'],
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
                Div('Investment Type', cls='uk-text-small'),
                H3(
                    Select(
                        *[Option(title) for title in investment_options],
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
                cls='uk-margin'
            ),
            cls='uk-card uk-card-body uk-card-default uk-margin'
        ) for investment in investments] if investments else Div(),
        P(
            'An ',
            Strong('investment'),
            ' is the allocation of money or resources into assets like stocks, bonds, real estate, or businesses with '
            'the expectation of generating a return or profit over time. It aims to grow wealth, provide income, '
            'or achieve specific financial goals.',
            cls='uk-text-small'
        ),
        add_save_button('Add investment')
    )


def slider_item_transactions(transactions: list):
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
                            Th('Amount')
                        )
                    ),
                    Tbody(
                        *[Tr(
                            Td(
                                Span(
                                    uk_icon=f'icon:  '
                                            f'{"plus-circle" if transaction["type"] == "debit" else "minus-circle"}; ratio: 1.5',
                                    cls=f'uk-text-{"success" if transaction["type"] == "debit" else "danger"}'),
                                Div(
                                    Div(transaction['description'], cls='uk-text-bolder'),
                                    Div(f'{transaction["type"]} • {transaction["type"]}', cls='uk-text-small'),
                                    cls='uk-margin-small-left'
                                ),
                                cls='uk-flex uk-flex-middle'
                            ),
                            Td(Div(f'R {transaction["amount"]}', cls='uk-text-bolder'))
                        ) for transaction in transactions] if transactions else Div()
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
        ),
        P(
            'A ',
            Strong('transaction'),
            ' is a financial action involving the exchange of money or assets, such as buying or selling investments, '
            'transferring funds, or making payments. It is recorded in an account to track financial activity and '
            'balances.',
            cls='uk-text-small'
        ),
        add_save_button('Add transaction')
    )


def slider_item_client_goals(client_goals: list):
    goal_options = ['Retirement Savings', 'Emergency Fund', 'Education Fund', 'Home Purchase', 'Debt Reduction',
                    'Vacation Fund', 'Investment Growth', 'Business Start-Up', 'Charitable Giving',
                    'Wealth Accumulation', 'Major Purchase', 'Health and Wellness', 'Estate Planning',
                    'Early Retirement', 'Legacy Planning']

    return Div(
        *[Div(
            Div(
                Div('Progress (%)', cls='uk-text-small'),
                H2(f'R {goal["current_savings"]}',
                   cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                Div('Compared to last month ',
                    Span(f'{(goal["current_savings"] / goal["target_amount"]) * 100}%', cls='uk-text-success'),
                    cls='uk-text-small uk-margin-remove-top'),
                cls='uk-margin'
            ),
            Div(
                Div(
                    Div(
                        Div('Goal Description', cls='uk-text-small'),
                        H3(
                            Select(
                                *[Option(title) for title in goal_options],
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
                                Input(type='text', placeholder=goal['target_amount'],
                                      aria_label=goal['target_amount'],
                                      cls='uk-input uk-form-blank uk-text-bolder'),
                                cls='uk-margin-remove-top'
                            )
                        ),
                        Div(
                            Div('Goal Timeline', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=goal['target_date'],
                                      aria_label=goal['target_date'],
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
        ) for goal in client_goals] if client_goals else Div(),
        P(
            'A ',
            Strong('client goal'),
            ' is a specific financial objective set by an individual, such as saving for retirement, buying a home, '
            'or funding education. It guides investment strategies and decisions, helping to align financial planning with personal aspirations.',
            cls='uk-text-small'
        ),
        add_save_button('Add goal')
    )


def slider_item_payouts(dividends_and_payouts: list):
    latest_dividend = max(
        dividends_and_payouts,
        key=lambda x: datetime.strptime(x["payment_date"], "%Y-%m-%dT%H:%M:%SZ")
    )['amount'] if dividends_and_payouts else 0
    total_payouts_to_date = np.sum(
        [payout.get("amount", 0) for payout in dividends_and_payouts if dividends_and_payouts])

    return Div(
        Div(
            Div(
                Div('Last Dividend Paid', cls='uk-text-small'),
                H2(f'R {latest_dividend}',
                   cls='uk-text-bolder uk-margin-remove-top uk-margin-remove-bottom uk-text-truncate'),
                Div('Total payouts to date ',
                    Span(
                        f'R {total_payouts_to_date}',
                        cls='uk-text-success'
                    ),
                    cls='uk-text-small uk-margin-remove-top'),
                cls='uk-margin'
            ),
            *[Div(
                Div(
                    Div(
                        Div('Payout Date', cls='uk-text-small'),
                        H3(
                            Input(type='text', placeholder=payout['payment_date'],
                                  aria_label=payout['payment_date'],
                                  cls='uk-input uk-form-blank uk-text-bolder'),
                            cls='uk-margin-remove-top'
                        )
                    ),
                    Div(
                        Div(
                            Div('Payout Amount', cls='uk-text-small'),
                            H3(
                                Input(type='text', placeholder=payout['amount'],
                                      aria_label=payout['amount'],
                                      cls='uk-input uk-form-blank uk-text-bolder'),
                                cls='uk-margin-remove-top'
                            )
                        )
                    ),
                    data_uk_grid=True, cls='uk-child-width-1-2@m uk-grid-divider uk-margin'
                ),
                cls='uk-card uk-card-body uk-card-default uk-margin', style='background-color: #88A9C3;'
            ) for payout in dividends_and_payouts] if dividends_and_payouts else Div(),
            cls='uk-card uk-card-body uk-card-default uk-margin'
        ),
        P(
            'A ',
            Strong('dividend/payout'),
            ' is a payment made to investors from a company’s profits or from an investment’s earnings, typically in '
            'the form of cash or additional shares. It provides a way for investors to earn income from their '
            'investments.',
            cls='uk-text-small'
        ),
        add_save_button('Add payout')
    )


def page(client: dict):
    accounts = get_accounts(client['id'])
    client_goals = get_client_goals(client['id'])
    investments = [
        get_investments(account_id=account['id'])
        for account in (accounts or [])
        if account and account['id']
    ]
    transactions = [
        get_transactions(account_id=account['id'])
        for account in (accounts or [])
        if account and account['id']
    ]
    dividends_and_payouts = [
        get_dividends_and_payouts(account_id=account['id'])
        for account in (accounts or [])
        if account and account['id']
    ]

    return Div(
        Div(
            Div(style='background-image: url('
                      'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/marten'
                      '-bjork-6dW3xyQvcYE-unsplash_6_11zon.webp); filter: grayscale(90%);',
                data_uk_height_viewport=True, cls='uk-background-cover uk-visible@m'),
            Div(
                Ul(
                    *[Li(A(title, href='#')) for title in [
                        'Account', 'Investments', 'Transactions', 'Client Goals',
                        'Dividends/Payouts'
                    ]],
                    data_uk_tab='animation: uk-animation-slide-left-medium, uk-animation-slide-right-medium',
                    cls='uk-margin-large-bottom'
                ),
                Div(
                    slider_item_account(client=client, accounts=accounts),
                    slider_item_investments(investments=investments),
                    slider_item_transactions(transactions=transactions),
                    slider_item_client_goals(client_goals=client_goals),
                    slider_item_payouts(dividends_and_payouts=dividends_and_payouts),
                    cls='uk-switcher uk-margin'
                ),
                cls='uk-padding-large',
            ),
            data_uk_grid=True,
            cls='uk-grid-collapse uk-child-width-1-2@m'
        ),
        hx_history=False
    )
