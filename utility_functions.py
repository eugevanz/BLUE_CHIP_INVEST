from datetime import datetime
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
            print('No clients exist')
    except Exception as e:
        print(f'Error fetching clients: {e}')


def get_client(id: str):
    try:
        response = (
            supabase_admin.table('profiles')
            .select('id, email, profile_picture_url, first_name, last_name, phone_number, created_at')
            .eq('id', id)
            .maybe_single()
            .execute()
        )
        if response and response.data:
            return response.data
        else:
            print('Client does not exist')
    except Exception as e:
        print(f'Error fetching client: {e}')


def get_accounts(profile_id: str):
    try:
        response = (
            supabase_admin.table('accounts')
            .select('id, balance, updated_at, account_type')
            .eq('profile_id', profile_id)
            .maybe_single()
            .execute()
        )
        if response and response.data:
            return response.data
        else:
            print('No accounts for client')
    except Exception as e:
        print(f'Error fetching client: {e}')


def get_client_goals(profile_id: str):
    try:
        response = (
            supabase_admin.table('client_goals')
            .select('id, goal_type, target_amount, current_savings, target_date')
            .eq('profile_id', profile_id)
            .maybe_single()
            .execute()
        )
        if response and response.data:
            return response.data
        else:
            print('No goals for client')
    except Exception as e:
        print(f'Error fetching client: {e}')


def get_investments(account_id: str):
    try:
        response = (
            supabase_admin.table('investments')
            .select('id, investment_type, symbol, quantity, purchase_price, current_price, purchase_date')
            .eq('account_id', account_id)
            .maybe_single()
            .execute()
        )
        if response and response.data:
            return response.data
        else:
            print('No investments for client')
    except Exception as e:
        print(f'Error fetching client: {e}')


def get_transactions(account_id: str):
    try:
        response = (
            supabase_admin.table('transactions')
            .select('id, type, amount, description')
            .eq('account_id', account_id)
            .maybe_single()
            .execute()
        )
        if response and response.data:
            return response.data
        else:
            print('No transactions for client')
    except Exception as e:
        print(f'Error fetching client: {e}')


def get_dividends_and_payouts(account_id: str):
    try:
        response = (
            supabase_admin.table('dividends_and_payouts')
            .select('id, amount, payment_date')
            .eq('account_id', account_id)
            .maybe_single()
            .execute()
        )
        if response and response.data:
            return response.data
        else:
            print('No payouts for account')
    except Exception as e:
        print(f'Error fetching client: {e}')


def get_portfolio_performance(account_id: str):
    try:
        response = (
            supabase_admin.table('portfolio_performance')
            .select('id, return_on_investment')
            .eq('account_id', account_id)
            .execute()
        )
        if response and response.data:
            return response.data
        else:
            print('No portfolio performance')
    except Exception as e:
        print(f'Error fetching client: {e}')


dt_object = lambda timestamp: datetime.strptime(
    timestamp, '%Y-%m-%dT%H:%M:%S.%f%z'
).strftime('%B %d, %Y') if timestamp else datetime.now().strftime('%B %d, %Y')
