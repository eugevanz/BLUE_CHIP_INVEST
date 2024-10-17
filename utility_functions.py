from os import environ

from supabase import create_client

SUPABASE_URL = environ.get('SUPABASE_URL')
SUPABASE_KEY = environ.get('SUPABASE_KEY')
SUPABASE_SERVICE_ROLE_KEY = environ.get('SUPABASE_SERVICE_ROLE_KEY')
supabase = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY)
supabase_admin = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_SERVICE_ROLE_KEY)


def get_clients():
    try:
        response = (
            supabase_admin.table('profiles')
            .select('id, email, profile_picture_url, first_name, last_name, phone_number, created_at, '
                    'accounts(balance, updated_at, account_type, portfolio_performance(return_on_investment))')
            .eq('type', 'client')
            .execute()
        )
        if response and response.data:
            return response.data
        else:
            print(response)
    except Exception as e:
        print(f'Error fetching clients: {e}')


def get_client(id: str):
    try:
        response = (
            supabase_admin.table('profiles')
            .select(
                'id, email, profile_picture_url, first_name, last_name, phone_number, created_at, accounts(id, '
                'balance, updated_at, account_type, portfolio_performance(id, return_on_investment), investments(id, '
                'investment_type, symbol, quantity, purchase_price, current_price, purchase_date), transactions(id, '
                'type, amount, description), client_goals(id, goal_type, target_amount, current_savings, target_date), '
                'dividends_and_payouts(id, amount, payment_date), advisors(id, name, email, phone_number, '
                'clients_assigned)'
            )
            .eq('id', id)
            .maybe_single()
            .execute()
        )
        if response and response.data:
            return response.data
        else:
            print(response)
    except Exception as e:
        print(f'Error fetching client: {e}')


def get_profile_id(data:dict):
    return data.get('id') or 'N/A'


def get_profile_email(data:dict):
    return data.get('email') or 'No email provided'


def get_profile_picture_url(data:dict):
    return data.get(
        'profile_picture_url') or ('https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images'
                                   '/jurica-koletic-7YVZYZeITc8-unsplash_3_11zon.webp')


def get_profile_first_name(data:dict):
    return data.get('first_name') or 'No first name'


def get_profile_last_name(data:dict):
    return data.get('last_name') or 'No last name'


def get_profile_phone_number(data:dict):
    return data.get('phone_number') or 'No phone number'


def get_profile_created_at(data:dict):
    return data.get('created_at') or 'Unknown creation date'


def get_accounts_from_data(data:dict):
    return data.get('accounts') or []


def get_portfolio_performance_from_data(data:dict):
    accounts = data.get('accounts') or []
    portfolio_performances = []

    for account in accounts:
        portfolio_performance = account.get('portfolio_performance') or []
        portfolio_performances.extend(portfolio_performance)

    return portfolio_performances


def get_investments_from_data(data:dict):
    accounts = data.get('accounts') or []
    investments = []

    for account in accounts:
        investment = account.get('investments') or []
        investments.extend(investment)

    return investments


def get_transactions_from_data(data:dict):
    accounts = data.get('accounts') or []
    transactions = []

    for account in accounts:
        transaction = account.get('transactions') or []
        transactions.extend(transaction)

    return transactions


def get_client_goals_from_data(data:dict):
    accounts = data.get('accounts') or []
    client_goals = []

    for account in accounts:
        goal = account.get('client_goals') or []
        client_goals.extend(goal)

    return client_goals


def get_dividends_and_payouts_from_data(data:dict):
    accounts = data.get('accounts') or []
    dividends_and_payouts = []

    for account in accounts:
        dividend = account.get('dividends_and_payouts') or []
        dividends_and_payouts.extend(dividend)

    return dividends_and_payouts


def get_advisors_from_data(data:dict):
    accounts = data.get('accounts') or []
    advisors = []

    for account in accounts:
        advisor = account.get('advisors') or []
        advisors.extend(advisor)

    return advisors
