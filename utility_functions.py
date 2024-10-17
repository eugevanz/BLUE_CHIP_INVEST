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
            print(response)
    except Exception as e:
        print(f'Error fetching clients: {e}')


def get_profile_client_id(client: dict):
    return client.get('id', None)


def get_profile_created_at(client: dict):
    created_at = client.get('created_at', None)
    if created_at:
        try:
            dt = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f%z')
            return dt.strftime('%B %d, %Y')
        except ValueError:
            return 'Invalid date format'
    else:
        return 'Today'


def get_profile_client_email(client: dict):
    return client.get('email', 'No email') or 'No email'


def get_profile_address(client: dict):
    return client.get('address', 'No address') or 'No address'


def get_profile_picture_url(client: dict):
    return client.get(
        'profile_picture_url',
        'https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jurica-koletic'
        '-7YVZYZeITc8-unsplash_3_11zon.webp'
    ) or ('https://oujdrprpkkwxeavzbaow.supabase.co/storage/v1/object/public/website_images/jurica-koletic-7YVZYZeITc8'
          '-unsplash_3_11zon.webp')


def get_profile_first_name(client: dict):
    return client.get('first_name', 'First name') or 'First name'


def get_profile_last_name(client: dict):
    return client.get('last_name', 'Last name') or 'Last name'


def get_portfolio_performance_return_on_investment(client: dict):
    return_on_investment = 0.0
    if client.get('accounts'):
        account = client['accounts'][0]
        return_on_investment = account.get('portfolio_performance', {}).get('return_on_investment', 0.0)
    return return_on_investment


def get_account_balance(client: dict):
    balance = 0.0
    if client.get('accounts'):
        balance = client['accounts'][0].get('balance', 0.0)
    if balance is None:
        balance = 0.0
    return balance


def get_account_updated_at(client: dict):
    updated_at = None
    if client.get('accounts'):
        updated_at = client['accounts'][0].get('updated_at', 'No update')
    if updated_at is None:
        updated_at = 'No update'
    return updated_at


def get_account_account_type(client: dict):
    return client.get('account_type') or 'No type'
