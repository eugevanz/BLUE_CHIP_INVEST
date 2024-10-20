import json

from fasthtml.components import Div, Ul, Li, A, H1, Input, Span, Table, Thead, Tr, \
    Th, Tbody, Td, P, Strong, Form, H3, Button, Select, Option

from interface import add_save_button
from utility_functions import get_accounts, get_investments, get_transactions, get_client_goals, \
    get_dividends_and_payouts, dt_object


def account_form(profile_id: str):
    return Div(
        Form(
            Div('Account Type', cls='uk-text-small'),
            H3(
                Select(
                    *[Option(title) for title in [
                        'Savings Account', 'Investment Account', 'Retirement Account',
                        'Brokerage Account', 'Trust Account', 'Custodial Account',
                        'Taxable Account', 'Tax-Deferred Account', 'Tax-Exempt Account',
                        'Money Market Account', 'Certificate of Deposit (CD) Account',
                        'Mutual Fund Account', 'Pension Account',
                        'Self-Directed Investment Account', 'High-Yield Savings Account',
                        'Fixed-Income Account', 'Annuity Account', 'Forex Trading Account',
                        'Commodities Trading Account'
                    ]],
                    aria_label='Custom controls',
                    cls='uk-select uk-text-center', name='account_type'
                ),
                Span(
                    Span(),
                    Span(data_uk_icon='icon: pencil')
                ),
                cls='uk-text-bolder uk-margin-remove-top',
                data_uk_form_custom='target: > * > span:first-child'
            ),
            Div('Account Number', cls='uk-text-small'),
            H3(
                Input(type='text', placeholder='Account Number', aria_label='Account Number',
                      cls='uk-input uk-form-blank uk-text-bolder', name='account_number'),
                cls='uk-margin-remove-top'
            ),
            Div('Balance', cls='uk-text-small'),
            H3(
                Input(type='number', placeholder='Balance', aria_label='Balance',
                      cls='uk-input uk-form-blank uk-text-bolder', name='balance'),
                cls='uk-margin-remove-top'
            ),
            Button('Save', type='submit', cls='uk-button uk-button-primary uk-margin-large-top uk-modal-close',
                   hx_post='/update-client/', hx_target='#account-table', hx_swap='beforeend',
                   hx_vals=json.dumps({'target': 'accounts', 'profile_id': profile_id})),
            cls='uk-modal-dialog uk-modal-body'
        ),
        id='account-modal', data_uk_modal=True
    )


def select_account(accounts: list):
    return Div(
        Div('Account', cls='uk-text-small'),
        H3(
            Select(
                *[Option(f'{account["account_type"]} #{account["account_number"]}', value=account['id']) for
                  account in accounts],
                aria_label='Custom controls',
                cls='uk-select uk-text-center', name='account_id'
            ),
            Span(
                Span(),
                Span(data_uk_icon='icon: pencil')
            ),
            cls='uk-text-bolder uk-margin-remove-top',
            data_uk_form_custom='target: > * > span:first-child'
        )
    )


def investment_form(accounts: list):
    return Div(
        Form(
            select_account(accounts),
            Div('Investment Type', cls='uk-text-small'),
            H3(
                Select(
                    *[Option(title) for title in [
                        'Stocks (Equities)', 'Bonds (Fixed Income)', 'Mutual Funds', 'Exchange-Traded Funds (ETFs)',
                        'Real Estate', 'Commodities', 'Cryptocurrency', 'Private Equity', 'Hedge Funds',
                        'Savings Accounts & Certificates of Deposit (CDs)', 'Annuities', 'Options'
                    ]],
                    aria_label='Custom controls',
                    cls='uk-select uk-text-center', name='investment_type'
                ),
                Span(
                    Span(),
                    Span(data_uk_icon='icon: pencil')
                ),
                cls='uk-text-bolder uk-margin-remove-top',
                data_uk_form_custom='target: > * > span:first-child'
            ),
            Div('Investment Amount', cls='uk-text-small'),
            H3(
                Input(type='text', placeholder='Investment Amount', aria_label='Investment Amount',
                      cls='uk-input uk-form-blank uk-text-bolder', name='quantity'),
                cls='uk-margin-remove-top'
            ),
            Div('Investment Purchase Price', cls='uk-text-small'),
            H3(
                Input(type='text', placeholder='Investment Purchase Price', aria_label='Investment Purchase Price',
                      cls='uk-input uk-form-blank uk-text-bolder', name='purchase_price'),
                cls='uk-margin-remove-top'
            ),
            Div('Investment Start Date', cls='uk-text-small'),
            H3(
                Input(type='number', placeholder='Investment Start Date', aria_label='Investment Start Date',
                      cls='uk-input uk-form-blank uk-text-bolder', name='purchase_date'),
                cls='uk-margin-remove-top'
            ),
            Button('Save', type='submit', cls='uk-button uk-button-primary uk-margin-large-top uk-modal-close',
                   hx_post='/update-client/', hx_target='#invest-table', hx_swap='beforeend',
                   hx_vals='{"target": "investments"}'),
            cls='uk-modal-dialog uk-modal-body'
        ) if accounts and len(accounts) > 0 else Div(
            'Add account to profile',
            cls='uk-text-danger uk-text-uppercase uk-text-bolder'
        ),
        id='invest-modal', data_uk_modal=True
    )


def transaction_form(accounts: list):
    return Div(
        Form(
            select_account(accounts),
            Div('Transaction', cls='uk-text-small'),
            H3(
                Select(
                    *[Option(title) for title in ['debit', 'credit']],
                    aria_label='Custom controls',
                    cls='uk-select uk-text-center', name='type'
                ),
                Span(
                    Span(),
                    Span(data_uk_icon='icon: pencil')
                ),
                cls='uk-text-bolder uk-margin-remove-top',
                data_uk_form_custom='target: > * > span:first-child'
            ),
            Div('Description', cls='uk-text-small'),
            H3(
                Input(type='text', placeholder='Transaction Description', aria_label='Transaction Description',
                      cls='uk-input uk-form-blank uk-text-bolder', name='description'),
                cls='uk-margin-remove-top'
            ),
            Div('Transaction Amount', cls='uk-text-small'),
            H3(
                Input(type='text', placeholder='Transaction Amount', aria_label='Transaction Amount',
                      cls='uk-input uk-form-blank uk-text-bolder', name='amount'),
                cls='uk-margin-remove-top'
            ),
            Div('Transaction Date', cls='uk-text-small'),
            H3(
                Input(type='number', placeholder='Transaction Date', aria_label='Transaction Date',
                      cls='uk-input uk-form-blank uk-text-bolder', name='updated_at'),
                cls='uk-margin-remove-top'
            ),
            Button('Save', type='submit', cls='uk-button uk-button-primary uk-margin-large-top uk-modal-close',
                   hx_post='/update-client/', hx_target='#transaction-table', hx_swap='beforeend',
                   hx_vals='{"target": "transactions"}'),
            cls='uk-modal-dialog uk-modal-body'
        ) if accounts and len(accounts) > 0 else Div(
            'Add account to profile',
            cls='uk-text-danger uk-text-uppercase uk-text-bolder'
        ),
        id='transaction-modal', data_uk_modal=True
    )


def client_goals_form(profile_id: str):
    return Div(
        Form(
            Div('Goal', cls='uk-text-small'),
            H3(
                Select(
                    *[Option(title) for title in [
                        'Retirement Savings', 'Emergency Fund', 'Education Fund', 'Home Purchase', 'Debt Reduction',
                        'Vacation Fund', 'Investment Growth', 'Business Start-Up', 'Charitable Giving',
                        'Wealth Accumulation', 'Major Purchase', 'Health and Wellness', 'Estate Planning',
                        'Early Retirement', 'Legacy Planning'
                    ]],
                    aria_label='Custom controls',
                    cls='uk-select uk-text-center', name='goal_type'
                ),
                Span(
                    Span(),
                    Span(data_uk_icon='icon: pencil')
                ),
                cls='uk-text-bolder uk-margin-remove-top',
                data_uk_form_custom='target: > * > span:first-child'
            ),
            Div('Target Amount', cls='uk-text-small'),
            H3(
                Input(type='text', placeholder='Target Amount', aria_label='Target Amount',
                      cls='uk-input uk-form-blank uk-text-bolder', name='target_amount'),
                cls='uk-margin-remove-top'
            ),
            Div('Target Date', cls='uk-text-small'),
            H3(
                Input(type='text', placeholder='Target Date', aria_label='Target Date',
                      cls='uk-input uk-form-blank uk-text-bolder', name='target_date'),
                cls='uk-margin-remove-top'
            ),
            Button('Save', type='submit', cls='uk-button uk-button-primary uk-margin-large-top uk-modal-close',
                   hx_post='/update-client/', hx_target='#goals-table', hx_swap='beforeend',
                   hx_vals=json.dumps({'target': 'client_goals', 'profile_id': profile_id})),
            cls='uk-modal-dialog uk-modal-body'
        ),
        id='goal-modal', data_uk_modal=True
    )


def payouts_form(accounts: list):
    return Div(
        Form(
            select_account(accounts),
            Div('Payout Date', cls='uk-text-small'),
            H3(
                Input(type='text', placeholder='Payout Date', aria_label='Payout Date',
                      cls='uk-input uk-form-blank uk-text-bolder', name='payment_date'),
                cls='uk-margin-remove-top'
            ),
            Div('Amount', cls='uk-text-small'),
            H3(
                Input(type='text', placeholder='Amount', aria_label='Amount',
                      cls='uk-input uk-form-blank uk-text-bolder', name='amount'),
                cls='uk-margin-remove-top'
            ),
            Button(
                'Save', type='submit', cls='uk-button uk-button-primary uk-margin-large-top uk-modal-close',
                hx_post='/update-client/', hx_target='#payout-table', hx_swap='beforeend',
                hx_vals='{"target": "dividends_and_payouts"}'
            ),
            cls='uk-modal-dialog uk-modal-body'
        ) if accounts and len(accounts) > 0 else Div(
            'Add account to profile',
            cls='uk-text-danger uk-text-uppercase uk-text-bolder'
        ),
        id='payout-modal', data_uk_modal=True
    )


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
        P('A financial ',
          Strong('account'),
          ' manages your assets, such as stocks, bonds, and savings. It tracks transactions, portfolio performance, '
          'and balance, while providing advisory services to support your financial goals.',
          cls='uk-text-small'),
        Div(
            Table(
                Thead(
                    Tr(Th('Balance'), Th('Account'), Th('Account #'), Th('Last Updated'), Th(''))
                ),
                Tbody(
                    *[Tr(
                        Td(f'R {account["balance"]}'),
                        Td(account['account_type']),
                        Td(account['account_number']),
                        Td(account['updated_at']),
                        Td(A(href='', data_uk_icon='trash', cls='uk-icon-button uk-text-danger'))
                    ) for account in accounts if account is not None and isinstance(account, dict)] if accounts and len(
                        accounts) > 0 else Span(),
                    id='account-table'
                ),
                cls='uk-table uk-table-justify uk-table-divider uk-table-small'
            ),
            cls='uk-overflow-auto'
        ),
        add_save_button('Add account', target='account'),
        account_form(profile_id=client['id'])
    )


def slider_item_investments(investments: list, accounts: list):
    print(investments)
    return Div(
        P(
            'An ',
            Strong('investment'),
            ' is the allocation of money or resources into assets like stocks, bonds, real estate, or businesses with '
            'the expectation of generating a return or profit over time. It aims to grow wealth, provide income, '
            'or achieve specific financial goals.',
            cls='uk-text-small'
        ),
        Table(
            Thead(
                Tr(Th('Investment'), Th('Amount'), Th('Purchase Price'), Th('Current Price'), Th('Start Date'), Th(''))
            ),
            Tbody(
                *[Tr(
                    Td(investment['investment_type']),
                    Td(investment['quantity']),
                    Td(investment['purchase_price']),
                    Td(investment['current_price']),
                    Td(investment['purchase_date'])
                ) for investment in investments if
                    investment is not None and isinstance(investment, dict)] if investments and len(investments) > 0
                else Span(),
                id='invest-table'
            ),
            cls='uk-table uk-table-justify uk-table-divider'
        ),
        add_save_button('Add investment', target='invest'),
        investment_form(accounts=accounts)
    )


def slider_item_transactions(transactions: list, accounts: list):
    return Div(
        P(
            'A ',
            Strong('transaction'),
            ' is a financial action involving the exchange of money or assets, such as buying or selling investments, '
            'transferring funds, or making payments. It is recorded in an account to track financial activity and '
            'balances.',
            cls='uk-text-small'
        ),
        Table(
            Thead(
                Tr(Th('Description'), Th('Transaction'), Th('Amount'), Th('Last Updated'), Th(''))
            ),
            Tbody(
                *[Tr(
                    Td(transaction['description']),
                    Td(transaction['type'], cls=f'uk-text-{"success" if transaction["type"] == "debit" else "danger"}'),
                    Td(f'R {transaction["amount"]}'),
                    Td(A(href='', data_uk_icon='trash', cls='uk-icon-button'))
                ) for transaction in transactions if
                    transaction is not None and isinstance(transaction, dict)] if transactions and len(
                    transactions) > 0 else Span(),
                id='transaction-table'
            ),
            cls='uk-table uk-table-justify uk-table-divider'
        ),
        add_save_button('Add transaction', target='transaction'),
        transaction_form(accounts=accounts)
    )


def slider_item_client_goals(client_goals: list, profile_id: str):
    return Div(
        P(
            'A ',
            Strong('client goal'),
            ' is a specific financial objective set by an individual, such as saving for retirement, buying a home, '
            'or funding education. It guides investment strategies and decisions, helping to align financial planning with personal aspirations.',
            cls='uk-text-small'
        ),
        Table(
            Thead(
                Tr(Th('Current Savings'), Th('Target Amount'), Th('Goal'), Th('Target Date'), Th(''))
            ),
            Tbody(
                *[Tr(
                    Td(f'R {goal["current_savings"]}'),
                    Td(goal['target_amount']),
                    Td(goal['goal_type']),
                    Td(goal['target_date']),
                    Td(A(href='', data_uk_icon='trash', cls='uk-icon-button'))
                ) for goal in client_goals if goal is not None and isinstance(goal, dict)] if client_goals and len(
                    client_goals) > 0 else Span(),
                id='goals-table'
            ),
            cls='uk-table uk-table-justify uk-table-divider'
        ),
        add_save_button('Add goal', target='goal'),
        client_goals_form(profile_id)
    )


def slider_item_payouts(dividends_and_payouts: list, accounts: list):
    return Div(
        P(
            'A ',
            Strong('dividend/payout'),
            ' is a payment made to investors from a company’s profits or from an investment’s earnings, typically in '
            'the form of cash or additional shares. It provides a way for investors to earn income from their '
            'investments.',
            cls='uk-text-small'
        ),
        Table(
            Thead(
                Tr(Th('Payment Date'), Th('Amount'), Th(''))
            ),
            Tbody(
                *[Tr(
                    Td(payout['payment_date']),
                    Td(f'R {payout["amount"]}'),
                    Td(A(href='', data_uk_icon='trash', cls='uk-icon-button'))
                ) for payout in dividends_and_payouts if
                    payout is not None and isinstance(payout, dict)] if dividends_and_payouts and len(
                    dividends_and_payouts) > 0 else Span(),
                id='payout-table'
            ),
            cls='uk-table uk-table-justify uk-table-divider'
        ),
        add_save_button('Add payout', target='payout'),
        payouts_form(accounts=accounts)
    )


def page(client: dict):
    accounts = get_accounts(client['id'])
    client_goals = get_client_goals(client['id'])
    investments = [
        investment
        for account in (accounts or [])
        for investment in get_investments(account_id=account['id'])
    ]
    transactions = [
        transaction
        for account in (accounts or [])
        for transaction in get_transactions(account_id=account['id'])
    ]
    dividends_and_payouts = [
        payout
        for account in (accounts or [])
        for payout in get_dividends_and_payouts(account_id=account['id'])
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
                    slider_item_investments(investments=investments, accounts=accounts),
                    slider_item_transactions(transactions=transactions, accounts=accounts),
                    slider_item_client_goals(client_goals=client_goals, profile_id=client['id']),
                    slider_item_payouts(dividends_and_payouts=dividends_and_payouts, accounts=accounts),
                    cls='uk-switcher uk-margin'
                ),
                cls='uk-padding-large',
            ),
            data_uk_grid=True,
            cls='uk-grid-collapse uk-child-width-1-2@m'
        ),
        hx_history=False
    )
